import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  divisions,
  core,
  personal,
  drawers,
  drawerOf,
  byDrawer,
  underParent,
  freeUnits,
  pageOf,
  referencesIn,
  stats,
} from './divisions.ts';
import { rows, index, ambiguous, termCounts } from './lookup.ts';

const codes = new Set(divisions.map((d) => d.code));
const personalCodes = new Set(personal.map((d) => d.code));

test('every code is four digits in a real drawer', () => {
  for (const d of divisions) {
    assert.match(d.code, /^[1-5]\d{3}$/, `${d.code} ${d.name}`);
  }
});

test('codes are unique', () => {
  assert.equal(codes.size, divisions.length);
});

test('drawers are the N000 codes, and there are five', () => {
  assert.deepEqual(
    drawers.map((d) => d.code),
    ['1000', '2000', '3000', '4000', '5000'],
  );
  for (const d of divisions) {
    assert.equal(d.kind === 'drawer', d.code.endsWith('000'), `${d.code} ${d.name}`);
  }
});

test('a division ends in zero, a sub-division does not', () => {
  for (const d of divisions) {
    if (d.kind === 'division') assert.ok(d.code.endsWith('0'), `${d.code} ${d.name}`);
    if (d.kind === 'subdivision') assert.ok(!d.code.endsWith('0'), `${d.code} ${d.name}`);
  }
});

test('a sub-division shares its parent tens and the parent exists', () => {
  for (const d of divisions) {
    if (d.kind !== 'subdivision') continue;
    assert.ok(d.parent, `${d.code} has no parent`);
    assert.ok(codes.has(d.parent!), `${d.code} parent ${d.parent} missing`);
    assert.equal(d.code.slice(0, 3), d.parent!.slice(0, 3), `${d.code} is not under ${d.parent}`);
  }
});

test('every division has a scope note', () => {
  for (const d of divisions) {
    assert.ok(d.scope.trim().length > 20, `${d.code} ${d.name}`);
  }
});

/**
 * Scope notes name competing divisions ("…the underlying biochemistry is 3050")
 * and the page renders those as anchors. A code that no longer exists becomes a
 * link to nowhere, which is invisible in a green build.
 */
test('every code cross-referenced in a scope note exists', () => {
  for (const d of divisions) {
    for (const ref of referencesIn(d.scope)) {
      assert.ok(codes.has(ref), `${d.code} ${d.name} points at missing ${ref}`);
      assert.notEqual(ref, d.code, `${d.code} ${d.name} points at itself`);
    }
  }
});

test('byDrawer covers every row of the tier exactly once', () => {
  for (const [tier, expected] of [
    ['core', core.length - drawers.length],
    ['personal', personal.length],
  ] as const) {
    const seen = byDrawer(tier).flatMap((g) => g.rows.map((r) => r.code));
    assert.equal(seen.length, expected, tier);
    assert.equal(new Set(seen).size, seen.length, tier);
    for (const g of byDrawer(tier)) {
      for (const r of g.rows) {
        assert.equal(drawerOf(r.code), g.drawer.code);
        assert.equal(r.tier, tier);
      }
    }
  }
});

test('every row is in exactly one tier, and the tiers partition the table', () => {
  for (const d of divisions) {
    assert.ok(d.tier === 'core' || d.tier === 'personal', `${d.code} tier ${d.tier}`);
  }
  assert.equal(core.length + personal.length, divisions.length);
  assert.equal(stats.core + stats.personal, stats.rows);
});

test('the core tier is the whole division layer, and the drawers are core', () => {
  assert.deepEqual(
    core.map((d) => d.code),
    divisions.filter((d) => d.code.endsWith('0')).map((d) => d.code),
  );
  for (const d of drawers) assert.equal(d.tier, 'core', d.code);
});

/**
 * The whole point of the split is that the core list can be adopted by someone
 * who never sees the personal tier. A core scope note that names a personal
 * code sends that reader to a row their box does not contain — and the page
 * would render a link off to another tier, which reads as canonical.
 */
test('a core scope note never references a personal code', () => {
  for (const d of core) {
    for (const ref of referencesIn(d.scope)) {
      assert.ok(!personalCodes.has(ref), `core ${d.code} ${d.name} points at personal ${ref}`);
    }
  }
});

/** A core row must not hang off a personal one, or the tiers are not separable. */
test('no core row has a personal parent', () => {
  for (const d of core) {
    if (d.parent) assert.ok(!personalCodes.has(d.parent), `${d.code} parent ${d.parent}`);
  }
});

test('pageOf sends each tier to its own route, and rejects unknown codes', () => {
  for (const d of divisions) {
    assert.equal(pageOf(d.code), d.tier === 'core' ? '/core' : '/extensions', d.code);
  }
  assert.throws(() => pageOf('9999'), /no division 9999/);
});

test('every code cross-referenced in a scope note resolves to a page', () => {
  for (const d of divisions) {
    for (const ref of referencesIn(d.scope)) assert.doesNotThrow(() => pageOf(ref));
  }
});

test('underParent covers every personal row under an existing parent', () => {
  const seen = underParent().flatMap((g) => g.rows.map((r) => r.code));
  assert.deepEqual(
    seen.slice().sort(),
    personal.map((d) => d.code).sort(),
  );
  for (const g of underParent()) {
    assert.ok(codes.has(g.parent.code), `missing parent ${g.parent.code}`);
    for (const r of g.rows) assert.equal(r.parent ?? drawerOf(r.code), g.parent.code);
  }
});

/** The units digit is the room the split depends on, so the count must be real. */
test('freeUnits never goes negative and matches the children on record', () => {
  for (const d of divisions) {
    const used = divisions.filter((x) => x.parent === d.code).length;
    assert.equal(freeUnits(d.code), 9 - used, d.code);
    assert.ok(freeUnits(d.code) >= 0, d.code);
  }
});

test('every lookup row targets a real division', () => {
  for (const r of rows) {
    assert.ok(codes.has(r.division), `${r.term} (${r.source}) -> ${r.division}`);
  }
});

test('lookup rows never target a drawer', () => {
  const drawerCodes = new Set(drawers.map((d) => d.code));
  for (const r of rows) {
    if (r.source.includes('/')) {
      assert.ok(!drawerCodes.has(r.division), `${r.term} filed at drawer ${r.division}`);
    }
  }
});

test('the search index dedupes term+division but keeps two-home terms', () => {
  const idx = index();
  assert.ok(idx.length <= rows.length);
  assert.equal(new Set(idx.map((r) => `${r.q} ${r.d}`)).size, idx.length);

  // Glaciology is listed under both Earth science and Geography in the source.
  // Both are correct, so both survive.
  const glaciology = idx.filter((r) => r.q === 'glaciology');
  assert.ok(glaciology.length > 1, 'glaciology should keep more than one home');
});

test('ambiguous terms report every home they have', () => {
  for (const [term, homes] of ambiguous()) {
    assert.ok(homes.length > 1, term);
    for (const h of homes) assert.ok(codes.has(h), `${term} -> ${h}`);
  }
});

/**
 * The extensions page states how many of its rows the source outline never
 * reaches, and the core page claims every canonical division is reached. Both
 * are load-bearing claims about the split, so assert the counts here rather
 * than trusting the prose.
 */
test('every core division is reached by a source term; some personal rows are not', () => {
  const counts = termCounts();
  for (const d of core) {
    if (d.kind === 'drawer') continue;
    assert.ok((counts.get(d.code) ?? 0) > 0, `${d.code} ${d.name} is reached by nothing`);
  }
  const unreached = personal.filter((d) => (counts.get(d.code) ?? 0) === 0);
  assert.ok(unreached.length > 0, 'the vocabulary-gap finding no longer holds');
});

import { test } from 'node:test';
import assert from 'node:assert/strict';
import { compare, parse, divisionOf, drawerOf, splitForDisplay, branchDepth } from './address.ts';

const order = (...addrs: string[]) => [...addrs].sort(compare);

test('numeric segments compare by value, not lexically', () => {
  assert.deepEqual(order('2090/10', '2090/9'), ['2090/9', '2090/10']);
  assert.deepEqual(order('2090/130', '2090/2', '2090/19'), ['2090/2', '2090/19', '2090/130']);
});

test('a child sits between its parent and the parent next sibling', () => {
  assert.deepEqual(order('1040/9d2', '1040/9d1a'), ['1040/9d1a', '1040/9d2']);
  assert.deepEqual(
    order('1040/9d2', '1040/9d1b', '1040/9d1', '1040/9d1a1', '1040/9d1a'),
    ['1040/9d1', '1040/9d1a', '1040/9d1a1', '1040/9d1b', '1040/9d2'],
  );
});

test('letter overflow: aa sorts after z, not before b', () => {
  assert.deepEqual(order('3021/50aa', '3021/50b'), ['3021/50b', '3021/50aa']);
  assert.deepEqual(order('2010/7aa', '2010/7z', '2010/7a'), ['2010/7a', '2010/7z', '2010/7aa']);
});

test('a parent precedes all of its descendants', () => {
  assert.deepEqual(
    order('1010/1d1', '1010/1d', '1010/1', '1010'),
    ['1010', '1010/1', '1010/1d', '1010/1d1'],
  );
});

test('divisions order numerically across drawers', () => {
  assert.deepEqual(order('5100', '1010', '2103', '1000'), ['1000', '1010', '2103', '5100']);
});

test('the published worked sequence lands in the documented drawer order', () => {
  // context/02-filing-rules.md — written 1..7, card 6 must land 4th.
  const written = [
    '1040/9d1', '1040/9d1a', '1040/9d1a1', '1040/9d1b',
    '1040/9d1b1', '1040/9d1a2', '1040/9d2',
  ];
  assert.deepEqual(order(...written), [
    '1040/9d1', '1040/9d1a', '1040/9d1a1', '1040/9d1a2',
    '1040/9d1b', '1040/9d1b1', '1040/9d2',
  ]);
});

test('compare is a consistent total order', () => {
  // Normalised so -0 never reaches the assertion: Object.is(0, -0) is false.
  const sign = (n: number): number => (n > 0 ? 1 : n < 0 ? -1 : 0);
  const sample = ['1000', '1040/9d1a', '2090/9', '2090/10', '3021/50aa', '3021/50b', '1040/9d2'];
  for (const a of sample) {
    assert.equal(sign(compare(a, a)), 0, `${a} should equal itself`);
    for (const b of sample) {
      assert.equal(sign(compare(a, b)), sign(-compare(b, a)), `antisymmetry: ${a} vs ${b}`);
    }
  }
});

test('parse splits alternating segments', () => {
  assert.deepEqual(parse('1040/9d1a').segs.map((s) => s.n || s.s), [9, 'd', 1, 'a']);
  assert.deepEqual(parse('3021/50aa').segs.map((s) => s.n || s.s), [50, 'aa']);
  assert.deepEqual(parse('1010/1d10').segs.map((s) => s.n || s.s), [1, 'd', 10]);
  assert.deepEqual(parse('1000').segs, []);
});

test('address helpers', () => {
  assert.equal(divisionOf('1040/9d1a'), '1040');
  assert.equal(divisionOf('1040'), '1040');
  assert.equal(drawerOf('5100/21a'), '5000');
  assert.deepEqual(splitForDisplay('1040/9d1a'), ['1040', '/9d1a']);
  assert.deepEqual(splitForDisplay('1040'), ['1040', '']);
  assert.equal(branchDepth('1040/9d1a'), 4);
  assert.equal(branchDepth('1040'), 0);
});

/**
 * The worked example's data, typed.
 *
 * Address grammar lives in `address.ts` and is re-exported here so there is
 * exactly one comparator in the codebase — the one the tests cover.
 */
import raw from '../../context/data/numbered.json' with { type: 'json' };
import { compare, divisionOf, drawerOf } from './address.ts';

export {
  compare,
  parse,
  divisionOf,
  drawerOf,
  splitForDisplay,
  branchDepth,
} from './address.ts';

/** `h` = a four-digit division (guide card); `b` = an entry branching off one. */
export type Kind = 'h' | 'b';

export interface Entry {
  /** Full address, e.g. `1040/9d1a`. Permanent — never recomputed. */
  num: string;
  k: Kind;
  /** Heading level in the source outline (2–5), or list indent depth (0–3). */
  lvl: number;
  /** Title, verbatim from the source outline. */
  t: string;
  /** Line number in `context/data/academic-disciplines.md`. */
  ln: number;
  note: string | null;
  /** Render depth: 0–3 for divisions, 4–7 for branch entries. */
  depth: number;
}

export const entries = raw as Entry[];

/** Entries in drawer order. */
export function sorted(list: Entry[] = entries): Entry[] {
  return [...list].sort((a, b) => compare(a.num, b.num));
}

/** The 65 four-digit divisions — the guide cards. */
export const divisions: Entry[] = entries.filter((e) => e.k === 'h');

/** The five top-level drawers. */
export const drawers: Entry[] = divisions.filter((e) => e.depth === 0);

/** Every entry that hangs off a given division, in drawer order. */
export function inDivision(division: string): Entry[] {
  return sorted(entries.filter((e) => divisionOf(e.num) === division && e.num !== division));
}

/** Every entry in a given drawer, in drawer order. */
export function inDrawer(drawer: string): Entry[] {
  return sorted(entries.filter((e) => drawerOf(e.num) === drawer));
}

/**
 * Titles that appear more than once inside a single division. The source outline
 * lists some disciplines under two parents; both addresses are valid and
 * distinct. Filing practice is to pick one as live and cross-reference.
 */
export function duplicatesWithinDivision(): Map<string, Entry[]> {
  const groups = new Map<string, Entry[]>();
  for (const e of entries) {
    const key = `${divisionOf(e.num)} ${e.t.toLowerCase()}`;
    const bucket = groups.get(key);
    if (bucket) bucket.push(e);
    else groups.set(key, [e]);
  }
  const dups = new Map<string, Entry[]>();
  for (const [key, list] of groups) {
    if (list.length > 1) dups.set(key, list);
  }
  return dups;
}

export const stats = {
  total: entries.length,
  divisions: divisions.length,
  drawers: drawers.length,
  /** Deepest branch level reached, counting the division as level 0. */
  maxDepth: entries.reduce((m, e) => Math.max(m, e.depth), 0) - 3,
} as const;

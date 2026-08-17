/**
 * Antinet address grammar — pure functions, no data import.
 *
 * An address is a four-digit division, optionally followed by `/` and a branch
 * path whose segments alternate number → letter → number → letter. The type
 * switch is the level separator, which is why there is only ever one slash.
 *
 * Kept free of imports so it can be unit-tested with plain `node --test`.
 * See `context/01-numbering-scheme.md` for the full specification.
 */

interface Seg {
  type: 0 | 1;
  n: number;
  s: string;
}

export interface Parsed {
  div: number;
  segs: Seg[];
}

/** Split an address into its division and its alternating branch segments. */
export function parse(addr: string): Parsed {
  const slash = addr.indexOf('/');
  const div = Number.parseInt(slash === -1 ? addr : addr.slice(0, slash), 10);
  const branch = slash === -1 ? '' : addr.slice(slash + 1);
  const segs: Seg[] = [];
  for (const m of branch.matchAll(/\d+|[a-z]+/g)) {
    const s = m[0];
    segs.push(
      s.charCodeAt(0) <= 57
        ? { type: 0, n: Number.parseInt(s, 10), s: '' }
        : { type: 1, n: 0, s },
    );
  }
  return { div, segs };
}

/**
 * Drawer order.
 *
 * Three rules a naive string sort gets wrong:
 *   - numeric segments compare by VALUE   → `2090/9` before `2090/10`
 *   - a shorter address precedes its own children, so a child lands between its
 *     parent and the parent's next sibling → `1040/9d1a` before `1040/9d2`
 *   - letter segments compare by LENGTH first, then lexically, because the
 *     overflow alphabet runs a…z, aa, ab → `3021/50b` before `3021/50aa`
 */
export function compare(a: string, b: string): number {
  const A = parse(a);
  const B = parse(b);
  if (A.div !== B.div) return A.div - B.div;

  const shared = Math.min(A.segs.length, B.segs.length);
  for (let i = 0; i < shared; i++) {
    const x = A.segs[i]!;
    const y = B.segs[i]!;
    if (x.type !== y.type) return x.type - y.type;
    if (x.type === 0) {
      if (x.n !== y.n) return x.n - y.n;
    } else {
      if (x.s.length !== y.s.length) return x.s.length - y.s.length;
      if (x.s !== y.s) return x.s < y.s ? -1 : 1;
    }
  }
  return A.segs.length - B.segs.length;
}

/** Division number an address belongs to: `1040/9d1a` → `1040`. */
export function divisionOf(addr: string): string {
  const slash = addr.indexOf('/');
  return slash === -1 ? addr : addr.slice(0, slash);
}

/** Drawer an address belongs to: `1040/9d1a` → `1000`. */
export function drawerOf(addr: string): string {
  return `${addr[0]}000`;
}

/** Split an address for display: the division, and the branch including its slash. */
export function splitForDisplay(addr: string): [string, string] {
  const slash = addr.indexOf('/');
  return slash === -1 ? [addr, ''] : [addr.slice(0, slash), addr.slice(slash)];
}

/** Depth in branch segments. A division is 0. */
export function branchDepth(addr: string): number {
  return parse(addr).segs.length;
}

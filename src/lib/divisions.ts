/**
 * The division index — the published taxonomy, in two tiers.
 *
 * `core` is the canonical list: five drawers and the disciplines beneath them,
 * every code ending in zero. It is meant to be adoptable whole by a stranger,
 * so nothing in it depends on whose card box it is.
 *
 * `personal` is everything one filer's own cards have paid for. It lives on its
 * own page and takes the units digit the core tier leaves empty, which is why
 * adding to it can never move a core code.
 *
 * Every row is four digits with a scope note. Nothing below four digits is
 * published, because nothing below four digits is taxonomy: the branch suffix
 * carries position only, and a filer grows it from their own cards.
 *
 * `lookup.ts` maps the source outline onto these codes for the finder, which
 * searches both tiers.
 */
import raw from '../../context/data/divisions.json' with { type: 'json' };

export type DivisionKind = 'drawer' | 'division' | 'subdivision';

/** Which tier a row belongs to, and therefore which page publishes it. */
export type Tier = 'core' | 'personal';

export interface Division {
  /** Four digits: drawer (1) + discipline (2) + sub-discipline (1). */
  code: string;
  kind: DivisionKind;
  tier: Tier;
  name: string;
  /** What files here, and the tiebreak against the divisions it competes with. */
  scope: string;
  /** Present on sub-divisions only — the division whose units digit this takes. */
  parent?: string;
}

export const divisions = raw as Division[];

export const core = divisions.filter((d) => d.tier === 'core');
export const personal = divisions.filter((d) => d.tier === 'personal');
export const drawers = divisions.filter((d) => d.kind === 'drawer');

/**
 * The route each tier is published on.
 *
 * The two tiers are separate pages on purpose, so a scope-note cross-reference
 * can point at a row the current page does not render. Resolve one with
 * `pageOf` rather than assuming the anchor is local.
 */
export const PAGES: Record<Tier, string> = { core: '/core', personal: '/extensions' };

const routeByCode = new Map(divisions.map((d) => [d.code, PAGES[d.tier]]));

/**
 * The route that publishes a code, for a cross-page anchor.
 *
 * Throws on an unknown code. A cross-reference to a row that no longer exists
 * would otherwise render as a link to nowhere, which is invisible in a green
 * build — so it fails the build instead.
 */
export function pageOf(code: string): string {
  const route = routeByCode.get(code);
  if (!route) throw new Error(`no division ${code}`);
  return route;
}

/** The drawer a code belongs to: `5062` → `5000`. */
export function drawerOf(code: string): string {
  return `${code[0]}000`;
}

/** The rows of one tier grouped under their drawer, in code order. */
export function byDrawer(tier: Tier = 'core'): { drawer: Division; rows: Division[] }[] {
  return drawers.map((drawer) => ({
    drawer,
    rows: divisions.filter(
      (d) => d.kind !== 'drawer' && d.tier === tier && drawerOf(d.code) === drawer.code,
    ),
  }));
}

/**
 * Personal rows grouped under the division whose units digit they took.
 *
 * The extensions page reads as "what my cards added to which core row", so the
 * parent is the heading rather than the drawer.
 */
export function underParent(): { parent: Division; rows: Division[] }[] {
  const parents = [...new Set(personal.map((d) => d.parent ?? drawerOf(d.code)))].sort();
  return parents.map((code) => ({
    parent: divisions.find((d) => d.code === code)!,
    rows: personal.filter((d) => (d.parent ?? drawerOf(d.code)) === code),
  }));
}

/**
 * Codes named inside another division's scope note, as cross-references.
 *
 * Scope notes point at the division a near-miss card belongs in instead
 * ("…the underlying biochemistry is 3050"). Rendering those as links is what
 * turns the table from a list of names into a filing decision aid.
 */
export function referencesIn(scope: string): string[] {
  return [...new Set(scope.match(/\b[1-5]\d{3}\b/g) ?? [])];
}

/** Units digits still free under a division — the room an extension moves into. */
export function freeUnits(code: string): number {
  return 9 - divisions.filter((d) => d.parent === code).length;
}

export const stats = {
  rows: divisions.length,
  drawers: drawers.length,
  divisions: divisions.filter((d) => d.kind === 'division').length,
  subdivisions: divisions.filter((d) => d.kind === 'subdivision').length,
  core: core.length,
  personal: personal.length,
} as const;

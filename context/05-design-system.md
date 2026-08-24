# Design System

The visual identity used across all three artifacts. **Carry this into the Astro site** so the
site and the artifacts read as one body of work.

## Concept

Grounded in the physical subject: a library card drawer. Cool and institutional rather than
warm — deliberately *not* the cream-and-terracotta palette that generic AI design defaults to.
Card stock under fluorescent light, slate-navy ink, and one oxidised-brass accent standing in
for the drawer pull.

## Tokens

```css
:root{
  --ground:#F2F3F1;   /* card stock — off-white with a faint green bias, not cream */
  --surface:#FFFFFF;  /* the card itself */
  --ink:#1B2430;      /* deep slate-navy */
  --muted:#6B7580;    /* grey biased toward the ink */
  --rule:#D8DBD6;     /* hairlines */
  --brass:#8A6A2F;    /* THE accent — division numbers only */
  --brass-dim:#A98B4E;
  --tint:#E7E9E5;     /* row hover, inset panels */
  --warn:#8C4A2F;
  --good:#3D6B4A;
}
```

Dark theme — the drawer interior at night. Brass brightens rather than inverts:

```css
--ground:#151A1F; --surface:#1D242B; --ink:#E3E6E2; --muted:#8D97A1;
--rule:#2C353D;   --brass:#C9A227;   --brass-dim:#9C8330; --tint:#222A31;
--warn:#D08A5E;   --good:#7FB08D;
```

### Theme wiring — three states, not two

An explicit choice stamps `data-theme` on the root; the default "system" setting stamps
*nothing*. All three must be handled or the page renders one theme's text on the other's ground:

```css
:root { /* complete light palette */ }
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){ /* dark tokens */ } }
:root[data-theme="dark"]{ /* dark tokens again */ }
```

Style components through tokens only — **never declare a colour inside a media or
`[data-theme]` block.** `body` must set an explicit token background.

## Type

Three roles, all system stacks (no webfonts — the artifact CSP blocks font CDNs, and a
silent fallback is worse than a deliberate system stack):

| Role | Stack | Used for |
|---|---|---|
| Display | `ui-serif, Georgia, "Times New Roman", serif` | Division titles, headings — catalog-card lineage |
| Body | `ui-sans-serif, -apple-system, "Segoe UI", Roboto, sans-serif` | Running text, UI chrome |
| Data | `ui-monospace, "SF Mono", Menlo, monospace` | **Every address**, always with `font-variant-numeric: tabular-nums` |

Addresses are the point of the whole system, so they get the monospace column and must align
vertically. Uppercase micro-labels take `letter-spacing: .09em–.11em` at `.68rem–.72rem`.

## Layout

- Single column, `max-width: 54rem`–`60rem` depending on density.
- Sibling groups laid out with flex/grid `gap`, never per-element margins.
- Wide content gets its own `overflow-x: auto` container; the body never scrolls sideways.
- Depth shown by indent plus a hairline guide rail (`border-left: 1px solid var(--rule)`).
- Accent discipline: brass appears on division numbers, active states, and the single
  left-border of callouts. Nowhere else.

## Fragment links

Every section heading (`h2`–`h4`, not the page `h1`) is addressable and copyable.
`src/components/Heading.astro` cuts the `id` from the heading text at build time, so it is in
the served HTML and an inbound deep link scrolls on arrival rather than after a script runs.

- **The whole heading is the click target.** Clicking anywhere on it copies the absolute URL.
  The click is cancelled, so the page never jumps to the fragment it just copied; the address
  bar is updated with `replaceState` instead, which leaves the URL reachable when the clipboard
  refuses. `cursor: pointer` is the standing signal that the heading is live.
- **A trailing chain-link icon marks it**, drawn inline — the no-webfont rule holds, and one
  glyph is not worth a third-party request. Its strokes take `currentColor`. Hidden at rest and
  revealed on hovering the heading, by opacity rather than `display`, so nothing on the line
  moves. Muted when revealed, brass when the icon itself is hovered or focused — the accent
  stays on the active element. Where the device reports no hover the icon is left visible at
  `.55`, since there is no reveal to discover it by. Hidden in print.
- **What still behaves normally:** a link the heading already carries (a division code pointing
  at `/core`), a modified or middle click on the icon, and a click that ends a drag-selection of
  the heading's own words.

The icon is omitted where it cannot work: a heading already inside a link (the route cards on
`/`), and the uppercase micro-labels marked up as `h4` that label a diagram rather than opening
a section. Both are left out simply by not using the component.

## Published artifacts

| Artifact | URL | Favicon |
|---|---|---|
| Antinet Discipline Index | https://claude.ai/code/artifact/9e9d4ec0-46d9-4858-93ea-e2f535cdeff1 | 🗂️ |
| Hub Card Placements | https://claude.ai/code/artifact/74feb0e1-60f5-42a2-ba50-b669e4f28f82 | 🧭 |
| Antinet Filing Rules | https://claude.ai/code/artifact/4d675894-620c-4843-bcb6-c1af81a4a70e | 📇 |

Local copies in `artifacts/`. Regenerate with `scripts/02-04-*.py`.

These are private Claude artifacts — usable as reference and as the design source for the site,
but they are **not** a substitute for the site itself and should not be linked as if public.

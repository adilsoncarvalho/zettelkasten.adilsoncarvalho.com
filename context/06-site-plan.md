# Site Plan — Astro on GitHub Pages

## What this site is

**A living Antinet Zettelkasten implementation manual.** Public, for the owner and for anyone
seeking answers to the same questions.

It exists because the practical questions of running an Antinet either have no clear answers or
have answers scattered across many sources. The site's job is to answer them in one place, from
a worked implementation.

**It is not a place to publish the owner's own cards.** The reference material is the product;
the owner's card content stays private. Any future feature must be checked against this — a
design that assumes personal notes will be rendered is out of scope.

## Decided

| Question | Answer |
|---|---|
| Domain | `zettelkasten.adilsoncarvalho.com` — Route 53 record pending, owner will add |
| `base` | `/` — apex custom domain, so no path prefix |
| Repo visibility | **Private for now**, public at first publish |
| Audience | Public. Written for a stranger with the same problem, not just the owner |
| Root page | A **quick usage guide** to the site's contents — *not* the index listing |
| Divisions | Its own path, separate from the outline |
| Blog | `/blog` likely, later. Leave room; do not build yet |

## Routes

```
/             Quick usage guide — what's here, where to start, how to use it
/rules        Filing rules — child vs sibling, worked example, hub cards
/divisions    The 65 four-digit divisions
/outline      Full numbered outline, 2,576 addresses, searchable
/hubs         Hub card placements (worked example of applying the scheme)
/colophon     Sources, CC BY-SA attribution, how the numbering was generated
/blog         Future — not built
```

**`/outline`, not `/index`.** In Astro, `src/pages/index.astro` *is* the root route, so a page
at `/index` needs `src/pages/index/index.astro` and reads as a collision. `/outline` also
describes the content better.

## Data pipeline

`context/data/numbered.json` is canonical — 2,576 objects with
`{num, k, lvl, t, ln, note, depth}`. Astro imports it directly.

**Do not re-derive addresses in the site.** If the source outline changes, re-run
`context/scripts/01-number.py` and commit the regenerated JSON, so generation stays in one
place and the collision assertion keeps running.

### Sorting — the one real trap

Sort with the reference key in `01-numbering-scheme.md`. Numeric segments compare
**numerically**. A naive string sort scrambles every large branch. Unit-test these:

| Input | Correct output | Why |
|---|---|---|
| `2090/10`, `2090/9` | `2090/9`, `2090/10` | numeric, not lexical |
| `1040/9d2`, `1040/9d1a` | `1040/9d1a`, `1040/9d2` | child precedes parent's next sibling |
| `3021/50aa`, `3021/50b` | `3021/50b`, `3021/50aa` | `aa` sorts *after* `z` — length first, then lexical |

## Search

2,576 rows is the main UX question. The published artifact renders all rows statically and
filters with JS — proven, but ~400KB of HTML.

1. **Static rows + client filter** — simplest, proven. Start here.
2. **Pagefind** — built for Astro static sites, handles this scale. Move here if weight bites.
3. **Paginate by division** — lightest, but kills cross-drawer search, which is the whole point
   of a hub. Wrong on its own.

## Deployment

- GitHub Actions → `withastro/action` + `actions/deploy-pages`.
- `site: 'https://zettelkasten.adilsoncarvalho.com'`, `base: '/'`.
- `public/CNAME` containing the bare domain.
- Repo settings → Pages → Source: **GitHub Actions**.
- **Pages must be enabled and the repo made public before the site serves.** Private repos need
  a paid plan for Pages. Deploys will run green and serve nothing until then — expect that.

## Constraints

- **pnpm only.** Never npm/yarn/bun. `.gitignore` blocks the competing lockfiles.
- Node pinned to `24.1.0` via `.tool-versions` (LTS line; 25.x is a Current release and past
  EOL as of 2026-08). CI matches this.
- Branch + PR; `master` is the default branch.
- Conventional Commits.
- Local git identity `Adilson Carvalho <lc.adilson@gmail.com>` — set per-repo, since the
  machine default is a work address.
- **CC BY-SA 4.0 attribution on every page rendering outline content.** Share-alike, so
  derivative content inherits the obligation. Footer, not just a README.

## Still open

1. The malformed entry `1030/9c4` — fix, or render verbatim with a note? (See `04-findings.md`.)
2. The 37 within-division duplicates — surface as cross-links, or leave?
3. Root page content — agreed to be a usage guide; the actual copy is undefined.

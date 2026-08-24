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
| Divisions | Split in two: `/core` is the canonical table and the site's index; `/extensions` is the author's own rows, kept off it |
| Tier boundary | At the digit — core owns the first three, the filer owns the fourth. See `07-decisions.md` §12 |
| Outline | Demoted to the lookup corpus and stress test, not the index |
| Blog | `/blog` likely, later. Leave room; do not build yet |

## Vocabulary — one word per tier, in all published text

| Tier | Word | Example |
|---|---|---|
| First digit | **drawer** | `5000` Applied science and practice |
| Middle two digits | **discipline** | `5060` Business and management |
| Units digit | **sub-discipline** | `5063` Finance and investing |

**"Division" does not appear in published text.** The site used both words
interchangeably — often in one sentence — and the pair reads as a distinction that
does not exist. `discipline` won because it is what the rows actually are, and
because the digit anatomy on `/core` was already taught as drawer + discipline +
sub-discipline.

`division` survives only as a **code identifier**: `divisions.json`, `divisions.ts`,
`kind: "division"`, `divisionOf()`, `LookupRow.division`. Renaming those buys nothing
a reader of the site can see, and a comment saying "discipline" beside a field named
`division` would be worse than either word alone. If they are ever renamed, do it as
its own commit with no prose changes in it.

Two prose traps found during the sweep, both worth re-checking after any edit here:

- **Sentences that contrast the two words.** "Interests are practices and divisions
  are disciplines" becomes a tautology under a blind substitution. Three sentences had
  this shape; each now says *field of study* for the second half.
- **Source-outline nodes.** `03-hub-placements.md` and the hub `THEMES` structure call
  a four-digit source-outline node a division. Those are disciplines too, and the
  distinction that matters there is already carried by the words *source outline*, so
  they read "(source-outline discipline)". The source of truth is
  `scripts/03-build-hubs-artifact.py`; regenerate `data/hubs.json` after editing it.

## Routes

```
/             Quick usage guide — what's here, where to start, how to use it
/rules        Filing rules — child vs sibling, worked example, hub cards
/core         The canonical division table — 51 rows, each with a scope note
/extending    How to adopt the core as it is, and how to earn a row of your own
/extensions   The author's 5 sub-divisions, each with what paid for it
/find         Decision procedure, seam table, lookup, copyable prompt, print sheet
/outline      Source outline, 2,576 addresses, each showing where it now files
/hubs         Hub card placements (worked example of applying the scheme)
/colophon     Sources, CC BY-SA attribution, how the numbering was generated
/blog         Future — not built
```

**`/divisions` redirects to `/core`.** It was the route before the split; `astro.config.mjs`
emits a meta-refresh page so any link already made still lands.

**`/outline`, not `/index`.** In Astro, `src/pages/index.astro` *is* the root route, so a page
at `/index` needs `src/pages/index/index.astro` and reads as a collision. `/outline` also
describes the content better.

## Data pipeline

Two canonical files, and they are canonical for different things.

`context/data/divisions.json` is the **published taxonomy** — hand-authored, 56 rows of
`{code, kind, tier, name, scope, parent?}`. Edit it directly; there is no generator behind it.
`src/lib/divisions.test.ts` asserts the shape, and asserts that every code cross-referenced
inside a scope note actually exists — those render as anchors, so a dead one is invisible in
a green build.

**`tier` is an explicit field, not derived from `kind`.** Today every `core` row ends in zero
and every `personal` row is a sub-division, so the two could be inferred from each other —
but the whole point of the split is that the author can add a *division* of his own later, in
a free tens slot, and that row must land on `/extensions` without a code change. `pageOf()`
routes a code to its tier's page, so a scope-note cross-reference can point across the two.

Two invariants in the suite carry the split, and both fail loudly rather than rendering
something wrong: no core scope note may reference a personal code (or an adopter of the
canonical list follows a link to a row they do not have), and every core division must be
reached by at least one source term while some personal row is not (the evidence the line
falls where it does).

`context/data/numbered.json` is the **source outline** — 2,576 objects with
`{num, k, lvl, t, ln, note, depth}`, generated and never hand-edited.
`scripts/07-map-legacy.py` joins the two into `data/lookup.json`, which is what the finder
searches. Astro imports all three directly.

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

Two searches now, with different jobs. `/find` searches the scope notes *and* the corpus,
ranks table matches first, and groups corpus hits by division — that is the filing aid.
`/outline` keeps the flat filter over all rows — that is the audit trail.

**`/find` searches both tiers deliberately.** Splitting the pages is about what can be
published as canonical; it is not about what a filer holding a card should be able to find.
Results on the personal tier are tagged `mine` and link to `/extensions`. The copyable prompt
emits the two tiers as separate blocks for the same reason — a stranger can delete the second
block and keep a working assistant.

2,576 rows is the main UX question on `/outline`. The published artifact renders all rows statically and
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
4. ~~Source-outline addresses presented as current.~~ **Resolved** — the six hubs and the
   filing-rules worked example were re-anchored onto the curated index. See `07-decisions.md`
   §13 for the placements, how the anchors were chosen, and what the re-anchor turned up.

5. Whether `/find` should offer the printed sheet as a PDF rather than relying on the
   browser's print dialogue.

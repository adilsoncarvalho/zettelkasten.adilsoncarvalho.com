# Site Plan — Astro on GitHub Pages

Not started. This is the plan and the open questions, not a decided spec.

## Proposed structure

```
/                      Landing — what an Antinet is, what this reference is for
/rules                 Filing rules (source: 02-filing-rules.md)
/divisions             The 65 divisions (source: content/division-map.md)
/index                 Full searchable outline — 2,576 addresses
/index/[address]       Optional: a page per division, or per drawer
/hubs                  Hub placements (source: 03-hub-placements.md)
/colophon              Sources, CC BY-SA attribution, how it was generated
```

## Data pipeline

`data/numbered.json` is canonical. Astro can import it directly — it is 2,576 objects with
`{num, k, lvl, t, ln, note, depth}`. `data/addresses.csv` is the same data flat, if a loader
prefers it.

Do **not** re-derive addresses in the site. If the source outline changes, re-run
`scripts/01-number.py` and commit the regenerated JSON, so that generation stays in one place
and the collision assertion keeps running.

### Sorting

The site must sort with the reference key in `01-numbering-scheme.md` — numeric segments
compare numerically. A naive string sort puts `2090/10` before `2090/9` and silently
scrambles every large branch. Port it and unit-test it against these cases:

| Input order | Correct output |
|---|---|
| `2090/10`, `2090/9` | `2090/9`, `2090/10` |
| `1040/9d2`, `1040/9d1a` | `1040/9d1a`, `1040/9d2` |
| `3021/50aa`, `3021/50b` | `3021/50b`, `3021/50aa` |

The third case matters: `aa` sorts *after* `z`, not before `b`. Segment comparison is
(length, then lexical) for letters — not plain lexical.

## The search problem

2,576 rows is the site's main UX question. The index artifact renders all rows statically and
filters with JS, which works but ships ~400KB of HTML.

Options for the site, roughly in order of effort:

1. **Same approach** — static rows + client filter. Simplest, proven, heavy.
2. **Client-side index** (Pagefind, Fuse.js) — Pagefind is built for Astro static sites and
   handles this scale comfortably.
3. **Paginate by division** — 65 pages of ~40 entries. Lightest, but loses cross-drawer search,
   which is exactly what a hub card exists to provide. Probably wrong on its own.

Recommendation: start with (1) since the artifact already proves it, and move to Pagefind if
the page weight becomes a problem.

## GitHub Pages deployment

- Astro's official `withastro/action` + `actions/deploy-pages`, or a plain build-and-deploy job.
- Set `site` and `base` in `astro.config.mjs`. For a custom domain at the apex of
  `zettelkasten.adilsoncarvalho.com`, `base` stays `/`.
- Custom domain needs a `public/CNAME` file containing the domain, plus DNS. **Confirm the
  domain is actually intended and the DNS exists** — it is inferred from the repo name only.
- Enable Pages → Source: GitHub Actions, in repo settings.

## Open questions for the owner

1. **Domain** — is `zettelkasten.adilsoncarvalho.com` real and DNS-ready, or is this
   `adilsoncarvalho.github.io/zettelkasten...` for now?
2. **Audience** — personal reference, or a public resource? Changes how much explanation the
   landing page carries.
3. **Scope** — does the site publish only the reference material, or eventually the owner's
   actual card content too? The second is a much larger design problem and should not be
   assumed.
4. **The malformed entry** `1030/9c4` — fix, or render verbatim with a note? (See `04`.)
5. **Duplicates** — surface the 37 within-division duplicates as cross-links, or leave them?

## Constraints carried from the brief

- **pnpm only.** Never npm/yarn/bun.
- Branch + PR; never commit to `main` directly.
- Conventional Commits.
- Local git identity `Adilson Carvalho <lc.adilson@gmail.com>` — must be set per-repo, since
  the machine default is a work address.
- CC BY-SA 4.0 attribution must appear on every page rendering outline content.

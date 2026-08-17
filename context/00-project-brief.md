# Project Brief

## Goal

A static website that publishes the Antinet filing reference material: the numbered
discipline index, the filing rules, and the hub-card placements. Built with **Astro**,
deployed to **GitHub Pages**.

The material already exists and is verified (see `01`–`04`). The remaining work is
presentation and deployment.

## Repository

| | |
|---|---|
| Local path | `/Users/adilson/dev/github.com/adilsoncarvalho/zettelkasten.adilsoncarvalho.com` |
| Remote | `git@github.com:adilsoncarvalho/zettelkasten.adilsoncarvalho.com.git` |
| Site domain | `zettelkasten.adilsoncarvalho.com` (implied by repo name — confirm DNS/CNAME) |
| Commit identity | `Adilson Carvalho <lc.adilson@gmail.com>` |

**Repo state as of this dump: the local folder is NOT yet a git repository.** No `git init`,
no commit, no push has happened. The remote may or may not exist yet — check before assuming.

Set the identity locally rather than globally:

```bash
cd /Users/adilson/dev/github.com/adilsoncarvalho/zettelkasten.adilsoncarvalho.com
git init
git config user.name  "Adilson Carvalho"
git config user.email "lc.adilson@gmail.com"
```

Note this differs from the machine's default identity (`adilson.carvalho@airtasker.com`),
so the local `git config` is load-bearing — a global-identity commit would attribute this
personal project to a work address.

## Package management

Use **pnpm** exclusively — never `npm`, `yarn`, or `bun`. If a `package-lock.json` or
`yarn.lock` ever appears, remove it and run `pnpm install`.

## Working conventions

- Never commit directly to `main`/`master` — branch, then PR.
- Conventional Commits: `type(scope): description`.
- Keep PRs atomic.

## Source material and licensing

**Read `NOTICE.md` at the repo root before touching licence text anywhere.** It is the
authoritative map. Three licences apply:

| Material | Licence |
|---|---|
| Code — `src/`, `context/scripts/`, config | MIT (`LICENSE`) |
| Prose and the numbering scheme | CC BY-NC-SA 4.0 (`LICENSE-CONTENT`) |
| Outline-derived data — `context/data/`, `context/content/` | CC BY-SA 4.0 (`context/data/LICENSE`) |

The outline is from
[Outline of academic disciplines](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines)
(Wikipedia), retrieved **2026-08-17**.

### The boundary, and why it sits where it does

Individual discipline names are **not** copyrightable. What the source protects is the
selection and hierarchical arrangement — and an address encodes that arrangement directly. So
**an address paired with its name is adapted material**; neither half is protected alone.

The **numbering scheme** — division allocation, alternating branch grammar, filing rules,
hub-card model — derives from nothing and applies to any taxonomy. Original work, licensed
BY-NC-SA, with commercial rights reserved for a planned print edition.

**ShareAlike does not spread across the project.** It attaches to adapted material only; an
independent work displayed alongside licensed material forms a Collection. So a page can carry
a BY-SA table inside BY-NC-SA prose without the prose being infected.

### Implementation on the site

`Base.astro` takes a `derived` prop. Every page gets the BY-NC-SA copyright line; pages passing
`derived` additionally get the BY-SA attribution scoped **to the listings, not the page**.

Currently `derived`: `/outline`, `/divisions`, `/hubs`.
Not `derived`: `/`, `/rules` (3 names as examples — de minimis), `/colophon` (states its own
attribution in the Licensing section).

**Do not write "this page is a derivative work."** That is an overclaim — the page is a
Collection; the listings are the adapted part.

### Print edition

A manual covering only the scheme, rules and original examples contains no BY-SA material and
is entirely under the author's control. Keep the numbered outline out of it.

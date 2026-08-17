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

The outline is derived from
[Outline of academic disciplines](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines)
(Wikipedia), retrieved **2026-08-17**, licensed **CC BY-SA 4.0**.

**This matters for the site:** CC BY-SA 4.0 is a share-alike licence. The published site must
carry attribution and licence notice, and derivative content built on the outline inherits the
share-alike obligation. Put the attribution somewhere durable — a footer on every page that
renders outline content, plus a `LICENSE` note — not only in a README.

The *numbering scheme* applied on top is original work and is not itself Wikipedia content.

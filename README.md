# zettelkasten.adilsoncarvalho.com

A living implementation manual for the **Antinet Zettelkasten** — the practical questions of
running one, answered in one place from a worked implementation.

**→ [zettelkasten.adilsoncarvalho.com](https://zettelkasten.adilsoncarvalho.com)**

It exists because those questions either have no clear answer or have answers scattered across
a dozen half-agreeing sources. What number does this card get? How do I file one between two
others? What happens when my interests do not match the categories? The site answers them from
a complete numbering scheme applied at full scale, with the reasoning left in.

The worked example numbers an outline of academic disciplines into **2,576 collision-free
addresses** under **65 four-digit divisions** — large enough to break a scheme that does not
work. It is a demonstration, not the subject: this site publishes the method, not anyone's
personal cards.

## The scheme in one line

```
1040 / 9d1a
└─┬─┘   └┬─┘
  │      └── branch — position only, no meaning. Alternates number → letter → number → letter.
  └───────── division — 4 digits. The only place taxonomy lives.
```

Four digits decompose as drawer (1) + discipline (2) + sub-discipline (1) — exactly the budget
the source outline needs, since one list level fans out to 130 siblings and a positional scheme
would have wanted about eleven digits. Depth past the division is carried by an unbounded
alternating suffix, so cards insert without ever renumbering.

## Running it

Requires Node (pinned in `.tool-versions`), **pnpm**, and Python 3 for the generators.

```bash
pnpm install
pnpm dev        # dev server
pnpm build      # astro check && astro build → dist/
pnpm test       # address-grammar tests (node --test)
pnpm data       # regenerate addresses from the source outline
```

**pnpm only** — never npm, yarn, or bun.

`pnpm data` re-runs the generators and asserts every address is unique before writing, so a
collision fails locally instead of shipping. CI runs the same check and fails on drift between
the committed data and a fresh generation.

## Layout

| Path | |
|---|---|
| `src/pages/` | The six routes: `/`, `/rules`, `/divisions`, `/outline`, `/hubs`, `/colophon` |
| `src/lib/address.ts` | Address grammar and the drawer-order comparator — pure, no imports, unit-tested |
| `src/lib/antinet.ts` | Typed data access; re-exports `address.ts` so there is one comparator |
| `context/` | Design notes, findings, decisions, and the canonical data |
| `.github/workflows/` | Verify → build → deploy to GitHub Pages |

### `context/`

Everything needed to pick this up cold. Start with `context/00-project-brief.md`.

| File | |
|---|---|
| `00-project-brief.md` | Goal, repo, licensing map, conventions |
| `01-numbering-scheme.md` | The address spec and why four digits is the exact budget |
| `02-filing-rules.md` | Child vs sibling, the worked sequence, the three index devices |
| `03-hub-placements.md` | Worked example: six themes mapped onto the scheme |
| `04-findings.md` | Verified audits and the data quirks that affect rendering |
| `05-design-system.md` | Palette, type, theme wiring |
| `06-site-plan.md` | Routes, search options, deployment, open questions |
| `07-decisions.md` | Judgment calls and rationale — read before reversing one |
| `data/` | Canonical `numbered.json`, flat CSV, source outline |
| `scripts/` | Generators, numbered in run order |
| `content/` | Generated Markdown |

## Licensing

Three licences apply, and the boundary is deliberate. **See [`NOTICE.md`](NOTICE.md).**

| Material | Licence |
|---|---|
| Code | [MIT](LICENSE) |
| The numbering scheme, filing rules, and all prose | [CC BY-NC-SA 4.0](LICENSE-CONTENT) |
| Outline-derived data | [CC BY-SA 4.0](context/data/LICENSE) — inherited, not ours to relicense |

Individual discipline names are not copyrightable; what the source protects is the selection
and arrangement, and an address encodes that arrangement. So an address paired with its name is
adapted material while neither half is protected alone.

**Using the method needs no permission at all.** A way of arranging index cards is not a
copyrightable work, and numbering your own cards is not reproduction. The terms govern the
expression, not the practice. Build your Antinet freely.

---

Source outline: [Outline of academic disciplines](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines)
(Wikipedia), retrieved 2026-08-17, CC BY-SA 4.0.

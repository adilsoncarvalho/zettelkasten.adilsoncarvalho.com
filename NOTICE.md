# Licensing

This repository holds three kinds of material under three different licences.
The boundary matters, so it is drawn explicitly here.

| Material | Licence | Why |
|---|---|---|
| **Code** — `src/`, `context/scripts/`, config files | [MIT](LICENSE) | Permissive, attribution-preserving, standard for code |
| **Prose, the numbering scheme, and the division table** — `context/*.md`, `context/data/divisions.json`, page copy, the filing rules | [CC BY-NC-SA 4.0](LICENSE-CONTENT) | Original authorship. Attribution required, commercial use reserved |
| **Outline-derived data** — `context/data/`, `context/content/` | [CC BY-SA 4.0](context/data/LICENSE) | Inherited from Wikipedia. Not ours to relicense |

## What is encumbered, and what is not

### Encumbered — CC BY-SA 4.0, inherited

Derived from
[Outline of academic disciplines](https://en.wikipedia.org/wiki/Outline_of_academic_disciplines)
(Wikipedia), retrieved 2026-08-17.

- `context/data/academic-disciplines.md` — the source, verbatim
- `context/data/numbered.json`, `context/data/addresses.csv`, `context/data/lookup.json`
- `context/content/numbered-outline.md`, `context/content/division-map.md`
- On the site: the address-and-name listings on `/outline`, the lookup on `/find`, and
  the satellite tables on `/hubs`

Individual discipline names are not copyrightable — nobody owns "Rhetoric". What is
protected is the **selection and hierarchical arrangement**, and our addresses encode
that arrangement. An address paired with its name is therefore adapted material, and
carries the ShareAlike obligation. We cannot relicense it, and neither can you.

### Not encumbered — original work

Nothing below derives from Wikipedia. It would work identically applied to any taxonomy.

- **The numbering scheme** — the four-digit division allocation, the alternating
  number/letter branch grammar, the sort order
- **The division table** — `context/data/divisions.json`, published as `/core` and
  `/extensions`. The drawers were re-cut, four religion divisions collapsed into one, law
  moved drawers, and every scope note was written here. Names alone carry no copyright and
  this arrangement is not the source's. What remains adapted is the *mapping* from source
  address to division, which lives in `lookup.json` and is listed above
- **The two-tier split and the expansion method** — the core/personal division of the table
  and the guidance on `/extending`
- **The filing decision procedure** — the four questions and the theory–practice seam
  table on `/find`
- **The filing rules** — child vs sibling, insertion, the worked sequence, the "never" list
- **Hub cards** and the three-index model
- **All prose** on the site and in `context/*.md`
- **All code**

## ShareAlike does not spread across this project

CC BY-SA 4.0 applies ShareAlike to *Adapted Material* only. An independent work merely
collected alongside licensed material forms a Collection and does not inherit the
obligation. This repository and the site are Collections: the encumbered data sits
beside original prose without absorbing it.

Concretely, on `/find`, the lookup table is BY-SA while the decision procedure around it is
BY-NC-SA. They are separate works displayed together.

## Using this material

**Reusing the scheme, the rules, or the prose** — permitted with attribution, for
non-commercial purposes, with derivatives shared alike. Attribute to
*Adilson Carvalho, zettelkasten.adilsoncarvalho.com*. For commercial use, ask.

**Reusing the numbered outline data** — permitted under CC BY-SA 4.0, including
commercially. You must attribute both Wikipedia and this project, and license your
adaptation under BY-SA.

**Building your own Antinet from the scheme** — no permission needed for anything. A
numbering method is not a copyrightable work, and using it is not reproduction. Number
your own cards freely.

## A note on the print edition

A printed manual covering only the scheme, the rules, the division table, and original
examples contains no BY-SA material and is unencumbered. Keep the numbered outline and the
source-address mapping out of it, and the whole book is under the author's sole control.

---

Copyright © 2026 Adilson Carvalho. See `LICENSE`, `LICENSE-CONTENT`, and
`context/data/LICENSE` for full terms.

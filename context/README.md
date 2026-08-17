# Context — Antinet Zettelkasten Site

Everything a fresh session needs to continue this work. **Read `00-project-brief.md` first.**

The work so far: a Wikipedia outline of academic disciplines was converted into a complete
Antinet (Scheper-scheme) filing address system — 2,576 unique addresses under 65 four-digit
divisions — and published as three HTML artifacts. The next phase is rendering that material
as a static Astro site on GitHub Pages.

## Folder map

| Path | What it is |
|---|---|
| `00-project-brief.md` | Goal, repo, deploy target, commit identity. **Start here.** |
| `01-numbering-scheme.md` | The address spec: allocation, grammar, why 4 digits works |
| `02-filing-rules.md` | Operating manual: child vs sibling, worked example, hub cards |
| `03-hub-placements.md` | The owner's six standing interests, mapped to addresses |
| `04-findings.md` | Verified audits, data quirks, the vocabulary-gap finding |
| `05-design-system.md` | Palette, type, layout tokens used across the three artifacts |
| `06-site-plan.md` | Astro + GitHub Pages plan and open questions |
| `07-decisions.md` | Judgment calls made and why — do not re-litigate without reading |
| `content/division-map.md` | Generated: the 65 divisions as a table |
| `content/numbered-outline.md` | Generated: all 2,576 addresses in drawer order |
| `data/academic-disciplines.md` | Source outline (Wikipedia, CC BY-SA 4.0, retrieved 2026-08-17) |
| `data/numbered.json` | **Canonical data.** Every entry with its address, depth, source line |
| `data/addresses.csv` | Same data, flat, for site builds |
| `scripts/01-number.py` | Generates `numbered.json` from the source outline |
| `scripts/02-04-*.py` | Generate the three published HTML artifacts |
| `scripts/05-emit-markdown.py` | Generates `content/*.md` and `data/addresses.csv` |
| `artifacts/*.html` | The three published artifacts, as published |

## Regenerating everything

```bash
cd context/scripts
python3 01-number.py              # data/numbered.json  (asserts no address collisions)
python3 05-emit-markdown.py       # content/*.md, data/addresses.csv
python3 02-build-index-artifact.py
python3 03-build-hubs-artifact.py
python3 04-build-rules-artifact.py
```

No dependencies beyond the Python 3 standard library.

## State

- [x] Source outline analysed, numbering scheme designed and verified
- [x] 2,576 addresses generated, collision-free
- [x] Three artifacts published (URLs in `05-design-system.md` and `06-site-plan.md`)
- [x] Context dumped to this folder
- [ ] `git init`, first commit, push to remote — **not done, see `00-project-brief.md`**
- [ ] Astro scaffold
- [ ] GitHub Pages workflow

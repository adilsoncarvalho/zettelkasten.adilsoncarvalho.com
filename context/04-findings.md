# Verified Findings

Everything here was checked against the data, not asserted. Re-running
`scripts/01-number.py` re-verifies the collision assertion.

## Scale

| Metric | Value |
|---|---|
| Total addresses | **2,576** (65 headings + 2,511 list items) |
| Unique addresses | 2,576 — **no collisions** (asserted in `01-number.py`) |
| Four-digit divisions | 65 |
| Longest address | `1020/1b2a` (9 characters) |
| Max depth | 7 levels |
| Source file | 2,719 lines |

## Per-drawer load

| Drawer | Entries | Fill vs. 999 |
|---|---|---|
| `1000` Humanities | 454 | 45% |
| `2000` Social science | 668 | 67% |
| `3000` Natural science | 434 | 43% |
| `4000` Formal science | 273 | 27% |
| `5000` Applied science | 742 | 74% |

Applied science is the tightest, with ~257 free slots and 84 unused discipline numbers.
A flat sequential scheme would have fit, but barely — which is a further argument for
branching rather than flat numbering.

## Fan-out audit

| Level | Groups | Max siblings |
|---|---|---|
| `##` | 1 | 5 |
| `###` | 5 | 15 (Applied science) |
| `####` | 6 | 7 (Engineering and technology) |
| `#####` | 2 | 1 |
| list L1 | 55 | **130** (`### Sociology`, source line 940) |
| list L2 | 222 | 34 |
| list L3 | 68 | 12 |
| list L4 | 6 | 5 |

Source-list indentation is 0/2/4/6 spaces — four list levels, counts
1,138 / 1,161 / 197 / 15.

## Data quirks — these affect rendering

### 1. Multi-letter segments (4 addresses)

Sibling groups exceeding 26 force `aa`-style overflow:

- `2010/7aa` Public anthropology
- `3021/50aa` Zootomy
- `5030/3aa` Special education
- `5110/22aa` Security

**Any address parser must handle multi-character letter segments.**

### 2. Duplicate titles within a division (37 cases)

The source outline lists some disciplines twice under different parents. Examples:

| Title | Addresses |
|---|---|
| Glaciology | `2050/1o`, `2050/1p1` (also `3015/8i` in another division) |
| Latin American history | `1030/9b1`, `1030/10` |
| Feminist philosophy | `1060/2o2`, `1060/8f` |
| Biocultural anthropology | `2010/1a`, `2010/6` |
| Oceanography | `2050/1p4`, `2050/1u` |
| Rhetoric | `1040/9d`, `2060/24` |

Both addresses are valid and distinct. For filing, pick one as live and cross-reference.
**For the site: consider surfacing duplicates as cross-links rather than silently repeating.**

### 3. One malformed source line

`1030/9c4` reads `Mississippian culture* Art History` — a Wikipedia artifact where two
entries collapsed onto one line (`data/academic-disciplines.md:191`). Left verbatim to stay
faithful to source. **Decide whether the site fixes this or renders it as-is with a note.**

### 4. Empty drawer roots

No address branches directly off any `N000` division — all five `N000/…` spaces are
completely empty and available.

## The vocabulary-gap finding

Of 23 terms probed from the owner's keyword list, **22 have no entry in the source outline**.
Only "storytelling" exists (`1010/6d`).

Absent: sales, selling, startup, keto, ketogenic, carnivore, fasting, metabolism, productivity,
attention, habit, note-taking, incentive, persuasion, copywriting, negotiation, pricing,
branding, venture capital, business process, people management, focus.

The outline maps academic disciplines; the owner's interests are practices. Full discussion in
`03-hub-placements.md`. **This shapes the site's framing:** the index is a skeleton of anchors,
not a catalogue to be completed.

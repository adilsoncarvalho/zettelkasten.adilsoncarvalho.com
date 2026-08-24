# Decisions and Rationale

Judgment calls already made. Read before reversing any of them — each was reasoned, and
several were checked against alternatives that looked better at first glance.

## 1. Four digits for all heading levels, `#####` sharing the units tier

**Decision:** every heading in the source gets a 4-digit division number. The two `#####`
headings take the next units digit after their `####` parent's siblings rather than branching.

- `3011` Space sciences → `3012` Astronomy
- `4032` Applied mathematics → `4033` Statistics

**Why:** the digit budget is exactly 1 (drawer) + 2 (discipline) + 1 (sub-discipline) = 4, with
nothing left for a fourth heading tier. Both `#####` cases are only children, so flattening
costs almost nothing and puts the card exactly where a filer reaches.

**Cost:** Astronomy gets a peer number for what is structurally a child of Space sciences.
**Alternative:** `3011a` preserves hierarchy but breaks "every heading is 4 digits."
**Owner was offered the reversal and did not take it.** Status: settled unless asked.

## 2. Alternation, not repeated slashes

**Decision:** one `/` after the division; everything after alternates number/letter.

**Why:** the type switch is already an unambiguous level separator, so a second separator adds
nothing and creates a conflicting signal. Concretely, the owner initially proposed
`1010/1d/1`, which reduces to `1010/1d1` — already Choral conducting. This was caught by
testing the proposal against the real data.

## 3. Hubs at centre of gravity, not at drawer roots

**Decision:** each hub card sits behind its theme's densest anchor.

**Why:** `N000/1` is free in all five drawers and would be legal. It is still wrong, because a
card's neighbours are the payload, and a trunk card's neighbours are every discipline in the
drawer with none of them as its subject.

**Note:** there is a real counter-argument that a hub *does not need* meaningful neighbours,
since its whole job is to point elsewhere. It was rejected for consistency and because a hub
near its material is easier to use in practice. Reasonable to revisit.

## 4. Metabolism filed under clinical practice, not physiology

**Decision:** hub at `5051/1`, behind `5051` Nutrition and metabolic health — not `3050`
Biology.

**Why:** keto and carnivore are protocols, not mechanisms. Practice is the centre of gravity;
the mechanism is one hop away via the hub.

**Superseded coordinates:** this originally read `5100/21a` behind Nutrition and dietetics,
against the source outline. The reasoning survived the re-cut untouched — see §13 — and the
theme now anchors on a row of the personal tier that exists because of these very cards.

## 5. Source text kept verbatim

**Decision:** entry titles reproduce the source exactly, including the malformed
`Mississippian culture* Art History` at `1030/9c4`.

**Why:** the index should be a faithful, auditable derivative of a CC BY-SA source. Silent
cleanup makes the mapping back to `academic-disciplines.md:191` unverifiable.
**Open for the site** — see `06-site-plan.md` question 4.

## 6. Duplicates get distinct addresses

**Decision:** the 37 within-division duplicate titles each keep their own address rather than
being merged.

**Why:** they occupy genuinely different positions in the source hierarchy, and merging would
break the 1:1 correspondence with the source. The filing guidance is to pick one as live and
cross-reference — a *practice*, not a data change.

## 7. The index is a skeleton, not a catalogue

**Not a design decision so much as a finding that should govern the site's framing.**

22 of 23 probed keywords from the owner's actual interests have no entry in the outline. The
numbered entries are anchors for original cards, not a set of slots to fill in. A site that
presents the index as "the knowledge map to complete" would misrepresent how it will be used.

## 8. System font stacks, no webfonts

**Decision:** three system stacks (serif display / sans body / mono data).

**Why:** the artifact CSP blocks font CDNs, and a silently-failed webfont is worse than a
deliberate system stack. If the Astro site self-hosts fonts it is free to change this — but
the mono role must keep `tabular-nums`, because address alignment is functional, not cosmetic.

## 9. The published index is curated, not derived

**Decision:** the site publishes a hand-cut table of 46 divisions and 5 sub-divisions, all
four digits, each with a scope note (`data/divisions.json`). The 2,576-address outline is demoted to a lookup corpus.

**Why:** the derived index was faithful and unusable. It carried four adjacent religion
divisions (`1070` Religious studies, `1080` Divinity, `1090` Theology, `1100` Religion), put
Law under Humanities, and wrapped Physics/Chemistry/Earth science inside a `3010` Physical
Science node while Biology sat at peer level. None of that is wrong about Wikipedia; all of
it is wrong at a card box. And decision 7 already said the leaves were not load-bearing —
22 of 23 probed keywords had no entry among them.

**The model was an external PDF** ("Antinet Zettelkasten Academic Disciplines Index", 53 codes over
three pages) which stops at four digits and adds a *Scope & Filing Examples* column. Its
digit layout was not copied: it spends one digit on the discipline, so a drawer holds nine,
and its Applied drawer already runs 5100–5700. Ours keeps two digits — 99 per drawer.

**Cost:** addresses moved. Anyone who had filed against the derived divisions must renumber
guide cards. Accepted because no physical cards existed at the time, and because the mapping
is published on `/outline` so any old address resolves.

**Second-order effect, and it is the larger one.** A re-cut arrangement with our own scope
notes is not adapted material. Discipline names carry no copyright and the arrangement is no
longer the source's, so the table left CC BY-SA for BY-NC-SA — which unblocks the print
edition that `00-project-brief.md` reserves. The mapping stays BY-SA and stays on `/outline`.

## 10. Sub-divisions are seeded, and said to be seeded

**Decision:** five sub-divisions ship in the table — `5031` note-taking, `5051` nutrition,
`5061` sales, `5062` marketing, `5063` finance — and the page states they are examples.

**Why:** the units digit gives every division nine sub-divisions for free. Leaving all of
them empty would reproduce the vocabulary gap the finding identified; filling them by
anticipation would hand a stranger someone else's interests as if they were canon. Naming
them as seeded is the honest middle.

**The evidence is in the mapping:** `5031` and `5061` are the only two rows that no source
term reaches at all. The academy has no card for note-taking or for selling.

## 11. The filing tiebreak is one rule, not a table of special cases

**Decision:** `/find` names a single rule — *mechanism files with the science, action files
with the practice* — and lists the eleven seams it resolves.

**Why:** the hard calls all turned out to be the same call. Economics/Business,
Biology/Nutrition, Ecology/Sustainability, Computer science/Software engineering,
Political science/Public administration, Literature/Writing all split on that one axis.
Writing eleven tiebreaks would have hidden that they are one.

**Cost:** the rule does not resolve everything. 228 source terms have two defensible homes
regardless, and the page says so rather than pretending otherwise — pick either, cross-
reference the other.

## 12. The table publishes in two tiers, split at the digit

**Decision:** every row carries an explicit `tier`. `core` is the 5 drawers and all 46
divisions — every code ending in zero — published at `/core` as the canonical list. `personal`
is the 5 sub-divisions, published at `/extensions` as one filer's worked example. `/extending`
carries the method. `/find` searches both. `/divisions` redirects to `/core`.

**Why:** decision 10 already said the sub-divisions were seeded rather than canon, but saying
it in a paragraph under the table did not make it true in use. Anyone wanting a canonical list
still had to read the table and decide for themselves which five rows were someone else's
interests, and every future row the owner adds made that worse. Splitting the pages inverts
the default: the canonical list is now adoptable without a caveat, and the personal tier can
grow without ever contaminating it.

**Why the line falls at the digit, and not at "which rows feel academic".** The alternative
considered was a stricter canon that also moved `2100` Futures and foresight and `5150` Home
and personal management — the two thinnest, least academic divisions — onto the personal tier.
Rejected, because the digit line is the only one that states as a rule ("the first three
digits are canon, the fourth is yours") and the only one with evidence behind it. Mapping the
source outline onto the table reaches **every one of the 46 divisions** and misses two
sub-divisions entirely. The canonical tier is exactly the tier the academy can account for,
which is a finding, not a preference. `divisions.test.ts` asserts both halves.

**Second-order effect: three scope notes had to be repointed.** `1060` and `2080` named `5062`
as their tiebreak, and `4070` named `5031` — so the canonical table was sending a reader to
codes it did not contain. They now point at the core parent (`5060`, `5030`). A test forbids a
core scope note from referencing a personal code, because the failure is invisible otherwise:
the link renders, resolves to another page, and reads as canonical.

**`tier` is explicit rather than inferred from `kind`.** Today the two agree exactly, so
inference would work. It would also silently misfile the first division the owner adds of his
own, in a free tens slot — a `personal` row that does not end in a non-zero digit. Explicit
costs one field and removes that failure entirely.

**Follow-on: the published text now says *discipline*, never *division*.** The site had
been using both for the same thing, which read as a distinction that does not exist — and
the split made it worse by adding "core rows" as a third name. One word per tier: drawer,
discipline, sub-discipline. `division` survives only as a code identifier
(`divisions.json`, `kind: "division"`, `divisionOf()`); see the vocabulary table in
`06-site-plan.md`.

**Cost:** two more routes, and the nav is now nine items. Also `/find`'s printed sheet has
three seams that resolve to personal rows; the page names them rather than hiding it.

**What was deliberately not split:** search. The tier split is about what can be published as
canonical, not about what a filer holding a card should be able to find — so the finder covers
both tiers and tags personal hits `mine`. The copyable prompt emits them as two blocks so a
stranger can delete the second.

## 13. The hubs and the worked examples were re-anchored onto the curated index

**Decision:** every published address now names a row of the curated index. The six hubs moved
off source-outline coordinates, and the filing-rules worked example moved with them.

| Theme | Was | Now | Behind |
|---|---|---|---|
| Persuasion | `1040/9d1` | `1060/1` | `1060` Writing and rhetoric |
| Organisations | `2103/11` | `5060/1` | `5060` Business and management |
| Ventures | `2020/8a` | `5060/2` | `5060` Business and management |
| Mind | `2080/62` | `2040/1` | `2040` Psychology |
| Metabolism | `5100/21a` | `5051/1` | `5051` Nutrition and metabolic health |
| Formation | `1090/3c1` | `1020/1` | `1020` Religion and theology |

**Why:** the pages were presenting dead coordinates as current. `1040` is Language and
linguistics now, not Rhetoric's parent, and nothing branches off the outline's own structure
any more. `03-hub-placements.md` carried a warning banner about this; the rendered pages did
not, so a reader had no way to know. Annotating was the alternative and was rejected — a
manual is not the place to teach in coordinates that no longer resolve.

**Anchors were chosen from the data, not by taste.** Each theme's satellites were mapped
through `lookup.json` and the hub placed at the discipline where its material concentrates —
Organisations 13 of 20 satellites at `5060`, Mind 8 of 21 at `2040`, Formation 9 of 21 at
`1020`. Two departures from raw density, both stated on the page:

- **Persuasion** anchors on `1060`, not the denser `2080` Communication and media. `2080`'s
  count is an artefact of the outline's fat journalism node; the theme's live vocabulary is
  sales, copywriting and negotiation, which sit at `1060`, `5061` and `5062`.
- **Metabolism** anchors on `5051`, not the denser `5050` Medicine and health, because `5051`
  is the sub-discipline that exists for exactly these cards.

**Second-order effects, all of them findings rather than costs:**

- **Organisations and Ventures now share an anchor.** Both centre on `5060`, so they sit at
  `5060/1` and `5060/2`. That is what a two-digit discipline tier buys and costs at once:
  fewer, broader rows, with the hub doing the separating instead of the number.
- **The satellite lists changed shape.** They were flat source addresses; each row is now one
  discipline plus the subjects of that theme filing there. That is strictly more useful — it
  shows a hub spanning few disciplines and many subjects — and it dissolved the duplicate
  problem, since `Marketing` and `Marketing (dup)` collapse the moment both resolve to a
  discipline. Organisations lost a whole group to that collapse.
- **The gap table now points at rows that exist.** Sales, note-taking, keto and the rest are
  still absent from the outline, but four of the five rows they file behind today are
  sub-disciplines the personal tier added — which is the clearest evidence for that tier
  anywhere on the site.
- **`/rules` and `02-filing-rules.md` moved too.** The worked example sat at `1040/9d`; it now
  hangs off `1060`, which also let the derivation table show the case a filer meets first,
  where the parent is a bare discipline and no branch exists yet.

## Corrections made during the work

Recorded so they are not silently reintroduced:

- **`1000/1` was claimed to be taken by Music. It is not.** Music is `1010/1`; no address
  branches off any `N000` root.
- **Sociology is `2090`, not `2080`.** `2080` is Psychology. An early filter conflated them.
- **`1010/1e` is Early music, not "early jazz."** Jazz studies is `1010/1f`.
- **Child/sibling was initially framed as two operations.** It is one operation with a
  different parent — the cleaner formulation, and the one in `02-filing-rules.md`.

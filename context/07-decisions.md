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
card's neighbours are the payload — a hub at `1000/1` has 454 unrelated disciplines around it.

**Note:** there is a real counter-argument that a hub *does not need* meaningful neighbours,
since its whole job is to point elsewhere. It was rejected for consistency and because a hub
near its material is easier to use in practice. Reasonable to revisit.

## 4. Metabolism filed under clinical practice, not physiology

**Decision:** hub at `5100/21a`, behind Nutrition and dietetics — not `3021/39` Physiology.

**Why:** keto and carnivore are protocols, not mechanisms. Practice is the centre of gravity;
physiology is one hop away via the hub.

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

## Corrections made during the work

Recorded so they are not silently reintroduced:

- **`1000/1` was claimed to be taken by Music. It is not.** Music is `1010/1`; no address
  branches off any `N000` root.
- **Sociology is `2090`, not `2080`.** `2080` is Psychology. An early filter conflated them.
- **`1010/1e` is Early music, not "early jazz."** Jazz studies is `1010/1f`.
- **Child/sibling was initially framed as two operations.** It is one operation with a
  different parent — the cleaner formulation, and the one in `02-filing-rules.md`.

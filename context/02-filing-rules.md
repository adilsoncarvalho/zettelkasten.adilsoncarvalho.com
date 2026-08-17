# Filing Rules

The operating manual. Published as an artifact; this is the source content.

## The core distinction

Child and sibling are **not two operations**. They are one operation with a different parent.

| You want | Parent is | From `1040/9d1a` you get |
|---|---|---|
| **Child** — digs into the card | the card itself | `1040/9d1a1` |
| **Sibling** — continues past it | the card's parent (drop last segment) | `1040/9d1b` |

The question at the drawer: **does this continue the card in my hand, or dig into it?**
Continue → step back one segment and append. Dig in → append directly.

## Worked sequence

Seven cards filed behind Rhetoric `1040/9d`. Verified against the real data — all addresses
were free before filing.

### Order written

| # | Address | Card | Filed behind |
|---|---|---|---|
| 1 | `1040/9d1` | Persuasion — HUB | `1040/9d` |
| 2 | `1040/9d1a` | Definition of a thesis | `1040/9d1` |
| 3 | `1040/9d1a1` | Thesis vs. hypothesis | `1040/9d1a` |
| 4 | `1040/9d1b` | Ethos, pathos, logos | `1040/9d1` |
| 5 | `1040/9d1b1` | Aristotle, *Rhetoric* Bk I | `1040/9d1b` |
| 6 | `1040/9d1a2` | A thesis must be contestable | `1040/9d1a` |
| 7 | `1040/9d2` | Rhetoric ≠ sophistry | `1040/9d` |

### Order in the drawer

```
1040/9d       Rhetoric — guide card (from the index)
1040/9d1      Persuasion — HUB
1040/9d1a       Definition of a thesis
1040/9d1a1        Thesis vs. hypothesis
1040/9d1a2        A thesis must be contestable      ← written 6th, sits 4th
1040/9d1b       Ethos, pathos, logos
1040/9d1b1        Aristotle, Rhetoric Bk I
1040/9d2      Rhetoric ≠ sophistry
```

**Card 6 is the whole argument for the scheme.** Written sixth, it lands fourth, slotted
between two cards that already existed, with nothing renumbered.

### Derivation

| # | Parent | Ends in | Append | Address |
|---|---|---|---|---|
| 1 | `1040/9d` | letter `d` | number → `1` | `1040/9d1` |
| 2 | `1040/9d1` | number `1` | letter → `a` | `1040/9d1a` |
| 3 | `1040/9d1a` | letter `a` | number → `1` | `1040/9d1a1` |
| 4 | `1040/9d1` | number `1` | letter → `b` (`a` taken) | `1040/9d1b` |
| 5 | `1040/9d1b` | letter `b` | number → `1` | `1040/9d1b1` |
| 6 | `1040/9d1a` | letter `a` | number → `2` (`1` taken) | `1040/9d1a2` |
| 7 | `1040/9d` | letter `d` | number → `2` (`1` taken) | `1040/9d2` |

## The three index devices

Not interchangeable.

| Device | Holds | Lives | Rewritten |
|---|---|---|---|
| **Hub card** | A list of addresses on one theme — a switchboard, not prose | In place, at the theme's centre of gravity | Freely, often |
| **Keyword index** | Term → one or two *entry-point* addresses. Deliberately sparse | Its own drawer, alphabetical | Rarely, by addition |
| **Bibliographic card** | One source, its details, cards drawn from it | Its own drawer, by author | Never — append only |

### What makes a hub card work

A hub is the one card you are *allowed* to rewrite, because it holds no thinking — only
pointers. That licence is what lets it collapse the drawer separation the four-digit numbers
impose: a Persuasion hub can point at `1040/9d`, `5080/4p` and `2020/15` on the same line, and
no filing scheme could have put those three together.

Keep it a list. The moment a hub contains arguments, it has become a card that belongs
somewhere and the index is lost.

For scale calibration: Luhmann's keyword index ran to ~3,200 terms against ~90,000 cards.
Sparse on purpose — you find the door, then follow the branch and the links.

## Never

| Rule | Why |
|---|---|
| **Never renumber a card** | Other cards point at that address, and so does the keyword index. An address is a promise. |
| **Never use more than one slash** | The alternation already marks every level. `1010/1d/1` collides with `1010/1d1` (Choral conducting). |
| **Never file at a drawer root** | `N000/1` is free in all five drawers and still wrong — 454 unrelated disciplines as neighbours, and neighbours are the point. |
| **Never make the branch taxonomic** | The index reads that way only because it was seeded from a taxonomy. Your own cards will not. Forcing it is the Dewey trap one level down. |
| **Never wait for the right category** | There is no right category — only the card this one is talking back to. File behind the nearest anchor and let the hub find it. |

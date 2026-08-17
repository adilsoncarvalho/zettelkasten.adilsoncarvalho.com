# The Numbering Scheme

## Anatomy of an address

```
1040 / 9d1a
└─┬─┘   └┬─┘
  │      └── branch — position only, no meaning. Alternates number → letter → number → letter.
  └───────── division — 4 digits. The ONLY place taxonomy lives.
```

The four digits decompose as:

| Digit(s) | Meaning | Capacity | Widest actual |
|---|---|---|---|
| 1 | Drawer (top-level branch) | 9 | 5 |
| 2–3 | Discipline | 99 | 15 (Applied science) |
| 4 | Sub-discipline | 9 | 7 (Engineering and technology) |

Total budget: 1 + 2 + 1 = **exactly 4 digits**, with nothing to spare. This is why list items
*must* branch rather than consume more digits.

## Why a positional scheme fails

Fan-out audit of the source outline:

| Level | Groups | Max siblings | Digits needed if positional |
|---|---|---|---|
| `##` top | 1 | 5 | 1 |
| `###` | 5 | 15 | 2 |
| `####` | 6 | 7 | 1 |
| `#####` | 2 | 1 | — |
| list L1 | 55 | **130** (Sociology) | 3 |
| list L2 | 222 | 34 | 2 |
| list L3 | 68 | 12 | 2 |
| list L4 | 6 | 5 | 1 |

A digit-per-level scheme would need **~11 digits**. A Dewey-style block allocation
(`1000 / 1100 / 1110 / 1111`) gives only 9 slots per level and fails at `###` immediately.

Scheper's scheme sidesteps this: the four digits identify the *division*, and depth is carried
by an unbounded suffix. Sociology's 130 flat children become `2090/1` … `2090/130` with no
capacity pressure at all.

## Branch grammar

After the single `/`, segments alternate:

```
number → letter → number → letter → …
```

**The type switch is the level separator.** No further punctuation is needed or permitted:
consecutive digits form one segment, consecutive letters form one segment. So `3021/50aa`
reads unambiguously as `50` → `aa`, and `1010/1d10` reads as `1` → `d` → `10`.

Letters run `a`…`z`, then `aa`, `ab`, … (spreadsheet-column style). Four addresses in the
current data need multi-letter segments — see `04-findings.md`.

**Using `/` more than once is a bug.** It creates a second, conflicting depth signal, and it
collides: `1010/1d/1` reduces to `1010/1d1`, which is already Choral conducting.

## Division allocation

Within a thousand-block, disciplines are numbered by tens (`N010`, `N020`, …) and
sub-disciplines take the units digit (`N011`, `N012`, …).

**The one judgment call:** `#####` headings share the units tier with their `####` siblings
rather than branching. This occurs exactly twice in the source, and in both cases the `#####`
is an only child:

- `3011` Space sciences → `3012` Astronomy (Astronomy is a `#####` *inside* Space sciences)
- `4032` Applied mathematics → `4033` Statistics (same shape)

The effect is that Astronomy gets a peer number for a child concept, but sits immediately
after its parent in the drawer — which is where a filer reaches for it. The alternative
(`3011a`) preserves the hierarchy at the cost of every heading no longer being 4 digits.
See `07-decisions.md`.

## Computing the next address

1. Decide which card the new one hangs off — the **parent**.
2. Parent's last segment ends in a **number** → append a **letter**.
   Ends in a **letter** → append a **number**.
3. Take the next unused one. Permanent.

**Child vs sibling is the same operation with a different parent:**

- Child of `X` → parent is `X` → append
- Sibling of `X` → parent is `X` minus its last segment → append

## Sort order

The drawer is ordered by this key. Numeric segments compare **numerically**, not
lexically — `2090/9` sorts before `2090/10`.

```python
import re
def key(addr):
    div, _, br = addr.partition('/')
    k = [int(div)]
    for s in re.findall(r'\d+|[a-z]+', br):
        k.append((0, int(s), '') if s.isdigit() else (1, 0, s))
    return k
```

The tuple shape `(type, number, letters)` makes a numeric segment sort before a letter segment
at the same position, which is what makes a child sit between its parent and the parent's next
sibling. This function is the reference implementation — **the site's sorting must match it.**

## Insertion

There is no "between", only "behind". To place a card between `X` and the card after it,
append to `X`; sorting does the rest.

The one genuine limit: nothing can sit between a card and its own *first* child. That gap is
closed and does not matter, because sibling order carries no meaning.

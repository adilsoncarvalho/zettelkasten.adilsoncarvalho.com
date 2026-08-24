#!/usr/bin/env python3
"""Map the source-outline addresses onto the curated division index.

The outline (`numbered.json`) stops being the published index and becomes the
lookup corpus behind the category finder: 2,576 discipline names, each pointing
at the curated division a card on that subject belongs in.

Mapping is by legacy division. Where one legacy division splits across several
curated ones, the split is resolved on the division's first-level children,
which is the coarsest level at which the split is unambiguous.

Emits `data/lookup.json`.
"""

import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"

# Legacy 4-digit division -> curated division.
DIVISION_MAP = {
    # Humanities
    "1000": "1000",  # Humanities (drawer)
    "1010": "1080",  # Performing arts
    "1020": "1070",  # Visual arts
    "1030": "1030",  # History
    "1040": "1050",  # Languages and literature -> Literature (see CHILD_MAP)
    "1050": "5070",  # Law -> Applied
    "1060": "1010",  # Philosophy
    "1070": "1020",  # Religious studies  ┐
    "1080": "1020",  # Divinity           ├ collapse to Religion and theology
    "1090": "1020",  # Theology           │
    "1100": "1020",  # Religion           ┘
    # Social science
    "2000": "2000",  # Social science (drawer)
    "2010": "2010",  # Anthropology
    "2011": "2020",  # Archaeology -> own division
    "2020": "5060",  # Business -> Applied
    "2030": "2050",  # Economics
    "2040": "2100",  # Futurology -> Futures and foresight
    "2050": "2070",  # Geography
    "2060": "1040",  # Linguistics -> Humanities (see CHILD_MAP)
    "2070": "2060",  # Political science
    "2080": "2040",  # Psychology
    "2090": "2030",  # Sociology
    "2100": "2090",  # Interdisciplinary studies
    "2101": "2090",  # Area studies
    "2102": "2090",  # Ethnic and cultural studies
    "2103": "5060",  # Organizational studies -> Business and management
    # Natural science
    "3000": "3000",  # Natural science (drawer)
    "3010": "3010",  # Physical Science (wrapper, no direct children)
    "3011": "3030",  # Space sciences
    "3012": "3030",  # Astronomy
    "3013": "3010",  # Physics
    "3014": "3020",  # Chemistry
    "3015": "3040",  # Earth science
    "3020": "3050",  # Life science
    "3021": "3050",  # Biology
    # Formal science
    "4000": "4000",  # Formal science (drawer)
    "4010": "4040",  # Computer science (see CHILD_MAP)
    "4020": "4010",  # Logic
    "4030": "4020",  # Mathematics
    "4031": "4020",  # Pure mathematics
    "4032": "4020",  # Applied mathematics
    "4033": "4030",  # Statistics
    # Applied science
    "5000": "5000",  # Applied science (drawer)
    "5010": "5010",  # Agriculture
    "5020": "5020",  # Architecture and design
    "5030": "5030",  # Education
    "5040": "5040",  # Engineering and technology
    "5041": "5040",  # Chemical engineering
    "5042": "5040",  # Civil engineering
    "5043": "5030",  # Educational technology
    "5044": "5040",  # Electrical engineering
    "5045": "5040",  # Materials science
    "5046": "5040",  # Mechanical engineering
    "5047": "4070",  # Systems science -> Information and systems science
    "5050": "5090",  # Environmental studies and forestry
    "5060": "5150",  # Family and consumer science
    "5070": "5130",  # Human physical performance and recreation
    "5080": "2080",  # Journalism, media studies and communication
    "5090": "5100",  # Library and museum studies
    "5100": "5050",  # Medicine and health
    "5110": "5080",  # Military sciences
    "5120": "5110",  # Public administration
    "5130": "5110",  # Public policy
    "5140": "5120",  # Social work
    "5150": "5140",  # Transportation
}

# Legacy first-level branch -> curated division, overriding DIVISION_MAP for
# that address and everything beneath it. Only for divisions that genuinely
# split; each entry is a subject the parent division no longer covers.
CHILD_MAP = {
    "1040/11": "1040",  # Languages           -> Language and linguistics
    "1040/4": "1060",  # Creative writing     -> Writing and rhetoric
    "2060/24": "1060",  # Rhetoric            -> Writing and rhetoric
    "2060/2": "1060",  # Composition studies  -> Writing and rhetoric
    "4010/4": "4060",  # Artificial intelligence
    "4010/22": "4050",  # Software engineering
    "5060/3": "5020",  # Interior design      -> Architecture and design
    # Ecology is listed three times in the source, under Earth science,
    # Biology, and Environmental studies. All three are the science.
    "3015/11": "3060",
    "3021/15": "3060",
    "5050/8": "3060",
    # Business splits into the seeded practice sub-divisions.
    "2020/5": "5070",  # Business law         -> Law and jurisprudence
    "2020/10": "5063",  # Finance             -> Finance and investing
    "2020/15": "5062",  # Marketing           -> Marketing and branding
    "2020/20": "4070",  # Systems science     -> Information and systems science
    "5080/4a": "5062",  # Advertising
    "5080/4k": "5062",  # Marketing
    "5080/4q": "5062",  # Public relations
    # Nutrition as practice, in both places the source lists it.
    "5060/4": "5051",
    "5100/21": "5051",
}


def branch_prefixes(num):
    """Every ancestor address of `num`, longest first, including itself.

    `2060/24a1` yields `2060/24a1`, `2060/24a`, `2060/24`. Segment boundaries
    follow the branch grammar: a run of digits or a run of letters.
    """
    div, _, br = num.partition("/")
    if not br:
        return []
    out, cur = [], ""
    for ch in br:
        if cur and ch.isdigit() != cur[-1].isdigit():
            out.append(f"{div}/{cur}")
        cur += ch
    out.append(f"{div}/{cur}")
    return list(reversed(out))


def main():
    entries = json.loads((DATA / "numbered.json").read_text())
    divisions = json.loads((DATA / "divisions.json").read_text())
    valid = {d["code"] for d in divisions}
    names = {d["code"]: d["name"] for d in divisions}

    unknown = {c for c in DIVISION_MAP.values() if c not in valid}
    unknown |= {c for c in CHILD_MAP.values() if c not in valid}
    assert not unknown, f"map targets not in divisions.json: {sorted(unknown)}"

    legacy_divisions = {e["num"] for e in entries if "/" not in e["num"]}
    missing = legacy_divisions - set(DIVISION_MAP)
    assert not missing, f"legacy divisions with no mapping: {sorted(missing)}"

    lookup = []
    for e in entries:
        div = e["num"].split("/")[0]
        target = next(
            (CHILD_MAP[p] for p in branch_prefixes(e["num"]) if p in CHILD_MAP),
            DIVISION_MAP[div],
        )
        lookup.append(
            {
                "term": e["t"],
                "division": target,
                "divisionName": names[target],
                "source": e["num"],
            }
        )

    assert len(lookup) == len(entries), "lost entries while mapping"
    (DATA / "lookup.json").write_text(json.dumps(lookup, indent=0) + "\n")

    covered = {r["division"] for r in lookup}
    empty = sorted(valid - covered)
    print(f"mapped {len(lookup)} terms onto {len(covered)} of {len(valid)} divisions")
    if empty:
        print(f"no source terms map to: {', '.join(empty)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

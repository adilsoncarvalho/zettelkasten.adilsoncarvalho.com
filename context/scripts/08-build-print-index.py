#!/usr/bin/env python3
"""Emit a print-ready HTML page of the division index.

Laid out to match the printed index this table was modelled on — US Letter,
Helvetica, a three-column table with a header row repeated on every page — so
that setting the two side by side compares the taxonomy rather than the
typography.

Render to PDF with headless Chrome:

    chrome --headless --disable-gpu --no-pdf-header-footer \\
           --print-to-pdf=<out>.pdf file://<abs path to the emitted html>
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "artifacts" / "division-index-print.html"

TITLE = "Antinet Zettelkasten Discipline Index"
INTRO = (
    "The canonical taxonomy of a working Antinet: five drawers and {divisions} disciplines, "
    "every code four digits and every code ending in zero. There is deliberately nothing "
    "beneath it \u2014 position past the discipline carries no meaning and is grown from your own "
    "cards. The third column is the filing aid: it says what belongs here, and where two "
    "disciplines compete it names the winner. Each discipline keeps nine free units digits for "
    "the sub-disciplines your own cards earn; the author's are listed separately overleaf, "
    "as an example rather than as part of the list."
)
MINE_TITLE = "The author's sub-disciplines \u2014 not part of the canonical list"
MINE_INTRO = (
    "These {personal} rows are one filer's own, each taking a free units digit under a core "
    "discipline. They are printed here so the notation is legible in use, not because they "
    "should be adopted. Cut yours where your cards ask for them."
)
RULE = (
    "When two disciplines both fit, the card is usually explaining a mechanism or guiding an "
    "action. Mechanism files with the science; action files with the practice."
)

CSS = """
@page { size: Letter; margin: 0.75in 0.7in; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font: 9pt/1.35 Helvetica, Arial, sans-serif;
  color: #000;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
h1 { font-size: 17pt; margin: 0 0 6pt; letter-spacing: -0.2pt; }
.intro { font-size: 8.6pt; line-height: 1.45; margin: 0 0 8pt; max-width: 46em; }
.rule {
  font-size: 8.6pt;
  line-height: 1.45;
  margin: 0 0 12pt;
  padding: 5pt 8pt;
  border-left: 2pt solid #8a6a2f;
  background: #f3f1ec;
}
.rule b { letter-spacing: 0.1pt; }
table { width: 100%; border-collapse: collapse; }
thead { display: table-header-group; }
th {
  text-align: left;
  font-size: 7.2pt;
  letter-spacing: 0.5pt;
  text-transform: uppercase;
  padding: 0 6pt 3pt 0;
  border-bottom: 0.75pt solid #000;
}
tr { break-inside: avoid; }
td {
  padding: 3.2pt 6pt 3.2pt 0;
  border-bottom: 0.4pt solid #cfcfcf;
  vertical-align: top;
}
td.code { width: 44pt; font-weight: bold; font-variant-numeric: tabular-nums; }
td.name { width: 148pt; }
td.scope { font-size: 8.4pt; color: #333; }
tr.drawer td {
  padding-top: 9pt;
  border-bottom: 0.75pt solid #000;
  font-weight: bold;
}
tr.drawer td.scope { font-weight: normal; font-style: italic; color: #555; }
tr.sub td.name { padding-left: 10pt; }
tr.sub td.code { padding-left: 8pt; font-weight: normal; }
h2.mine {
  font-size: 11pt;
  margin: 16pt 0 5pt;
  padding-top: 8pt;
  border-top: 0.75pt solid #000;
  break-before: auto;
}
.foot {
  margin-top: 14pt;
  padding-top: 6pt;
  border-top: 0.4pt solid #cfcfcf;
  font-size: 7.4pt;
  color: #555;
}
"""


def esc(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def main():
    divisions = json.loads((DATA / "divisions.json").read_text())

    def render(rows_in):
        out = []
        for d in rows_in:
            if d["kind"] == "drawer":
                cls = "drawer"
                name = f"{esc(d['name'])} (drawer)"
            else:
                cls = "sub" if d["kind"] == "subdivision" else ""
                name = esc(d["name"])
            out.append(
                f'<tr class="{cls}">'
                f'<td class="code">{d["code"]}</td>'
                f'<td class="name">{name}</td>'
                f'<td class="scope">{esc(d["scope"])}</td>'
                "</tr>"
            )
        return chr(10).join(out)

    # The two tiers print as two tables. A canonical list that silently carries
    # one person's sub-disciplines is the thing this split exists to prevent.
    core = [d for d in divisions if d["tier"] == "core"]
    mine = [d for d in divisions if d["tier"] == "personal"]
    rows = render(core)
    mine_rows = render(mine)

    counts = {
        k: sum(1 for d in divisions if d["kind"] == k)
        for k in ("drawer", "division", "subdivision")
    }

    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{esc(TITLE)}</title>
<style>{CSS}</style>
</head><body>
<h1>{esc(TITLE)}</h1>
<p class="intro">{esc(INTRO.format(divisions=counts["division"]))}</p>
<p class="rule"><b>The tiebreak.</b> {esc(RULE)}</p>
<table>
<thead><tr>
  <th>Code</th><th>Discipline</th><th>Scope &amp; filing examples</th>
</tr></thead>
<tbody>
{rows}
</tbody></table>
<h2 class="mine">{esc(MINE_TITLE)}</h2>
<p class="intro">{esc(MINE_INTRO.format(personal=len(mine)))}</p>
<table>
<thead><tr>
  <th>Code</th><th>Sub-discipline</th><th>Scope &amp; filing examples</th>
</tr></thead>
<tbody>
{mine_rows}
</tbody></table>
<p class="foot">
  {counts['drawer']} drawers &middot; {counts['division']} disciplines, all canonical &middot;
  {counts['subdivision']} sub-disciplines, none of them canonical &middot; a code ending in a
  non-zero digit is a sub-discipline of the code above it ending in zero.
  zettelkasten.adilsoncarvalho.com &middot; CC BY-NC-SA 4.0
</p>
</body></html>
"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    print(f"{OUT.relative_to(ROOT)}  {len(core)} core + {len(mine)} personal rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())

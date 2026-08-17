"""Emit the site-ready Markdown from data/numbered.json.  Run from context/scripts/."""
import json, re
o=json.load(open('../data/numbered.json'))
divs=[x for x in o if x['k']=='h']

# ---- division map ----
L=["# The 65 Divisions","",
   "The four-digit numbers. These are the guide cards — the only place taxonomy lives.",
   "Everything after a `/` is position, not meaning.","",
   "| Address | Level | Division | Note |","|---|---|---|---|"]
for x in divs:
    lvl=['Branch','Discipline','Sub-discipline','Sub-sub'][x['depth']]
    ind='&nbsp;'*(x['depth']*4)
    L.append(f"| `{x['num']}` | {lvl} | {ind}{x['t']} | {x['note'] or ''} |")
open('../content/division-map.md','w').write('\n'.join(L)+'\n')

# ---- full numbered outline ----
M=["# Numbered Outline","",
   f"All {len(o):,} addresses, in drawer order. Generated from `data/numbered.json`.","",
   "Indentation reflects the source outline's nesting. Addresses are permanent.",""]
for x in o:
    if x['k']=='h':
        hashes='#'*min(x['depth']+2,6)
        M.append('')
        M.append(f"{hashes} `{x['num']}` {x['t']}")
        if x['note']: M.append(f"_{x['note']}_")
        M.append('')
    else:
        M.append(f"{'  '*(x['depth']-4)}- `{x['num']}` {x['t']}")
open('../content/numbered-outline.md','w').write('\n'.join(M)+'\n')

# ---- machine-readable flat CSV for the site build ----
import csv
with open('../data/addresses.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['address','kind','depth','title','source_line','note'])
    for x in o: w.writerow([x['num'],x['k'],x['depth'],x['t'],x['ln'],x['note'] or ''])

print(f"content/division-map.md      {len(divs)} divisions")
print(f"content/numbered-outline.md  {len(o):,} entries")
print(f"data/addresses.csv           {len(o):,} rows")

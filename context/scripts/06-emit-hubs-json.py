"""Emit data/hubs.json from the THEMES structure in 03-build-hubs-artifact.py,
so the site, the artifact and 03-hub-placements.md cannot drift apart."""
import json
src = open('03-build-hubs-artifact.py').read()
ns = {}
exec(src.split('CSS = """')[0], ns)           # data section only, not the HTML builder

themes = [
    {"name": nm, "hub": hub, "anchor": anc, "anchorTitle": anct, "why": why,
     "groups": [{"name": g, "items": [{"address": a, "title": t} for a, t in items]}
                for g, items in groups]}
    for nm, hub, anc, anct, why, groups in ns['THEMES']
]
gaps = [{"theme": t, "absent": g, "fileBehind": a.replace('&middot;', '·')}
        for t, g, a in ns['GAPS']]

json.dump({"themes": themes, "gaps": gaps}, open('../data/hubs.json', 'w'), indent=2, ensure_ascii=False)
print(f"data/hubs.json — {len(themes)} themes, "
      f"{sum(len(i['items']) for t in themes for i in t['groups'])} satellites, {len(gaps)} gaps")

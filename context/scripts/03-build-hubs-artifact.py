THEMES = [
 ("Persuasion","1060/1","1060","Writing and rhetoric",
  "Rhetoric is the spine, and the re-cut finally gave it a home of its own: 1060 Writing and rhetoric, the craft rather than the criticism. The outline listed rhetoric twice and the copy under literary theory maps to 1050 Literature — that is the reading of it, not the doing. Everything else here is an application: channel at 2080, influence at 5062, and selling at 5061, which the academy has no word for at all.",
  [("Craft",[("1050",["Literary theory","Poetics"]),("1060",["Creative writing","Literary journalism"]),("1080",["Storytelling"]),("2080",["Narratology"])]),
   ("Channel",[("2080",["Journalism, media studies & communication","Communication studies","Speech communication","Nonverbal communication","Technical writing","Communication design"])]),
   ("Influence",[("2080",["Propaganda","Popular culture studies"]),("5062",["Advertising","Public relations"])]),
   ("Mechanism",[("1040",["Discourse analysis","Pragmatics","Semiotics"]),("1060",["Rhetoric"])])]),

 ("Organisations","5060/1","5060","Business and management",
  "The outline gave organizational studies its own node and then duplicated management, HR and industrial organization across two more. The re-cut folds all of it into 5060 Business and management, which dissolves this theme's duplicate problem outright: what needed two groups and a pick-the-live-branch note is now one guide card.",
  [("Core",[("5060",["Management","Organizational behavior","Organization theory","Project management","Human resources management","Quality control","Industrial & labor relations","Collective bargaining","Corporate governance","Operations management","Decision science"])]),
   ("Behaviour & theory",[("2030",["Organizational theory","Critical management studies"]),("2040",["Organizational psychology"]),("2080",["Organizational communication"])]),
   ("Systems & leadership",[("4070",["Systems engineering","Management cybernetics"]),("5030",["Educational leadership"]),("5080",["Leadership","Supply chain management"])])]),

 ("Ventures","5060/2","5060","Business and management",
  "Entrepreneurship was a single childless bullet in the outline, which tells you how thinly the academy treats it — expect this branch to be almost entirely your own cards. It shares 5060 with Organisations, so the two hubs sit side by side at 5060/1 and 5060/2. The money side reaches into 5063 Finance and investing, the product side into 5020 Architecture and design.",
  [("Venture core",[("2050",["Entrepreneurial economics"]),("5060",["Business administration","Business analysis","E-Business","Strategy / Strategic Management"])]),
   ("Product",[("5020",["Industrial design (product design)","User experience design","Interaction design","Information architecture"])]),
   ("Money",[("2030",["Sociology of finance"]),("2050",["Public finance"]),("4040",["Computational finance"]),("5060",["Risk management & insurance"])]),
   ("Market forces",[("2050",["Microeconomics","Industrial organization","Consumer economics","Behavioural economics"]),("5060",["Industrial organization","International trade"])])]),

 ("Mind","2040/1","2040","Psychology",
  "Psychology was the largest single branch in the outline, 61 children, and the re-cut keeps it whole at 2040. Decision-making is still genuinely split — now across 2040, 2050 Economics, 4030 Statistics and probability and 1010 Philosophy — so the hub card earns its keep here more than anywhere else.",
  [("Psychology proper",[("2040",["Cognitive psychology","Positive psychology","Problem solving","Personality psychology","Evolutionary psychology","Social psychology","Psychometrics"])]),
   ("Substrate",[("2040",["Neuropsychology"]),("3050",["Neuroscience","Behavioral neuroscience"]),("4060",["Cognitive science"])]),
   ("Decision-making",[("2050",["Behavioural economics"]),("4020",["Decision analysis"]),("4030",["Decision theory"]),("5060",["Decision science"])]),
   ("Learning & knowing",[("1010",["Epistemology","Philosophy of mind","Philosophy of perception"]),("5030",["Educational psychology","Mastery learning","Cooperative learning"])])]),

 ("Metabolism","5051/1","5051","Nutrition and metabolic health",
  "The one hub that sits behind the personal tier. 5051 Nutrition and metabolic health exists because cards like these had nowhere to go: 5050 Medicine and health is the clinic and 3050 Biology is the mechanism. Practice wins the hub because keto and fasting are protocols, not physiology — and the satellites keep 3050 one hop away, which is the whole point of the seam.",
  [("Clinical",[("5050",["Internal medicine","Endocrinology","Gastroenterology","Clinical biochemistry","Public health"])]),
   ("Mechanism",[("3020",["Biochemistry"]),("3050",["Physiology","Human physiology","Endocrinology","Biochemistry"])]),
   ("Performance",[("3050",["Exercise physiology"]),("5050",["Sports medicine"]),("5130",["Exercise physiology","Kinesiology / Performance science"])]),
   ("Food as system",[("2010",["Nutritional anthropology"]),("2030",["Sociology of food"]),("3050",["Nutrition"]),("5010",["Food science"]),("5110",["Food policy"])])]),

 ("Formation","1020/1","1020","Religion and theology",
  "The widest-spanning theme, and the one the re-cut helped most. The outline carried four adjacent religion nodes — religious studies, divinity, theology, religion — and they are now one discipline at 1020. Catholic theology is the centre of gravity for formation specifically; ethics and philosophy at 1010 hang off it as satellites rather than the reverse.",
  [("Theology",[("1020",["Christian theology","Divinity","Moral theology","Christian ethics","Systematic theology","Dogmatic theology"])]),
   ("Sources & practice",[("1020",["Hermeneutics","Biblical studies / Sacred Scripture","Liturgy"]),("1030",["Ecclesiastical history of the Catholic Church"]),("5070",["Canon law"])]),
   ("Ethics & philosophy",[("1010",["Ethics","Normative ethics","Virtue ethics","Applied ethics","Medieval philosophy","Philosophy of religion"])]),
   ("Letters & memory",[("1030",["Intellectual history"]),("1050",["Classics","History of literature","Comparative literature"])])]),

]

GAPS = [
 ("Persuasion","sales, selling, copywriting, negotiation, branding, pricing","5061 Sales and negotiation &middot; 5062 Marketing and branding"),
 ("Organisations","incentives, business process, people management","5060 Business and management"),
 ("Ventures","startups, venture capital","5063 Finance and investing &middot; 5060 Business and management"),
 ("Mind","productivity, attention, focus, habit, note-taking","2040 Psychology &middot; 5031 Note-taking and knowledge systems"),
 ("Metabolism","keto, carnivore, fasting, metabolism","5051 Nutrition and metabolic health"),
]

CSS = """
:root{--ground:#F2F3F1;--surface:#FFFFFF;--ink:#1B2430;--muted:#6B7580;--rule:#D8DBD6;
 --brass:#8A6A2F;--brass-dim:#A98B4E;--tint:#E7E9E5;--focus:#8A6A2F;--warn:#8C4A2F}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#151A1F;--surface:#1D242B;--ink:#E3E6E2;--muted:#8D97A1;--rule:#2C353D;
 --brass:#C9A227;--brass-dim:#9C8330;--tint:#222A31;--focus:#C9A227;--warn:#D08A5E}}
:root[data-theme="dark"]{--ground:#151A1F;--surface:#1D242B;--ink:#E3E6E2;--muted:#8D97A1;
 --rule:#2C353D;--brass:#C9A227;--brass-dim:#9C8330;--tint:#222A31;--focus:#C9A227;--warn:#D08A5E}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
 font:15px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:58rem;margin:0 auto;padding:0 1.25rem 6rem}
header{padding:3.5rem 0 2rem;border-bottom:1px solid var(--rule)}
h1{font:400 2.6rem/1.1 ui-serif,Georgia,serif;margin:0 0 .6rem;letter-spacing:-.015em;text-wrap:balance}
.sub{color:var(--muted);max-width:64ch;margin:0}
h2{font:400 1.3rem/1.2 ui-serif,Georgia,serif;margin:3.5rem 0 .4rem;padding-top:2rem;border-top:1px solid var(--rule)}
.lede{color:var(--muted);margin:0 0 1.5rem;max-width:66ch;font-size:.93rem}
mono,code,.ad{font-family:ui-monospace,"SF Mono",Menlo,monospace;font-variant-numeric:tabular-nums}
/* summary strip */
.strip{display:grid;gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden;margin-top:1.5rem}
.strip a{display:flex;gap:1rem;align-items:baseline;background:var(--surface);padding:.65rem .95rem;text-decoration:none;color:inherit}
.strip a:hover{background:var(--tint)}
.strip .ad{font-weight:600;font-size:.87rem;color:var(--brass);flex:0 0 6rem}
.strip .nm{font:600 .97rem ui-serif,Georgia,serif;flex:0 0 9rem}
.strip .bh{color:var(--muted);font-size:.87rem}
/* theme blocks */
.th{background:var(--surface);border:1px solid var(--rule);border-radius:3px;padding:1.6rem;margin-bottom:1.5rem}
.th h3{font:600 1.45rem/1.1 ui-serif,Georgia,serif;margin:0 0 .2rem}
.anchor{display:flex;flex-wrap:wrap;gap:.5rem 1.5rem;align-items:baseline;margin:.9rem 0 1rem;
 padding:.7rem .9rem;background:var(--tint);border-left:3px solid var(--brass);border-radius:2px}
.anchor b{font-family:ui-monospace,Menlo,monospace;font-size:1.05rem;color:var(--brass);font-variant-numeric:tabular-nums}
.anchor span{font-size:.83rem;color:var(--muted);letter-spacing:.05em;text-transform:uppercase}
.why{color:var(--muted);font-size:.9rem;margin:0 0 1.4rem;max-width:66ch}
.grp{margin-bottom:1.1rem}
.grp h4{font:500 .7rem/1 ui-sans-serif,sans-serif;letter-spacing:.11em;text-transform:uppercase;
 color:var(--muted);margin:0 0 .5rem;padding-bottom:.35rem;border-bottom:1px solid var(--rule)}
.grp ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(19rem,1fr));gap:.1rem .5rem}
.grp li{display:flex;gap:.7rem;align-items:baseline;padding:.12rem 0;font-size:.9rem}
.grp .ad{font-size:.79rem;color:var(--brass-dim);flex:0 0 5.2rem}
/* gaps */
.gap{border-collapse:collapse;width:100%;font-size:.9rem}
.gap th{text-align:left;font:500 .7rem/1 ui-sans-serif,sans-serif;letter-spacing:.1em;
 text-transform:uppercase;color:var(--muted);padding:.5rem .7rem;border-bottom:1px solid var(--rule)}
.gap td{padding:.55rem .7rem;border-bottom:1px solid var(--rule);vertical-align:top}
.gap td:first-child{font:600 .93rem ui-serif,Georgia,serif;white-space:nowrap}
.gap td:nth-child(2){color:var(--warn)}
.gap td:last-child{font-family:ui-monospace,Menlo,monospace;font-size:.78rem;color:var(--muted)}
.callout{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--brass);
 border-radius:2px;padding:1.2rem 1.4rem;margin:1.5rem 0}
.callout p{margin:0 0 .7rem;max-width:64ch}.callout p:last-child{margin:0}
.tbl{overflow-x:auto}
@media(max-width:640px){h1{font-size:2rem}.strip a{flex-wrap:wrap;gap:.2rem .8rem}
 .strip .ad,.strip .nm{flex-basis:auto}.grp li{flex-wrap:wrap;gap:0 .7rem}.grp .ad{flex-basis:100%}}
"""

blocks=[]
for nm,hub,anc,anct,why,groups in THEMES:
    gs=[]
    for gname,items in groups:
        lis=''.join(f'<li><span class="ad">{c}</span><span>{", ".join(ts)}</span></li>'
                    for c,ts in items)
        gs.append(f'<div class="grp"><h4>{gname}</h4><ul>{lis}</ul></div>')
    blocks.append(f"""<div class="th" id="{nm.lower()}">
<h3>{nm}</h3>
<div class="anchor"><span>Hub card</span><b>{hub}</b><span>behind</span><b>{anc}</b><span>{anct}</span></div>
<p class="why">{why}</p>{''.join(gs)}</div>""")

strip=''.join(f'<a href="#{nm.lower()}"><span class="ad">{hub}</span><span class="nm">{nm}</span>'
              f'<span class="bh">behind {anc} &middot; {anct}</span></a>' for nm,hub,anc,anct,_,_ in THEMES)

gaprows=''.join(f'<tr><td>{t}</td><td>{g}</td><td>{a}</td></tr>' for t,g,a in GAPS)

HTML=f"""<title>Hub Card Placements</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<div class="wrap">
<header>
<h1>Hub Card Placements</h1>
<p class="sub">Where your six standing interests live in the Antinet Discipline Index &mdash; the address to write on each hub card, and the disciplines that hub should point into.</p>
</header>

<h2>The six hubs</h2>
<p class="lede">Write these six cards first. Each one is a list of addresses, not prose &mdash; a switchboard you rewrite freely as the collection grows.</p>
<div class="strip">{strip}</div>

<h2>Theme by theme</h2>
<p class="lede">Satellites are grouped by the role they play, not by drawer &mdash; a hub card's job is to collapse the drawer separation, so grouping by number would defeat it. Each row is one discipline of the index and the subjects of this theme that file there.</p>
{''.join(blocks)}

<h2>The vocabulary gap</h2>
<p class="lede">Of 23 terms from your list that I probed for, <b>22 have no entry in the outline at all</b> &mdash; only &ldquo;storytelling&rdquo; exists (<span class="ad">1010/6d</span>).</p>
<div class="tbl"><table class="gap">
<tr><th>Theme</th><th>Absent from the outline</th><th>File behind</th></tr>
{gaprows}
</table></div>
<div class="callout">
<p>This is the most useful thing the search turned up, and it is not a defect in the index. The outline maps <em>academic disciplines</em> &mdash; how universities partition inquiry. Your interests are largely <em>practices</em>: things people do, sell, cook, and pray. The academy has no chair of keto.</p>
<p>So expect the shape of your Antinet to invert the index. The 2,576 pre-numbered entries are a <strong>skeleton of anchors</strong>, and the overwhelming majority of your cards will be your own thinking branching off them &mdash; not entries you fill in. A card on carnivore adaptation is not a missing discipline; it is <span class="ad">5051/1</span>&rsquo;s descendant, and it will sit among dozens of siblings that Wikipedia never imagined.</p>
<p>Which is the argument for keeping the keyword index sparse and the hub cards fat. The numbers cannot find your material, because your material is not what was numbered.</p>
</div>
</div>
"""
open('../artifacts/hub-placements.html','w').write(HTML)
print("written:", len(HTML), "bytes")

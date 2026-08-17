import json, html
o = json.load(open('../data/numbered.json'))
E = html.escape

divs = [x for x in o if x['k']=='h']
tot  = len(o)

# division map
dmap=[]
for x in divs:
    cls = ['dv', f"dv{x['depth']}"]
    note = f'<span class="nt">{E(x["note"])}</span>' if x['note'] else ''
    dmap.append(f'<a class="{" ".join(cls)}" href="#n{x["num"]}"><span class="a">{x["num"]}</span><span class="t">{E(x["t"])}{note}</span></a>')

# full outline
rows=[]
for x in o:
    d = x['depth']
    if x['k']=='h':
        note = f'<span class="nt">{E(x["note"])}</span>' if x['note'] else ''
        rows.append(f'<div class="r h h{d}" id="n{x["num"]}" data-s="{E(x["t"].lower())} {x["num"]}" data-d="{d}">'
                    f'<span class="a">{x["num"]}</span><span class="t">{E(x["t"])}{note}</span></div>')
    else:
        num=x['num']; div,suf = num.split('/')
        rows.append(f'<div class="r b b{d}" data-s="{E(x["t"].lower())} {E(num)}" data-d="{d}">'
                    f'<span class="a"><i>{div}/</i>{E(suf)}</span><span class="t">{E(x["t"])}</span></div>')

CSS = """
:root{
  --ground:#F2F3F1; --surface:#FFFFFF; --ink:#1B2430; --muted:#6B7580;
  --rule:#D8DBD6; --brass:#8A6A2F; --brass-dim:#A98B4E; --tint:#E7E9E5; --focus:#8A6A2F;
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --ground:#151A1F; --surface:#1D242B; --ink:#E3E6E2; --muted:#8D97A1;
  --rule:#2C353D; --brass:#C9A227; --brass-dim:#9C8330; --tint:#222A31; --focus:#C9A227;
}}
:root[data-theme="dark"]{
  --ground:#151A1F; --surface:#1D242B; --ink:#E3E6E2; --muted:#8D97A1;
  --rule:#2C353D; --brass:#C9A227; --brass-dim:#9C8330; --tint:#222A31; --focus:#C9A227;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font:15px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:60rem;margin:0 auto;padding:0 1.25rem 6rem}
header{padding:3.5rem 0 2rem;border-bottom:1px solid var(--rule)}
h1{
  font:400 2.6rem/1.1 ui-serif,Georgia,"Times New Roman",serif;
  margin:0 0 .5rem; letter-spacing:-.015em; text-wrap:balance;
}
.sub{color:var(--muted);max-width:62ch;margin:0}
.stats{display:flex;flex-wrap:wrap;gap:1.75rem;margin-top:1.75rem}
.stat{display:flex;flex-direction:column;gap:.15rem}
.stat b{font:600 1.5rem/1 ui-monospace,"SF Mono",Menlo,monospace;font-variant-numeric:tabular-nums;color:var(--brass)}
.stat span{font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
h2{
  font:400 1.35rem/1.2 ui-serif,Georgia,serif;margin:3.25rem 0 .35rem;
  padding-top:2rem;border-top:1px solid var(--rule)
}
h2:first-of-type{border-top:0;padding-top:0}
.lede{color:var(--muted);margin:0 0 1.5rem;max-width:64ch;font-size:.93rem}
/* address grammar decoder */
.grammar{background:var(--surface);border:1px solid var(--rule);border-radius:3px;padding:1.5rem;margin-bottom:1rem}
.spec{font:600 1.7rem/1 ui-monospace,"SF Mono",Menlo,monospace;letter-spacing:.02em;display:flex;flex-wrap:wrap;margin-bottom:1.25rem}
.spec i{font-style:normal;position:relative;padding-bottom:1.4rem}
.spec i::after{
  content:attr(data-l);position:absolute;left:0;bottom:0;white-space:nowrap;
  font:500 .62rem/1 ui-sans-serif,sans-serif;letter-spacing:.07em;text-transform:uppercase;color:var(--muted)
}
.spec i:nth-child(1){color:var(--brass)}
.spec i:nth-child(2),.spec i:nth-child(4){color:var(--ink)}
.spec i:nth-child(3),.spec i:nth-child(5){color:var(--brass-dim)}
.gk{display:grid;grid-template-columns:auto 1fr;gap:.4rem 1rem;font-size:.88rem;align-items:baseline}
.gk code{font:500 .85rem ui-monospace,Menlo,monospace;color:var(--brass);white-space:nowrap}
.gk span{color:var(--muted)}
/* division map */
.map{display:grid;gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.dv{display:flex;gap:1rem;background:var(--surface);padding:.5rem .9rem;text-decoration:none;color:inherit;align-items:baseline}
.dv:hover{background:var(--tint)}
.dv .a{font:600 .84rem ui-monospace,Menlo,monospace;font-variant-numeric:tabular-nums;color:var(--brass);flex:0 0 3.4rem}
.dv0{background:var(--tint)}
.dv0 .t{font:600 .95rem ui-serif,Georgia,serif;letter-spacing:.01em}
.dv1 .t{padding-left:1rem}
.dv2 .t{padding-left:2.2rem;color:var(--muted)}
.nt{display:block;font-size:.75rem;color:var(--muted);font-style:italic;font-family:ui-serif,Georgia,serif}
/* filter */
.bar{position:sticky;top:0;z-index:5;background:var(--ground);padding:1rem 0 .75rem;border-bottom:1px solid var(--rule)}
.fwrap{display:flex;gap:.75rem;align-items:center}
input[type=search]{
  flex:1;font:400 .95rem ui-sans-serif,sans-serif;color:var(--ink);
  background:var(--surface);border:1px solid var(--rule);border-radius:3px;padding:.6rem .8rem;
}
input[type=search]:focus{outline:2px solid var(--focus);outline-offset:-1px;border-color:transparent}
.count{font:500 .78rem ui-monospace,Menlo,monospace;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
/* outline rows */
.list{margin-top:.25rem}
.r{display:flex;gap:1rem;align-items:baseline;padding:.16rem 0;border-bottom:1px solid transparent}
.r .a{
  font:400 .8rem ui-monospace,"SF Mono",Menlo,monospace;font-variant-numeric:tabular-nums;
  flex:0 0 7.2rem;color:var(--ink);cursor:pointer;
}
.r .a i{font-style:normal;color:var(--muted)}
.r .a:hover{color:var(--brass)}
.r.h .a{color:var(--brass);font-weight:600}
.r .t{flex:1;min-width:0}
.h0{margin-top:2.5rem;padding-top:.6rem;border-top:2px solid var(--brass)}
.h0 .t{font:600 1.3rem/1.2 ui-serif,Georgia,serif}
.h1{margin-top:1.4rem}
.h1 .t{font:600 1.02rem ui-serif,Georgia,serif}
.h2 .t{font:600 .93rem ui-serif,Georgia,serif;padding-left:1rem}
.h3 .t{font:600 .88rem ui-serif,Georgia,serif;padding-left:2rem;color:var(--muted)}
.b4 .t{padding-left:0}
.b5 .t{padding-left:1.15rem}
.b6 .t{padding-left:2.3rem}
.b7 .t{padding-left:3.45rem}
.b5,.b6,.b7{color:var(--muted)}
.b5 .t,.b6 .t,.b7 .t{border-left:1px solid var(--rule);margin-left:.35rem;padding-left:1rem}
.b6 .t{margin-left:1.5rem}
.b7 .t{margin-left:2.65rem}
.r:hover{background:var(--tint)}
.r[hidden]{display:none}
.empty{padding:2rem 0;color:var(--muted);font-style:italic}
.notes li{margin-bottom:.6rem;color:var(--muted);font-size:.9rem}
.notes code{font:500 .85em ui-monospace,Menlo,monospace;color:var(--brass)}
.toast{
  position:fixed;bottom:1.5rem;left:50%;transform:translateX(-50%) translateY(200%);
  background:var(--ink);color:var(--ground);padding:.5rem 1rem;border-radius:3px;
  font:500 .82rem ui-monospace,Menlo,monospace;transition:transform .18s ease;z-index:20
}
.toast.on{transform:translateX(-50%) translateY(0)}
@media (prefers-reduced-motion:reduce){.toast{transition:none}}
@media(max-width:640px){
  h1{font-size:2rem}
  .r{flex-wrap:wrap;gap:.15rem 1rem}
  .r .a{flex-basis:100%}
  .dv .a{flex-basis:3rem}
}
"""

JS = """
const rows=[...document.querySelectorAll('.list .r')];
const box=document.getElementById('q'), cnt=document.getElementById('cnt');
const toast=document.getElementById('toast'); let tid;
function filter(){
  const q=box.value.trim().toLowerCase();
  if(!q){rows.forEach(r=>r.hidden=false); cnt.textContent=rows.length+' entries'; return;}
  let n=0; const keep=new Set();
  rows.forEach((r,i)=>{
    if(r.dataset.s.includes(q)){ keep.add(i); n++;
      // keep ancestors visible for context
      let d=+r.dataset.d;
      for(let j=i-1;j>=0&&d>0;j--){ const jd=+rows[j].dataset.d; if(jd<d){keep.add(j); d=jd;} }
    }
  });
  rows.forEach((r,i)=>r.hidden=!keep.has(i));
  cnt.textContent=n+' match'+(n===1?'':'es');
}
box.addEventListener('input',filter);
document.addEventListener('keydown',e=>{
  if(e.key==='/'&&document.activeElement!==box){e.preventDefault();box.focus();}
  if(e.key==='Escape'&&document.activeElement===box){box.value='';filter();box.blur();}
});
document.querySelector('.list').addEventListener('click',e=>{
  const a=e.target.closest('.a'); if(!a)return;
  const t=a.textContent;
  navigator.clipboard?.writeText(t).then(()=>{
    toast.textContent=t+'  copied'; toast.classList.add('on');
    clearTimeout(tid); tid=setTimeout(()=>toast.classList.remove('on'),1400);
  });
});
cnt.textContent=rows.length+' entries';
"""

HTML = f"""<title>Antinet Discipline Index</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<div class="wrap">
<header>
  <h1>Antinet Discipline Index</h1>
  <p class="sub">A Scheper-scheme filing reference for the outline of academic disciplines. Every entry carries a unique address: a four-digit division number, then alternating numeric and alphabetic branches for depth.</p>
  <div class="stats">
    <div class="stat"><b>{tot:,}</b><span>Addresses</span></div>
    <div class="stat"><b>{len(divs)}</b><span>Divisions</span></div>
    <div class="stat"><b>5</b><span>Drawers</span></div>
    <div class="stat"><b>7</b><span>Max depth</span></div>
  </div>
</header>

<h2>Reading an address</h2>
<p class="lede">The four-digit number gets you to the drawer and the guide card. Everything after the slash is branching, alternating number and letter, exactly as Scheper's scheme prescribes — so a card can always be interleaved without renumbering its neighbours.</p>
<div class="grammar">
  <div class="spec"><i data-l="division">3011</i><i data-l="">/</i><i data-l="branch">1</i><i data-l="sub">d</i><i data-l="sub">3</i></div>
  <div class="gk">
    <code>3011</code><span>Space sciences — the guide card the rest hangs behind</span>
    <code>/1</code><span>Aerospace engineering</span>
    <code>d</code><span>Astronautics</span>
    <code>3</code><span>Space commercialization</span>
  </div>
</div>
<div class="gk" style="margin-top:1rem">
  <code>1&ndash;5</code><span>Drawer: the five top-level branches of knowledge</span>
  <code>x<b>NN</b>0</code><span>Discipline &mdash; two digits, so a drawer holds up to 99</span>
  <code>xNN<b>N</b></code><span>Sub-discipline &mdash; one digit, up to 9 per discipline</span>
  <code>/n a n a</code><span>Unbounded branching past the division number</span>
</div>

<h2>The 65 division numbers</h2>
<p class="lede">These are your guide cards. Cut a tab for each; everything else files behind one of them.</p>
<div class="map">{''.join(dmap)}</div>

<h2>Full numbered outline</h2>
<p class="lede">Click any address to copy it. Press <code>/</code> to jump to the filter.</p>
<div class="bar"><div class="fwrap">
  <input type="search" id="q" placeholder="Filter by discipline or address&hellip;" autocomplete="off" spellcheck="false">
  <span class="count" id="cnt"></span>
</div></div>
<div class="list">{''.join(rows)}</div>

<h2>Filing notes</h2>
<ul class="notes">
  <li><b>Numbers are addresses, not a classification.</b> Two adjacent numbers mean two adjacent cards &mdash; nothing more. Resist the urge to make the number carry meaning it cannot hold.</li>
  <li><b>Letters run past <code>z</code> as <code>aa</code>, <code>ab</code>.</b> Four addresses need this today: <code>2010/7aa</code>, <code>3021/50aa</code>, <code>5030/3aa</code>, <code>5110/22aa</code>.</li>
  <li><b>37 titles repeat inside a single division.</b> The source outline lists some disciplines twice under different parents &mdash; <i>Glaciology</i> at <code>2050/1o</code> and <code>2050/1p1</code>, for instance. File one card and cross-reference the other address rather than writing two.</li>
  <li><b>One source line is malformed.</b> <code>1030/9c4</code> reads &ldquo;Mississippian culture* Art History&rdquo; &mdash; a Wikipedia artifact where two entries collapsed into one. File as two cards if you need both.</li>
  <li><b>Growth is free.</b> A new sub-discipline becomes a new branch segment; a new discipline takes the next free <code>xNN0</code>. Nothing renumbers.</li>
</ul>
</div>
<div class="toast" id="toast"></div>
<script>{JS}</script>
"""
open('../artifacts/antinet-index.html','w').write(HTML)
print("written:", len(HTML), "bytes")

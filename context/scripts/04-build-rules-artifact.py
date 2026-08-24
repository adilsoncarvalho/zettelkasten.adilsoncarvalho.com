CSS = """
:root{--ground:#F2F3F1;--surface:#FFFFFF;--ink:#1B2430;--muted:#6B7580;--rule:#D8DBD6;
 --brass:#8A6A2F;--brass-dim:#A98B4E;--tint:#E7E9E5;--warn:#8C4A2F;--good:#3D6B4A}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#151A1F;--surface:#1D242B;--ink:#E3E6E2;--muted:#8D97A1;--rule:#2C353D;
 --brass:#C9A227;--brass-dim:#9C8330;--tint:#222A31;--warn:#D08A5E;--good:#7FB08D}}
:root[data-theme="dark"]{--ground:#151A1F;--surface:#1D242B;--ink:#E3E6E2;--muted:#8D97A1;
 --rule:#2C353D;--brass:#C9A227;--brass-dim:#9C8330;--tint:#222A31;--warn:#D08A5E;--good:#7FB08D}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
 font:15px/1.6 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:54rem;margin:0 auto;padding:0 1.25rem 6rem}
header{padding:3.5rem 0 2rem;border-bottom:1px solid var(--rule)}
h1{font:400 2.6rem/1.1 ui-serif,Georgia,serif;margin:0 0 .6rem;letter-spacing:-.015em;text-wrap:balance}
.sub{color:var(--muted);max-width:64ch;margin:0}
h2{font:400 1.35rem/1.2 ui-serif,Georgia,serif;margin:3.5rem 0 .4rem;padding-top:2rem;border-top:1px solid var(--rule)}
h3{font:600 1.02rem ui-serif,Georgia,serif;margin:1.8rem 0 .5rem}
p{max-width:66ch}
.lede{color:var(--muted);margin:0 0 1.5rem;max-width:66ch;font-size:.93rem}
.ad,code{font-family:ui-monospace,"SF Mono",Menlo,monospace;font-variant-numeric:tabular-nums}
code{font-size:.88em;color:var(--brass)}
/* anatomy diagram */
.anat{background:var(--surface);border:1px solid var(--rule);border-radius:3px;padding:2rem 1.6rem 1.4rem;margin:1.5rem 0}
.spec{font:600 2.3rem/1 ui-monospace,"SF Mono",Menlo,monospace;display:flex;flex-wrap:wrap;justify-content:center;margin-bottom:2.2rem}
.spec i{font-style:normal;position:relative;padding-bottom:2.6rem}
.spec i::before{content:'';position:absolute;left:8%;right:8%;top:1.25em;height:.5rem;
 border:1px solid var(--brass-dim);border-top:0}
.spec i::after{content:attr(data-l);position:absolute;left:50%;transform:translateX(-50%);bottom:.4rem;
 white-space:nowrap;font:500 .6rem/1.35 ui-sans-serif,sans-serif;letter-spacing:.07em;
 text-transform:uppercase;color:var(--muted);text-align:center}
.spec i.sep{color:var(--muted)}.spec i.sep::before,.spec i.sep::after{display:none}
.spec i.d{color:var(--brass)}.spec i.b{color:var(--ink)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:.5rem}
.two>div{padding-top:1rem;border-top:1px solid var(--rule)}
.two h4{font:500 .68rem/1 ui-sans-serif,sans-serif;letter-spacing:.11em;text-transform:uppercase;margin:0 0 .6rem}
.two:first-of-type>div:first-child h4{color:var(--brass)}
.two p{font-size:.88rem;color:var(--muted);margin:0;max-width:none}
/* the rule box */
.rule{background:var(--tint);border-left:3px solid var(--brass);border-radius:2px;padding:1.3rem 1.5rem;margin:1.5rem 0}
.rule p{margin:0 0 .5rem}.rule p:last-child{margin:0}
.rule b{color:var(--brass)}
/* tables */
.tbl{overflow-x:auto;margin:1.2rem 0}
table{border-collapse:collapse;width:100%;font-size:.9rem}
th{text-align:left;font:500 .68rem/1 ui-sans-serif,sans-serif;letter-spacing:.1em;text-transform:uppercase;
 color:var(--muted);padding:.55rem .7rem;border-bottom:1px solid var(--rule);white-space:nowrap}
td{padding:.5rem .7rem;border-bottom:1px solid var(--rule);vertical-align:top}
td.ad{color:var(--brass);font-weight:600;white-space:nowrap}
td.op{white-space:nowrap;font-size:.84rem}
.pill{display:inline-block;padding:.1rem .5rem;border-radius:2px;font:500 .72rem ui-sans-serif,sans-serif;
 letter-spacing:.04em;text-transform:uppercase}
.pill.c{background:color-mix(in srgb,var(--brass) 18%,transparent);color:var(--brass)}
.pill.s{background:color-mix(in srgb,var(--muted) 18%,transparent);color:var(--muted)}
/* worked example */
.work{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin:1.4rem 0}
.work>div{background:var(--surface);border:1px solid var(--rule);border-radius:3px;padding:1.2rem}
.work h4{font:500 .68rem/1 ui-sans-serif,sans-serif;letter-spacing:.11em;text-transform:uppercase;
 color:var(--muted);margin:0 0 .9rem;padding-bottom:.5rem;border-bottom:1px solid var(--rule)}
.work ol{list-style:none;counter-reset:s;margin:0;padding:0}
.work li{display:flex;gap:.6rem;align-items:baseline;padding:.22rem 0;font-size:.85rem}
.work .n{counter-increment:s;color:var(--muted);font:500 .7rem ui-monospace,Menlo,monospace;flex:0 0 1rem}
.work .n::before{content:counter(s)}
.work .a{font:400 .78rem ui-monospace,Menlo,monospace;color:var(--brass-dim);flex:0 0 5.6rem}
.work .t{flex:1;min-width:0}
.work li.hi{background:color-mix(in srgb,var(--brass) 12%,transparent);border-radius:2px;
 margin:0 -.4rem;padding-left:.4rem;padding-right:.4rem}
.work li.hi .a{color:var(--brass);font-weight:600}
.work .gd{color:var(--muted)}
.drawer li{font-family:ui-monospace,Menlo,monospace;font-size:.8rem}
.drawer .t{font-family:ui-sans-serif,sans-serif;font-size:.85rem}
/* never list */
.never{list-style:none;padding:0;margin:1rem 0}
.never li{padding:.6rem 0 .6rem 1.7rem;border-bottom:1px solid var(--rule);position:relative;max-width:66ch}
.never li::before{content:'\\00d7';position:absolute;left:.3rem;top:.5rem;color:var(--warn);
 font:600 1.1rem ui-sans-serif,sans-serif}
.never b{font-weight:600}
.never span{display:block;color:var(--muted);font-size:.87rem;margin-top:.15rem}
.callout{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--brass);
 border-radius:2px;padding:1.2rem 1.4rem;margin:1.4rem 0}
.callout p{margin:0 0 .7rem}.callout p:last-child{margin:0}
@media(max-width:680px){h1{font-size:2rem}.spec{font-size:1.5rem}.work,.two{grid-template-columns:1fr}}
"""

HTML = f"""<title>Antinet Filing Rules</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<div class="wrap">
<header>
<h1>Antinet Filing Rules</h1>
<p class="sub">How to compute an address, when to branch and when to continue, and what a hub card is for. The operating manual for the Discipline Index.</p>
</header>

<h2>Anatomy of an address</h2>
<div class="anat">
<div class="spec"><i class="d" data-l="drawer">1</i><i class="d" data-l="discipline">04</i><i class="d" data-l="sub&#8209;disc.">0</i><i class="sep">/</i><i class="b" data-l="branch">9d1a</i></div>
<div class="two">
<div><h4>The four digits &mdash; meaning</h4>
<p>Fixed in advance. 65 of them. This is the <em>only</em> place taxonomy lives: <code>1040</code> is Languages and literature, and it always will be. You never invent one.</p></div>
<div><h4>After the slash &mdash; position</h4>
<p>Pure address. Answers &ldquo;where does this card physically sit?&rdquo; and nothing else. It grows as you file and never means anything.</p></div>
</div></div>
<p class="lede">One slash, ever. After it, segments alternate <b>number &rarr; letter &rarr; number &rarr; letter</b>. The type switch <em>is</em> the level marker, which is why no further punctuation is needed: consecutive digits form one segment, consecutive letters form one segment. <code>3021/50aa</code> reads unambiguously as 50 &rarr; aa.</p>

<h2>Computing the next address</h2>
<div class="rule">
<p><b>1.</b> Decide which card the new one hangs off. Call it the <b>parent</b>.</p>
<p><b>2.</b> Look at the parent&rsquo;s last segment. Ends in a <b>number</b> &rarr; append a <b>letter</b>. Ends in a <b>letter</b> &rarr; append a <b>number</b>.</p>
<p><b>3.</b> Take the next unused one. Done &mdash; permanently.</p>
</div>
<p>That is the whole computation. There is no lookup, no renumbering, and no way to run out of room.</p>

<h2>Child or sibling</h2>
<p class="lede">These are not two operations. They are the same operation with a different parent &mdash; which is what makes the system easy to run at 2am with a card in your hand.</p>
<div class="tbl"><table>
<tr><th>You want</th><th>Parent is</th><th>From <code>1060/1a</code> you get</th></tr>
<tr><td><span class="pill c">Child</span> digs into the card</td><td>the card itself</td><td class="ad">1060/1a1</td></tr>
<tr><td><span class="pill s">Sibling</span> continues past it</td><td>the card&rsquo;s parent &mdash; drop the last segment</td><td class="ad">1060/1b</td></tr>
</table></div>
<div class="rule"><p>The question to ask at the drawer: <b>does this continue the card in my hand, or dig into it?</b> Continue &rarr; step back one segment and append. Dig in &rarr; append directly.</p></div>

<h2>A worked sequence</h2>
<p class="lede">Seven cards filed behind <code>1060</code> Writing and rhetoric, in the order they were written. Watch card&nbsp;6.</p>
<div class="work">
<div><h4>Order written</h4><ol>
<li><span class="n"></span><span class="a">1060/1</span><span class="t">Persuasion &mdash; HUB</span></li>
<li><span class="n"></span><span class="a">1060/1a</span><span class="t">Definition of a thesis</span></li>
<li><span class="n"></span><span class="a">1060/1a1</span><span class="t">Thesis vs. hypothesis</span></li>
<li><span class="n"></span><span class="a">1060/1b</span><span class="t">Ethos, pathos, logos</span></li>
<li><span class="n"></span><span class="a">1060/1b1</span><span class="t">Aristotle, <i>Rhetoric</i> Bk I</span></li>
<li class="hi"><span class="n"></span><span class="a">1060/1a2</span><span class="t">A thesis must be contestable</span></li>
<li><span class="n"></span><span class="a">1060/2</span><span class="t">Rhetoric &ne; sophistry</span></li>
</ol></div>
<div class="drawer"><h4>Order in the drawer</h4><ol style="counter-reset:none">
<li><span class="a gd">1060</span><span class="t gd">Writing and rhetoric &mdash; guide card</span></li>
<li><span class="a">1060/1</span><span class="t">Persuasion &mdash; HUB</span></li>
<li><span class="a">1060/1a</span><span class="t">Definition of a thesis</span></li>
<li><span class="a">1060/1a1</span><span class="t">Thesis vs. hypothesis</span></li>
<li class="hi"><span class="a">1060/1a2</span><span class="t">A thesis must be contestable</span></li>
<li><span class="a">1060/1b</span><span class="t">Ethos, pathos, logos</span></li>
<li><span class="a">1060/1b1</span><span class="t">Aristotle, <i>Rhetoric</i> Bk I</span></li>
<li><span class="a">1060/2</span><span class="t">Rhetoric &ne; sophistry</span></li>
</ol></div>
</div>
<p>Card 6 was written sixth and sits fourth. It slid between two cards that already existed, and nothing moved to accommodate it. That is the entire payoff of the alternating scheme &mdash; and the reason you must never renumber: a card&rsquo;s address is the only stable thing other cards can point at.</p>

<h3>How each address was derived</h3>
<div class="tbl"><table>
<tr><th>#</th><th>Parent</th><th>Ends in</th><th>So append</th><th>Address</th></tr>
<tr><td>1</td><td><code>1060</code></td><td>the discipline &mdash; no branch yet</td><td>number &rarr; <code>1</code></td><td class="ad">1060/1</td></tr>
<tr><td>2</td><td><code>1060/1</code></td><td>number <code>1</code></td><td>letter &rarr; <code>a</code></td><td class="ad">1060/1a</td></tr>
<tr><td>3</td><td><code>1060/1a</code></td><td>letter <code>a</code></td><td>number &rarr; <code>1</code></td><td class="ad">1060/1a1</td></tr>
<tr><td>4</td><td><code>1060/1</code></td><td>number <code>1</code></td><td>letter &rarr; <code>b</code> (<code>a</code> taken)</td><td class="ad">1060/1b</td></tr>
<tr><td>5</td><td><code>1060/1b</code></td><td>letter <code>b</code></td><td>number &rarr; <code>1</code></td><td class="ad">1060/1b1</td></tr>
<tr><td>6</td><td><code>1060/1a</code></td><td>letter <code>a</code></td><td>number &rarr; <code>2</code> (<code>1</code> taken)</td><td class="ad">1060/1a2</td></tr>
<tr><td>7</td><td><code>1060</code></td><td>the discipline</td><td>number &rarr; <code>2</code> (<code>1</code> taken)</td><td class="ad">1060/2</td></tr>
</table></div>

<h2>Inserting between two cards</h2>
<p>There is no <em>between</em>. There is only <em>behind</em> &mdash; and behind turns out to be enough, because a child always sits between its parent and its parent&rsquo;s next sibling.</p>
<div class="rule"><p>To place a card between <code>X</code> and the card after it: <b>append to X.</b> Sorting does the rest.</p></div>
<p>The one genuine limit: nothing can sit between a card and its own <em>first</em> child. That gap is closed. You will never need it, because sibling order carries no meaning &mdash; <code>9d2</code> is not &ldquo;more important than&rdquo; <code>9d3</code>. When sequence genuinely matters, that is a hub card&rsquo;s job, not the number&rsquo;s.</p>

<h2>Hub cards</h2>
<p class="lede">If the number cannot tell you what a card says, something else has to find it. Three devices do that work, and they are not interchangeable.</p>
<div class="tbl"><table>
<tr><th>Device</th><th>Holds</th><th>Lives</th><th>Rewritten</th></tr>
<tr><td><b>Hub card</b></td><td>A list of addresses on one theme &mdash; a switchboard, not prose</td><td>In place, at the theme&rsquo;s centre of gravity</td><td>Freely, often</td></tr>
<tr><td><b>Keyword index</b></td><td>Term &rarr; one or two <em>entry-point</em> addresses. Deliberately sparse</td><td>Its own drawer, alphabetical</td><td>Rarely, by addition</td></tr>
<tr><td><b>Bibliographic card</b></td><td>One source, its details, and the cards drawn from it</td><td>Its own drawer, by author</td><td>Never &mdash; append only</td></tr>
</table></div>
<h3>What makes a hub card work</h3>
<p>A hub is the one card in the system you are <em>allowed</em> to rewrite, because it holds no thinking &mdash; only pointers. That licence is what lets it do its job: it collapses the drawer separation that the four-digit numbers impose. Your Persuasion hub can point at <code>1060</code>, <code>5080/4p</code> and <code>2020/15</code> on the same line, and no filing scheme could have put those three together.</p>
<p>Keep it a list. The moment a hub starts containing arguments, it has become a card that belongs somewhere and you have lost your index.</p>
<div class="callout">
<p><b>Where a hub goes.</b> At its theme&rsquo;s centre of gravity &mdash; the anchor most of its material hangs off &mdash; not at the drawer root. <code>1000/1</code> is unoccupied and legal, but a card there has 454 unrelated disciplines as neighbours, and neighbours are the point.</p>
</div>

<h2>Never</h2>
<ul class="never">
<li><b>Renumber a card.</b><span>Other cards point at that address, and the keyword index does too. An address is a promise.</span></li>
<li><b>Use more than one slash.</b><span>The alternation already marks every level. A second separator creates a conflicting depth signal &mdash; and <code>1010/1d/1</code> collides with <code>1010/1d1</code>, which is Choral conducting.</span></li>
<li><b>File at a drawer root.</b><span><code>N000/1</code> is free in all five drawers, and still wrong: the neighbours are meaningless at that altitude.</span></li>
<li><b>Make the branch taxonomic.</b><span>The Discipline Index reads that way only because it was seeded from a taxonomy. Your own cards will not, and forcing it is the Dewey trap one level down.</span></li>
<li><b>Wait for the right category.</b><span>There is no right category &mdash; only the card this one is talking back to. If nothing fits, file behind the nearest anchor and let the hub card find it later.</span></li>
</ul>
</div>
"""
open('../artifacts/filing-rules.html','w').write(HTML)
print("written:", len(HTML), "bytes")

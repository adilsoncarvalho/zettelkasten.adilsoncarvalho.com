# Hub Card Placements

> **Re-anchored onto the curated index.** These hubs originally sat at source-outline
> addresses, from before the disciplines were re-cut — `1040/9d1` behind Rhetoric, and so on.
> Those coordinates are dead: `1040` is Language and linguistics now, and nothing branches off
> the outline's own structure any more. Each hub now sits behind a real row of the published
> index, at the first free position under it, and each satellite names the discipline the
> subject files in rather than an outline address. The *reasoning* is unchanged — a hub still
> hangs off a branch address, not off a discipline.

The owner's six standing interests, mapped onto the index. Published as an artifact;
this is the source content.

**Source of truth is `scripts/03-build-hubs-artifact.py`.** The `THEMES` structure there feeds
this document, `data/hubs.json` and the artifact. Edit it, then re-run
`03-build-hubs-artifact.py` and `06-emit-hubs-json.py`.

## The six hubs

| Theme | Hub address | Sits behind | Anchor |
|---|---|---|---|
| **Persuasion** | `1060/1` | `1060` | Writing and rhetoric |
| **Organisations** | `5060/1` | `5060` | Business and management |
| **Ventures** | `5060/2` | `5060` | Business and management |
| **Mind** | `2040/1` | `2040` | Psychology |
| **Metabolism** | `5051/1` | `5051` | Nutrition and metabolic health |
| **Formation** | `1020/1` | `1020` | Religion and theology |

Each hub sits at its theme's centre of gravity — the discipline most of its material hangs
off — and takes the first free position behind it, never a drawer root. Organisations and
Ventures both centre on `5060`, so they sit side by side at `5060/1` and `5060/2`.

## Theme detail

### Persuasion — `1060/1`

Behind `1060` Writing and rhetoric.

Rhetoric is the spine, and the re-cut finally gave it a home of its own: 1060 Writing and rhetoric, the craft rather than the criticism. The outline listed rhetoric twice and the copy under literary theory maps to 1050 Literature — that is the reading of it, not the doing. Everything else here is an application: channel at 2080, influence at 5062, and selling at 5061, which the academy has no word for at all.

**Craft**

- `1050` Literature — Literary theory, Poetics
- `1060` Writing and rhetoric — Creative writing, Literary journalism
- `1080` Performing arts — Storytelling
- `2080` Communication and media — Narratology

**Channel**

- `2080` Communication and media — Journalism, media studies & communication, Communication studies, Speech communication, Nonverbal communication, Technical writing, Communication design

**Influence**

- `2080` Communication and media — Propaganda, Popular culture studies
- `5062` Marketing and branding — Advertising, Public relations

**Mechanism**

- `1040` Language and linguistics — Discourse analysis, Pragmatics, Semiotics
- `1060` Writing and rhetoric — Rhetoric

### Organisations — `5060/1`

Behind `5060` Business and management.

The outline gave organizational studies its own node and then duplicated management, HR and industrial organization across two more. The re-cut folds all of it into 5060 Business and management, which dissolves this theme's duplicate problem outright: what needed two groups and a pick-the-live-branch note is now one guide card.

**Core**

- `5060` Business and management — Management, Organizational behavior, Organization theory, Project management, Human resources management, Quality control, Industrial & labor relations, Collective bargaining, Corporate governance, Operations management, Decision science

**Behaviour & theory**

- `2030` Sociology — Organizational theory, Critical management studies
- `2040` Psychology — Organizational psychology
- `2080` Communication and media — Organizational communication

**Systems & leadership**

- `4070` Information and systems science — Systems engineering, Management cybernetics
- `5030` Education and learning — Educational leadership
- `5080` Military and security — Leadership, Supply chain management

### Ventures — `5060/2`

Behind `5060` Business and management.

Entrepreneurship was a single childless bullet in the outline, which tells you how thinly the academy treats it — expect this branch to be almost entirely your own cards. It shares 5060 with Organisations, so the two hubs sit side by side at 5060/1 and 5060/2. The money side reaches into 5063 Finance and investing, the product side into 5020 Architecture and design.

**Venture core**

- `2050` Economics — Entrepreneurial economics
- `5060` Business and management — Business administration, Business analysis, E-Business, Strategy / Strategic Management

**Product**

- `5020` Architecture and design — Industrial design (product design), User experience design, Interaction design, Information architecture

**Money**

- `2030` Sociology — Sociology of finance
- `2050` Economics — Public finance
- `4040` Computer science — Computational finance
- `5060` Business and management — Risk management & insurance

**Market forces**

- `2050` Economics — Microeconomics, Industrial organization, Consumer economics, Behavioural economics
- `5060` Business and management — Industrial organization, International trade

### Mind — `2040/1`

Behind `2040` Psychology.

Psychology was the largest single branch in the outline, 61 children, and the re-cut keeps it whole at 2040. Decision-making is still genuinely split — now across 2040, 2050 Economics, 4030 Statistics and probability and 1010 Philosophy — so the hub card earns its keep here more than anywhere else.

**Psychology proper**

- `2040` Psychology — Cognitive psychology, Positive psychology, Problem solving, Personality psychology, Evolutionary psychology, Social psychology, Psychometrics

**Substrate**

- `2040` Psychology — Neuropsychology
- `3050` Biology — Neuroscience, Behavioral neuroscience
- `4060` Artificial intelligence — Cognitive science

**Decision-making**

- `2050` Economics — Behavioural economics
- `4020` Mathematics — Decision analysis
- `4030` Statistics and probability — Decision theory
- `5060` Business and management — Decision science

**Learning & knowing**

- `1010` Philosophy — Epistemology, Philosophy of mind, Philosophy of perception
- `5030` Education and learning — Educational psychology, Mastery learning, Cooperative learning

### Metabolism — `5051/1`

Behind `5051` Nutrition and metabolic health.

The one hub that sits behind the personal tier. 5051 Nutrition and metabolic health exists because cards like these had nowhere to go: 5050 Medicine and health is the clinic and 3050 Biology is the mechanism. Practice wins the hub because keto and fasting are protocols, not physiology — and the satellites keep 3050 one hop away, which is the whole point of the seam.

**Clinical**

- `5050` Medicine and health — Internal medicine, Endocrinology, Gastroenterology, Clinical biochemistry, Public health

**Mechanism**

- `3020` Chemistry — Biochemistry
- `3050` Biology — Physiology, Human physiology, Endocrinology, Biochemistry

**Performance**

- `3050` Biology — Exercise physiology
- `5050` Medicine and health — Sports medicine
- `5130` Sport and recreation — Exercise physiology, Kinesiology / Performance science

**Food as system**

- `2010` Anthropology — Nutritional anthropology
- `2030` Sociology — Sociology of food
- `3050` Biology — Nutrition
- `5010` Agriculture and food — Food science
- `5110` Public administration and policy — Food policy

### Formation — `1020/1`

Behind `1020` Religion and theology.

The widest-spanning theme, and the one the re-cut helped most. The outline carried four adjacent religion nodes — religious studies, divinity, theology, religion — and they are now one discipline at 1020. Catholic theology is the centre of gravity for formation specifically; ethics and philosophy at 1010 hang off it as satellites rather than the reverse.

**Theology**

- `1020` Religion and theology — Christian theology, Divinity, Moral theology, Christian ethics, Systematic theology, Dogmatic theology

**Sources & practice**

- `1020` Religion and theology — Hermeneutics, Biblical studies / Sacred Scripture, Liturgy
- `1030` History — Ecclesiastical history of the Catholic Church
- `5070` Law and jurisprudence — Canon law

**Ethics & philosophy**

- `1010` Philosophy — Ethics, Normative ethics, Virtue ethics, Applied ethics, Medieval philosophy, Philosophy of religion

**Letters & memory**

- `1030` History — Intellectual history
- `1050` Literature — Classics, History of literature, Comparative literature

## The vocabulary gap

Of 23 terms probed from the owner's keyword list, **22 have no entry in the source
outline at all**. Only "storytelling" exists — at source address `1010/6d`, which files at
`1080` Performing arts.

| Theme | Absent from the outline | Files behind, today |
|---|---|---|
| Persuasion | sales, selling, copywriting, negotiation, branding, pricing | 5061 Sales and negotiation · 5062 Marketing and branding |
| Organisations | incentives, business process, people management | 5060 Business and management |
| Ventures | startups, venture capital | 5063 Finance and investing · 5060 Business and management |
| Mind | productivity, attention, focus, habit, note-taking | 2040 Psychology · 5031 Note-taking and knowledge systems |
| Metabolism | keto, carnivore, fasting, metabolism | 5051 Nutrition and metabolic health |

### Why this matters

This is not a defect in the index. The outline maps *academic disciplines* — how universities
partition inquiry. The owner's interests are largely *practices*: things people do, sell, cook,
and pray. There is no chair of keto.

**Consequence for the site and for the filing:** the 2,576 pre-numbered entries are a
*skeleton of anchors*, not a set of slots to fill. The overwhelming majority of real cards will
be original thinking branching off an anchor, not entries filled in. A card on carnivore
adaptation is not a missing discipline; it is `5051/1`'s descendant.

This is the argument for keeping the keyword index sparse and the hub cards fat: the numbers
cannot find the owner's material, because the owner's material is not what was numbered.


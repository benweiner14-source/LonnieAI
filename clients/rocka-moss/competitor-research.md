# Rocka Moss — Meta Ad Library Competitor Research (2026-09-24)

Real, live-pulled data — not a guess. Closes the gap flagged 2026-09-24 (step 1 of `PROJECT_BRIEF.md`'s
6-step pitch: "Pull every sea moss competitor ad running right now on Instagram/Facebook — see
what's working before spending a dollar").

## Method

Direct browser fetches of `facebook.com/ads/library` are blocked (403, JS-rendering wall — same
pattern hit repeatedly elsewhere in this project). Ben supplied an Apify token; ran
`curious_coder/facebook-ads-library-scraper` (Apify's most-used Ad Library actor — 19.5M runs,
42K users, 4.77★/110 reviews), active US ads, all formats, in two passes:
- **Pass 1 (initial):** 3 keyword searches — `sea moss`, `sea moss gel`, `black wellness`. ~$0.05,
  60 ads pulled, 14 unique.
- **Pass 2 (widened, per Ben's "widen the search a little bit and run again"):** 8 keyword
  searches — `sea moss`, `sea moss gel`, `wildcrafted sea moss`, `irish sea moss`, `sea moss
  bladderwrack burdock`, `raw sea moss`, `black wellness`, `black owned supplement`. $0.116, 155
  ads pulled, **71 unique** after dedup across ~38 distinct brands/domains — a much wider net than
  pass 1, including two direct sea-moss competitors pass 1 missed entirely. Combined cost across
  both passes: ~$0.17.

**Not storing scraped video/image files in this repo** — same reproduction-caution posture as
elsewhere in this project (the theme-code, YouTube-transcript, and ad-reverse-engineering
cautions). Every entry below links to its real, public Meta Ad Library permalink so the actual
creative can be viewed directly.

## Update (pass 2): two more direct sea-moss competitors found, plus a category-wide ad pattern

The widened search surfaced what pass 1's narrower 3 terms missed — most importantly, **Infinite
Age is a second, major direct sea-moss competitor**, arguably a more useful reference than True Sea
Moss because it runs a genuinely different playbook (subscription-first, storytelling-led, doctor/
nurse-testimonial framed) instead of True Sea Moss's benefit-list structure. A third, smaller direct
competitor (Aztlan Herbal Remedies) also surfaced.

### Infinite Age (infiniteage.com) — "Sea Moss Advanced" (Sea Moss + Bladderwrack + Burdock Root)

A real, proven, subscription-based direct competitor — same core ingredient blend one of the widened
search terms targeted. 4 unique ad variants, 12-167 days running each.

- **Subscription-first offer, not one-time:** *"The $44 Bottle Is $19 Right Now... Locked in for
  life. Every single month."* — this is a real subscribe-and-save mechanism in the sea-moss
  category, directly relevant since `access-checklist.md`/`kpi-targets.md` already flagged Rocka
  Moss has **zero** selling-plan/subscription infrastructure as a confirmed open lever. A
  competitor is actively selling subscription-locked pricing as the hook itself, not a quiet
  backend option.
- **Storytelling/heritage hook, a genuinely different angle type than anything in pass 1:**
  *"Somewhere between Africa and the pharmacy waiting room… we lost something that was keeping us
  alive. Sit with that for a moment. 98% of us are born healthy... But by the time we reach our
  4[0s]..."* — an ancestral/heritage-loss narrative before any product mention. Given Rocka Moss's
  own audience overlap with this demographic, this is a genuinely different creative angle worth
  testing alongside the benefit-list structure True Sea Moss uses — not a replacement for it.
- **Doctor/nurse-testimonial framing:** *"Doctor said no more meds after THIS"* / *"I'm a real
  nurse. And I'm ashamed to admit I was on 4 different prescription pills..."* — a first-person
  medical-authority character before the product reveal.
- **⚠️ Same caution as True Sea Moss, sharper here:** leans on implied medical-outcome claims
  ("blood sugar," "cholesterol," "no more meds") even more directly than True Sea Moss's benefit
  list. Study the subscription mechanic and the heritage-storytelling structure — not the
  medical-claims language, consistent with this project's standing no-medical-claims rule.

### Aztlan Herbal Remedies (aztlanherbalremedies.com) — confirms a third direct sea-moss seller

234 days running (a proven, not new, ad). Sells "Wildcrafted Irish [Sea] Moss" directly, framed as
a colon-detox/cleanse starter-bundle product — a narrower, more clinical/herbalist positioning than
either True Sea Moss or Infinite Age's broader wellness framing. Useful mainly as confirmation that
sea moss competitors span a spectrum from "superfood smoothie add-in" (True Sea Moss) to "wellness
subscription" (Infinite Age) to "herbal cleanse" (Aztlan) — Rocka Moss's own flavored-jar format
sits closest to the True Sea Moss end of that spectrum.

### A category-wide pattern worth naming: the "personal confessional" hook

Across several *non*-sea-moss wellness/supplement brands in the widened pull (Alevia, American
Health Support Community, Rosabella/"Blood Pressure Secrets," Roots of Wellness), the same ad
structure recurs independent of any single brand: **a long first-person narrative about someone
else** (a spouse, neighbor, sibling) **opens the ad with no product mention at all**, building a
relatable crisis/mystery before the product appears — e.g. *"I had a brother once who looked dead
at 53..."*, *"I took care of my 85-year-old neighbor... the next morning her lawyer said she left
me ONE THING"*, *"I found a notebook in my husband's truck last March and I haven't told him I saw
it."* This is a distinct, widely-reused format from both True Sea Moss's benefit-list and Infinite
Age's heritage-narrative — worth keeping as a third angle type in the psychology-pillar-map /
ad-concept toolkit, even though no sea-moss brand in this pull uses it yet. It maps onto Frankie
Shaw's "curious ad" / storytelling-not-product-first framing already in `ai-ugc-playbook.md`'s
Section 0 — independent confirmation the technique works broadly in this exact wellness-ad
category, not just in AI-UGC-specific creator content.

**⚠️ One example (naturalrems.com, via a "Dr. Alina Marlowe - ENT Specialist" persona page)
crosses a real line, flag but don't emulate:** *"If you are a woman over 60 and your mucus has
thickened... you have somewhere between three and five years before the same hidden overgrowth
could spread through the rest of your body. I am an ENT with 19 years of practice."* — a
fabricated-doctor-persona advertorial using medical fear-mongering (a specific, invented health
timeline) to sell sea moss gummies. This is a harder version of the "don't copy the medical-claims
language" caution already standing for True Sea Moss/Infinite Age — worth calling out explicitly
since it's not just aggressive claims language, it's an invented medical-authority character making
a fabricated prognosis. Not a technique to study for structure either; just a data point on how far
this category's worst actors go.

### Black Girl Vitamins — reconfirms the whitelisting pattern, adds a strong demographic/tonal reference

Not sea moss, but reinforces two things already found with True Sea Moss: (1) the same
**multi-page whitelisting tactic** (ads run through personal-seeming pages — "Manika Runs,"
"Malinda Williams Fan Page" — not just the brand's own page), and (2) a genuinely useful
**positioning reference for Rocka Moss's own audience**: explicit "formulated for Black women's
specific health needs" messaging, a named medical advisor for credibility, and a community/equity
angle (scholarships for Black women in healthcare fields) instead of a generic wellness pitch.
Longest-running variant: 491 days — a proven, not experimental, positioning.

## Key finding (pass 1): only one real sea-moss-specific competitor showed up — but it's a strong, proven one

**True Sea Moss (trueseamoss.com)** dominates this category in the data. Not just one ad — **the
exact same core creative is running through 6 different Facebook Pages** (Stephanie DB, Maria
Gladys, Creatine Guru, True Sea Moss Health, Fitness Addiction Blog, The Dodo), each reading like
an independent creator/influencer page rather than the brand's own page. This is a real,
observable tactic worth naming directly: **whitelisting/creative-amplification through multiple
page fronts**, not just posting from one brand account. Directly relevant to Rocka Moss's own
planned influencer-seeding workstream — the same underlying idea, run at scale.

Longevity (a real performance signal per Meta's own dynamics — bad ads get killed fast, good ones
keep running) is extreme: the longest-running True Sea Moss variant has been active **232 days**,
with the group as a whole spanning 63-232 days across all 6 pages. This is a proven, not
speculative, ad.

### True Sea Moss's winning pattern (the one to study closely)

- **Headline is offer-led, not claim-led:** *"Nature's Finest Superfood: Up to 50% Off + Free
  Gift"* — the hook is the discount + gift, not a health claim.
- **Body copy: an emoji-bulleted benefit list**, one line per benefit (immune support, digestion/
  gut health, blood pressure, prebiotic, collagen/skin-nails-hair, energy/mental clarity, joint/
  muscle relief) — reads like a spec sheet, not a story.
- **Ingredient transparency as a trust signal:** *"Our main and only ingredients are: 100%
  Wildcrafted Sea Moss, Farm-Fresh Fruit, Spring Water, Natural Lime Juice"* — plain, short,
  no filler.
- **Usage instruction inside the ad itself:** *"Just two spoons a day... 90 essential vitamins
  and minerals"* — answers "how do I even use this" before it's asked.
- **CTA: plain `SHOP_NOW`**, nothing fancier.
- **Bilingual:** a Spanish-language variant of the same ad is also running, same offer/structure.
- **Also testing a second product line** (a hydration powder) with a *different* hook style —
  problem/pain-first framing ("modern life drains your minerals fast — stress, caffeine, sugar,
  late nights") instead of the sea moss ad's offer-first framing. Shows they test more than one
  angle type, not just one formula.

**⚠️ Real caution, don't copy this part:** True Sea Moss's benefit list leans into
borderline-medical claims ("Lower blood pressure," general immune/health claims stated flatly).
This is exactly what `docs/frankie-shaw-ai-ugc-method.md` and this playbook's own Section 0
already warn against for Rocka Moss specifically — a competitor running a claim doesn't make it
safe or the right call here. Study the *structure* (offer-led hook, ingredient transparency,
usage instructions), not the *claims language*.

### Two adjacent (non-sea-moss) references worth noting

- **MuscleMax Nutrition** (officialmusclemax(supps).com) — general wellness supplement brand,
  not sea moss, but a genuinely strong, long-running (178-520 days) hook worth studying:
  *"Stop Taking 10/15 Different Supplements Everyday — Just Take These 2!"* — a **consolidation
  pain point** (supplement fatigue) rather than a benefit list. They A/B test the specific number
  ("10" vs "15") and also run a separate testosterone-focused variant ("Boost T Levels
  Naturally"). Worth considering as an alternate angle type for Rocka Moss beyond the benefit-list
  structure True Sea Moss uses.
- **Culture Connection 360** (healthyculture360.com) — Black-owned body-care brand (shea
  butter/body oil, not sea moss), but genuinely notable: **physical locations in Chicago and
  Atlanta** — two of Rocka Moss's three actual expansion cities — and among the longest-running
  ads found in either pull (616-1389 days). Casual, personal, community-voice copy style
  (first-name energy, emoji-heavy, direct address — "Come see us today"), not corporate. A real
  structural/tonal reference for what reads as authentic in exactly Rocka Moss's target
  cities/demographic, even though the product category is different.

## Full list — direct sea-moss + key reference competitors (ranked by days running)

Pass 2 surfaced 71 unique ads across ~38 brands total; this table keeps the direct sea-moss
competitors plus the adjacent brands with real strategic relevance (whitelisting pattern,
demographic/tonal fit, or a distinct ad-format worth studying) rather than all 71 — the full raw
dataset is preserved in the Apify run (`runId: KbwE7fH9wPTzzUEdW`, `datasetId: xOnBIF2hLwHn77xkc`)
if a deeper cut is needed later.

| Advertiser | Category | Format | Days running | Ad Library link |
|---|---|---|---|---|
| Ginger's Roots | Adjacent (IG-only listing, unconfirmed niche) | Image | 1415 | https://www.facebook.com/ads/library/?id=1528637904246529 |
| Culture Connection 360 | Adjacent — Black-owned, target-city overlap | Image | 1389 | https://www.facebook.com/ads/library/?id=1854587274874683 |
| Culture Connection 360 | Adjacent — Black-owned, target-city overlap | Video | 616 | https://www.facebook.com/ads/library/?id=1626970728027954 |
| MuscleMax Nutrition | Adjacent — consolidation-pain hook | Image | 520 | https://www.facebook.com/ads/library/?id=638521059022164 |
| MuscleMax Nutrition | Adjacent — consolidation-pain hook | Image | 520 | https://www.facebook.com/ads/library/?id=2915127628674962 |
| MuscleMax Nutrition | Adjacent — consolidation-pain hook | Video | 511 | https://www.facebook.com/ads/library/?id=2657402541120718 |
| Black Girl Vitamins | Adjacent — demographic/tonal reference | Video | 491 | https://www.facebook.com/ads/library/?id=1042808314490835 |
| Aztlan Herbal Remedies | **Direct — sells sea moss** | Image | 234 | https://www.facebook.com/ads/library/?id=33756378080672196 |
| Aztlan Herbal Remedies | **Direct — sells sea moss** | Image | 234 | https://www.facebook.com/ads/library/?id=4207174419545602 |
| True Sea Moss (via "Stephanie DB") | **Direct — sells sea moss** | Video | 232 | https://www.facebook.com/ads/library/?id=1622784418708867 |
| MuscleMax Nutrition | Adjacent — consolidation-pain hook | Video | 178 | https://www.facebook.com/ads/library/?id=1620837889228218 |
| Infinite Age | **Direct — sells "Sea Moss Advanced" (subscription)** | Image | 167 | https://www.facebook.com/ads/library/?id=1295691402437579 |
| True Sea Moss (via "Maria Gladys") | **Direct — sells sea moss** | Video | 149 | https://www.facebook.com/ads/library/?id=1618740329206521 |
| True Sea Moss (via "Creatine Guru") | **Direct — sells sea moss** | Video | 140 | https://www.facebook.com/ads/library/?id=1454672926686595 |
| True Sea Moss Health (own page) | **Direct — sells sea moss** | Video | 137 | https://www.facebook.com/ads/library/?id=26254806004193321 |
| True Sea Moss Health (hydration powder) | **Direct — line extension** | Video | 133 | https://www.facebook.com/ads/library/?id=1630524021339696 |
| Infinite Age | **Direct — sells "Sea Moss Advanced" (subscription)** | Image | 126 | https://www.facebook.com/ads/library/?id=1020544373672952 |
| Black Girl Vitamins (via "Malinda Williams Fan Page") | Adjacent — whitelisting example | Video | 125 | https://www.facebook.com/ads/library/?id=1654893998966795 |
| True Sea Moss Health (Spanish variant) | **Direct — bilingual variant** | Video | 118 | https://www.facebook.com/ads/library/?id=961623883384743 |
| True Sea Moss (via "Fitness Addiction Blog") | **Direct — sells sea moss** | Video | 80 | https://www.facebook.com/ads/library/?id=2093173017898211 |
| Alevia | Adjacent — "personal confessional" hook format | Image | 80 | https://www.facebook.com/ads/library/?id=2032115717664795 |
| True Sea Moss (via "The Dodo," marked `#ad`) | **Direct — sells sea moss** | Image | 63 | https://www.facebook.com/ads/library/?id=2104845277080382 |
| Infinite Age | **Direct — sells "Sea Moss Advanced" (subscription)** | Video | 25 | https://www.facebook.com/ads/library/?id=2874471629660079 |
| Infinite Age | **Direct — sells "Sea Moss Advanced" (subscription)** | Image | 12 | https://www.facebook.com/ads/library/?id=2332132183989919 |
| naturalrems.com (via fabricated "Dr. Alina Marlowe" persona) | **Direct — sells sea moss gummies — ⚠️ study caution only** | Image | 6 | https://www.facebook.com/ads/library/?id=1375059997667848 |

## Honest limitation

Pass 1 found real, strong data on one direct sea-moss competitor (True Sea Moss) plus two adjacent
references — narrower than the brief's "10-15 distinct winning brands" framing implied. **The
widened pass-2 search (8 terms instead of 3) meaningfully closed that gap**: it surfaced two more
confirmed direct sea-moss sellers (Infinite Age, Aztlan Herbal Remedies) and ~35 additional adjacent
wellness/supplement brands, several genuinely useful as tonal/format references (Black Girl
Vitamins, the cross-brand "personal confessional" hook pattern). What's still true: the *direct*
sea-moss competitor set remains small in absolute terms — 3 confirmed direct sellers (True Sea
Moss, Infinite Age, Aztlan) is a real, not exhaustive, number for this specific product category,
which appears to be a genuinely under-advertised niche on Meta relative to general wellness
supplements. Running the same widened search again periodically (new ads start/stop constantly)
would be the way to keep this current, not further keyword-widening within the same category.

## Feeds directly into

- The **psychology pillar map** technique added to `ai-ugc-playbook.md`'s Section 0 — this is the
  competitor-research input it needs before synthesizing purchase-driver pillars.
- The `ads-competitor` skill (installed 2026-09-24) for any deeper follow-up pull.
- `access-checklist.md`'s "Competitor research" section — closing out step 1 of the brief's
  6-step pitch.

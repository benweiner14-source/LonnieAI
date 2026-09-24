# Rocka Moss — Meta Ad Library Competitor Research (2026-09-24)

Real, live-pulled data — not a guess. Closes the gap flagged 2026-09-24 (step 1 of `PROJECT_BRIEF.md`'s
6-step pitch: "Pull every sea moss competitor ad running right now on Instagram/Facebook — see
what's working before spending a dollar").

## Method

Direct browser fetches of `facebook.com/ads/library` are blocked (403, JS-rendering wall — same
pattern hit repeatedly elsewhere in this project). Ben supplied an Apify token; ran
`curious_coder/facebook-ads-library-scraper` (Apify's most-used Ad Library actor — 19.5M runs,
42K users, 4.77★/110 reviews) against 3 keyword searches, active US ads, all formats:
`sea moss`, `sea moss gel`, `black wellness`. Cost: ~$0.05 total (pay-per-ad, $0.00075/ad, 60 ads
pulled). 14 unique ads survived dedup across 3 distinct brands.

**Not storing scraped video/image files in this repo** — same reproduction-caution posture as
elsewhere in this project (the theme-code, YouTube-transcript, and ad-reverse-engineering
cautions). Every entry below links to its real, public Meta Ad Library permalink so the actual
creative can be viewed directly.

## Key finding: only one real sea-moss-specific competitor showed up — but it's a strong, proven one

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
  Atlanta** — two of Rocka Moss's three actual expansion cities — and the **longest-running ads
  in this entire pull** (616-1389 days). Casual, personal, community-voice copy style
  (first-name energy, emoji-heavy, direct address — "Come see us today"), not corporate. A real
  structural/tonal reference for what reads as authentic in exactly Rocka Moss's target
  cities/demographic, even though the product category is different.

## Full list (ranked by days running — longest-proven first)

| Advertiser | Format | Days running | Ad Library link |
|---|---|---|---|
| Culture Connection 360 | Image | 1389 | https://www.facebook.com/ads/library/?id=1854587274874683 |
| Culture Connection 360 | Video | 616 | https://www.facebook.com/ads/library/?id=1626970728027954 |
| MuscleMax Nutrition | Image | 520 | https://www.facebook.com/ads/library/?id=638521059022164 |
| MuscleMax Nutrition | Image | 520 | https://www.facebook.com/ads/library/?id=2915127628674962 |
| MuscleMax Nutrition | Video | 511 | https://www.facebook.com/ads/library/?id=2657402541120718 |
| True Sea Moss (via "Stephanie DB") | Video | 232 | https://www.facebook.com/ads/library/?id=1622784418708867 |
| MuscleMax Nutrition | Video | 178 | https://www.facebook.com/ads/library/?id=1620837889228218 |
| True Sea Moss (via "Maria Gladys") | Video | 149 | https://www.facebook.com/ads/library/?id=1618740329206521 |
| True Sea Moss (via "Creatine Guru") | Video | 140 | https://www.facebook.com/ads/library/?id=1454672926686595 |
| True Sea Moss Health (own page) | Video | 137 | https://www.facebook.com/ads/library/?id=26254806004193321 |
| True Sea Moss Health (hydration powder) | Video | 121 | https://www.facebook.com/ads/library/?id=1630524021339696 |
| True Sea Moss Health (Spanish variant) | Video | 118 | https://www.facebook.com/ads/library/?id=961623883384743 |
| True Sea Moss (via "Fitness Addiction Blog") | Video | 80 | https://www.facebook.com/ads/library/?id=2093173017898211 |
| True Sea Moss (via "The Dodo," marked `#ad`) | Image | 63 | https://www.facebook.com/ads/library/?id=2104845277080382 |

## Honest limitation

This pull found real, strong data on **one** direct sea-moss competitor (True Sea Moss) plus two
adjacent wellness/Black-owned-brand references — not the "10-15 distinct winning brands" the
brief's manual-alternative wording implies. The 3 keyword searches ("sea moss," "sea moss gel,"
"black wellness") are a reasonable first pass but a narrow net. If broader competitor variety is
wanted, worth running additional searches once specific competitor brand names are known (the
brief's own suggested third search term), or broadening keywords (e.g. "sea moss gel," "Irish
moss," "wildcrafted sea moss," specific flavor terms).

## Feeds directly into

- The **psychology pillar map** technique added to `ai-ugc-playbook.md`'s Section 0 — this is the
  competitor-research input it needs before synthesizing purchase-driver pillars.
- The `ads-competitor` skill (installed 2026-09-24) for any deeper follow-up pull.
- `access-checklist.md`'s "Competitor research" section — closing out step 1 of the brief's
  6-step pitch.

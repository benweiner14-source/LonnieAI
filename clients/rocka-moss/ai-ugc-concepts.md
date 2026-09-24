# Rocka Moss — AI UGC Character & Ad Concepts (2026-09-24)

Concept-first, per `ai-ugc-playbook.md`'s Section 0 rule ("concept first, prompt second") and
Ben's pipeline: `target-demo.md` → this doc → generate and lock a character sheet → generate the
concepts below. **Nothing here has been generated yet — concepts only, ready to greenlight.**

## The character

A synthetic (non-real) Black woman, working reference `RM-Char-01` — this is an internal label for
this doc, not text to render into any image or caption. Grounded in `target-demo.md`:

- **Casting:** a Black woman, confirmed by Ben directly (2026-09-24). Age range: working default
  is Women <30 (the archetype `ai-ugc-playbook.md` already maps Rocka Moss to), not locked —
  flag to Ben if a different age range is wanted before generating.
- **Vibe:** relatable, not aspirational-model — per Frankie Shaw's casting principle. Everyday
  presence, not influencer-polished. Rocka Moss's own athlete co-founder positioning supports a
  casual, active-adjacent look (gym-casual or everyday-athleisure) without being a fitness-model
  archetype specifically.
- **Setting logic:** Southeast-coded everyday environments (a modest apartment/kitchen, a parked
  car, a small local gym) — Columbia, SC or Charlotte, NC in *feeling*, never in literal on-screen
  place-name text (same standing rule this project already learned the hard way on Zion/Kazumi/
  Selena's packs — invented or real place names rendered as literal signage when spelled out in
  prompt text; describe the setting visually, never name the city).
- **Production path:** generate and lock via GPT Image 2.5 Sunburst (photoreal, not CGI-stylized —
  this is the opposite engine choice from the Zion/Kazumi/Selena avatar work), 2-3 regenerations
  to land a consistent identity, same approach as `clients/ai-ugc-agency/session-reference.md`'s
  character-reference step. Once locked, every concept below references that one locked identity
  image via the multi-image role-tagging technique (`docs/multi-image-role-tagging.md`).

## A caution before drafting angles: no verbatim Rocka Moss customer reviews exist yet

`seo-audit.md` confirmed zero visible reviews on the live product page. The "psychology pillar
map" technique (`ai-ugc-playbook.md`) calls for pillars backed by **verbatim real customer
quotes** — that data doesn't exist yet for Rocka Moss specifically. The two concepts below use
**category-level hypotheses** informed by the real competitor research already done
(`competitor-research.md`) and general sea-moss/wellness purchase psychology, explicitly **not**
presented as proven Rocka Moss customer language. Treat both as testable creative bets, not
locked psychology — and don't fabricate a "customer said this" line anywhere in the actual ad
copy, consistent with this project's standing no-fabricated-testimonials rule.

---

## Concept 1: "Morning Ritual" (Home/Lifestyle → mirror selfie)

**Psychology hypothesis (not a verified pillar):** *a ritual, not a chore* — positions the daily
sea moss habit as 2 minutes of self-care she actually looks forward to, not another supplement to
choke down. Distinct from True Sea Moss's benefit-list approach and Infinite Age's heritage/
medical-outcome framing (`competitor-research.md`) — leans into the *feeling* of the habit, not a
claim about what it does.

- **Format:** Home/lifestyle, shot as a real mirror selfie — reusing the mirror-selfie sub-genre
  already built and technically specified for Selena's photoreal pack (`prompts/selena-photoreal.md`):
  phone visibly held in the reflection, plain case, no screen content, genre-anchored as "a real
  iPhone mirror selfie photo of..." leading the prompt (not meta camera-position language, which
  this repo already proved doesn't work as reliably).
- **Flavor:** Strawberry Shortcake — the confirmed real sales leader (`target-demo.md`,
  `kpi-targets.md`), leading with it here for the first concept as planned.
- **5-beat outline** (per the transformational formula in `ai-ugc-playbook.md`):
  1. **Relatable scenario:** rushed weekday morning, coffee already going, hair not done yet — no
     product visible.
  2. **Character building:** normal get-ready routine reflected in the mirror, phone propped/held,
     casual talking-to-camera energy, mid-thought pauses (realism marker).
  3. **Progress, not before/after:** *"I've been doing this every morning for like three weeks
     now and I'm not gonna lie, my energy's been steadier — not like a jolt, just... steadier."*
     (Personal-experience framing, no medical claim.)
  4. **Introduce product:** reaches off-frame, comes back with the Rocka Moss Strawberry Shortcake
     jar, spoons it into a glass/smoothie — product held loosely, not presented to camera.
  5. **Soft close:** *"I'll leave it linked if you want to look into it."* No hard CTA, trails off
     naturally.
- **Realism markers carried in:** practical lighting only (bathroom/bedroom light, not studio),
  skin imperfections left in (no smoothing), one-handed handheld phone motion, performance that
  breaks eye contact/pauses rather than reading like a scripted line.
- **Production path:** generate the still via GPT Image 2.5 Sunburst (locked character reference +
  product reference role-tagged), then animate via Seedance 2.0 / Higgsfield Genjutsu per
  `docs/seedance-comfy-handoff.md`.

---

## Concept 2: "In-Car, Kind Of Random" (In-car confessional)

**Psychology hypothesis (not a verified pillar):** *consolidation, not another pill* — she used to
juggle several separate supplements, now it's one thing. Deliberately echoes the real, proven
**structure** of MuscleMax Nutrition's "stop taking 10 different supplements — just take these 2"
hook found in `competitor-research.md` (178-520 days running, a genuinely proven angle type) —
but rewritten entirely in Rocka Moss's own voice and specifics, not copied wording, consistent
with this project's standing reproduction-caution discipline.

- **Format:** In-car confessional — parked, engine off, natural daylight, unscripted "telling a
  friend something" energy, per `ai-ugc-playbook.md`'s named format list.
- **Flavor:** Strawberry Shortcake again for consistency across the first two concepts (keeps the
  character/product pairing recognizable) — Mango Magic (the #2 seller) is the natural next
  flavor once these two are validated.
- **5-beat outline:**
  1. **Relatable scenario:** sitting in a parked car about to head into work/an errand, phone
     propped on the dash or held loosely.
  2. **Character building:** *"So this is kind of random but..."* — mundane, low-stakes opener,
     not an ad-read cadence.
  3. **Progress, not before/after:** *"I used to have like five different things I was taking
     every morning and I'd always forget half of them. Now I just do this one thing."* (A
     consolidation/simplicity point, not a health-outcome claim.)
  4. **Introduce product:** holds up the Strawberry Shortcake jar, maybe takes a spoonful
     naturally mid-sentence — not a clean product-reveal shot.
  5. **Soft close:** trails off — *"Anyway... it's been good."* No CTA at all, deliberately
     softer than Concept 1's close, for variety.
- **Realism markers carried in:** same list as Concept 1 — practical light (real daylight through
  a car window, not studio), handheld phone angle typical of a dashboard-propped or hand-held
  selfie, natural speech pauses.
- **Production path:** same as Concept 1 — GPT Image 2.5 Sunburst still → Seedance/Genjutsu
  animation.

---

## Next step

Generate and lock `RM-Char-01`'s character sheet first (GPT Image 2.5 Sunburst, 2-3 regenerations
to confirm a consistent identity) — both concepts above depend on that one locked reference.
Then validate Concept 1 as a still before animating or drafting Concept 2's still, same
validate-before-batch discipline as every other pack in this repo. Not yet started — this doc is
concepts only, waiting on Ben's go-ahead to spend on generation.

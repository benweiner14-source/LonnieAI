# Tay — AI UGC / Dropshipping Production Method

A second creator's material, distinct from `docs/frankie-shaw-ai-ugc-method.md`. Where Frankie
Shaw's doc is creative philosophy (what should the ad *be*), this one is closer to an **end-to-end
production workflow and ad-launch/retention playbook** from a Shopify/dropshipping-focused
creator (referred to here as "Tay") — a different tool chain, a competitor-reverse-engineering
sourcing technique, and post-ad-launch tactics (Meta account structure, retention email flows)
that neither this repo nor the Frankie Shaw doc covers. Two videos, both transcripts pasted
directly by Ben and reviewed here — **not saved verbatim into this repo** (someone else's
copyrighted spoken content; everything below is paraphrased, new-information-only extraction,
same policy as the Frankie Shaw material).

---

## Video 1 — Turning a competitor's static image ad into a video ad

**Core technique: reverse-engineer a proven concept instead of inventing one from scratch.**
1. Find a competitor's static image ad that's already validated by engagement (he uses raw
   like/comment/share counts as the signal) and a well-built site behind it.
2. Source a similar, cheaper product (his example: an AliExpress equivalent of a $700 product),
   priced at roughly 3x landed cost.
3. Use AI to swap the competitor's product and model for your own inside the *same proven
   composition* — the concept and framing are what's proven, not the specific product or person
   in it.
4. Animate the resulting still into video, since video ads can outperform the same concept as a
   static image.

**Tool chain used:**
- **Claude (he used Opus 4.5)** — fed the competitor's static image + a clean photo of your own
  product, plus a written instruction of exactly what to swap (subject, product, any text/logo to
  remove). Claude's job here is purely to *write the image-generation prompt*, not generate the
  image itself.
- **Google Gemini's image model ("Pro" tier)** — takes that Claude-written prompt + the same two
  reference images and actually performs the swap/generation.
- **Canva's "magic eraser"** — removes the Gemini watermark from the output (paint over it,
  done).
- **A second Claude pass**, fed the new swapped image, writes a follow-up image-edit prompt for a
  second pose/state (his example: the same character in a "floating" variant) — building a start
  frame and an end frame from two separate generations, not one.
- **Kling AI, image-to-video, start-frame + end-frame mode** — animates between the two stills.
  Prompted with a third Claude-drafted prompt describing the motion. He recommends the "2.5 Turbo"
  tier over the newer "2.6" for better credit efficiency, and generating a single output rather
  than multiple at once to conserve credits.

**⚠️ Worth flagging given this repo's own posture:** this technique is explicitly "copy a
competitor's proven ad, put your own product/model twist on it" — closer to reproducing a
specific execution than inventing an original one. Tay's own caveat is to change the background/
details so it isn't a 1:1 copy. That's a floor, not necessarily enough on its own — this repo's
existing brand-deal methodology (`clients/rocka-moss/PROJECT_BRIEF.md`) already sources
comparison ads the safe way: **screenshotting public Meta Ad Library entries** for reference, not
scraping or closely reproducing a specific competitor's actual creative asset. If this technique
gets used for Rocka Moss, treat "proven ad" as inspiration for *structure and composition*
(subject placement, product framing, camera angle) — same spirit as this repo's own multi-image
role-tagging technique already does for identity — not as a source image to closely reproduce.

**A reusable B-roll technique, independent of the reverse-engineering angle:** generate a
"nobody in frame yet" starting image and a "product in use" state as two separate stills, then
animate between them to create a walk-up-and-use opening shot. He used this as an alternate hook
spliced in before the main scene — the same "different opening hook, same core scene" pattern is
directly reusable for Rocka Moss (e.g., someone walking up to a kitchen counter before the
mixing-a-smoothie moment).

**Facebook/Meta ad-account structure (his default, at this creator's reported scale — $250K/30
days on one store, one $18K day at 20% net margin):**
- One CBO (campaign budget optimization) campaign, started at **$50/day**.
- **One ad set, fully broad targeting** — no interest targeting, no age/gender constraints. The
  creative does the targeting, not the ad-set settings.
- Upload as many creatives as you have — 2-3 is a floor, not a target; more creatives = more
  surface area for Meta to find what works.
- Scale a working campaign **20% every 1-2 days**, not in large jumps.
- This is simpler than — and a useful comparison point against, not a replacement for — the
  `coreyhaines31/marketingskills` `ads` skill named in `clients/rocka-moss/PROJECT_BRIEF.md`
  (manual/cost-cap bid progression, 70/30 proven/testing budget split, the "zombie campaign"
  tactic). Worth having both in mind when Rocka Moss's account actually launches.

**Retention/email (Omnisend) — concrete flow types, reported at ~30% of total store revenue /
roughly $28K in a month for this creator:**
- **Cart/browse-abandonment recovery** — automated flow with a discount incentive; he defaults to
  the highest tier offered (15% in his example).
- **Post-purchase cross-sell** — auto-pulls best-sellers (or a manually chosen product list) with
  its own discount incentive (15-20% range).
- **High-value-customer segmentation** — e.g. "everyone who's spent $100+ lifetime," built with
  Omnisend's own segment-builder AI from a plain-language query, then targeted with dedicated
  campaigns (his example: a seasonal/holiday discount blast using a pre-built template).
- Gives the Rocka Moss brief's generic "Monthly reporting... no jargon" and general email/SMS
  ambitions a concrete starting workflow list, if/when Rocka Moss's engagement extends to
  retention email (not currently in scope per `clients/rocka-moss/ai-ugc-playbook.md`, which is
  scoped to image/video generation only).

**Profitability tracking:** he uses a Shopify app ("True Profit") that syncs ad spend (via ad
platform connections) and a manually entered per-product fulfillment cost to show real daily net
profit automatically. Worth evaluating as a category of tool once Rocka Moss's Meta Pixel/CAPI are
live (per `PROJECT_BRIEF.md`'s access-needed checklist) — feeds directly into the brief's
CPA/ROAS reporting ask.

---

## Video 2 — An AI agent (Manus) running the whole production pipeline autonomously

Describes using **Manus**, a general-purpose AI agent platform, to run an entire ad-production
pipeline from a single multi-step written brief plus one product URL. At a high level, the agent:

1. **Researches the product** from the given link. When it hit an access block on one site, it
   asked to take over the user's own logged-in Chrome browser (via a browser-extension bridge) to
   continue — worth flagging on its own: **this is the same shape of workaround** (using
   browser automation / a live session to get past an access block) **that this project has
   previously declined to force through** (the Selena reference-photo scraping block, see
   `CLAUDE.md`). The risk profile is different here — it's the product owner researching their
   own public product listing and reviews, not scraping a real person's private social content —
   but the pattern itself deserves the same checkpoint-before-adopting caution, not an automatic
   pass because the tool offers it as a built-in feature.
2. **Runs deep market research in parallel** across multiple sources (competitor sites, Reddit,
   Amazon reviews, YouTube reviews) via sub-agents working simultaneously.
3. **Scrapes recent high-performing TikTok videos** in the product's niche (his filter: last 30
   days, 1M+ views) and reverse-engineers hook/script patterns from what's actually working right
   now.
4. **Drafts multiple candidate ad scripts** (3, in his example) synthesized from all of the above.
5. **Generates a consistent UGC "character"** — three matching reference views (front/side/back)
   built from an uploaded product photo, so the character's interaction with the product stays
   accurate from every angle. Supports an interactive mark-up-and-reinstruct edit loop (select the
   wrong part of an image, describe the fix, regenerate just that region).
6. **Writes shot-by-shot prompts for Kling 3.0's multi-shot mode** — a single generation that
   produces several distinct ~5-second scenes/camera angles from one starting frame, driven by a
   separate text prompt per shot plus tagged reference images (an `@image` mention syntax to pin
   a specific reference to a specific shot).
7. **Generates additional B-roll** the same tagged-reference-image way, meant to be edited
   together with the "talking" shots in CapCut.

**Honesty check, from the creator himself:** results were not one-shot perfect — several
generated B-roll clips were unusable or made no sense, requiring multiple regeneration batches
before landing on usable shots. Treat this as a real tool with real iteration overhead, the same
validate-before-batching discipline this repo already applies everywhere else, not a
push-button pipeline.

**Genuinely new technical capability vs. this repo's current stack:** Kling 3.0's multi-shot mode
(one generation → several tagged-reference-driven scenes/angles) is a different capability from
the single-reference-set-per-generation pattern this repo has used with Seedance/Genjutsu so far.
Worth evaluating for a future Rocka Moss multi-shot sequence (the kind of thing built for Kazumi's
penthouse-party vignette) — **not yet tested in this project's own Comfy Cloud/Higgsfield
pipeline**, since Kling/Manus aren't currently wired into this project's toolset. This is a
"worth evaluating," not an "adopt now" — same discipline as every other new technique that's
crossed into this repo.

---

## What's not covered here

Manus/Kling/True Profit account setup, pricing tiers, and referral-link specifics are product
mechanics, not creative technique — skipped here as out of scope for this doc.

## Sources
Two YouTube videos, transcripts pasted directly by Ben, reviewed against this repo's existing
material for genuinely new content. Raw transcripts not saved into this repo.

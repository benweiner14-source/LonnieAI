# Tay — AI UGC / Dropshipping Production Method

A second creator's material, distinct from `docs/frankie-shaw-ai-ugc-method.md`. Where Frankie
Shaw's doc is creative philosophy (what should the ad *be*), this one is closer to an **end-to-end
production workflow and ad-launch/retention playbook** from a Shopify/dropshipping-focused
creator (referred to here as "Tay") — a different tool chain, a competitor-reverse-engineering
sourcing technique, granular Meta ad-account setup, AI-assisted performance reporting, and
product-page/landing-page generation that neither this repo nor the Frankie Shaw doc covers. Six
videos total, all transcripts pasted directly by Ben and reviewed here — **not saved verbatim
into this repo** (someone else's copyrighted spoken content; everything below is paraphrased,
new-information-only extraction, same policy as the Frankie Shaw material).

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
**The same caution applies to Video 6's "model your product page after a competitor's page"
technique below — it's the same pattern applied to page layout instead of ad creative.**

**A reusable B-roll technique, independent of the reverse-engineering angle:** generate a
"nobody in frame yet" starting image and a "product in use" state as two separate stills, then
animate between them to create a walk-up-and-use opening shot. He used this as an alternate hook
spliced in before the main scene — the same "different opening hook, same core scene" pattern is
directly reusable for Rocka Moss (e.g., someone walking up to a kitchen counter before the
mixing-a-smoothie moment).

---

## Video 3 — Granular Meta ad-account setup + AI-assisted daily performance review

A much more concrete walkthrough than Video 1's summary-level ad-structure notes — worth using
as the actual step-by-step when Rocka Moss's campaign gets built.

**Campaign setup, in order:**
- **Campaign level:** Sales objective; name the campaign after the product (+ "test" while
  testing); budget set at the **campaign level** (CBO), starting **no lower than $25/day** ($50
  if faster results matter more than budget conservatism); bid strategy = "highest volume."
- **Ad set level:** name it descriptively (he names it literally "broad" as a reminder of the
  targeting choice); conversion location = website; optimize for maximum number of conversions;
  select the store's connected pixel (set up once via the Shopify + Facebook app connection, a
  ~1-2 minute one-time task); conversion event = purchase; schedule the start for the next day at
  midnight in the ad account's own timezone (not immediate).
- **Audience:** touch nothing except location. **Test one single country at a time** —
  spreading an already-small $25-50 testing budget across multiple countries makes it too hard to
  tell whether the creative works for any specific market. No age/gender/interest targeting at
  all; the creative itself is what does the targeting. Ad-transparency settings only matter for
  EU-targeted campaigns.
- **Creatives:** test 2-3 *genuinely distinct* variations per new product — his emphasis is that
  a real test varies hook, script, *and* visuals together, not just re-edits of the same take.
  Per-ad setup: name each ad distinctly (e.g. "ad version one"); requires a Facebook Page (an
  Instagram connection is optional — ads can run to Instagram off the Page alone); manual upload,
  single image/video; deselect "multi-advertiser ads"; destination = the direct product-page URL.
- **Ad copy:** he uses a purpose-built custom GPT to generate three *formats* of copy (not just
  three variations of the same format) from a couple of product images — one straightforward
  benefit-led version, a second variant, and a third written as if it were a customer's own quote.
  He pastes **one from each format** into the ad as three separate Primary Text options, plus 3
  headlines and 2 descriptions the same way, so the ad naturally split-tests format alongside
  creative. CTA = "Shop Now." **He explicitly deselects Facebook's own AI-suggested ad copy and
  AI-generated image options every time** — calls the auto-generated copy "pretty terrible" and
  doesn't trust the auto images either.
- **Iterating without relaunching:** to test a new creative, "quick duplicate" an existing ad
  *within the same ad set* rather than creating a new ad set — this carries over all the proven
  copy/settings, and only the video needs swapping. He specifically likes this because Facebook's
  own algorithm decides how much (if any) budget to actually spend on the new variant automatically —
  he showed a live example where a recently added weak-looking batch of new ads was getting
  almost no spend allocated to it, which he treats as Facebook correctly recognizing they weren't
  as strong as the existing winners, not as something to intervene on manually.
- **Scaling discipline:** once a campaign is working, scale **20% every 1-2 days** — same number
  already in this doc, now with an explicit warning attached: **don't jump budget by 100%+ right
  after the first sales land.** A few early sales don't mean a product is ready to scale
  aggressively; his recommended next move at that point is to add more creative variations first
  (same ad set, same technique above), not to dramatically increase spend on what's already
  running.
- This remains simpler than — and still a useful comparison point against, not a replacement
  for — the `coreyhaines31/marketingskills` `ads` skill named in `clients/rocka-moss/
  PROJECT_BRIEF.md` (manual/cost-cap bid progression, 70/30 proven/testing split, the "zombie
  campaign" tactic). Worth having both in mind when Rocka Moss's account actually launches.

**AI-assisted daily performance review — new, and directly answers the brief's reporting ask.**
He connects Claude.ai to his Facebook Ads account, Shopify store, and the TrueProfit app via
custom MCP connectors (added under Claude's Settings → Connectors → Add custom connector, pointed
at a connector URL specific to each service), then just asks Claude in plain language for a
performance read: what happened, what the metrics mean, whether to keep running / kill / scale
the campaign, and what to fix. Claude pulls live numbers from all three sources and gives a
plain-English breakdown (CTR, CPC, CPM, CPA, break-even ROAS, day-over-day comparison) plus a
recommendation — genuinely no different in spirit from what a human media buyer would read off a
dashboard, just done conversationally. **If a Facebook MCP connector isn't available**, the same
thing works by exporting the campaign as a CSV from Ads Manager and uploading that file to Claude
instead — a reliable fallback path.

**This maps directly onto `PROJECT_BRIEF.md`'s Bucket 2 ask — "Monthly reporting: plain numbers
every month; impressions, clicks, purchases, cost per acquisition; no jargon."** This pattern
could deliver that at daily cadence rather than monthly if useful, using tools Ben already has
access to (Claude, and whichever Shopify profit-tracking app gets adopted). Worth setting up once
Rocka Moss's Meta Pixel/CAPI and ad account exist — see `PROJECT_BRIEF.md`'s access-needed
checklist.

**Profitability tracking (reinforced across multiple of these videos):** the "True Profit"
Shopify app syncs ad spend (via ad-platform connections) and a manually entered per-product
fulfillment cost to show real daily net profit automatically — and it has its own MCP connector,
which is what feeds the Claude-reporting pattern above. Worth evaluating as a category of tool
once Rocka Moss's Pixel/CAPI are live.

---

## Retention/email (Omnisend) — concrete flow types, from Video 1

Reported at ~30% of total store revenue / roughly $28K in a month for this creator:
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

---

## Video 4 — Seedance 2.0 as a fully autonomous "video agent" (via TopView)

A platform called TopView offers Seedance 2.0 through a built-in "video agent" that, given one
product reference image plus a written brief (character description, product image, desired
camera/pacing style, and a script), independently builds the character, camera work, and scene
switching — no separate manual character-sheet step.

**⚠️ Important, independently confirms something already in `docs/frankie-shaw-ai-ugc-method.md`:**
he explicitly warns that Seedance 2.0 is **sensitive about uploading a photo of an actual real
person** as a character reference and recommends writing a plain-text description of the desired
character instead, letting Seedance generate it from scratch. He mentions a partial workaround —
generating the character first through "Nano Banana" and feeding *that* image in sometimes gets
through — but found it unreliable and hit frequent errors, so his actual recommendation is just
to describe the character in words. **This independently confirms, from a completely different
creator and platform than Frankie Shaw's, the same real-face-upload restriction already
documented in `docs/frankie-shaw-ai-ugc-method.md`'s "Production Realities" section** — two
unrelated sources landing on the same platform behavior is a strong signal it's real and current,
not a one-off account quirk. Doesn't change the strategic fork already flagged for Rocka Moss
(synthetic character vs. Christian's real likeness via this repo's own Comfy Cloud path, which
has *not* hit this restriction per Kazumi's motion-transfer pilot) — just reinforces that the
restriction itself is real on at least some Seedance access points.

**Production-quality constraints worth carrying over regardless of platform:**
- **Sweet spot: no more than 2-3 scenes per generation.** Quality visibly degrades once a
  generation tries to pack in 4+ scenes. If an agent/tool proposes more, explicitly prompt it to
  condense to ≤3 scenes.
- **Match each scene's duration to its actual dialogue length**, or the character ends up
  talking too fast / cut off mid-sentence. Fix: increase that specific scene's duration by a
  couple of seconds and regenerate — the model redistributes the dialogue pacing to fit.
- **"Enhance all"-style prompt expansion**: some tools offer a feature that automatically
  rewrites terse scene prompts into detailed sub-shot-by-sub-shot direction (breaking a 4-second
  scene into named beats with specific timing) — worth checking whether any tool in this
  project's own stack (Comfy Cloud, Higgsfield) offers something equivalent, since it would save
  real manual prompt-writing effort on multi-beat scenes.
- **"Extend" / continue-from-last-clip mode exists but was flagged by the creator himself as
  currently buggy quality-wise** — conceptually useful for building sequences longer than one
  generation's scene cap (the same goal as this repo's own "chain off the actual previous
  rendered output" technique from Kazumi's penthouse-party vignette), but not something to rely
  on yet without testing quality first.
- **Realistic yield expectations:** generating the same script multiple times produces a mix —
  some fully usable takes, some with one boring/static stretch that needs B-roll patched over it,
  some outright discards. Same "generate several, keep the best, discard the rest" discipline
  already standard in this repo.

---

## Video 5 — Hermes agent (via Discord) running the same kind of pipeline

A second AI-agent example, functionally similar to Video 2's Manus workflow but accessed through
Discord and branded "Hermes." Given a product link, it researches the product, proposes 3 ad
angles and 3 scripts with its own recommendation, builds a full shot plan, generates reference
images (multiple product angles *and* a character), and produces the final video via Seedance 2.0
— including a self-correction loop (told about a mistake — e.g. a product detail rendering on the
wrong side — it regenerates with that fix applied within the same conversation). **Same honesty
caveat as Video 2, stated even more directly here:** the creator is explicit that this "looks
easy" only because he spent **multiple hours training this specific agent** beforehand on his own
process — a fresh, untrained agent won't reproduce the same one-shot quality, so budget for real
setup/iteration time before expecting this level of output.

**Not directly applicable to Rocka Moss, noted for completeness only:** a chunk of this video
covers using **Zendrop** (a dropship product-sourcing and fulfillment platform) to *find* a
product to sell in the first place, with an AI agent that can browse Zendrop's trending-products
list, check per-country fulfillment cost/delivery time, and auto-build a Shopify product page
from a sourced item. Rocka Moss already has its own real, established product — this
sourcing-a-product-to-dropship layer doesn't apply and isn't summarized further here.

---

## Video 6 — Building/redesigning a product page with Claude Design

A workflow for generating a full branded Shopify product page using **Claude Design** (a
distinct, canvas-based feature from plain Claude chat) plus a custom GPT for product photography —
maps onto `PROJECT_BRIEF.md`'s Phase 6 landing-page-quality ambitions ("Shopify theme refresh +
tighter homepage... could lift conversion rate without touching product").

- **Import the product** into Shopify via a connected sourcing platform (Zendrop in his case — not
  relevant to Rocka Moss, which already has its product listed) or, for Rocka Moss, presumably by
  working directly against the existing rockamoss.com product/theme once collaborator access is
  granted (per `PROJECT_BRIEF.md`'s access-needed checklist).
- **Model the page after a specific reference**, one of two ways: a general style-inspiration
  search (he uses Pinterest, searching "product page design"), or a **full-page screenshot of one
  specific competitor/brand's actual product page** (via a browser screenshot extension), given to
  Claude Design as a structural template to closely model section-by-section. **Same caution as
  Video 1's ad-reverse-engineering technique applies here** — modeling *layout and structure*
  after a reference is different from closely reproducing someone else's actual page; use it for
  structural inspiration (section order, layout rhythm), not as a source to copy closely.
- **A genuinely new, directly useful idea: feed the page-design prompt your actual running ad
  creative (raw video files, not just links)**, so Claude can read what claims/benefits/tone the
  ads are already making and match the landing page's copy and featured benefits to them. This is
  an ad-to-landing-page **message-consistency check** this repo hasn't had a technique for before —
  directly applicable once Rocka Moss has both an ad pack and a page redesign in flight, so the
  two don't drift apart.
- **Iterate via inline comments, batched:** mark up specific sections directly on the generated
  page with plain-language change requests (add icons, drop a column, remove a section entirely,
  rewrite a section's purpose), queue up several comments, submit them together, Claude applies
  all of them in one pass.
- **⚠️ A real caution, distinct from anything else flagged in this repo so far: one of his
  comment-requests explicitly asks Claude to populate an empty reviews section with fabricated
  customer reviews** ("realistic... varied writing lengths, tone... occasional grammar mistakes...
  emojis"). **Do not carry this over to Rocka Moss without Ben's explicit, separate sign-off.**
  Rocka Moss is an established brand with real customers and real reviews already (per
  `PROJECT_BRIEF.md`) — fabricating customer testimonials is a materially different risk category
  from anything else in this repo's guardrails (AI-generated ad creative and product photography
  are disclosed-or-obvious synthetic media; a fake review presented as a real customer's words is
  a deception risk — FTC guidance and most platforms' policies treat fabricated reviews as
  prohibited, not just an "optional/aggressive claim" the way this repo already treats bold
  medical claims). If Rocka Moss's page needs reviews, use real ones or leave the section out
  until real ones exist.
- **Product photography via a custom GPT**, three sub-modes: (1) direct product photography from
  multiple real reference angles of the actual product plus an in-use example; (2) infographic-
  style images modeled after another brand's infographic (same reference-modeling pattern as
  above); (3) UGC-style photos. Overlaps with, and reinforces, this repo's existing multi-image
  role-tagging technique and `clients/rocka-moss/ai-ugc-playbook.md`'s own Section 1 (product
  photography).
- **Model choice note:** he uses Sonnet 5/Opus 5 for the simpler import task, Fable 5 (medium
  effort) for the more complex page-design generation, noting Opus 5 as a fine substitute if
  Fable 5 isn't available on a given plan.
- **Simple QA reminder worth keeping:** always manually click-test core page functionality (he
  specifically checks "Add to Cart") after any AI-driven page edit — something can silently break
  during a generated change, and it's cheap to catch before it costs a sale.

---

## What's not covered here

Manus/Hermes/Kling/TopView/Zendrop/True Profit account setup, pricing tiers, and referral-link
specifics are product mechanics, not creative or tactical technique — skipped here as out of
scope for this doc.

## Sources
Six YouTube videos, transcripts pasted directly by Ben, reviewed against this repo's existing
material for genuinely new content. Raw transcripts not saved into this repo.

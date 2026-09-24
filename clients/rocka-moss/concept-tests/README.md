# Concept 1 ("Morning Ritual") — product-intro beat, GPT Image 2.5 vs. Nano Banana Pro (2026-09-24)

First test render of Concept 1's "introduce the product" beat — editing the locked
`character-sheet/rm-char-01_full-body-mirror.png` to add the Strawberry Shortcake jar into her
hand. Ben asked to try both engines side by side (this project's standing recipe for photoreal UGC
is GPT Image 2.5; Nano Banana Pro is the CGI-stylization engine used for the Zion/Kazumi/Selena
avatar work — this is the first time this project has tested Nano Banana Pro specifically for
Rocka Moss's photoreal UGC use case, not just assumed the standing recipe applies).

**Both used the same single-reference-image technique** (her locked mirror-selfie photo as the
edit base, the actual Strawberry Shortcake jar described in precise text rather than as a second
image — GPT Image 2.5's edit path only accepts one reference image via this route; Nano Banana
Pro's multi-image path needs public URLs, not Comfy-uploaded files, so a two-image call wasn't
straightforward either way for this test) — same standing "smooth glass, don't copy the reference
photo's embossed MASON text" fix from the original product-photo test.

## Results

- **`concept1_product-intro_gpt25-sunburst.png`** — **identity, pose, and setting held almost
  perfectly** against the locked reference (same face, same expression looking at camera, same
  bedroom framing). Glass rendered smooth, no embossing leak. **Weakness: most of the label's
  small text rendered blank/illegible** — "SEA MOSS" and "Wildcrafted" script are legible, but the
  top logo area and the bottom mineral-claim/net-weight bars are mostly blank — the same
  small-text limitation flagged on the very first Rocka Moss product-photo test.
- **`concept1_product-intro_nano-banana-pro.png`** — **attempted more of the label text** (the
  "ROCKA MOSS" logo/wordmark is actually legible here, unlike the GPT version) but with a real
  **spelling error**: "Wildcrafted" rendered as "Wilderafted." **Weakness: identity/pose drifted**
  from the locked reference — she's looking down at the jar instead of at the camera, and the
  room's framing/proportions shifted slightly. Glass also rendered clean, no embossing leak.

## Read

**GPT Image 2.5 Sunburst is the stronger pick for this use case.** Keeping the character visually
identical across a whole ad series matters more than legible side-bar text — and a real iPhone
selfie photo usually doesn't hold small label text sharply either, so blank-but-plausible reads as
more "real" than a typo does. Nano Banana Pro's label-text attempt is a genuine plus worth
remembering if a future shot needs the label to actually be read clearly (e.g. a close-up product
insert), but its identity drift here is a real cost for a character meant to stay consistent shot
to shot. **This empirically confirms, on this exact character/product combination, the standing
project-wide finding that GPT Image 2.5 is the right engine for Rocka Moss's photoreal UGC work**
— not just carried over by assumption from the earlier Selena-pack decision.

## v2 — Ben's real feedback, 2 fixes (2026-09-24)

Ben confirmed Nano Banana Pro is out. Two more findings on the GPT-2.5 version specifically:

1. **The bedroom setting didn't make narrative sense** — holding the product in a bedroom doesn't
   resonate; sea moss prep/consumption belongs in a kitchen. Fixed by editing the locked
   `character-sheet/rm-char-01_three-quarter.png` (already set in her actual kitchen, matching
   seed B's own establishing shot) instead of the bedroom mirror shot — dropped the "mirror
   selfie" device entirely rather than trying to force a mirror into a kitchen that likely
   wouldn't realistically have a full-length one.
2. **The GPT-2.5 still read a little uncanny-valley / visibly AI-generated, needed more authentic
   UGC iPhone feel.** Pulled concrete language from `docs/frankie-shaw-ai-ugc-method.md`'s V4
   Realism Laws (still-photo-appropriate subset: believable practical light only, no
   cinematic/studio polish, real skin texture/blemishes not airbrushed, ordinary/slightly-worn
   surfaces, anti-"digital render" language) rather than a vague "make it look more real" ask.

**`concept1_product-intro_v2_kitchen-realism.png`** — kitchen setting confirmed correct (same
kitchen as the locked character reference). Label came out cleaner as a side benefit — the
"ROCKA MOSS" logo and "Wildcrafted" (correctly spelled this time) are both legible, better than
either v1 attempt. Realism read is improved (more natural lighting asymmetry) but **not yet
confirmed as fully clearing the "does this look AI" bar — sent to Ben for a direct judgment call**,
same standing discipline as every recipe in this repo (nothing confirmed until Ben's eyes are on
it). If it's still not authentic enough, the next lever to pull is a genuinely imperfect crop/
framing (off-center, slightly cut off) rather than more lighting/skin-texture language, since
`docs/tay-ai-ugc-dropship-method.md` and this project's own iPhone-selfie work both point at
framing/POV as the strongest authenticity signal, stronger than texture-level prompt tweaks alone.

## v3 — the real root cause: no camera device implied, so it read as a posed portrait (2026-09-24)

Ben's follow-up on v2: **"it just feels like it's posed... no one is sitting in their kitchen
[taking] a highly professional photo posed holding a jar."** His fix, stated directly: **"I
whipped out my phone, I'm taking a selfie, or I'm standing my iPhone up... using that as a stand
to take a selfie."** The real diagnosis: v1/v2 never implied any camera device at all — no phone
in her hand, no propped-phone framing cue — so the model defaulted to composing it like a
professional portrait shot by someone else, the exact same root-cause pattern this project's own
`skills/iphone-selfie-style/SKILL.md` already solved for the CGI-avatar work (genre-anchoring
beats meta camera-position instructions). Rebuilt around the **propped-phone-on-the-counter**
technique Ben specifically named — a real, common amateur-UGC move, distinct from a held-out
selfie: genre-led as "a real, candid photo captured by her own iPhone, propped up standing against
a container on the kitchen counter... using it as a makeshift stand/tripod," explicit "phone is
out of frame, it's the camera taking this shot" instruction, and a wider/further-back framing
(since a propped phone sits further away than a held one) with a slightly imperfect/tilted angle
and mid-motion, not-looking-at-camera body language instead of a held pose.

**`concept1_product-intro_v3_propped-phone.png`** — genuine step change. She's caught mid-motion
reaching toward the jar (sitting on the counter, not yet gripped), looking down/away rather than
at the camera, no posed smile, wider off-center framing with real kitchen clutter (dishes in the
sink, knives, coffee maker) — reads as an actual candid propped-phone photo, not a professional
portrait. One honest trade to flag: this changes the beat from "already holding the product up"
to "reaching for it," a fair, more candid variant of the same moment, not a beat this project
invented arbitrarily — matches the "caught mid-motion, not posed" instruction directly. **Sent to
Ben for judgment, not self-certified.**

## v4 — fixed the hallucinated/illegible label via a proper multi-image edit (2026-09-24)

Ben's real feedback on v3: "getting better. Still not there yet. but in this the jar is not really
legible and has some text hallucination." Real root cause: v3's jar was described in text only
(no image reference) — GPT-2.5's simplified `partner_generate` edit path only accepts one
`image` role, no second `reference_image`, which is why the label kept getting invented/garbled
rather than illegible-but-plausible. **Fixed by dropping down to a hand-built `submit_workflow`
graph** using the `OpenAIGPTImageNodeV2` node directly, which exposes `model.images.image_1`
through `image_16` (confirmed via `get_node`) — something `partner_generate`'s simplified
`medias[]` interface doesn't surface for this model. Wired **two** LoadImage nodes: image_1 = the
v3 propped-phone photo itself (the scene to edit, kept identical), image_2 = the real Strawberry
Shortcake jar photo from `refs/` (label reference only, explicitly told to ignore its bench
background/embossing/watermark). Validated with `dry_run: true` before spending.

**`concept1_product-intro_v4_label-fix.png`** — the v3 scene preserved exactly (same mid-motion
reach, same off-center framing, same kitchen clutter) with the jar's label now genuinely accurate
and legible: correct "ROCKA MOSS" logo, correctly-spelled "Wildcrafted," the kelp graphic, the
flavor tag — copied from the real reference instead of invented. No embossed glass text. **Sent to
Ben for final judgment**, but this closes the two outstanding defects (posed feel, illegible/
hallucinated label) in one pass.

## Next step

Waiting on Ben's read of v4. If this lands, it's the full technique to reuse going forward for any
shot needing both a candid propped-phone scene AND an accurate product label: build the scene via
a single-image edit first (get pose/setting/realism right), then do a second pass with the real
product photo wired in via `submit_workflow`'s two-image `OpenAIGPTImageNodeV2` path to fix the
label without disturbing the scene — not something `partner_generate`'s simpler interface can do
in one call for this model.

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

## v5 — schema-driven single-pass regeneration (2026-09-24)

Ben asked to try Concept 1 again using `ai-ugc-json-schema.md`'s v2 schema — a real test of
whether writing the full spec (role-tagged refs + `reference_fidelity` + `negative_prompt` +
`canvas`) up front gets to v4-quality output in **one** generation instead of the four iterative
rounds (v1→v4) it took to discover the same fixes piecemeal.

**Built directly from the schema, not chained off v3/v4.** Used `submit_workflow` +
`OpenAIGPTImageNodeV2` with two LoadImage nodes from the start (not as a second corrective pass):
image_1 = `character-sheet/rm-char-01_three-quarter.png` (identity + kitchen environment, told to
ignore its pose), image_2 = `refs/rockamoss_strawberry_jar_bench.jpg` (label only, told to ignore
its bench background/embossing/watermark — same "this jar's glass is smooth, unlike the
reference's embossed glass" wording that fixed the original product-shot test). The prompt text
compiled the schema's `final_generation_instruction` + `negative_prompt` fields directly: genre-led
propped-phone-on-counter POV, mid-motion reach (not posed), off-center wide framing, morning window
light, plus an explicit negative list (no visible phone, no embossed glass, no illegible label, no
studio lighting, no CGI look, no extra/fused fingers). `dry_run: true` validated first, `n: 2` for
two seeds in one job, 1152×2048 (exact 9:16).

**`concept1_v5_schema_seedA.png` / `concept1_v5_schema_seedB.png`** — both landed cleanly on the
first attempt: accurate legible label (logo, "Wildcrafted" script, teal tagline, flavor tag,
mineral claim, net weight, no hallucinated text, no embossed glass), no visible phone anywhere in
frame, off-center mid-motion framing (not posed), real kitchen clutter, natural window light, no
CGI/studio tell. Seed B added an unprompted smoothie-prep detail (banana, strawberries, blender on
a cutting board) reinforcing the narrative. **One thing flagged for Ben's eye, not resolved
here:** skin tone/curl pattern reads slightly different between the two seeds — normal seed
variance, but worth checking which (if either) still reads as a close match to the locked RM-Char-01
reference. **Sent to Ben for judgment**, not self-certified.

**Real validation of the schema's value:** this is the first time this project got scene + label +
no-phone-in-frame all correct in a single generation, on the first attempt, for this concept —
compare to v1-v4's four-round discovery process for the same three fixes. Worth using this
"write the full schema first, generate once" pattern as the default going forward, falling back to
the iterative single-field-fix approach only when something in a first pass still needs isolating.

## Next step (superseded by Concept 2's first pass below)

Waiting on Ben's read of v5 (and a call on which seed, if either, is the stronger identity match).
If v5 holds up, the schema-first single-pass method above becomes the default technique for
Concept 2 and any future shot — write the JSON spec fully, then generate once via `submit_workflow`
+ two LoadImage nodes, rather than iterating field-by-field as v1-v4 did.

---

# Concept 2 ("In-Car, Kind Of Random") — in-car confessional (2026-09-25)

First generation of Concept 2, using the same schema-first single-pass method that worked for
Concept 1 v5 — role-tagged identity ref + product ref, `submit_workflow` + `OpenAIGPTImageNodeV2`,
compiled `final_generation_instruction` + `negative_prompt`, `dry_run: true` validated first,
`n: 2`. image_1 = `character-sheet/rm-char-01_three-quarter.png` (identity only, told to ignore its
kitchen background/pose since this is a different scene), image_2 =
`refs/rockamoss_strawberry_jar_bench.jpg` (label only, same embossing/bench-background exclusion as
every other product-ref use in this project).

## v1 — real result, two real deviations flagged

**`concept2_v1_schema_seedA.png` / `concept2_v1_schema_seedB.png`** — strong on identity (arguably
tighter match to RM-Char-01 than Concept 1 v5's seed B), label accuracy (logo, "Wildcrafted"
script, flavor tag, mineral claim, net weight, no hallucinated text, no embossed glass), no visible
phone anywhere in frame, natural daylight, genuine mid-sentence "talking to a friend" energy — not
posed, not looking composed for camera. No real signage, no CGI tell.

**Two real deviations from the written concept, not self-certified as fine:**
1. **Product presentation.** The concept's beat says "holds up the jar, maybe takes a spoonful
   mid-sentence — not a clean product-reveal shot," but both seeds show her holding the jar
   directly toward camera, label fully faced-out — closer to a product-reveal shot than the loose,
   incidental handling the concept called for.
2. **Framing tighter than scripted.** The prompt's `camera_device` field said "propped on the
   dashboard," matching Concept 1's further-back propped-phone logic — but both outputs read as a
   close held-out selfie distance, not a dashboard-propped wide shot. The model didn't honor that
   part of the instruction as literally as Concept 1's kitchen-counter version did.

**Sent to Ben for judgment, deviations flagged directly** rather than presented as a clean win —
same discipline as flagging Concept 1 v5's seed-variance issue. If either deviation needs fixing,
the likely lever (per this project's own standing lesson) is a more concrete physical instruction
for what "held loosely" looks like — e.g. "resting in her lap, not raised toward the lens" — rather
than a bare negation of "not presented," which this project has repeatedly found doesn't reliably
steer composition on its own.

## Next step

Waiting on Ben's read of Concept 2 v1. Once both concepts have a confirmed still, the launch-batch
plan (`ai-ugc-playbook.md`) calls for 2 video ads live in round 1 — these two concepts are meant to
be exactly that pair, animated via Seedance/Genjutsu once their stills are locked.

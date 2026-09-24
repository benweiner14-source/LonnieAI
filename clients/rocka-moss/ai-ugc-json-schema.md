# Rocka Moss AI UGC — JSON Prompting Schema (2026-09-24, v2)

Ben referenced his own structured prompting approach (named, not detailed, in
`docs/frankie-shaw-ai-ugc-method.md`'s Sources as "JSON prompting") and asked whether it was worth
adopting here. Real reason to do it, not just novelty: every iteration round on Concept 1
(`concept-tests/README.md` v1→v4) was hand-translated from `ai-ugc-concepts.md`'s prose into tool
calls from scratch each time — a schema makes that translation mechanical, diffable, and reusable
across shots/concepts instead of re-derived from memory each round.

This is a **documentation schema for planning/handoff, not a literal API payload** — it still gets
translated into an actual `partner_generate`/`submit_workflow` call by hand (the underlying Comfy
Cloud tools have their own required shapes, e.g. `OpenAIGPTImageNodeV2`'s `model.images.image_1..n`
for the two-image label-fix technique). The value is having one canonical, versionable spec per
concept/shot that encodes everything this project has already learned the hard way, so the next
iteration edits a field instead of re-writing prose.

## v2 update — real worked example found and folded in (2026-09-24)

Ben linked a tweet (`x.com/noneugc/status/2102447818786930793`, pulled via Apify's
`apidojo/tweet-scraper` — same session-only token pattern already used for Instagram/Ad-Library
research elsewhere in this project, since plain `WebFetch` can't reach X per this project's own
standing finding). It's a real, much more granular JSON-prompting example for GPT Image 2.5 — a
"reference reconstruction with product replacement" prompt (swap one product into an otherwise
identical reference photo). **Not saved verbatim into this repo** — it's someone else's specific
creative example (a different brand's whitening-strips ad), same reproduction-caution discipline
already applied to the Frankie Shaw/Tay YouTube material and the ad-reverse-engineering caution in
`docs/tay-ai-ugc-dropship-method.md`. Folded the *structure* into our own schema below instead.

**Four real upgrades this example had that v1 of this schema didn't**, now added:

1. **`negative_prompt`** — an explicit array of things to actively exclude (wrong product,
   anatomy errors, CGI/3D-render/illustration, heavy beauty filter, studio photography, visible
   UI/status-bar/screenshot chrome). v1 only had a `brand_safety` list, which covers logos/place
   names/claims but not quality/anatomy/style negatives — a real gap, since this project has hit
   exactly these failure modes before (warped hands on the SDXL/LoRA pipeline test, "digital
   render" look on Concept 1 v1/v2) without ever writing them down as a reusable checklist.
2. **`reference_fidelity.preserve_exactly` / `change_only`** — an explicit diff structure. This
   maps almost exactly onto our own two-pass label-fix technique (Concept 1 v3→v4: keep the scene
   identical, change only the label) — now a structured field instead of ad hoc prose each time.
3. **A richer `canvas` object** (orientation, aspect_ratio, crop, subject_alignment,
   camera_position, camera_height) replacing v1's flat `framing` string — more precise handoff to
   whoever (or whichever future session) executes the shot.
4. **`final_generation_instruction`** — a flattened prose paragraph at the very end that restates
   the structured fields as one coherent instruction. Real lesson: even a fully "JSON-prompted"
   example still ends in a compiled natural-language paragraph — the JSON is organized notes, not
   a literal replacement for the instruction actually sent to the model. Kept as a required
   closing field below, not dropped in favor of pure structure.

## Schema

```json
{
  "concept_id": "string — matches the heading in ai-ugc-concepts.md, e.g. concept1-morning-ritual",
  "prompt_type": "candid_ugc_still | reference_reconstruction_with_product_replacement | character_sheet_edit",
  "character": {
    "ref_id": "RM-Char-01",
    "locked_images": {
      "face": "clients/rocka-moss/character-sheet/rm-char-01_seed-b.png",
      "full_body": "clients/rocka-moss/character-sheet/rm-char-01_full-body-mirror.png",
      "three_quarter": "clients/rocka-moss/character-sheet/rm-char-01_three-quarter.png"
    },
    "identity_notes": "natural coily hair, natural unsmoothed skin texture (no airbrushing/glow), minimal-to-no makeup — do not deviate from the locked reference's face/hair/skin tone"
  },
  "product": {
    "flavor": "Strawberry Shortcake | Mango Magic | Pineapple Breeze | Apple Pie",
    "ref_image": "clients/rocka-moss/refs/rockamoss_strawberry_jar_bench.jpg",
    "label_fix_notes": "completely smooth, plain glass body — this jar's glass is unmarked, unlike the reference photo's glass which happens to have embossed wording on it; do not copy that embossed wording. Reproduce the label (logo, wordmark, teal tagline bar, flavor tag, mineral claim, net weight, gold lid) accurately from the reference.",
    "requires_two_image_label_pass": "true if the scene is a single-image character edit that can't also hold a second product reference — see engine.generation_path"
  },
  "scene": {
    "format": "mirror-selfie | propped-phone-counter | in-car-confessional | candid-friend-taken",
    "camera_device": "how the phone is physically implied — e.g. 'propped standing against a container on the kitchen counter, used as a makeshift stand/tripod' — must be a concrete physical device, never a bare 'not third-person' negation (negations don't reliably steer composition, proven on the iPhone Selfie POV fixes)",
    "setting_description": "visual description only — NEVER a literal place name (Columbia/Charlotte/etc.) in prompt text; place names render as literal on-screen signage, proven repeatedly on Zion/Kazumi/Selena and again on Kazumi's penthouse-party vignette ('MIAMI' leak)",
    "canvas": {
      "orientation": "portrait",
      "aspect_ratio": "9:16",
      "crop": "e.g. 'from slightly above the head to the lower torso' — precise, not just 'close' or 'wide'",
      "subject_alignment": "e.g. 'slightly off-center' — off-center by default, per the standing camera-variety lesson from the CGI-avatar packs",
      "camera_position_and_height": "e.g. 'held at arm's length, approximately eye level' or 'propped at counter height, slightly below eye level'"
    }
  },
  "reference_fidelity": {
    "preserve_exactly": ["array — everything that must NOT change from the base/chained reference image: pose, expression, hair, outfit, room, lighting, crop, etc."],
    "change_only": ["array — the one or two things this specific pass is allowed to change, e.g. 'the product in her hand'"]
  },
  "realism_constraints": [
    "believable practical light only (window/room light), no studio/ring-light polish",
    "real skin texture and minor imperfections, not airbrushed",
    "ordinary/slightly-worn real-world surfaces, not styled/staged",
    "explicit anti-'digital render'/anti-AI-generated-look wording",
    "mid-motion or not-looking-at-camera body language, not a held pose — a posed portrait is the most common failure mode without this"
  ],
  "negative_prompt": [
    "wrong/generic product",
    "extra fingers, fused fingers, warped hand",
    "CGI, 3D render, illustration, anime (unless the concept explicitly wants the CGI-avatar look, in which case invert this)",
    "heavy beauty filter, studio photography, plastic skin",
    "visible phone, phone screen, second phone in frame",
    "watermark, visible UI, status bar, screenshot chrome",
    "real place-name signage, real third-party logos"
  ],
  "beats": [
    {"beat": "relatable_scenario", "action": "string, no product visible yet"},
    {"beat": "character_building", "action": "string, normal routine, mid-thought realism markers"},
    {"beat": "progress_not_before_after", "line": "personal-experience-framed dialogue, no medical claim"},
    {"beat": "introduce_product", "action": "string, product handled loosely, not presented to camera"},
    {"beat": "soft_close", "line": "no hard CTA / trails off naturally"}
  ],
  "brand_safety": [
    "no real place-name signage (see scene.setting_description)",
    "no real logos/brand names other than Rocka Moss's own product label",
    "no fabricated 'a customer said' lines — no real reviews exist yet, per seo-audit.md",
    "no medical/outcome claims — personal-experience framing only, per the standing no-medical-claims rule"
  ],
  "engine": {
    "model": "gpt-image-2.5-sunburst",
    "generation_path": "single-image edit via partner_generate (medias role=image, base=locked character image) — use ONLY when no second product-label reference is needed in the same call; OR two-image submit_workflow via OpenAIGPTImageNodeV2 (image_1=scene base, image_2=product ref) when both an already-working scene AND an accurate label are needed in one pass — see concept-tests/README.md v4 for why this second path exists",
    "seed_variants": "generate 2-3, pick on identity/realism/label-accuracy, not first-result"
  },
  "final_generation_instruction": "one compiled prose paragraph restating the fields above as the actual instruction text sent alongside the reference image(s) — the JSON is planning structure, this is what the model actually reads",
  "status": "draft | rendered | ben-reviewed | locked"
}
```

## Field notes tied to real findings in this project

- `character.identity_notes` exists because edits must chain off the **locked seed-B image itself**
  (or its own extension images), never regenerate from text — same lesson as Kazumi's
  penthouse-party vignette chaining technique, applied here to a still image instead of
  multi-shot video.
- `scene.camera_device` is the single most load-bearing field. The whole v1→v3 iteration on
  Concept 1 was this field going from *absent* → *meta negation ("not third-person")* → *a real,
  named physical device (propped-phone-on-counter)* before it worked. Any new concept/shot should
  fill this field first, concretely, before writing anything else.
- `reference_fidelity` (new in v2) formalizes what Concept 1's v3→v4 pass already did ad hoc:
  keep everything about a working scene fixed, touch only the one broken thing (the label). Fill
  this in explicitly on any edit-of-an-existing-render pass, not just the label-fix case — it's
  the general pattern for "the scene works, fix one detail without disturbing it."
- `negative_prompt` (new in v2) is deliberately separate from `brand_safety` — brand safety covers
  real-world leakage (logos, place names, claims), negative_prompt covers rendering-quality/anatomy
  failures this project has hit before but never written down as a standing checklist (warped
  hands on the SDXL/LoRA pipeline test; "digital render" look on Concept 1 v1/v2; the visible
  phone/second-phone bugs from the iPhone Selfie style's v1-v3 fixes).
- `product.requires_two_image_label_pass` exists because `partner_generate`'s simplified interface
  only accepts one `image` role for GPT Image 2.5 edits — a second product-reference image needs
  the hand-built `submit_workflow` + `OpenAIGPTImageNodeV2` route (confirmed via `get_node`), not
  `partner_generate`.
- `realism_constraints` is the still-photo-appropriate subset of
  `docs/frankie-shaw-ai-ugc-method.md`'s V4 Realism Laws — kept as a flat checklist here so it's
  easy to confirm nothing got dropped between iterations (v2's uncanny-valley regression happened
  partly from not having this as an explicit checked list).
- `final_generation_instruction` (new in v2) is the field that actually gets sent to the model —
  every other field exists to make writing this one paragraph disciplined and complete, not to
  replace it. Don't skip straight from the structured fields to a tool call without writing this
  out first; that's exactly the "re-derived prose each round" problem this schema exists to fix.

## Concept 1 — "Morning Ritual" as JSON

```json
{
  "concept_id": "concept1-morning-ritual",
  "prompt_type": "candid_ugc_still",
  "character": {
    "ref_id": "RM-Char-01",
    "locked_images": {
      "face": "clients/rocka-moss/character-sheet/rm-char-01_seed-b.png",
      "full_body": "clients/rocka-moss/character-sheet/rm-char-01_full-body-mirror.png",
      "three_quarter": "clients/rocka-moss/character-sheet/rm-char-01_three-quarter.png"
    },
    "identity_notes": "natural coily hair, natural unsmoothed skin texture, minimal-to-no makeup — match the locked seed-B face exactly"
  },
  "product": {
    "flavor": "Strawberry Shortcake",
    "ref_image": "clients/rocka-moss/refs/rockamoss_strawberry_jar_bench.jpg",
    "label_fix_notes": "completely smooth, plain glass body — do not copy the reference photo's embossed 'MASON' wording. Reproduce the label accurately.",
    "requires_two_image_label_pass": true
  },
  "scene": {
    "format": "propped-phone-counter",
    "camera_device": "phone propped standing against a container on the kitchen counter, used as a makeshift stand/tripod — phone itself never visible in frame, it IS the camera taking this shot",
    "setting_description": "a modest, lived-in apartment kitchen, morning window light only, real everyday clutter (dishes in the sink, a coffee maker, a knife block) — no studio staging",
    "canvas": {
      "orientation": "portrait",
      "aspect_ratio": "9:16",
      "crop": "wide enough to show most of the kitchen counter and her upper body — wider than a held-selfie crop",
      "subject_alignment": "off-center, reaching toward the jar rather than centered facing camera",
      "camera_position_and_height": "propped at counter height, slightly below eye level, further back than an arm's-length selfie"
    }
  },
  "reference_fidelity": {
    "preserve_exactly": ["the kitchen scene, pose, camera angle, and off-center framing confirmed in v3 (concept-tests/concept1_product-intro_v3_propped-phone.png)"],
    "change_only": ["the jar's label — replace the illegible/hallucinated v3 label with the accurate one from rockamoss_strawberry_jar_bench.jpg"]
  },
  "realism_constraints": [
    "believable practical morning window light only, no studio/ring-light polish",
    "real skin texture, not airbrushed",
    "ordinary lived-in kitchen surfaces, not styled",
    "explicit anti-digital-render / anti-AI-look wording",
    "mid-motion, not looking at camera, no posed smile"
  ],
  "negative_prompt": [
    "posed professional portrait",
    "visible phone or phone screen in frame",
    "illegible or hallucinated product label text",
    "embossed jar glass",
    "studio lighting",
    "real place-name signage"
  ],
  "beats": [
    {"beat": "relatable_scenario", "action": "rushed weekday morning, coffee already going, hair not done yet, no product visible"},
    {"beat": "character_building", "action": "normal get-ready routine, talking to the propped phone with casual mid-thought pauses"},
    {"beat": "progress_not_before_after", "line": "I've been doing this every morning for like three weeks now and I'm not gonna lie, my energy's been steadier — not like a jolt, just... steadier."},
    {"beat": "introduce_product", "action": "reaches off-frame, comes back with the Strawberry Shortcake jar, spoons it into a glass, held loosely not presented"},
    {"beat": "soft_close", "line": "I'll leave it linked if you want to look into it."}
  ],
  "brand_safety": [
    "no real place-name signage",
    "no real logos/brand names other than Rocka Moss's own product label",
    "no fabricated customer-review lines",
    "no medical/outcome claims — personal-experience framing only"
  ],
  "engine": {
    "model": "gpt-image-2.5-sunburst",
    "generation_path": "two-pass: (1) partner_generate single-image edit off rm-char-01_full-body-mirror.png or _three-quarter.png for the propped-phone kitchen scene, (2) submit_workflow OpenAIGPTImageNodeV2 two-image pass (image_1=pass-1 output, image_2=rockamoss_strawberry_jar_bench.jpg) to fix the label",
    "seed_variants": "2-3"
  },
  "final_generation_instruction": "Recreate the confirmed v3 kitchen scene exactly — same off-center framing, same mid-motion reach toward the jar, same morning window light, same lived-in counter clutter, same face/hair/skin matching RM-Char-01's locked reference. Change only the jar's label: replace the illegible text with an accurate reproduction of the Rocka Moss Strawberry Shortcake label from the second reference image (logo, wordmark, teal tagline bar, flavor tag, mineral claim, net weight, gold lid), on a completely smooth unmarked glass jar — do not copy the second reference photo's own embossed glass wording or background. No visible phone anywhere in frame. No real place-name signage.",
  "status": "v5 rendered — regenerated in ONE pass straight from this schema (see concept-tests/README.md v5), sent to Ben for judgment; supersedes the v1-v4 iterative discovery process as the reference technique"
}
```

**v5 result (2026-09-24):** generating directly from this schema — two role-tagged reference
images + the compiled `final_generation_instruction`/`negative_prompt` text, in a single
`submit_workflow` call — landed scene + accurate label + no-visible-phone all correct on the first
attempt (`concept-tests/concept1_v5_schema_seedA.png` / `_seedB.png`). Confirms the schema's actual
value: writing the full spec before generating beats discovering the same fixes one iteration at a
time. Use this "schema first, generate once" order for Concept 2 and future shots.

## Concept 2 — "In-Car, Kind Of Random" as JSON

```json
{
  "concept_id": "concept2-in-car-confessional",
  "prompt_type": "candid_ugc_still",
  "character": {
    "ref_id": "RM-Char-01",
    "locked_images": {
      "face": "clients/rocka-moss/character-sheet/rm-char-01_seed-b.png",
      "full_body": "clients/rocka-moss/character-sheet/rm-char-01_full-body-mirror.png",
      "three_quarter": "clients/rocka-moss/character-sheet/rm-char-01_three-quarter.png"
    },
    "identity_notes": "natural coily hair, natural unsmoothed skin texture, minimal-to-no makeup — match the locked seed-B face exactly"
  },
  "product": {
    "flavor": "Strawberry Shortcake",
    "ref_image": "clients/rocka-moss/refs/rockamoss_strawberry_jar_bench.jpg",
    "label_fix_notes": "completely smooth, plain glass body — do not copy the reference photo's embossed 'MASON' wording. Reproduce the label accurately.",
    "requires_two_image_label_pass": true
  },
  "scene": {
    "format": "in-car-confessional",
    "camera_device": "phone propped on the dashboard or held loosely at arm's length — not a third-person shot of her; if held, arm/hand fills part of the foreground per the iPhone-selfie proximity-blur technique to keep the phone itself out of frame",
    "setting_description": "parked car, engine off, natural daylight through the windshield/window — no visible street signage or place names through the windows",
    "canvas": {
      "orientation": "portrait",
      "aspect_ratio": "9:16",
      "crop": "casual dashboard-propped or handheld framing, not a centered composed portrait",
      "subject_alignment": "slightly off-angle, consistent with a propped or handheld phone rather than a tripod",
      "camera_position_and_height": "dashboard height if propped, or arm's length if held — either way, roughly eye level from the driver's seat"
    }
  },
  "reference_fidelity": {
    "preserve_exactly": ["RM-Char-01's face/hair/skin from the locked reference"],
    "change_only": ["setting (car interior instead of kitchen), outfit/context appropriate to being out for an errand"]
  },
  "realism_constraints": [
    "believable practical daylight only, no studio polish",
    "real skin texture, not airbrushed",
    "ordinary car interior, not staged/detailed",
    "explicit anti-digital-render / anti-AI-look wording",
    "unscripted 'telling a friend something' body language and pacing, not an ad-read pose"
  ],
  "negative_prompt": [
    "posed professional portrait",
    "visible phone or phone screen in frame",
    "illegible or hallucinated product label text",
    "embossed jar glass",
    "studio lighting",
    "real street signage or place names visible through windows"
  ],
  "beats": [
    {"beat": "relatable_scenario", "action": "sitting in a parked car about to head into work/an errand, phone propped on the dash or held loosely"},
    {"beat": "character_building", "line": "So this is kind of random but...", "action": "mundane, low-stakes opener, not an ad-read cadence"},
    {"beat": "progress_not_before_after", "line": "I used to have like five different things I was taking every morning and I'd always forget half of them. Now I just do this one thing."},
    {"beat": "introduce_product", "action": "holds up the Strawberry Shortcake jar, maybe takes a spoonful mid-sentence — not a clean product-reveal shot"},
    {"beat": "soft_close", "line": "Anyway... it's been good.", "note": "deliberately softer than Concept 1's close, no CTA at all"}
  ],
  "brand_safety": [
    "no real place-name signage (through the car windows or otherwise)",
    "no real logos/brand names other than Rocka Moss's own product label",
    "no fabricated customer-review lines",
    "no medical/outcome claims — a consolidation/simplicity point, not a health-outcome claim"
  ],
  "engine": {
    "model": "gpt-image-2.5-sunburst",
    "generation_path": "same two-pass technique as Concept 1 once validated: single-image edit for scene/pose/realism, then submit_workflow two-image pass to lock the label",
    "seed_variants": "2-3"
  },
  "final_generation_instruction": "A real, candid iPhone photo of RM-Char-01 sitting in a parked car, engine off, natural daylight through the window, phone propped on the dashboard or held at arm's length with her arm/hand naturally blocking the phone itself from view. Casual, unscripted body language — not posed, not looking directly composed for camera. Match her face/hair/skin exactly to the locked reference. Ordinary car interior, no staging. Once the scene is confirmed, a second pass replaces only the product label with an accurate reproduction from the Rocka Moss Strawberry Shortcake reference image, on a smooth unmarked jar. No visible phone. No real street signage or place names.",
  "status": "draft — not yet generated, waiting on Concept 1's v4 to be confirmed first"
}
```

## Next step

Nothing generates differently because this schema exists — it's a planning/handoff layer, not a
new technique. Use it going forward: when Ben's feedback changes a field (a camera device, a
realism constraint, a beat), edit the JSON here first, then translate that diff into the actual
tool call — cheaper to review and version than re-deriving prose each round, as happened across
`concept-tests/README.md`'s v1-v4. The `reference_fidelity` and `negative_prompt` fields added in
v2 are worth applying retroactively the next time either concept iterates, even though v1's fields
already covered the substance informally.

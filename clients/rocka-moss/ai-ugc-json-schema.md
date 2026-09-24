# Rocka Moss AI UGC — JSON Prompting Schema (2026-09-24)

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

## Schema

```json
{
  "concept_id": "string — matches the heading in ai-ugc-concepts.md, e.g. concept1-morning-ritual",
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
    "framing": "wide/off-center vs. close — a propped phone sits further back than a held one; note explicitly to avoid defaulting to a tight posed portrait crop"
  },
  "realism_constraints": [
    "believable practical light only (window/room light), no studio/ring-light polish",
    "real skin texture and minor imperfections, not airbrushed",
    "ordinary/slightly-worn real-world surfaces, not styled/staged",
    "explicit anti-'digital render'/anti-AI-generated-look wording",
    "mid-motion or not-looking-at-camera body language, not a held pose — a posed portrait is the most common failure mode without this"
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
- `product.requires_two_image_label_pass` exists because `partner_generate`'s simplified interface
  only accepts one `image` role for GPT Image 2.5 edits — a second product-reference image needs
  the hand-built `submit_workflow` + `OpenAIGPTImageNodeV2` route (confirmed via `get_node`), not
  `partner_generate`.
- `realism_constraints` is the still-photo-appropriate subset of
  `docs/frankie-shaw-ai-ugc-method.md`'s V4 Realism Laws — kept as a flat checklist here so it's
  easy to confirm nothing got dropped between iterations (v2's uncanny-valley regression happened
  partly from not having this as an explicit checked list).

## Concept 1 — "Morning Ritual" as JSON

```json
{
  "concept_id": "concept1-morning-ritual",
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
    "framing": "wide/off-center, further back than a held selfie (a propped phone sits at a distance) — she is caught mid-motion reaching toward the jar, not already holding it up posed"
  },
  "realism_constraints": [
    "believable practical morning window light only, no studio/ring-light polish",
    "real skin texture, not airbrushed",
    "ordinary lived-in kitchen surfaces, not styled",
    "explicit anti-digital-render / anti-AI-look wording",
    "mid-motion, not looking at camera, no posed smile"
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
  "status": "rendered — v4 sent to Ben for final judgment, not yet locked"
}
```

## Concept 2 — "In-Car, Kind Of Random" as JSON

```json
{
  "concept_id": "concept2-in-car-confessional",
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
    "framing": "casual, slightly off-angle dashboard-propped or handheld framing — not a centered composed portrait"
  },
  "realism_constraints": [
    "believable practical daylight only, no studio polish",
    "real skin texture, not airbrushed",
    "ordinary car interior, not staged/detailed",
    "explicit anti-digital-render / anti-AI-look wording",
    "unscripted 'telling a friend something' body language and pacing, not an ad-read pose"
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
  "status": "draft — not yet generated, waiting on Concept 1's v4 to be confirmed first"
}
```

## Next step

Nothing generates differently because this schema exists — it's a planning/handoff layer, not a
new technique. Use it going forward: when Ben's feedback changes a field (a camera device, a
realism constraint, a beat), edit the JSON here first, then translate that diff into the actual
tool call — cheaper to review and version than re-deriving prose each round, as happened across
`concept-tests/README.md`'s v1-v4.

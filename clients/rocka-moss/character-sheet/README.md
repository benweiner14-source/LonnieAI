# RM-Char-01 — AI UGC Character Reference Set (2026-09-24)

3 seed variants generated for the synthetic AI UGC character described in `ai-ugc-concepts.md`
and grounded in `target-demo.md`. **✅ Locked: seed B, Ben's pick (2026-09-24).**

## Extended reference set — face + body + angle

Ben asked whether this would include a character turnaround (different angles, body proportions)
— a single close-up selfie doesn't establish body type at all, and Concept 1 ("Morning Ritual")
specifically needs a full-body mirror selfie. Rather than a formal 3D-style orthographic
turnaround (front/side/back T-pose), used this repo's own proven pattern instead: purpose-tagged
reference images (face, body, angle), same multi-image role-tagging technique used throughout this
project. Generated 2 more images as GPT Image 2.5 **edits** of the locked seed B image (`medias`
role `"image"`, seed B's own output as the base) — this keeps the exact same face/hair/skin tone
rather than regenerating from scratch:

- `rm-char-01_full-body-mirror.png` — full-body mirror selfie, bedroom setting. **Doubles as the
  actual base shot for Concept 1** ("Morning Ritual"), not just a body reference — same character,
  phone correctly shows its back (not the screen) in the reflection per the established
  mirror-selfie recipe.
- `rm-char-01_three-quarter.png` — three-quarter angle, medium-full shot (knees up), kitchen
  setting, different pose/angle for general body-proportion consistency.

Both checked directly for identity consistency against seed B (same face, hair, skin tone) and for
brand-safety leaks (none found — no visible text, logos, or brand names in either background).

## Recipe

- **Engine:** GPT Image 2.5 Sunburst via Comfy Cloud `partner_generate` (`openai/images-generations`,
  `model: gpt-image-2.5-sunburst`), 9:16, text-to-image (no reference photo — fully synthetic).
- **Same approach as `clients/ai-ugc-agency/session-reference.md`'s character-reference step**
  (a single selfie-style portrait, regenerated 2-3 times to lock a face), not the 3-view front/
  three-quarter/profile pattern used for Kazumi's photoreal pilot — this character is meant to be
  reused as a single locked identity reference for downstream Seedance i2v shots, same as that
  doc's `@Image1` pattern.
- **Prompt (identical across all 3 seeds, only the seed number changed):** genre-led "a real,
  candid iPhone selfie-style photo of a Black woman in her mid-20s," natural coily hair worn down,
  natural skin texture (explicitly not airbrushed/glowing/smoothed), minimal-to-no makeup, casual
  oversized t-shirt, modest lived-in apartment kitchen, warm morning window light only (no studio/
  ring light), selfie framing with slight handheld imperfection, explicit "no text, no logos, no
  signage, no visible brand names" clause.

## Candidates

- `rm-char-01_seed-a.png` — brown t-shirt, kitchen with dark cabinets, warm sunlit background.
- `rm-char-01_seed-b.png` — olive/sage t-shirt, brighter white-cabinet kitchen.
- `rm-char-01_seed-c.png` — brown t-shirt (close to seed A's tone), white-cabinet kitchen, black
  fridge.

All three landed clean on the brand-safety check — no visible logos, brand names, or readable text
anywhere in frame (checked directly, not just prompted-for). All three read as genuinely candid/
photoreal, not posed or produced — consistent with Frankie Shaw's "if it looks planned, it failed"
realism law already documented in `docs/frankie-shaw-ai-ugc-method.md`.

## Next step

`rm-char-01_seed-b.png` is the locked identity reference. Combined with the two extension images
above, that's face + full-body + three-quarter angle — enough to generate Concept 1 and Concept 2
consistently. Next: validate Concept 1 as a still (it's effectively already shot — the full-body
mirror image above just needs the Rocka Moss product added via the same multi-image role-tagging
technique), then animate via Seedance/Genjutsu.

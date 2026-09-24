# RM-Char-01 — AI UGC Character Reference Candidates (2026-09-24)

3 seed variants generated for the synthetic AI UGC character described in `ai-ugc-concepts.md`
and grounded in `target-demo.md`. **Not yet locked — waiting on Ben's pick.**

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

**Ben picks one** (or asks for another round with different specifics — hair style, outfit, exact
setting) to lock as the actual `RM-Char-01` reference. Once locked, that one image becomes the
identity reference for both concepts in `ai-ugc-concepts.md` going forward — same image reused
across every future generation for this character, not regenerated per scene.

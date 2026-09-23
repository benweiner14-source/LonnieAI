# Rocka Moss — test renders

AI-generated test outputs for this client, kept separate from `refs/` (real, unedited brand
photography) so the two are never confused. Nothing here is a final creative asset — these are
validation tests per `ai-ugc-playbook.md`'s standing "validate before batching" discipline.

## `strawberry_studio_v1.png` — 2026-09-23

First product-photography validation test for this client. **Result: strong pass, one minor
flaw.**

- **Recipe:** GPT Image 2.5 Sunburst (`openai/images-generations`, `params.model:
  "gpt-image-2.5-sunburst"`) via Comfy Cloud `partner_generate`, single reference image
  (`refs/rockamoss_strawberry_jar_bench.jpg`, role `image`), no CGI/stylization language in the
  prompt — per `ai-ugc-playbook.md`'s product-photography recipe (photoreal engine, fight toward
  nothing, just don't add game-engine/style-reference language).
- **Prompt approach:** role-tagged the reference image as the single source of truth for
  bottle/cap/label — explicit "do not alter the label text, logo, color bands, or artwork"
  instruction — then described a clean Studio-style scene (seamless white-to-gray gradient
  background, soft diffused lighting, straight-on angle) entirely in text, with an explicit
  "no other bottles/props/logos" clause per the playbook's brand-safety-in-reverse guidance.
- **What worked:** front label reproduced with strong fidelity — logo, "SEA MOSS Wildcrafted"
  wordmark, "FUEL YOUR GLOW FROM THE SEA BELOW" teal bar, "STRAWBERRY" pink flavor tag, "RICH IN
  92+ ESSENTIAL MINERALS," net weight, gold twist lid, mason-jar shape, pink/red gel product
  color — all match the reference. Clean, plain studio background with a soft shadow/reflection,
  no unwanted props or extra logos, reads as a real photograph (not a render or illustration).
- **Flaw found:** the side-panel text (ingredients/caution copy, smaller and denser than the
  front label) rendered as garbled, illegible scribbles — a known limitation of GPT-Image-family
  models on small/dense text, not something this prompt caused. Doesn't affect the front label,
  which is what a Studio product shot foregrounds anyway, but worth knowing: any future crop or
  angle that puts the side panel in sharp, legible focus will likely need either a second
  reference image specifically of that panel, or cropping the final output to hide it.
- **Not yet tested:** the other 4 styles (Floating, Ingredient, In Use, Lifestyle), the other 3
  flavors, or the testimonial/POV-selfie recipe. This single test validates the *recipe*
  (GPT-2.5 Sunburst + single clean reference + no style language) — worth running 1-2 more before
  calling the whole product-photography direction locked, same standing discipline as every other
  pack in this repo.

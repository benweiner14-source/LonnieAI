# Rocka Moss — test renders

AI-generated test outputs for this client, kept separate from `refs/` (real, unedited brand
photography) so the two are never confused. Nothing here is a final creative asset — these are
validation tests per `ai-ugc-playbook.md`'s standing "validate before batching" discipline.

## Strawberry Shortcake, Studio style — 2026-09-23, 3 iterations, now confirmed clean

First product-photography validation test for this client, run via Comfy Cloud's
`partner_generate` (GPT Image 2.5 Sunburst, `openai/images-generations`), single reference image
(`refs/rockamoss_strawberry_jar_bench.jpg`, role `image`), no CGI/stylization language — per
`ai-ugc-playbook.md`'s product-photography recipe.

- **`strawberry_studio_v1.png`** — first pass. **Strong result overall**: front label reproduced
  with real fidelity (logo, wordmark, teal tagline bar, flavor tag, mineral claim, net weight,
  gold lid, mason-jar shape, gel color all match), clean plain studio background, no unwanted
  props/logos, reads as a real photograph. **Flaw found (Ben caught it):** the glass itself came
  out with "MASON" embossed into it, faithfully copied from the reference photo — a generic
  canning-jar detail Ben confirmed shouldn't appear in generated product photography (the real
  jars still have it, but it's not something to carry into marketing images). Also, separately,
  the side-panel ingredients/caution text rendered as illegible scribbles — a known GPT-Image
  limitation on small/dense text.
- **`strawberry_studio_v2_noemboss_partial.png`** — first fix attempt, a bare negation ("the
  glass itself is plain — no embossed text, lettering, or brand marks on the jar body"). **Only
  partially worked** — the embossing was fainter but still legible on close zoom. Confirms this
  repo's standing lesson (from the iPhone Selfie POV fixes) that negation instructions reliably
  lose to a strong visual signal already present in a reference image's actual pixels.
- **`strawberry_studio_v2_smoothglass.png`** — second fix attempt, reworded to lead with a
  positive physical description and explicitly flag the reference photo's embossing as something
  NOT to carry over (see the exact wording in `ai-ugc-playbook.md`'s product-photography
  section). **Confirmed clean** — completely smooth glass neck, no embossing at any zoom level,
  front label still accurate. **This is the version/recipe to reuse going forward.**

**Recipe now locked for this specific issue** (folded into `ai-ugc-playbook.md`): every future
product-photography prompt using a real jar reference photo needs the "smooth glass, explicitly
told to ignore the reference's embossing" wording, not the simpler negation version.

**Not yet tested:** the other 4 styles (Floating, Ingredient, In Use, Lifestyle), the other 3
flavors, the side-panel-text legibility issue, or the testimonial/POV-selfie recipe. This single
scene validates the *recipe* (GPT-2.5 Sunburst + single clean reference + no style language +
smooth-glass wording) — worth running 1-2 more before calling the whole product-photography
direction locked, same standing discipline as every other pack in this repo.

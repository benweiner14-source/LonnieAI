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

## Next step

Continue with GPT Image 2.5 Sunburst as Concept 1's still. The label-text gap is a known,
lower-priority flaw (matches this project's very first product-shot test) — worth a second
attempt with a closer, more legible product angle if the label ever needs to be readable in a
given shot, not urgent for this wide mirror-selfie framing.

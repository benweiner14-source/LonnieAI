# Multi-image role-tagging (Nano Banana Pro / GPT Image 2 multi-ref prompting)

Both Nano Banana Pro (up to 14 images) and the GPT Image 2 partner node (2 images) have **no
explicit "role" field** for attached images — the model infers what each image is *for* purely
from how the text prompt describes it. So the text must explicitly assign a job to each image,
in the same order the images are actually attached.

## The pattern
```
REFERENCE IMAGE 1: use ONLY for [X]. Ignore everything else in this image (pose/background/etc).
REFERENCE IMAGE 2: use ONLY for [Y]. Ignore everything else in this image.
REFERENCE IMAGE 3: use ONLY for [Z]. Ignore everything else in this image.
...
[rest of the normal scene prompt]
```

**⚠️ Critical: image order must match slot order.** "Reference image 1" in the text must be the
actual first image you attach (first upload / first `image_1`-type slot), and so on. If the order
doesn't match, the model will apply the wrong instruction to the wrong picture.

**⚠️ Style references may contain real logos baked into the pixels.** The 2K screenshots in
`reference-material/2k-screenshots/` (and even the `textures/` crops — some still show jersey
wordmarks) have **real NBA/2K/team branding physically in the image**, regardless of what the
text says. Always add an explicit instruction to the style reference's role: *"ignore and do not
reproduce any logos, team names, league marks, jersey text, or watermarks visible in this
reference — use it for rendering technique only."* Text genericization alone (no "NBA 2K" in the
prompt) doesn't stop the model from copying a logo it can literally see in a reference photo.

---

## Worked example — Zion, 4-image role-tagged gym scene

**Attach in this exact order:**
1. `creators/zion-clark/refs/zion_gym_parallette.jpg` (clean frontal face)
2. `creators/zion-clark/refs/zion_back_noexcuses_tattoo.jpg` (tattoo)
3. `creators/zion-clark/refs/soul-id/soul_12.jpg` (body/pose)
4. `reference-material/2k-screenshots/2k_02.jpg` (style)

> Full ready-to-paste version (plus a **multi-style variant** using 6 style images at once,
> within the 14-image cap) is in `prompts/zion-clark.md` under "multi-ref role-tagged."

**Prompt:**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific gym in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a muscular Black adaptive athlete born without legs, medium-length dreadlocks in a top-knot, short beard, gold chain with a cross pendant, supporting himself on his hands mid-training on a gym floor, chalked palms, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — the entire frame (character AND environment) rendered in a polished sports-simulation CGI game-engine style, obviously computer-generated, NOT a photograph. No real league, team, studio, or brand logos or trademarks anywhere in the output; no readable brand text. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

## Extending further (up to 14 images on Nano Banana Pro)
Add more slots the same way, e.g.:
- A **second face angle** (another `soul-id/` shot) for stronger identity — role: "additional
  facial reference, same person as Image 1."
- A **jewelry/chain close-up** — role: "use ONLY for the gold chain and cross pendant design."
- A **second style reference** (a different 2K frame or a `textures/` crop) — same "style only,
  ignore any logos/text" instruction.

More images ≠ automatically better — prioritize *distinct, clean* signal per role over stacking
near-duplicates. If results get confused, cut back to the 4 core roles above first.

## Report back
Note which images/roles you used and paste the result — we judge identity, tattoo accuracy, body
authenticity, and style separately, then tune whichever axis is weakest.

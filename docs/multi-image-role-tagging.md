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

**⚠️ "3D CGI, not a photograph" can drift to Disney/Pixar instead of a game render.** Confirmed
in testing: pushing "obviously CGI, computer-generated" without more can pull the output toward
an *animated-film* look (rounded/cute proportions, glossy toon shading) rather than a
sports-game cutscene — because "3D CGI human" training data skews heavily toward animated
movies, not game engines. This is a *different* failure from staying photoreal, and needs its
own counter-instruction in the style role: explicitly rule out Disney/Pixar/DreamWorks/cartoon,
and state realistic (not exaggerated/cute) human proportions + muted broadcast color grading
instead of warm saturated animated-movie color. See the style-role text in
`prompts/zion-clark.md`'s "multi-ref role-tagged" entries for the exact wording.

---

## ✅ LOCKED — this recipe is confirmed (Ben's v2 test, "one of the best so far")

**Attach in this exact order (v4 — added a second face angle + dedicated arm/chest tattoo
reference):**
1. `creators/zion-clark/refs/zion_gym_parallette.jpg` (face, angle 1 — locked, used in every prompt)
2. `creators/zion-clark/refs/zion_face_agt.jpg` (face, angle 2 — same person, different
   angle/lighting; used alongside Image 1 in every prompt, not instead of it)
3. `creators/zion-clark/refs/zion_chest_arm_tattoo.jpg` (arm/chest tattoo — used whenever his
   front/arms are visible; see below)
4. `creators/zion-clark/refs/zion_back_noexcuses_tattoo.jpg` (back tattoo — only when his back is
   visible in the scene, in place of the arm/chest tattoo ref)
5. `creators/zion-clark/refs/soul-id/soul_12.jpg` (body — gym/portrait scenes; swap to
   `zion_track_noexcuses.jpg` for track scenes, `zion_boxing_ring.jpg` for WWE/combat scenes)
6. `reference-material/2k-screenshots/2k_02.jpg` (style — locked, used in every prompt, with the
   anti-Disney/Pixar clause)

**Why the arm/chest tattoo ref was added:** Ben flagged that arm/chest tattoos were "getting
generated willy nilly" — only the back tattoo had a photo reference, so the model had nothing to
anchor his chest/arm ink to and improvised a different design each generation. Fix: sourced a
sharp, well-lit close-up (`zion_chest_arm_tattoo.jpg`, from a promo photo Ben linked) showing his
real "330 Clark" chest/collarbone script tattoo and his left arm/bicep tattoo clearly, and gave it
its own always-included role (like face and style) in every scene where he's shown front-on or
with bare arms. Scenes shot from behind or in silhouette keep using the back-tattoo reference
instead — see `prompts/zion-clark.md` for the per-scene reference lists.

All 16 of Zion's scenes are now built this way in `prompts/zion-clark.md` — that file is the
source of truth; this doc explains *why* the pattern works.

**Prompt** (v3 example — see `prompts/zion-clark.md`'s `[nba2k · gym]` entry for the current
canonical version, kept in sync there; this is illustrative):
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

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

## Alternate/additional refs (sourced from a Google Images sweep, Ben-approved)
Three more candidates were pulled from public press/podcast coverage (filtered to ≥2MP via image
search metadata, downloaded, and reviewed) and approved by Ben for specific roles:
- `zion_face_agt.jpg` — an AGT red-carpet photo, sharp and front-facing. **Added as a second face
  reference alongside `zion_gym_parallette.jpg`** (used together, not as a replacement — Ben
  wants both angles feeding identity).
- `zion_plyobox_bodycomp.jpg` — approved for body composition; a good alternate to `soul_12.jpg`
  if that one isn't reading well in testing.
- `zion_chest_tattoo_closeup_alt.jpg` — approved as a second clean look at the chest tattoo;
  alternate to `zion_chest_arm_tattoo.jpg` if that one isn't reading well in testing.

## Applied to Kazumi (not yet test-confirmed)
Same method, `prompts/kazumi.md`: face=`kazumi_yellow_polo_portrait.jpg`,
body=`kazumi_olive_tank_denim.jpg`, style=real GTA V / Cyberpunk 2077 **gameplay** screenshots
(`skills/gta6-style/reference/gtav_skyline_dusk.jpg`,
`skills/cyberpunk-2077-style/reference/cp2077_neon_street.jpg`) — deliberately NOT the cover-art
images (`gtav_keyart.jpg`, `cp2077_boxart.jpg`), which are dominated by the real trademarked
logo/title itself and are too risky even with an "ignore logos" instruction. Run one scene first
to confirm before batching, same as Zion's process.

## Report back
Note which images/roles you used and paste the result — we judge identity, tattoo accuracy, body
authenticity, and style separately, then tune whichever axis is weakest.

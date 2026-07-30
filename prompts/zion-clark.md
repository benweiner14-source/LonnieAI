# Prompt Pack — Zion Clark

**✅ RECIPE LOCKED (v6 — added an iPhone-selfie camera style).** Every prompt
below uses the proven multi-image role-tagged recipe: **Nano Banana Pro** (Google Gemini partner
node / `gemini-3-pro-image-preview` in Comfy, or "Nano Banana" in Higgsfield), 5–6 reference
images each assigned ONE explicit job in the text, 9:16. This beat every other approach tested
(Higgsfield GPT Image 2 img2img/Soul ID, Comfy's GPT Image 2 partner node, plain SDXL) on identity,
brand safety, and — after the anti-Disney/Pixar fix — style. Full technique:
`docs/multi-image-role-tagging.md`.

**Authentic representation (read first — exact anatomy):** Zion was **born without legs**
(caudal regression syndrome). **His body ends at/just past his belly button** — there is no
hip, pelvis, thigh, or leg structure below that, not even partial/"stump" legs. Depict him
**authentically and heroically** — powerful upper body and core, moving on his **hands** or in
a **racing wheelchair**. **Do NOT generate fabricated legs, stump legs, hips, or a standing
figure.** He is the hero of every frame: elite, dignified, motivational.

**His real look (from `refs/`, woven into every prompt):** a muscular Black adaptive athlete,
**medium-length dreadlocks often in a top-knot**, full short beard, **gold chain with a cross
pendant**, a **"330 Clark" script tattoo across his chest/collarbone** and a tattoo on his
**left arm/bicep**, and a bold **"NO EXCUSES" tattoo across his upper back/shoulders**; often in
his own **"Z" lightning "No Excuses"** branded gear (purple/gold/black), or shirtless training.

**One look: FULL CGI RENDER.** Every prompt renders the **entire frame — character AND
environment — in the game engine** (an in-game cutscene).

**⚠️ Brand safety — no real logos/trademarks.** Every prompt describes the *aesthetic only*
(polished sports-simulation CGI render) — never a real league, studio, or game title — and
explicitly tells the style reference image(s) to ignore any logos/text visible in the photo
itself (screenshots have real logos baked into their pixels regardless of what the text says).

**⚠️ Style must read as sports-broadcast CGI, not an animated film.** "3D CGI, not a photo"
alone can drift toward Disney/Pixar (rounded proportions, toon shading) because that's the
dominant "CGI human" association in most training data. Every style-role instruction below
explicitly rules that out and asks for realistic proportions + muted broadcast color grading.

**⚠️ Tattoos were being generated inconsistently ("willy nilly") with no visual anchor for his
arms/chest** — only the back tattoo had a reference photo. Fixed by adding a dedicated
**chest/arm tattoo reference** (`zion_chest_arm_tattoo.jpg`) to every scene where his front/arms
are visible. Scenes shot from behind or in silhouette keep using the back-tattoo reference only.

**Two face references, not one.** `zion_gym_parallette.jpg` (the original face ref) and
`zion_face_agt.jpg` (a sharp AGT red-carpet photo Ben approved for face fidelity) are used
**together** on every prompt — both are the same person from different angles/lighting, which
reinforces identity rather than competing with it.

**⚠️ The torso cutoff was reading bare/exposed in some WWE renders (flagged on `victory`).** Ben
noticed his real reference photos never show bare skin right at the torso cutoff — a shirt hem or
loose shorts/trunks typically drapes past it. Every full-body scene below now explicitly says his
shorts/trunks/shirt hem drape loosely and emptily past the end of his torso (not shaped like a leg)
instead of ending in bare skin. Upper-body-only portrait crops (framed above the waist) don't need
this since they don't reach that part of the frame.

**⚠️ Everything was reading too centered/symmetrical — no camera variety.** Ben flagged that both
his and Kazumi's packs default to flat, centered hero shots because the prompts never specified an
angle, lens, or off-center framing. Every scene below now ends with an explicit **Camera:** clause
— a mix of low/high/Dutch angles, specific focal lengths (20mm wide through 135mm telephoto), and
off-center/asymmetrical framing, no two scenes alike. Keep this up on any new scenes you add.

---

## How to run each prompt
1. Nano Banana Pro (Comfy Cloud "Google Gemini Image" node) or Nano Banana in Higgsfield.
   Aspect ratio **9:16**.
2. Attach the reference images **in the exact order listed** for that prompt — the numbering in
   the text ("REFERENCE IMAGE 1", "2", etc.) must match the actual upload order.
3. Paste the prompt text unmodified.
4. **Generate 3–4 seed variants per prompt**, not just 1–2 — anatomy compliance and style/photoreal
   balance both vary noticeably seed to seed even with identical wording. Pick the best, and
   discard any variant with a leg/foot/stump visible or with real-logo leakage rather than trying
   to "fix" it after the fact.

**Reference files used throughout** (all in `creators/zion-clark/refs/`):
- **Face, angle 1 (identity, every prompt):** `zion_gym_parallette.jpg`
- **Face, angle 2 (identity, every prompt):** `zion_face_agt.jpg`
- **Arm/chest tattoo (every prompt where his front/arms are visible):** `zion_chest_arm_tattoo.jpg`
  (alternate: `zion_chest_tattoo_closeup_alt.jpg`)
- **Back tattoo (only when his back is visible / silhouetted):** `zion_back_noexcuses_tattoo.jpg`
- **Body/pose (varies by scene — gym: `soul-id/soul_12.jpg` or `zion_plyobox_bodycomp.jpg`; track:
  `zion_track_noexcuses.jpg`; combat/wrestling: `zion_boxing_ring.jpg`)**
- **Style (every prompt):** `reference-material/2k-screenshots/2k_02.jpg`

**Reusable role blocks** (used verbatim across every prompt below):
```
FACE — REFERENCE IMAGE: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

FACE (SECOND ANGLE) — REFERENCE IMAGE: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

ARM/CHEST TATTOO — REFERENCE IMAGE: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

BACK TATTOO — REFERENCE IMAGE: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

STYLE — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.
```

**Tags:** `[style · scene]`. Full style DNA in `skills/nba2k-style/`, `skills/wwe2k-style/`, and
`skills/iphone-selfie-style/`.

> v6 — added a new **iPhone Selfie** camera style (2 scenes): still full CGI render, character
> AND environment both in-engine — only the camera language changes (wide-angle selfie
> distortion, on-camera flash, chaotic energy). Not a return to the dropped "composited into a
> real photo" look — see the style's own header note in `skills/iphone-selfie-style/SKILL.md`.
> v5 added a distinct Camera clause (angle + focal length + off-center framing) to every scene
> to break the default centered/symmetrical look. v4 added the second face angle
> (`zion_face_agt.jpg`) alongside the original face ref, all scenes renumbered.

---

## NBA 2K  (`skills/nba2k-style/`)

**[nba2k · gym]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg` (face, 2nd angle)
3) `zion_chest_arm_tattoo.jpg` (arm/chest tattoo) 4) `soul-id/soul_12.jpg` (body) 5) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a muscular Black adaptive athlete born without legs, medium-length dreadlocks in a top-knot, short beard, gold chain with a cross pendant, supporting himself on his hands mid-training on a gym floor, chalked palms, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: low-angle hero shot, 24mm wide lens, subject positioned slightly left-of-center with exaggerated foreground-to-background perspective. 9:16 vertical.
```

**[nba2k · gym — back / NO EXCUSES tattoo]** — _1) `zion_gym_parallette.jpg` (face)
2) `zion_face_agt.jpg` (face, 2nd angle) 3) `zion_back_noexcuses_tattoo.jpg` (back tattoo)
4) `soul-id/soul_12.jpg` (body) 5) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: seen from behind, seated on a gym floor, powerful back and shoulders showing the bold "NO EXCUSES" tattoo across his upper back, medium-length dreadlocks. Bright modern gym with equipment in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: eye-level angle shot from directly behind, 50mm lens, subject placed in the lower third of frame with negative space above toward the gym ceiling. 9:16 vertical.
```

**[nba2k · gym — parallette hold]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: reclined with his torso flat against the gym floor, resting up on his forearms in a relaxed pose between sets, gold chain, relaxed confident expression looking toward camera. Bright modern gym with cable machines and dumbbells in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: high overhead angle looking down at a slight tilt, 28mm wide lens, asymmetrical framing with negative space to one side. 9:16 vertical.
```

**[nba2k · training-facility]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: training with battle ropes from a seated hand-supported position, powerful shoulders and back, gold chain, on a turf floor with padded walls and staff at lower detail in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: Dutch angle (12° tilt), 35mm lens, dynamic diagonal composition. 9:16 vertical.
```

**[nba2k · training-facility — sled]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: leaning low with his torso close to the ground, pulling a resistance sled backward by a strap with both arms, powerful shoulders engaged, on a performance turf floor with equipment visible in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: extreme low angle looking up, 20mm wide lens, dramatic foreshortening. 9:16 vertical.
```

**[nba2k · track]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg` (face, 2nd angle)
3) `zion_chest_arm_tattoo.jpg` (arm/chest tattoo) 4) `zion_track_noexcuses.jpg` (body) 5) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic composition with his racing wheelchair. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: in a racing wheelchair on an outdoor stadium track, gripping the push rims mid-sprint, powerful arms and shoulders, aerodynamic racing gloves and helmet. Red synthetic track lanes with crisp white lines, grandstands, bright natural daylight, blue sky, banners — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: wide establishing shot, 24mm lens, subject framed off-center to the right with the track receding into the distance. Racing wheelchair, authentic adaptive athlete. 9:16 vertical.
```

**[nba2k · track — start line]** — _same refs as [nba2k · track]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic composition with his racing wheelchair. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: at the start line in his racing wheelchair, coiled and ready, intense focus, gold chain. Stadium track and grandstands in the background, bright daylight — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: telephoto compression, 85mm lens, flattened background, subject framed left-of-center. Racing wheelchair, authentic adaptive athlete. 9:16 vertical.
```

**[nba2k · portrait]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: broadcast close-up portrait, intense determined expression, sweat specular on forehead and shoulders, the chest tattoo and left arm tattoo visible, black "No Excuses" compression top. Shallow depth of field with a blurred facility in the background, dramatic broadcast lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. Upper-body hero portrait, framed above the waist — his body ends at/just past the belly button, no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. Camera: telephoto close-up, 100mm lens, extremely shallow depth of field, eyes positioned on the upper-left third of frame. 9:16 vertical.
```

### Signature moments (exact-gesture)

**[nba2k · signature · chalk-clap]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: seated upright on the gym floor, torso vertical, clapping both chalked hands together in front of his chest to explode a burst of white chalk dust into the air, mouth open in an intense fired-up yell, eyes locked forward. Chest tattoo and left arm tattoo visible, shirtless or in a black "No Excuses" cutoff, sweat specular sheen on shoulders and forehead. Gym backdrop, shallow depth of field, dramatic rim light — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: Dutch tilt (15°), 28mm wide lens, dynamic broadcast-camera energy. 9:16 vertical.
```

**[nba2k · signature · double-flex]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg`
(face, 2nd angle) 3) `zion_chest_arm_tattoo.jpg` (arm/chest tattoo) 4) `zion_back_noexcuses_tattoo.jpg`
(back tattoo) 5) `soul-id/soul_12.jpg` (body) 6) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 5: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 6: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: supported on one hand while raising the other arm in a hard double-take flex — bicep peaked, veins showing, the left arm tattoo visible on the flexed arm, fist clenched, jaw set in a roaring intense expression. "NO EXCUSES" tattoo across his upper back catching the light, gold cross chain, sweat specular on skin. Dark moody gym, hard rim and key light, shallow depth of field — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: low three-quarter angle, 35mm lens, subject off-center with negative space to the right. 9:16 vertical.
```

---

## WWE 2K  (`skills/wwe2k-style/`)

**[wwe2k · entrance]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg` (face, 2nd angle)
3) `zion_chest_arm_tattoo.jpg` (arm/chest tattoo) 4) `zion_boxing_ring.jpg` (body) 5) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: positioned low at the front edge of the entrance stage, torso reclined and propped up on his forearms, surveying the crowd with an intense heroic expression, custom "No Excuses" entrance gear leaving his arms and chest tattoo visible, gold chain. Both his hands/forearms are clearly planted on the stage floor supporting his upper body; nothing below his torso is in frame. Giant LED video wall glowing behind (purple and gold), cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: extreme low angle looking up from the crowd, 24mm wide lens, dramatic scale, subject framed off-center. 9:16 vertical.
```

**[wwe2k · entrance — silhouette]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg`
(face, 2nd angle) 3) `zion_back_noexcuses_tattoo.jpg` (back tattoo) 4) `zion_boxing_ring.jpg` (body)
5) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: torso reclined flat and silhouetted against the glowing LED wall at the top of the entrance ramp, propped up on both forearms with one arm lifting slightly in a triumphant gesture, the "NO EXCUSES" back tattoo catching the rim light, purple-and-gold pyro erupting, haze and follow-spots, roaring dark crowd below at low detail. Only his torso, arms, and head are silhouetted — nothing below his torso is in frame — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: slight high angle from a side platform, 35mm lens, subject offset to one side of the ramp, not centered. 9:16 vertical.
```

**[wwe2k · ring]** — _same refs as [wwe2k · entrance — silhouette]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: center-ring on the canvas, supported on his hands in a commanding heroic pose, ropes and padded turnbuckles around, bold graphic mat design, dark arena crowd at reduced detail, overhead truss lighting. Oiled muscular sheen catching the lights, "NO EXCUSES" visible across the back — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: high three-quarter angle from the turnbuckle, 50mm lens, subject in the lower half of frame. 9:16 vertical.
```

**[wwe2k · victory]** — _same refs as [wwe2k · entrance — silhouette]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: supporting himself with both hands gripping the middle turnbuckle ropes, torso raised and chest out in a triumphant victory pose, "NO EXCUSES" back tattoo visible, backlit by purple-and-gold stage lighting and pyro, dark roaring crowd below at low fidelity, a championship-style belt on the mat. His hands are clearly gripping the ropes/turnbuckle pad supporting his weight; nothing below his torso is in frame — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: low Dutch angle (10° tilt), 28mm lens, dynamic tilted horizon. 9:16 vertical.
```

**[wwe2k · dramatic-gym]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a dark, moody gym lit dramatically — hard rim and colored spotlights, mid-lift supported on his hands, gold chain, equipment in deep shadow, saturated purple accent lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching how he actually dresses in his reference photos, rather than his torso ending abruptly in bare exposed skin. Camera: side-profile angle, 50mm lens, subject framed left-of-center, deep shadow filling the right side of frame. 9:16 vertical.
```

**[wwe2k · portrait]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 5: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: intense expression, oiled skin with strong specular and sweat highlights, chest and left arm tattoos visible, a championship-style belt over the shoulder. Dark arena bokeh in the background with purple/gold stage-light glow, dramatic lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. Upper-body hero portrait, framed above the waist — his body ends at/just past the belly button, no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. Camera: telephoto, 135mm lens, extremely shallow depth of field, off-center framing with negative space to one side. 9:16 vertical.
```

---

## iPhone Selfie  (`skills/iphone-selfie-style/`)

**This is a camera/photography style, not a different look-category.** The entire frame —
character AND environment — still renders fully in the CGI game engine, same as every other
scene in this pack. The only thing that changes is *what kind of shot it is*: instead of a
cinematic broadcast/cutscene camera, it's shot like a real iPhone front-facing selfie — close,
wide-angle-distorted, hard on-camera flash, chaotic energy. Nothing in the frame is a real
photograph. No dedicated style-reference screenshot exists for this look yet, so these two
scenes run on 4 refs (both face angles + the arm/chest tattoo + a body/pose ref) with the
CGI-render instruction carried entirely in the prompt text — keep that instruction explicit and
early in the prompt, it's the detail most likely to drift toward a real-photo read if dropped.

**[iphone-selfie · celebration]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg`
(face, 2nd angle) 3) `zion_chest_arm_tattoo.jpg` (arm/chest tattoo) 4) `zion_track_noexcuses.jpg` (body)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic composition with his racing wheelchair. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

Now render: a real iPhone front-facing selfie photo of him, taken amid a dense, chaotic celebratory crowd at night. He is a CGI video-game character rendered in a real-time 3D game engine — smooth subsurface-scattering skin, a subtle polished sheen on the forehead and cheekbones, simplified rendered hair as a clean texture map — clearly a high-fidelity rendered character, not a real photoreal person. Rectangular 9:16 photo — no circular vignette, no dark corners, no fisheye lens crop, just the normal subtle wide-angle perspective of a real phone selfie camera. The phone itself must NEVER be visible anywhere in the shot — it IS the camera taking this photo. Only the extended arm and hand may enter the frame; no phone body, no phone screen, no displayed photo, no second phone. Seated upright in his racing wheelchair, face large and close to the lens with wide-angle selfie-lens distortion, mouth open mid-shout of celebration, one arm extended toward the camera, only the arm and hand visible — the phone itself is never shown in frame, since the camera taking this shot IS the phone's own lens, gold chain with a cross pendant, medium-length dreadlocks in a top-knot, short beard, chest and left-arm tattoos visible on his sleeveless "No Excuses" gear. Face lit by harsh, direct, on-camera flash with sharp falloff into a darker background — the same flat hard flash lighting the nearest fans. Behind him, a dense crowd packed tightly right up against the camera, bodies overlapping and partly cropped, faces turned toward the lens mid-celebration, smeared with motion blur — rendered in the same CGI game-engine style as him, nothing photoreal anywhere in frame. Further back, blurred neon signage, streetlights, and scattered flashes from other phones dissolve into out-of-focus glow, also fully CGI-rendered. Simulated low-light phone-camera artifacts: motion blur, sensor noise, lens haze, slight overexposure where the flash hits — all rendered as part of the CG shot, not composited from a real photograph. Clean CG geometry throughout. No real league, team, studio, brand logos, event names, or readable signage anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — he is seated in the racing wheelchair's seat, torso upright, the composition must not require or imply a leg. Camera: 20mm ultra-wide selfie lens, natural arm's-length tilt, off-center framing. 9:16 vertical.
```

**[iphone-selfie · gym]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_face_agt.jpg`
(face, 2nd angle) 3) `zion_chest_arm_tattoo.jpg` (arm/chest tattoo) 4) `soul-id/soul_12.jpg` (body)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY as an additional facial reference of the same person as Image 1, to reinforce identity and likeness from a different angle/lighting. Ignore the pose, clothing, and background in this image.

REFERENCE IMAGE 3: use ONLY for the exact tattoo designs on his chest/collarbone (a script-lettering tattoo) and his left arm/bicep — their exact linework, lettering, and placement. Ignore the pose and background in this image.

REFERENCE IMAGE 4: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

Now render: a real iPhone front-facing selfie photo of him, taken mid-training in a gym. He is a CGI video-game character rendered in a real-time 3D game engine — smooth subsurface-scattering skin, a subtle polished sheen on the forehead and cheekbones, simplified rendered hair as a clean texture map — clearly a high-fidelity rendered character, not a real photoreal person. Rectangular 9:16 photo — no circular vignette, no dark corners, no fisheye lens crop, just the normal subtle wide-angle perspective of a real phone selfie camera. The phone itself must NEVER be visible anywhere in the shot — it IS the camera taking this photo. Only the extended arm and hand may enter the frame; no phone body, no phone screen, no displayed photo, no second phone. Torso propped on one forearm on the gym floor, face large and close to the lens with wide-angle selfie-lens distortion, a playful confident grin, one arm extended toward the camera, only the arm and hand visible — the phone itself is never shown in frame, since the camera taking this shot IS the phone's own lens, gold chain, sweat sheen on his shoulders, chest and left-arm tattoos visible, chalk dust hanging in the air near him. Face lit by harsh, direct, on-camera flash with sharp falloff into a dim background. Behind him, blurred power racks and rim-lit equipment dissolve into soft out-of-focus shapes — rendered in the same CGI game-engine style as him, nothing photoreal anywhere in frame. Simulated low-light phone-camera artifacts: sensor noise, lens haze, a touch of motion blur, slight overexposure where the flash hits — all rendered as part of the CG shot, not composited from a real photograph. Clean CG geometry throughout. No real league, team, studio, or brand logos anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs, no feet, no shoes visible anywhere in the frame — the composition must not require or imply a leg. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath. Camera: 18mm ultra-wide selfie lens, slight high tilt as if the phone is propped above him, off-center. 9:16 vertical.
```

---

_18 scenes (16 broadcast/cutscene + 2 iPhone-selfie), all locked to the proven multi-ref
role-tagged recipe with two face angles + the dedicated arm/chest tattoo reference. Add more by
mixing any scene modifier from the skill files into the same "Now render: ..." pattern, keeping
the reference blocks and every guardrail (anatomy, brand safety, anti-Disney style, fully-CGI)
exactly as written._

# Prompt Pack — Zion Clark

**✅ RECIPE LOCKED (v2, confirmed best result).** Every prompt below uses the proven multi-image
role-tagged recipe: **Nano Banana Pro** (Google Gemini partner node / `gemini-3-pro-image-preview`
in Comfy, or "Nano Banana" in Higgsfield), 3–4 reference images each assigned ONE explicit job in
the text, 9:16. This beat every other approach tested (Higgsfield GPT Image 2 img2img/Soul ID,
Comfy's GPT Image 2 partner node, plain SDXL) on identity, brand safety, and — after the
anti-Disney/Pixar fix — style. Full technique: `docs/multi-image-role-tagging.md`.

**Authentic representation (read first — exact anatomy):** Zion was **born without legs**
(caudal regression syndrome). **His body ends at/just past his belly button** — there is no
hip, pelvis, thigh, or leg structure below that, not even partial/"stump" legs. Depict him
**authentically and heroically** — powerful upper body and core, moving on his **hands** or in
a **racing wheelchair**. **Do NOT generate fabricated legs, stump legs, hips, or a standing
figure.** He is the hero of every frame: elite, dignified, motivational.

**His real look (from `refs/`, woven into every prompt):** a muscular Black adaptive athlete,
**medium-length dreadlocks often in a top-knot**, full short beard, **gold chain with a cross
pendant**, **chest/collarbone tattoos**, and a bold **"NO EXCUSES" tattoo across his upper
back/shoulders**; often in his own **"Z" lightning "No Excuses"** branded gear
(purple/gold/black), or shirtless training.

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

---

## How to run each prompt
1. Nano Banana Pro (Comfy Cloud "Google Gemini Image" node) or Nano Banana in Higgsfield.
   Aspect ratio **9:16**.
2. Attach the reference images **in the exact order listed** for that prompt — the numbering in
   the text ("REFERENCE IMAGE 1", "2", etc.) must match the actual upload order.
3. Paste the prompt text unmodified.
4. Generate 2–3 variants, keep the best. Verify the body is represented authentically and no
   real logos leaked in.

**Reference files used throughout** (all in `creators/zion-clark/refs/`):
- **Face (identity, every prompt):** `zion_gym_parallette.jpg`
- **Tattoo (only when his back is visible in the scene):** `zion_back_noexcuses_tattoo.jpg`
- **Body/pose (varies by scene — gym: `soul-id/soul_12.jpg`; track: `zion_track_noexcuses.webp`;
  combat/wrestling: `zion_boxing_ring.jpg`)**
- **Style (every prompt):** `reference-material/2k-screenshots/2k_02.jpg`

**Reusable role blocks** (used verbatim across every prompt below):
```
FACE — REFERENCE IMAGE: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

TATTOO — REFERENCE IMAGE: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

STYLE — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.
```

**Tags:** `[style · scene]`. Full style DNA in `skills/nba2k-style/` and `skills/wwe2k-style/`.

> v4 — recipe locked, all scenes converted to multi-ref role-tagged.

---

## NBA 2K  (`skills/nba2k-style/`)

**[nba2k · gym]** — _1) `zion_gym_parallette.jpg` (face) 2) `soul-id/soul_12.jpg` (body)
3) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a muscular Black adaptive athlete born without legs, medium-length dreadlocks in a top-knot, short beard, gold chain with a cross pendant, supporting himself on his hands mid-training on a gym floor, chalked palms, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · gym — back / NO EXCUSES tattoo]** — _1) `zion_gym_parallette.jpg` (face)
2) `zion_back_noexcuses_tattoo.jpg` (tattoo) 3) `soul-id/soul_12.jpg` (body) 4) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: seen from behind, seated on a gym floor, powerful back and shoulders showing the bold "NO EXCUSES" tattoo across his upper back, medium-length dreadlocks. Bright modern gym with equipment in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · gym — parallette hold]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: supporting himself on his hands in a strength hold on a gym floor, arms and core engaged, gold chain, determined face. Bright modern gym with cable machines and dumbbells in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · training-facility]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: training with battle ropes from a seated hand-supported position, powerful shoulders and back, gold chain, on a turf floor with padded walls and staff at lower detail in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · training-facility — sled]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: driving a weight sled with his arms across a performance turf floor, equipment visible in the background — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · track]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_track_noexcuses.webp` (body)
3) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic composition with his racing wheelchair. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: in a racing wheelchair on an outdoor stadium track, gripping the push rims mid-sprint, powerful arms and shoulders, aerodynamic racing gloves and helmet. Red synthetic track lanes with crisp white lines, grandstands, bright natural daylight, blue sky, banners — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. Racing wheelchair, authentic adaptive athlete. 9:16 vertical.
```

**[nba2k · track — start line]** — _same refs as [nba2k · track]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic composition with his racing wheelchair. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: at the start line in his racing wheelchair, coiled and ready, intense focus, gold chain. Stadium track and grandstands in the background, bright daylight — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. Racing wheelchair, authentic adaptive athlete. 9:16 vertical.
```

**[nba2k · portrait]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: broadcast close-up portrait, intense determined expression, sweat specular on forehead and shoulders, tattoos visible on arms and neck, black "No Excuses" compression top. Shallow depth of field with a blurred facility in the background, dramatic broadcast lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. Upper-body hero portrait — his body ends at/just past the belly button, no hips, no legs, no stump legs. 9:16 vertical.
```

### Signature moments (exact-gesture)

**[nba2k · signature · chalk-clap]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: clapping both chalked hands together in front of his chest to explode a burst of white chalk dust into the air, arms flexed, mouth open in an intense fired-up yell, eyes locked forward. Chest and collarbone tattoos visible, shirtless or in a black "No Excuses" cutoff, sweat specular sheen on shoulders and forehead. Gym backdrop, shallow depth of field, dramatic rim light — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · signature · double-flex]** — _1) `zion_gym_parallette.jpg` (face)
2) `zion_back_noexcuses_tattoo.jpg` (tattoo) 3) `soul-id/soul_12.jpg` (body) 4) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: supported on one hand while raising the other arm in a hard double-take flex — bicep peaked, veins showing, fist clenched, jaw set in a roaring intense expression. "NO EXCUSES" tattoo across his upper back catching the light, gold cross chain, sweat specular on skin. Dark moody gym, hard rim and key light, shallow depth of field — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

---

## WWE 2K  (`skills/wwe2k-style/`)

**[wwe2k · entrance]** — _1) `zion_gym_parallette.jpg` (face) 2) `zion_boxing_ring.jpg` (body)
3) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: entering on his hands onto an entrance stage, arms mid-stride, intense heroic face, custom "No Excuses" entrance gear, gold chain. Giant LED video wall glowing behind (purple and gold), cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[wwe2k · entrance — silhouette]** — _1) `zion_gym_parallette.jpg` (face)
2) `zion_back_noexcuses_tattoo.jpg` (tattoo) 3) `zion_boxing_ring.jpg` (body) 4) `2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: backlit in silhouette at the top of an entrance ramp, arms raised, the "NO EXCUSES" back tattoo catching the rim light, purple-and-gold pyro erupting, LED wall blazing, haze and follow-spots, roaring dark crowd below at low detail — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[wwe2k · ring]** — _same refs as [wwe2k · entrance — silhouette]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: center-ring on the canvas, supported on his hands in a commanding heroic pose, ropes and padded turnbuckles around, bold graphic mat design, dark arena crowd at reduced detail, overhead truss lighting. Oiled muscular sheen catching the lights, "NO EXCUSES" visible across the back — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[wwe2k · victory]** — _same refs as [wwe2k · entrance — silhouette]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: raised on top of a turnbuckle balanced on his hands, arms and torso in a triumphant victory pose, "NO EXCUSES" back tattoo visible, backlit by purple-and-gold stage lighting and pyro, dark roaring crowd below at low fidelity, a championship-style belt on the mat — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[wwe2k · dramatic-gym]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a dark, moody gym lit dramatically — hard rim and colored spotlights, mid-lift supported on his hands, gold chain, equipment in deep shadow, saturated purple accent lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[wwe2k · portrait]** — _same refs as [nba2k · gym]_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific background in this image.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. This is a broadcast sports-simulation video game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions; muted, slightly desaturated broadcast color grading, not warm saturated animated-film colors. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: intense expression, oiled skin with strong specular and sweat highlights, a championship-style belt over the shoulder. Dark arena bokeh in the background with purple/gold stage-light glow, dramatic lighting — the entire frame rendered in the CGI style described above. No real league, team, studio, or brand logos or trademarks anywhere in the output. Upper-body hero portrait — his body ends at/just past the belly button, no hips, no legs, no stump legs. 9:16 vertical.
```

---

_16 scenes, all locked to the proven multi-ref role-tagged recipe. Add more by mixing any scene
modifier from the skill files into the same "Now render: ..." pattern, keeping the reference
blocks and every guardrail (anatomy, brand safety, anti-Disney style) exactly as written._

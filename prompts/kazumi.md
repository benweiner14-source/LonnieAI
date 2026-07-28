# Prompt Pack — Kazumi

**Recipe: same locked technique as Zion** (see `prompts/zion-clark.md`, `docs/multi-image-role-tagging.md`) —
**Nano Banana Pro**, multi-image role-tagging, anti-Disney/Pixar wording. **Not yet test-confirmed
for Kazumi specifically** (Zion's recipe was validated across several rounds; this is the same
method applied fresh to her — run one scene first and report back before batching the rest).

**Her real look (from `refs/`, woven into every prompt):** a Filipina-American woman with an
hourglass figure, **long wavy balayage hair (blonde with darker roots)** worn down or in a **high
ponytail**, **full glam makeup** (bold winged liner, long lashes, arched brows, glossy nude-pink
lips), and **gold hoops + a green jade teardrop pendant**. Confident, sultry, camera-aware.

**One look: FULL CGI RENDER.** Every prompt renders the **entire frame — character AND
environment — in the game engine** (an in-game shot).

**⚠️ Brand safety — no real logos/trademarks.** Every prompt describes the *aesthetic only*
(open-world crime-saga neon look; neon-noir cyberpunk look) — never a real game, studio, or
engine name — with invented place names (**Bayview City**, **Neo City**) instead of real
trademarked ones. The style reference images are real gameplay screenshots (not cover art —
cover art is dominated by the real logo/title and was rejected as too risky) but may still
contain incidental readable text, so every style role explicitly says to ignore it.

**⚠️ Style must read as a stylized game render, not an animated film.** Same failure mode
confirmed on Zion's pack: "3D CGI, not a photo" alone can drift toward Disney/Pixar (rounded
proportions, toon shading) instead of a game-engine look. Every style-role instruction below
rules that out explicitly.

---

## How to run each prompt
1. Nano Banana Pro (Comfy Cloud "Google Gemini Image" node) or Nano Banana in Higgsfield.
   Aspect ratio **9:16**.
2. Attach the reference images **in the exact order listed** — the numbering in the text
   ("REFERENCE IMAGE 1", "2", "3") must match the actual upload order.
3. Paste the prompt text unmodified.
4. Generate 2–3 variants, keep the best. Keep everything **SFW** and verify no real logos leaked.

**Reference files used throughout** (all in `creators/kazumi/refs/` unless noted):
- **Face (identity, every prompt):** `kazumi_yellow_polo_portrait.jpg`
- **Body/figure (every prompt):** `kazumi_olive_tank_denim.jpg`
- **Style — GTA VI scenes:** `skills/gta6-style/reference/gtav_skyline_dusk.jpg`
- **Style — Cyberpunk 2077 scenes:** `skills/cyberpunk-2077-style/reference/cp2077_neon_street.jpg`

**Reusable role blocks:**
```
FACE — REFERENCE IMAGE: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

STYLE (GTA) — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

STYLE (Cyberpunk) — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.
```

**Tags:** `[style · scene]`. Full style DNA in `skills/gta6-style/` and `skills/cyberpunk-2077-style/`.

> v4 — converted to multi-ref role-tagging (same method as Zion's locked recipe). Cyberpunk
> prompts keep her balayage waves but add optional neon streaks for the cosplay; swap back to
> natural if preferred.

---

## GTA VI  (`skills/gta6-style/`) — style ref: `gtav_skyline_dusk.jpg`

**[gta6 · nightlife]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a glamorous Filipina-American woman with long wavy balayage-blonde hair, full glam makeup (winged liner, glossy nude-pink lips), gold hoops and a green jade pendant, in a cropped designer top and gold jewelry, leaning against a neon-underlit convertible on a night street. Art-deco hotels with hot-pink and cyan neon, wet reflective asphalt, palm trees strung with lights, distant Bayview City skyline glow — the entire frame rendered in the CGI style described above. Low hero camera angle, poster-like composition. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[gta6 · nightlife — club entrance]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage waves in a high ponytail, full glam, gold jewelry, in a fitted blazer over a bodysuit and heels stepping out of a club entrance with a velvet rope, neon marquee overhead in pink and purple, valet supercars at the curb, wet street reflecting the signage — the entire frame rendered in the CGI style described above. Confident poster framing, slight low angle. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City nightlife. SFW.
```

**[gta6 · beach]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage-blonde waves, full glam, gold hoops and jade pendant, in a fashionable one-piece and oversized sunglasses walking a boardwalk at golden hour, turquoise ocean, white sand, pastel art-deco buildings, palm trees, a parked convertible — the entire frame rendered in the CGI style described above. Full-body fashion framing, slight low angle. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[gta6 · beach — marina]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long wavy balayage hair, in chic beachwear and a sarong at a marina at golden hour — yachts, palms, pastel buildings, warm low sun — the entire frame rendered in the CGI style described above. Confident fashion pose. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. SFW.
```

**[gta6 · luxury-car]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage waves, full glam, gold jewelry and jade pendant, in a linen set and designer sunglasses leaning on the hood of a glossy candy-orange supercar convertible at a gas station, palm-lined boulevard behind — chrome and candy paint catching golden-hour reflections, humid skin sheen — the entire frame rendered in the CGI style described above. Confident low-angle hero framing, cover-art energy. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. SFW.
```

**[gta6 · luxury-car — night]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a long blonde ponytail and winged-liner makeup, seated sideways in the driver's seat of a neon-underlit convertible at night, door open, one heel on the sill, city neon behind — wet reflective street, pink and cyan neon bloom, humid sheen — the entire frame rendered in the CGI style described above. Poster-like low framing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. SFW.
```

**[gta6 · penthouse]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage waves, full glam, gold hoops and jade pendant, in glamorous loungewear at a rooftop infinity pool at dusk, floor-to-ceiling glass, neon skyline reflected in the water, modern designer furniture, palms, warm interior practical light, city-light bokeh in the distance — purple-orange dusk sky, humid sheen — the entire frame rendered in the CGI style described above. Elegant full-body framing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. SFW.
```

**[gta6 · penthouse — balcony]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. This is a stylized open-world action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a long blonde ponytail and full glam makeup, in chic evening wear on a luxury penthouse balcony overlooking a neon skyline at night, city-light bokeh — warm practical light, saturated cinematic grade, humid sheen — the entire frame rendered in the CGI style described above. Glamorous confident pose. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. SFW.
```

---

## Cyberpunk 2077  (`skills/cyberpunk-2077-style/`) — style ref: `cp2077_neon_street.jpg`

**[cyberpunk · street]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long wavy balayage hair (blonde with subtle teal and magenta neon streaks), sharp winged-liner glam, a subtle chrome cheek accent and faintly glowing cyber-eyes, wearing a neon-trimmed techwear jacket, standing in a rain-slick back alley. Holographic signage glows overhead, puddles mirror the neon, steam rises from vents — the entire frame rendered in the CGI style described above. Dramatic low-angle framing, neon bokeh. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · street — techwear]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage hair in a high ponytail, glossy glam makeup, gold and chrome accents, in glossy black techwear with LED trim, walking a neon-soaked street, holo-billboards towering above, wet asphalt reflecting cyan and magenta, distant crowd with cyberware at low detail — the entire frame rendered in the CGI style described above. Cinematic low angle, shallow DOF with neon bokeh. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · megabuilding]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage waves with neon streaks, full glam, gold jade pendant, on a high walkway among towering megabuildings at night, giant animated holo-billboards, flying vehicles with light trails in the neon canyon below, teal-and-magenta city glow — the entire frame rendered in the CGI style described above. Dramatic vertical composition emphasizing scale, low hero angle. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Neo City. SFW.
```

**[cyberpunk · cyber-bar]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long wavy balayage hair, glossy glam makeup, gold hoops, leaning on the LED-lit counter of a neon noodle bar, holographic menu boards, warm sodium mixed with cold neon, patrons with cyberware blurred behind, steam catching colored light, reflective wet counter — the entire frame rendered in the CGI style described above. Intimate underlit framing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · cosplay-hero]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: centered and lit like a character-select hero portrait — long wavy balayage hair with teal/magenta streaks, sharp winged-liner glam, glossy techwear, subtle chrome jaw accent, glowing cybernetic optic implants. Dramatic teal rim light on one side, magenta on the other, electric-yellow accent, dark foggy background with faint holo-signage bokeh — the entire frame rendered in the CGI style described above. Confident direct pose, poster-quality hero framing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · cosplay-hero — tight portrait]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: tight portrait — almond eyes, sharp winged-liner glam, glossy lips, a subtle chrome cheek jewel and glowing cyber-eyes, wet-look styled hair — against a dark neon-bokeh background. Strong teal/magenta split lighting, electric-yellow rim — the entire frame rendered in the CGI style described above. Intense direct gaze. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · neon-vehicle]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: ray-traced neon reflections, volumetric fog, bloom, teal-and-magenta lighting, clean CG geometry. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage hair with neon streaks, full glam, posed beside a neon-underlit motorcycle on a wet street, chrome and carbon bodywork reflecting teal and magenta, headlight glare and light trails, holo-signage overhead — the entire frame rendered in the CGI style described above. Low-angle hero framing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Neo City. SFW.
```

---

_15 scenes, converted to multi-ref role-tagging. **Not yet validated in testing like Zion's
pack** — run the first GTA and first Cyberpunk scene, confirm identity/style/brand-safety hold,
then batch the rest. Add more by mixing any scene modifier from the skill files into the same
"Now render: ..." pattern, keeping the reference blocks and every guardrail exactly as written._

# Prompt Pack — Kazumi

**⚠️ Everything was reading too centered/symmetrical — no camera variety.** Ben flagged that both
her and Zion's packs default to flat, centered hero shots because the prompts never specified an
angle, lens, or off-center framing. Every scene below now ends with an explicit **Camera:** clause
— a mix of low/high/Dutch angles, specific focal lengths (20mm wide through 85mm telephoto), and
off-center/asymmetrical framing, no two scenes alike (one deliberate exception: `cosplay-hero`
stays centered on purpose — it's mimicking a character-select screen). Keep this up on any new
scenes.

**Recipe status (v6 — second test round found issues on both sides, both reworked below):**
- **Cyberpunk: ⚠️ REWORKED, not yet retested.** The automated pass ([cyberpunk · street] 4/4
  seeds — identity/logos/SFW all clean) missed something Ben caught on direct look: the results
  read as a **CGI character composited into a photoreal background** rather than a unified
  in-engine render — exactly the "composited" look this project explicitly dropped early on (see
  `CLAUDE.md` locked decisions) — and the environments were **busy/over-stylized** (too many
  simultaneous neon/fog/bloom layers competing for attention). **Fixed below**: the style role now
  explicitly requires character and environment to render in one unified CGI style, and the 4
  busiest scenes (`street`, `megabuilding`, `cyber-bar`, `cosplay-hero`) had their environment
  descriptions trimmed to 1-2 clean elements instead of 3-5 stacked ones. Retest `[cyberpunk ·
  street]` again before batching the other 6.
- **GTA VI: ⚠️ REWORKED, not yet retested.** `[gta6 · nightlife]` failed two ways in the first
  round — see below — both fixed here. Ben's first-glance read on the raw `nightlife` output was
  "pretty good," which is a positive early signal, but this is still the reworked prompt, not yet
  re-run — confirm before batching the other 7 GTA scenes.

**What went wrong with GTA and the fix:**
1. **Style read too photoreal** — the character and the neon-street environment rendered as a real
   photograph of real-world Miami, not a CGI game screenshot (same failure mode as Zion's
   "plainest" gym scene — not enough environmental exaggeration to force the CGI tell). **Fixed:**
   the GTA style role now explicitly says "obviously computer-generated, in-engine, NOT a real
   photograph" (this line was missing before — Cyberpunk's read passed without it, but GTA
   apparently needs it stated), and `[gta6 · nightlife]`'s environment description was punched up
   with more exaggerated neon saturation and lighting to read as clearly stylized.
2. **3 of 4 seeds refused by Gemini's safety filter** — traced to the GTA body reference,
   `kazumi_olive_tank_denim.jpg` (olive tank + denim cutoffs), combined with "cropped designer
   top" in the prompt text. Checked all 8 photos in `creators/kazumi/refs/` for a less-revealing
   replacement — **none work**: the two bikini shots are more revealing, not less;
   `kazumi_leather_blonde.jpg`, `kazumi_printed_cutout_mirror.jpg`, and
   `kazumi_terracotta_halter.jpg` are all similarly or more revealing; `kazumi_ponytail_jade.jpg`
   and `kazumi_yellow_polo_portrait.jpg` are modest but both tight shoulders-up crops that don't
   actually show her figure, so they wouldn't serve the BODY role's purpose anyway. **Fixed:**
   dropped the image-based body reference for GTA scenes entirely — they now run on **2 refs**
   (face + style) instead of 3, with her figure carried by text ("hourglass figure") instead of an
   image. Cyberpunk scenes keep the 3-ref version since that recipe already passed clean. If Ben
   sources a genuinely modest full-figure photo later, the body ref can be added back to GTA.

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

**⚠️ Style must read as a stylized game render, not an animated film — or a real photo.** Two
distinct failure modes seen so far: (1) "3D CGI, not a photo" alone can drift toward Disney/Pixar
(rounded proportions, toon shading) instead of a game-engine look (same lesson as Zion's pack);
(2) it can also just... stay photoreal, if the scene doesn't have enough visual exaggeration to
force the CGI tell (GTA nightlife's original failure). Every style-role instruction below rules
out both.

---

## How to run each prompt
1. Nano Banana Pro (Comfy Cloud "Google Gemini Image" node) or Nano Banana in Higgsfield.
   Aspect ratio **9:16**.
2. Attach the reference images **in the exact order listed** — the numbering in the text
   ("REFERENCE IMAGE 1", "2", "3") must match the actual upload order. **GTA scenes use 2 refs
   (face + style); Cyberpunk scenes use 3 (face + body + style)** — don't mix them up.
3. Paste the prompt text unmodified.
4. Generate 3–4 variants, keep the best. Keep everything **SFW** and verify no real logos leaked.

**Reference files used throughout** (all in `creators/kazumi/refs/` unless noted):
- **Face (identity, every prompt):** `kazumi_yellow_polo_portrait.jpg`
- **Body/figure (Cyberpunk scenes only):** `kazumi_olive_tank_denim.jpg`
- **Style — GTA VI scenes:** `skills/gta6-style/reference/gtav_skyline_dusk.jpg`
- **Style — Cyberpunk 2077 scenes:** `skills/cyberpunk-2077-style/reference/cp2077_neon_street.jpg`

**Reusable role blocks:**
```
FACE — REFERENCE IMAGE: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

STYLE (GTA) — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

STYLE (Cyberpunk) — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.
```

**Tags:** `[style · scene]`. Full style DNA in `skills/gta6-style/` and `skills/cyberpunk-2077-style/`.

> v7 — added a distinct Camera clause (angle + focal length + off-center framing) to every scene;
> everything was defaulting to flat, centered "hero framing" with no lens or angle variety. v6 —
> both style tracks reworked from round-1 feedback. GTA: dropped the body image (tripped Gemini's
> safety filter) + stronger anti-photoreal wording + a punched-up environment on `nightlife`.
> Cyberpunk: fixed the composited-character-on-photoreal-background look + trimmed busy/stacked
> environment effects on 4 scenes. Retest `nightlife` and `street` once each before batching the
> rest.

---

## GTA VI  (`skills/gta6-style/`) — style ref: `gtav_skyline_dusk.jpg` — **2 refs: face + style**

**[gta6 · nightlife]** — retest this one first
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a glamorous Filipina-American woman with an hourglass figure, long wavy balayage-blonde hair, full glam makeup (winged liner, glossy nude-pink lips), gold hoops and a green jade pendant, in a cropped designer top and gold jewelry, leaning against a neon-underlit convertible on a night street. Art-deco hotels with exaggerated saturated hot-pink and cyan neon signage, glossy wet reflective asphalt throwing colored bounce light, palm trees strung with oversized string lights, a stylized Bayview City skyline glowing unnaturally bright in the distance — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph of a real city. Camera: low-angle hero shot, 24mm wide lens, subject off-center to the left, exaggerated foreground-to-background perspective. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · nightlife — club entrance]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with long balayage waves in a high ponytail, full glam, gold jewelry, in a fitted blazer over a bodysuit and heels stepping out of a club entrance with a velvet rope, neon marquee overhead in pink and purple, valet supercars at the curb, wet street reflecting the signage — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: Dutch angle (10° tilt), 35mm lens, dynamic diagonal energy. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City nightlife. Fully clothed, SFW.
```

**[gta6 · beach]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with long balayage-blonde waves, full glam, gold hoops and jade pendant, in a fashionable one-piece and oversized sunglasses walking a boardwalk at golden hour, turquoise ocean, white sand, pastel art-deco buildings, palm trees, a parked convertible — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 24mm lens, subject placed in the right third of frame, ocean horizon visible. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · beach — marina]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with long wavy balayage hair, in chic beachwear and a sarong at a marina at golden hour — yachts, palms, pastel buildings, warm low sun — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high three-quarter angle, 50mm lens, subject off-center with negative space to the left. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. Fully clothed, SFW.
```

**[gta6 · luxury-car]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with long balayage waves, full glam, gold jewelry and jade pendant, in a linen set and designer sunglasses leaning on the hood of a glossy candy-orange supercar convertible at a gas station, palm-lined boulevard behind — chrome and candy paint catching golden-hour reflections, humid skin sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: extreme low angle looking up, 20mm wide lens, dramatic foreshortening on the car and figure. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. Fully clothed, SFW.
```

**[gta6 · luxury-car — night]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with a long blonde ponytail and winged-liner makeup, seated sideways in the driver's seat of a neon-underlit convertible at night, door open, one heel on the sill, city neon behind — wet reflective street, pink and cyan neon bloom, humid sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: telephoto compression, 85mm lens, flattened neon bokeh background, subject framed left-of-center. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. Fully clothed, SFW.
```

**[gta6 · penthouse]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with long balayage waves, full glam, gold hoops and jade pendant, in glamorous loungewear at a rooftop infinity pool at dusk, floor-to-ceiling glass, neon skyline reflected in the water, modern designer furniture, palms, warm interior practical light, city-light bokeh in the distance — purple-orange dusk sky, humid sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level wide shot, 28mm lens, subject small in frame with expansive skyline negative space. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. Fully clothed, SFW.
```

**[gta6 · penthouse — balcony]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: an hourglass-figured woman with a long blonde ponytail and full glam makeup, in chic evening wear on a luxury penthouse balcony overlooking a neon skyline at night, city-light bokeh — warm practical light, saturated cinematic grade, humid sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: slight high angle, 35mm lens, subject offset to one side of the balcony railing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Bayview City. Fully clothed, SFW.
```

---

## Cyberpunk 2077  (`skills/cyberpunk-2077-style/`) — style ref: `cp2077_neon_street.jpg` — **⚠️ reworked, 3 refs: face + body + style**

**[cyberpunk · street]** — retest this one first (identity/logos/SFW passed clean 4/4 last round; style role reworked below to fix the composited-look + busy-background issues)
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long wavy balayage hair (blonde with subtle teal and magenta neon streaks), sharp winged-liner glam, a subtle chrome cheek accent and faintly glowing cyber-eyes, wearing a neon-trimmed techwear jacket, standing in a rain-slick back alley. Neon signage glows overhead, wet pavement reflects the light — clean, uncluttered composition — the entire frame rendered in the CGI style described above. Camera: Dutch angle (12° tilt), 28mm wide lens, dynamic diagonal composition. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · street — techwear]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage hair in a high ponytail, glossy glam makeup, gold and chrome accents, in glossy black techwear with LED trim, walking a neon-soaked street, holo-billboards towering above, wet asphalt reflecting cyan and magenta, distant crowd with cyberware at low detail — the entire frame rendered in the CGI style described above. Camera: low three-quarter angle, 35mm lens, subject off-center with negative space to one side. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · megabuilding]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage waves with neon streaks, full glam, gold jade pendant, on a high walkway among towering megabuildings at night, teal-and-magenta city glow, a few distant light trails in the canyon below — clean, uncluttered composition — the entire frame rendered in the CGI style described above. Camera: extreme low angle looking straight up, 20mm wide lens, dramatic vertical scale. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Neo City. SFW.
```

**[cyberpunk · cyber-bar]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long wavy balayage hair, glossy glam makeup, gold hoops, leaning on the LED-lit counter of a neon noodle bar, warm sodium light mixed with cool neon, reflective wet counter — clean, uncluttered composition, a soft out-of-focus background — the entire frame rendered in the CGI style described above. Camera: eye-level close angle, 50mm lens, shallow depth of field, subject framed left-of-center. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · cosplay-hero]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: centered and lit like a character-select hero portrait — long wavy balayage hair with teal/magenta streaks, sharp winged-liner glam, glossy techwear, subtle chrome jaw accent, glowing cybernetic optic implants. Dramatic teal-and-magenta rim lighting, dark uncluttered background — the entire frame rendered in the CGI style described above. Camera: eye-level telephoto, 85mm lens — intentionally centered and symmetrical (character-select screen convention, the one deliberate exception to off-center framing in this pack). No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · cosplay-hero — tight portrait]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: tight portrait — almond eyes, sharp winged-liner glam, glossy lips, a subtle chrome cheek jewel and glowing cyber-eyes, wet-look styled hair — against a dark neon-bokeh background. Strong teal/magenta split lighting, electric-yellow rim — the entire frame rendered in the CGI style described above. Intense direct gaze. Camera: low Dutch angle (8° tilt), 35mm lens, off-center framing with negative space to one side. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. SFW.
```

**[cyberpunk · neon-vehicle]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished neon-noir cyberpunk CGI game-engine look: teal-and-magenta lighting, clean CG geometry, restrained neon accents. This is a stylized futuristic action game render, NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. The character and the environment must render in the SAME unified CGI game-engine style — do NOT composite a CGI-looking character onto a photoreal background, and do NOT let the environment read as a real photograph while the character reads as CGI; skin, environment, lighting, and materials all match one consistent render. Keep the environment clean and uncluttered — a few clear light sources and clean geometry, not stacked layers of neon signage, fog, and bloom competing for attention. Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: long balayage hair with neon streaks, full glam, posed beside a neon-underlit motorcycle on a wet street, chrome and carbon bodywork reflecting teal and magenta, headlight glare and light trails, holo-signage overhead — the entire frame rendered in the CGI style described above. Camera: wide low angle, 24mm lens, subject and motorcycle framed off-center to the right. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Neo City. SFW.
```

---

_15 scenes (8 GTA, 7 Cyberpunk). Both style tracks reworked from round-1 feedback — retest
`[gta6 · nightlife]` and `[cyberpunk · street]` each once more to confirm before batching the
remaining 7 GTA and 6 Cyberpunk scenes. Add more by mixing any scene modifier from the skill files
into the same "Now render: ..." pattern, keeping the reference blocks and every guardrail exactly
as written._

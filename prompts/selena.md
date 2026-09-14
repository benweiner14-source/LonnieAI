# Prompt Pack — Selena

New POC creator (third alongside Zion and Kazumi). Ben's ask: GTA mockups, back to this
project's core thesis — the entire frame (character *and* environment) rendered as a full CGI
game-engine shot, not a real photo and not a composited character on a real background.

**Status: not yet test-rendered.** Same validate-before-batch process as every other pack in
this repo — run `[gta6 · nightlife]` first, confirm identity/style/logos/SFW clean, *then*
batch the rest.

**Body ref chosen to avoid Kazumi's GTA safety-filter failure.** Kazumi's GTA scenes lost their
body reference entirely after a revealing outfit combined with "cropped designer top" in the
prompt text tripped Gemini's safety filter on 3/4 seeds. Selena's chosen body ref
(`selena_black_sweats_mirror.jpg`) is a loose, modest oversized-sweats fit specifically to avoid
that failure mode — so this pack starts with the full **3-ref (face + body + style)** recipe
Kazumi's GTA scenes never got to keep. If it also trips the filter, drop the body ref the same
way Kazumi's pack did.

**Her real look (from `refs/`, woven into every prompt):** a young woman with long wavy dark
brunette hair, green/hazel-blue eyes, full glam makeup (sharp winged liner, glossy lips), fair
complexion with light freckles, a nose stud, gold hoop earrings, and layered dainty gold
necklaces (an interlocking-ring pendant + a small sun/star charm). Slim, toned figure.

**One look: FULL CGI RENDER.** Character AND environment both render in the game engine.

**⚠️ Brand safety — no real logos/trademarks.** Describes the *aesthetic only* (open-world
crime-saga neon look), invented place names, no real game/studio/engine name in the prompt
text. The style reference image is a real gameplay screenshot (not cover art) but may still
carry incidental readable text — the style role instructs the model to ignore it.

---

## How to run each prompt
1. Nano Banana Pro (Comfy Cloud "Google Gemini Image" node) or Nano Banana in Higgsfield.
   Aspect ratio **9:16**.
2. Attach the reference images **in the exact order listed** — REFERENCE IMAGE 1/2/3 numbering
   must match upload order. All scenes below use **3 refs: face, body, style**.
3. Paste the prompt text unmodified.
4. Generate 3–4 variants per prompt, keep the best. Verify SFW and no real logos leaked before
   moving to the next scene.

**Reference files used throughout** (all in `creators/selena/refs/` unless noted):
- **Face (identity, every prompt):** `selena_car_daylight_portrait.jpg`
- **Body/figure (every prompt):** `selena_black_sweats_mirror.jpg`
- **Style — GTA VI scenes:** `skills/gta6-style/reference/gtav_skyline_dusk.jpg`

**Reusable role blocks:**
```
FACE — REFERENCE IMAGE: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

STYLE (GTA) — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.
```

**Tags:** `[gta6 · scene]`. Full style DNA in `skills/gta6-style/`.

---

## GTA VI  (`skills/gta6-style/`) — style ref: `gtav_skyline_dusk.jpg` — **3 refs: face + body + style**

**[gta6 · nightlife]** — run this one first
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark brunette hair, green eyes, full glam makeup (winged liner, glossy lips), a nose stud and layered gold necklaces, in a fitted black going-out dress, leaning against a neon-underlit convertible on a night street. Art-deco hotels with exaggerated saturated hot-pink and cyan neon signage, glossy wet reflective asphalt throwing colored bounce light, palm trees strung with oversized string lights, a stylized fictional skyline glowing unnaturally bright in the distance — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph of a real city. Camera: low-angle hero shot, 24mm wide lens, subject off-center to the left, exaggerated foreground-to-background perspective. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · nightlife — club entrance]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a slim young woman with long wavy dark hair, full glam, gold hoop earrings, layered necklaces, in a strapless black bodycon dress and heels stepping out of a club entrance with a velvet rope, neon marquee overhead in pink and purple, valet supercars at the curb, wet street reflecting the signage — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: Dutch angle (10° tilt), 35mm lens, dynamic diagonal energy. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · beach]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark brunette hair, green eyes, full glam makeup, gold hoops and layered necklaces, in a fashionable cover-up and oversized sunglasses walking a boardwalk at golden hour, turquoise ocean, white sand, pastel art-deco buildings, palm trees, a parked convertible — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 24mm lens, subject placed in the right third of frame, ocean horizon visible. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · luxury-car]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, gold jewelry, in a fitted going-out fit and designer sunglasses leaning on the hood of a glossy candy-red supercar convertible at a gas station, palm-lined boulevard behind — chrome and candy paint catching golden-hour reflections, humid skin sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low three-quarter angle, 24mm wide lens, dramatic foreshortening on the car's hood and grille, subject framed beside it. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · penthouse]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops and layered necklaces, in glamorous loungewear at a rooftop infinity pool at dusk, floor-to-ceiling glass, neon skyline reflected in the water, modern designer furniture, palms, warm interior practical light, city-light bokeh in the distance — purple-orange dusk sky, humid sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level wide shot, 28mm lens, subject small in frame with expansive skyline negative space. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · casino]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, layered gold necklaces, in a fitted black lace-up top, walking confidently through a glamorous casino-resort lobby lit by warm gold light and glowing signage, marble floors reflecting the light, an out-of-focus crowd in the background rendered at lower detail — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens, subject slightly off-center, shallow depth of field on the background crowd. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · gaming-room]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 3: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, casual glam makeup, in a cozy oversized top, seated in a plush gaming chair at a streaming setup — multiple monitors glowing with soft ambient light, LED strip lighting in pink and purple along the desk and walls, a headset resting on the desk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. No readable text, logos, or game footage visible on any screen — monitors show only soft abstract glow. Camera: eye-level three-quarter angle, 35mm lens, subject centered-left with the glowing desk setup filling the right side of frame. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

---

## Next up
Run `[gta6 · nightlife]` first, confirm identity/style/logos/SFW clean (same process as Zion and
Kazumi), then batch the remaining 6 scenes. If the body ref trips a safety filter the way
Kazumi's did, drop it and fall back to the 2-ref (face + style) recipe. Once GTA is confirmed,
consider porting Cyberpunk / NBA-adjacent / iPhone Selfie styles for her the same way they were
built for Zion and Kazumi.

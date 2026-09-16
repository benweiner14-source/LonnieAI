# Prompt Pack — Selena

New POC creator (third alongside Zion and Kazumi). Ben's ask: GTA mockups, back to this
project's core thesis — the entire frame (character *and* environment) rendered as a full CGI
game-engine shot, not a real photo and not a composited character on a real background.

**Status: validated.** `[gta6 · nightlife]` + a 5-scene/2-seed Nano Banana Pro batch
(club-entrance, beach, luxury-car, penthouse, casino) confirmed identity and the signage fix
hold up; found and fixed one new leak (real automaker logos/badges on vehicles — see the STYLE
role block below). Face refs were swapped after this validation (see "How to run" below).

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
2. Attach the reference images **in the exact order listed** — REFERENCE IMAGE 1/2/3/4 numbering
   must match upload order. All scenes below use **4 refs: face ×2, body, style** (same
   dual-face-ref pattern as Zion's pack — two angles reinforce identity better than one).
3. Paste the prompt text unmodified.
4. Generate 3–4 variants per prompt, keep the best. Verify SFW and no real logos leaked before
   moving to the next scene — **check vehicles specifically for real automaker badges/logos**,
   not just signage (found leaking on the `club-entrance`/`luxury-car` validation renders).

**Reference files used throughout** (all in `creators/selena/refs/` unless noted):
- **Face (identity, every prompt, both used together):** `selena_gaming_room_pink_chair.png` +
  `selena_skull_tank_vacation.png` — swapped in from the original single face ref
  (`selena_car_daylight_portrait.jpg`) after Ben judged these two as stronger likeness refs
  following the `[gta6 · nightlife]` + 5-scene validation batch.
- **Body/figure (every prompt):** `selena_black_sweats_mirror.jpg`
- **Style — GTA VI scenes:** `skills/gta6-style/reference/gtav_skyline_dusk.jpg`

**Reusable role blocks:**
```
FACE — REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

FACE — REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

STYLE (GTA) — REFERENCE IMAGE: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.
```

**Tags:** `[gta6 · scene]`. Full style DNA in `skills/gta6-style/`.

---

## GTA VI  (`skills/gta6-style/`) — style ref: `gtav_skyline_dusk.jpg` — **3 refs: face + body + style**

**[gta6 · nightlife]** — run this one first
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark brunette hair, green eyes, full glam makeup (winged liner, glossy lips), a nose stud and layered gold necklaces, in a fitted black going-out dress, leaning against a neon-underlit convertible on a night street. Art-deco hotels with exaggerated saturated hot-pink and cyan neon signage, glossy wet reflective asphalt throwing colored bounce light, palm trees strung with oversized string lights, a stylized fictional skyline glowing unnaturally bright in the distance — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph of a real city. Camera: low-angle hero shot, 24mm wide lens, subject off-center to the left, exaggerated foreground-to-background perspective. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · nightlife — club entrance]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a slim young woman with long wavy dark hair, full glam, gold hoop earrings, layered necklaces, in a strapless black bodycon dress and heels stepping out of a club entrance with a velvet rope, neon marquee overhead in pink and purple, valet supercars at the curb, wet street reflecting the signage — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: Dutch angle (10° tilt), 35mm lens, dynamic diagonal energy. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · beach]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark brunette hair, green eyes, full glam makeup, gold hoops and layered necklaces, in a fashionable cover-up and oversized sunglasses walking a boardwalk at golden hour, turquoise ocean, white sand, pastel art-deco buildings, palm trees, a parked convertible — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 24mm lens, subject placed in the right third of frame, ocean horizon visible. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · luxury-car]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, gold jewelry, in a fitted going-out fit and designer sunglasses leaning on the hood of a glossy candy-red supercar convertible at a gas station, palm-lined boulevard behind — chrome and candy paint catching golden-hour reflections, humid skin sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low three-quarter angle, 24mm wide lens, dramatic foreshortening on the car's hood and grille, subject framed beside it. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · penthouse]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops and layered necklaces, in glamorous loungewear at a rooftop infinity pool at dusk, floor-to-ceiling glass, neon skyline reflected in the water, modern designer furniture, palms, warm interior practical light, city-light bokeh in the distance — purple-orange dusk sky, humid sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level wide shot, 28mm lens, subject small in frame with expansive skyline negative space. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · casino]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, layered gold necklaces, in a fitted black lace-up top, walking confidently through a glamorous casino-resort lobby lit by warm gold light and glowing signage, marble floors reflecting the light, an out-of-focus crowd in the background rendered at lower detail — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens, subject slightly off-center, shallow depth of field on the background crowd. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

**[gta6 · gaming-room]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, casual glam makeup, in a cozy oversized top, seated in a plush gaming chair at a streaming setup — multiple monitors glowing with soft ambient light, LED strip lighting in pink and purple along the desk and walls, a headset resting on the desk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. No readable text, logos, or game footage visible on any screen — monitors show only soft abstract glow. Camera: eye-level three-quarter angle, 35mm lens, subject centered-left with the glowing desk setup filling the right side of frame. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

---

## Variants & new locations (working toward ~50 total)

**Status: drafted, fully self-contained, mostly un-rendered.** Ben's ask: build toward a
~50-scene pack by reusing the 7 confirmed locations above (nightlife, club-entrance, beach,
luxury-car, penthouse, casino, gaming-room) as a base, adding 4 new Florida-lifestyle locations
(jet-ski, marina, helicopter, poolside-cabana) plus 2 more (golf-course, fishing-charter) — 13
locations total — then giving each location ~4 variants (camera angle/lens, pose, outfit).
13 × 4 = 52.

**These come from real-world Florida lifestyle imagery (jet skis, marinas, golf, fishing,
helicopters) — deliberately NOT sourced from any GTA VI trailer or other copyrighted game
footage**, per the standing brand-safety rule and to avoid any risk of reproducing someone else's
copyrighted material.

**Each variant below is a complete, paste-ready prompt** — its own REFERENCE IMAGE 1–4 block
plus "Now render" text, nothing to prepend. This is a deliberate change from the pack's original
format (which had scenes reference a shared block above to avoid duplicating identical text):
these 6 new locations needed a broadened STYLE clause (vehicles **and** watercraft/aircraft,
since jet skis/boats/a helicopter are now in the pack) that the shared block doesn't carry, so
duplicating it into every scene was the more reliable option. **When the STYLE wording needs
another fix, update it everywhere it appears** — the reusable block at the top (used by the
original 7 base-A scenes), plus every variant block below (all 48, since each is now
self-contained) — grep for the distinctive opening phrase ("cinematic teal-and-orange grade,
moderate and realistic dewy skin sheen") to find every occurrence.

**Validation status:** `nightlife`, `luxury-car`, `jet-ski`, and `helicopter` base-A renders are
confirmed working with this exact tightened wording (Ben: "yep solid" / "yep looks goos" on
2026-09-16) — identity, style consistency, and brand safety all checked out. **None of the other
48 variants below have been rendered yet** — same validate-before-batch process as every style in
this repo before trusting a full run.

### nightlife — variants B/C/D
```
[gta6 · nightlife-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark brunette hair, green eyes, full glam makeup, gold jewelry, in an off-shoulder red going-out dress, walking down the middle of a rain-slicked neon street at night, glancing back over her shoulder, art-deco hotel signage glowing behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: telephoto compression, 85mm lens, subject centered but background heavily compressed and blurred. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · nightlife-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, gold hoops, in a high-slit black dress, seated on the hood of a parked sports car (invented/generic design) on a neon-lit street, one leg crossed over the other — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low wide-angle from street level, 20mm lens, exaggerated foreground-to-background perspective. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · nightlife-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, layered necklaces, in a fitted metallic mini dress, standing in a neon-lit doorway silhouetted from behind by a bar's glowing entrance — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: medium telephoto, 50mm lens, dramatic rim lighting, subject off-center. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### club-entrance — variants A/B/C/D
```
[gta6 · club-entrance-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a slim young woman with long wavy dark hair, full glam, gold hoop earrings, layered necklaces, in a strapless black bodycon dress and heels stepping out of a club entrance with a velvet rope, neon marquee overhead in pink and purple, valet supercars at the curb, wet street reflecting the signage — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: Dutch angle (10° tilt), 35mm lens, dynamic diagonal energy. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · club-entrance-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops, in a sequined mini dress, posing against a velvet rope under a neon marquee as if for photographers, hand on hip — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: close medium shot, 35mm lens, hard flash-lit look with sharp falloff. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · club-entrance-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, layered necklaces, in a fringe party dress, mid-laugh, an out-of-focus friend blurred beside her at lower render detail, valet supercars (invented/generic design) at the curb — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high candid angle, 24mm lens, dynamic off-center framing. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · club-entrance-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold jewelry, in a satin slip dress, checking her phone under a glowing marquee, neon reflections on the wet sidewalk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level wide shot, 28mm lens, subject off-center to the right. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### beach — variants A/B/C/D
```
[gta6 · beach-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark brunette hair, green eyes, full glam makeup, gold hoops and layered necklaces, in a fashionable cover-up and oversized sunglasses walking a boardwalk at golden hour, turquoise ocean, white sand, pastel art-deco buildings, palm trees, a parked convertible — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 24mm lens, subject placed in the right third of frame, ocean horizon visible. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · beach-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, a wide sunhat, sitting on a raised lifeguard-stand-style perch overlooking turquoise water, oversized sunglasses — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide low-angle from the sand, 24mm lens, dramatic sky filling the upper frame. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · beach-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold hoops, in a flowing white maxi dress, walking barefoot along the shoreline where wet sand meets surf — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: telephoto compression from a distance, 85mm lens, subject small in frame, ocean and sky compressed behind her. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · beach-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, layered necklaces, in a retro-print sundress, leaning on a beach-cruiser bicycle (invented/generic design, no real brand markings) on the boardwalk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens, subject slightly off-center. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### luxury-car — variants B/C/D
```
[gta6 · luxury-car-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, sunglasses, seated in the driver's seat of a glossy convertible (invented/generic design) with one arm resting on the open window frame, palm-lined street behind — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low three-quarter angle from the front bumper, 24mm lens, dramatic foreshortening. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · luxury-car-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, gold jewelry, in a fitted jumpsuit, standing beside a parked matte-black sports car (invented/generic design) at a scenic coastal overlook with a bridge/causeway in the background at dusk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 20mm lens, subject and car both small against the expansive skyline. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · luxury-car-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops, loading a designer bag into the open trunk of a glossy sports car (invented/generic design), glancing back playfully over her shoulder — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: medium telephoto, 50mm lens, subject off-center. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### penthouse — variants A/B/C/D
```
[gta6 · penthouse-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops and layered necklaces, in glamorous loungewear at a rooftop infinity pool at dusk, floor-to-ceiling glass, neon skyline reflected in the water, modern designer furniture, palms, warm interior practical light, city-light bokeh in the distance — purple-orange dusk sky, humid sheen — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level wide shot, 28mm lens, subject small in frame with expansive skyline negative space. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · penthouse-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold jewelry, in a silk robe, leaning on a rooftop balcony railing overlooking a glowing skyline at dusk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: medium close shot, 50mm lens, soft rim light from the skyline. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · penthouse-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, in patterned resortwear, seated on an outdoor daybed at sunset, floor-to-ceiling glass and city lights visible behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high angle from just inside the room looking out, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · penthouse-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops, in a fitted evening dress, standing at a floor-to-ceiling window from inside a penthouse with the city skyline reflected in the glass — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: symmetrical wide shot, 28mm lens, subject centered against the reflected skyline. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### casino — variants A/B/C/D
```
[gta6 · casino-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, layered gold necklaces, in a fitted black lace-up top, walking confidently through a glamorous casino-resort lobby lit by warm gold light and glowing signage, marble floors reflecting the light, an out-of-focus crowd in the background rendered at lower detail — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens, subject slightly off-center, shallow depth of field on the background crowd. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · casino-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold jewelry, in a sequined gown, leaning against a marble pillar near rows of glowing slot machines rendered at low detail in the background — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low-angle glam shot, 35mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · casino-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, layered necklaces, in an elegant jumpsuit, seated in a private high-stakes lounge booth, warm gold ambient light — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 50mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · casino-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops, in a dramatic ballgown, walking up a grand marble staircase under a glowing chandelier — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide low-angle from the base of the staircase, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### gaming-room — variants A/B/C/D
```
[gta6 · gaming-room-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, casual glam makeup, in a cozy oversized top, seated in a plush gaming chair at a streaming setup — multiple monitors glowing with soft ambient light, LED strip lighting in pink and purple along the desk and walls, a headset resting on the desk — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. No readable text, logos, or game footage visible on any screen — monitors show only soft abstract glow. Camera: eye-level three-quarter angle, 35mm lens, subject centered-left with the glowing desk setup filling the right side of frame. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · gaming-room-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, casual glam, a headset resting around her neck, reacting mid-laugh at her streaming desk — monitors show only soft abstract glow, no readable text or logos — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: close three-quarter angle, 50mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · gaming-room-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, casual glam, in an oversized hoodie, standing and stretching beside her gaming desk, pink/purple LED strip lighting along the walls — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level wide shot, 28mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · gaming-room-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names (e.g. no "Ocean Drive," no real Miami/city street or district names) as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle in the scene must have an invented/generic design — no real automaker logos, badges, grille emblems, or model-identifying details (e.g. no Ford, Audi, or other real car-brand markings). Ignore and do NOT reproduce any logos, vehicle brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, casual glam, in cozy loungewear, sitting cross-legged on the floor with a controller (invented/generic design, no real brand markings), gaming desk glowing softly behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high overhead-leaning angle, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### jet-ski — variants A/B/C/D
```
[gta6 · jet-ski-A] — confirmed working (Ben: "yep looks good")
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Yamaha, Sea-Doo, Ford, Audi, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold hoop earrings, layered necklaces, in a fitted athletic one-piece swimsuit with full coverage under an open zip-up rash guard, riding a jet ski (invented/generic design) across turquoise open water, spray kicking up behind her, a distant marina and pastel skyline visible on the horizon — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low-angle tracking shot from just above the waterline, 24mm wide lens, motion-blurred spray in the foreground, subject off-center to the right. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · jet-ski-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in the same full-coverage athletic swimsuit, idling on a jet ski near a wooden dock, one leg draped over the side, sunglasses pushed up on her head — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · jet-ski-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a full-coverage athletic swimsuit, mid-turn on a jet ski kicking up a wide spray arc, open water and coastline behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: dynamic wide-angle from a chase-boat perspective, 20mm lens, motion blur on the spray. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · jet-ski-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a swim cover-up over a full-coverage swimsuit, walking away from a parked jet ski on the shoreline toward the beach, looking back over her shoulder — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### marina — variants A/B/C/D
```
[gta6 · marina-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, gold jewelry, in a flowing sundress, walking along a wooden marina boardwalk lined with docked yachts and sailboats (invented/generic designs), golden-hour light glinting off the water, palm trees swaying, a pastel skyline in the distance — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high-angle three-quarter shot from an elevated dock walkway, 35mm lens, subject small in frame with rows of boats filling the background. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · marina-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a casual sundress, seated on a dock piling with her legs dangling above the water, boats moored behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low eye-level shot, 35mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · marina-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops, in elegant resortwear, stepping onto a yacht's boarding ramp (invented/generic design), marina and skyline behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: three-quarter angle, 28mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · marina-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, layered necklaces, standing at a marina railing at blue-hour dusk, string lights strung overhead, boats gently lit behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: medium telephoto, 50mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### helicopter — variants A/B/C/D
```
[gta6 · helicopter-A] — confirmed working (Ben: "yep looks good")
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam makeup, gold hoops and layered necklaces, in a fitted going-out fit, stepping off a sleek private helicopter (invented/generic design) onto a rooftop helipad at dusk, her hair caught in the rotor wash, a sprawling glowing city skyline spread out below and behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low three-quarter angle looking slightly up past the helicopter's skid toward her, 28mm wide lens, dramatic rim lighting from the skyline glow. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · helicopter-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, seated inside a helicopter cabin (invented/generic design, no visible instrument branding) looking out the window, a glowing city skyline visible far below — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: medium close shot, 35mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · helicopter-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold jewelry, standing beside a parked helicopter (invented/generic design) on a rooftop tarmac, hair windswept, dusk skyline behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide low-angle, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · helicopter-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, walking away from a parked helicopter toward a rooftop lounge area, dusk skyline glowing behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: telephoto compression, 85mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### poolside-cabana — variants A/B/C/D
```
[gta6 · poolside-cabana-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold jewelry, in a stylish swim cover-up over a full-coverage one-piece swimsuit, lounging at a poolside cabana under bright midday sun, rattan furniture, tropical drinks on a side table, palm trees and a resort building in the background — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 50mm lens, warm bright daylight grading (a deliberate contrast to the pack's usual neon-night look), subject off-center to the left. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · poolside-cabana-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a wide sunhat and full-coverage swim cover-up, standing at the pool's edge about to dip a foot in, bright midday light — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide bright daylight shot, 28mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · poolside-cabana-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a full-coverage swim cover-up, reading on a lounge chair under a cabana umbrella, relaxed pose — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 50mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · poolside-cabana-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold hoops, in a full-coverage swim cover-up, walking along the pool deck with a towel draped over one shoulder, bright midday sun — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high-angle bright shot, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### golf-course — variants A/B/C/D
```
[gta6 · golf-course-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold jewelry, in a polished golf-casual outfit (fitted polo and pleated skirt), teeing off on a manicured fairway, palm trees lining the course, a clubhouse visible in the distance, soft morning light — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide establishing shot, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · golf-course-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a casual-chic outfit, riding in a golf cart (invented/generic design) along a tree-lined cart path — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · golf-course-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, gold hoops, in an elegant resort-casual dress, standing on a clubhouse veranda overlooking the green, midday light — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: high angle, 28mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · golf-course-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a golf visor and casual sport outfit, walking across a small bridge over a water hazard on the course — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: telephoto compression, 85mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

### fishing-charter — variants A/B/C/D
```
[gta6 · fishing-charter-A]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold jewelry, in a sporty boating outfit, standing at the helm of a charter fishing boat (invented/generic design, rod holders visible), open ocean at sunset — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: low three-quarter angle, 24mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · fishing-charter-B]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, in a sporty boating outfit, reeling in a fishing line at the boat's stern, focused expression, open water behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: wide-angle action shot, 20mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · fishing-charter-C]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, glam makeup, gold hoops, in a casual boating outfit and sunglasses, relaxing on the boat's bow, open ocean and sky behind her — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: eye-level medium shot, 35mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.

[gta6 · fishing-charter-D]
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, and glam makeup style. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 2: use ONLY for facial identity and likeness, alongside Reference Image 1 — a second angle of the same face to reinforce her exact likeness. Ignore the clothing, pose, and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions and figure — her slim, toned silhouette. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished open-world crime-saga CGI game-engine look: cinematic teal-and-orange grade, moderate and realistic dewy skin sheen — subtle highlights only, NOT heavy oily/sweaty specular, NOT flat or matte skin either, clean CG geometry with full 3D volumetric shading and lighting throughout — NOT flat 2D cel-shaded or toon-shaded rendering, exaggerated cinematic lighting. This is a stylized open-world action game render, obviously computer-generated and in-engine — NOT a real photograph, NOT a real-world location. NOT a Disney/Pixar/DreamWorks animated movie style — NOT cartoon-stylized, NOT storybook or toy-like, NOT cute/rounded/exaggerated proportions. Realistic human anatomical proportions. Do not render any real-world neighborhood, street, or place names as legible signage or text anywhere in the output — any signage must be invented, generic, or illegible only. Any vehicle, watercraft, or aircraft in the scene must have an invented/generic design — no real brand logos, badges, or model-identifying details (e.g. no Ford, Audi, Yamaha, Sea-Doo, Bell, Robinson, or other real vehicle-brand markings). Ignore and do NOT reproduce any logos, brand names, readable signage/text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a young woman with long wavy dark hair, full glam, layered necklaces, standing on deck as the charter boat docks at a pier at golden hour, an out-of-focus crew member at lower render detail in the background — the entire frame rendered in the CGI style described above, obviously computer-generated, in-engine, NOT a real photograph. Camera: telephoto compression, 85mm lens. No real game, studio, or brand logos or trademarks anywhere in the output. 9:16 vertical. Fully clothed, SFW.
```

## Next up
**Recipe locked and validated (4-ref: face ×2 + body + style)** — tightened STYLE wording (skin
sheen/shading fix) plus the automaker-logo fix and its broadened watercraft/aircraft variant for
the new locations. `nightlife`, `luxury-car`, `jet-ski`, and `helicopter` base-A scenes are all
confirmed working with this exact recipe. **The remaining 48 variants below are drafted and
paste-ready but entirely un-rendered** — same validate-then-batch process as the rest of this
repo before trusting a full run: run a couple more spot-checks (e.g. one each of `marina`,
`poolside-cabana`, `golf-course`, `fishing-charter` — the 4 locations with zero renders so far),
then batch the rest.
Body ref hasn't tripped a safety filter for her the way Kazumi's did — if it ever does, drop it
and fall back to the 3-ref (face ×2 + style) recipe. Once the full 52-scene pack is confirmed,
consider porting Cyberpunk / NBA-adjacent / iPhone Selfie styles for her the same way they were
built for Zion and Kazumi.

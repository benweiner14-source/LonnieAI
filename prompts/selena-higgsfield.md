# Prompt Pack — Selena (Higgsfield, simple single-paragraph format)

**This is the "just mess around in Higgsfield" version.** No `REFERENCE IMAGE 1 / 2 / 3...`
role-tagging — just one flowing descriptive paragraph per scene. For the full-control version
with explicit multi-image role assignment (Comfy Cloud / Nano Banana Pro), use `prompts/selena.md`
instead — same 7 scenes, same guardrails, just wired for a tool that actually honors multiple
tagged reference images.

**How to run in Higgsfield:**
- **Attach one photo** — `creators/selena/refs/selena_gaming_room_pink_chair.png` or
  `selena_skull_tank_vacation.png` for identity (swapped in after Ben judged these two as
  stronger face refs than the original `selena_car_daylight_portrait.jpg` — Higgsfield only
  reliably uses one attached image, so pick whichever of the two reads as the stronger likeness
  for a given seed), or `selena_black_sweats_mirror.jpg` if you want her figure/silhouette to
  drive the reference instead.
- Paste the prompt text below unmodified. Generate a few seeds, keep the best, and check for any
  real logo/text leakage before using — **including on vehicles** (see below).

**Non-negotiable in every prompt:** strictly SFW / brand-safe (glam but clothed — no nudity or
explicit posing), no real game/studio/brand logos or trademarks, 9:16 vertical, obviously
CGI/in-engine — not a photograph, and not a Disney/Pixar/animated-movie look. **No real-world
place names as legible signage** — the Nano Banana Pro test on `nightlife` rendered "Ocean
Drive" (a real Miami street) as readable signage unprompted; if a scene starts showing real
street/neighborhood names, add "no real-world street or neighborhood names as legible text,
invented or illegible signage only" to that prompt. **No real automaker logos on vehicles** —
the Comfy/Nano Banana Pro validation batch rendered a real Ford Mustang grille badge and an Audi
rings badge unprompted on `luxury-car`/`club-entrance`; if a car-heavy scene leaks a real
automaker logo, add "invented/generic car design, no real automaker logos or badges" to that
prompt.

**Camera variety:** every scene ends with a specific angle + lens/focal-length + framing note
(low/high/Dutch angles, 24mm wide through 35mm, off-center framing) instead of a generic
centered "hero shot" — same standing rule as the Zion/Kazumi packs.

---

## GTA VI

**[gta6 · nightlife]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, a young woman with long wavy dark brunette hair, green eyes, full glam makeup (winged liner, glossy lips), a nose stud and layered gold necklaces, in a fitted black going-out dress, leaning against a neon-underlit convertible on a night street. Art-deco hotels with exaggerated saturated hot-pink and cyan neon signage, glossy wet reflective asphalt, palm trees strung with oversized string lights, a stylized fictional skyline glowing in the distance, all rendered in-engine. Cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. Camera: low-angle hero shot, 24mm wide lens, subject off-center to the left, exaggerated foreground-to-background perspective. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

**[gta6 · nightlife — club entrance]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, long wavy dark hair, full glam, gold hoop earrings, layered necklaces, in a strapless black bodycon dress and heels, stepping out of a club entrance with a velvet rope. Neon marquee overhead in pink and purple, valet supercars at the curb, wet street reflecting the signage, all rendered in-engine. Cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. Camera: Dutch angle (10° tilt), 35mm lens, dynamic diagonal energy. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

**[gta6 · beach]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, long wavy dark brunette hair, green eyes, full glam makeup, gold hoops and layered necklaces, in a fashionable cover-up and oversized sunglasses, walking a boardwalk at golden hour. Turquoise ocean, white sand, pastel art-deco buildings, palm trees, a parked convertible, all rendered in-engine. Cinematic teal-and-orange grade, humid skin sheen, wet specular reflections, clean CG geometry. Camera: wide establishing shot, 24mm lens, subject placed in the right third of frame, ocean horizon visible. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

**[gta6 · luxury-car]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, long wavy dark hair, full glam makeup, gold jewelry, in a fitted going-out fit and designer sunglasses, leaning on the hood of a glossy candy-red supercar convertible at a gas station, palm-lined boulevard behind. Chrome and candy paint catching golden-hour reflections, humid skin sheen, all rendered in-engine. Cinematic teal-and-orange grade, wet specular reflections, clean CG geometry. Camera: low three-quarter angle, 24mm wide lens, dramatic foreshortening on the car's hood and grille, subject framed beside it. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

**[gta6 · penthouse]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, long wavy dark hair, full glam, gold hoops and layered necklaces, in glamorous loungewear, at a rooftop infinity pool at dusk. Floor-to-ceiling glass, neon skyline reflected in the water, modern designer furniture, palms, warm interior practical light, city-light bokeh in the distance, purple-orange dusk sky, humid sheen, all rendered in-engine. Cinematic teal-and-orange grade, wet specular reflections, clean CG geometry. Camera: eye-level wide shot, 28mm lens, subject small in frame with expansive skyline negative space. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

**[gta6 · casino]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, long wavy dark hair, full glam makeup, layered gold necklaces, in a fitted black lace-up top, walking confidently through a glamorous casino-resort lobby lit by warm gold light and glowing signage. Marble floors reflecting the light, an out-of-focus crowd in the background at lower render detail, all rendered in-engine. Cinematic teal-and-orange grade, humid skin sheen, clean CG geometry. Camera: eye-level medium shot, 35mm lens, subject slightly off-center, shallow depth of field on the background crowd. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

**[gta6 · gaming-room]**
```
Open-world crime-saga video game cutscene screenshot, full in-engine render of character and environment. Selena, long wavy dark hair, casual glam makeup, in a cozy oversized top, seated in a plush gaming chair at a streaming setup. Multiple monitors glowing with soft ambient light, LED strip lighting in pink and purple along the desk and walls, a headset resting on the desk, all rendered in-engine — no readable text, logos, or game footage visible on any screen, monitors show only soft abstract glow. Cinematic teal-and-orange grade, clean CG geometry. Camera: eye-level three-quarter angle, 35mm lens, subject centered-left with the glowing desk setup filling the right side of frame. 9:16 vertical. stylized open-world action game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real game, studio, or brand logos or trademarks anywhere in the output. Fully clothed, SFW.
```

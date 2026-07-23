# Prompt Pack — Zion Clark

Paste-ready Higgsfield **GPT Image 2** prompts. Styles: **NBA 2K** and **WWE 2K**.
Grounded sports-game realism (see `creators/zion-clark/profile.md`).

**Authentic representation (read first):** Zion was **born without legs** (caudal regression
syndrome). Depict him **authentically and heroically** — powerful upper body and core, moving
on his **hands** or in a **racing wheelchair**. **Do NOT generate fabricated legs or a standing
figure.** He is the hero of every frame: elite, dignified, motivational.

**His real look (from `refs/`, woven into the prompts below):** a muscular Black adaptive
athlete, **medium-length dreadlocks often in a top-knot**, full short beard, **gold chain with
a cross pendant**, **chest/collarbone tattoos**, and a bold **"NO EXCUSES" tattoo across his
upper back/shoulders**; often in his own **"Z" lightning "No Excuses"** branded gear
(purple/gold/black), or shirtless training.

**How to run each prompt**
1. Higgsfield → GPT Image 2 → aspect ratio **9:16**, resolution 2k, quality high.
2. **Bind his identity:** attach a clean reference photo (image-to-image) or, better, use the
   Higgsfield **`<<<token>>>`** — the id of an attached ref image or a trained **Soul ID** on
   his `refs/`. Where a prompt says `Zion`, you can replace it with your real `<<<uuid>>>`.
3. Generate 2–3 variants, keep the best. Verify the body is represented authentically.

**⚠️ Getting a CGI character, not a photo.** GPT Image 2 in img2img tends to keep the real
photo looking real. The goal is an obvious **CGI game character**. If output is too photoreal,
follow **`docs/forcing-the-cgi-look.md`** — short version: train a **Soul ID** and use
text-to-image (not img2img), or lower img2img strength; attach a 2K screenshot as a style
reference; and **append the CGI-enforcement block** below. Do **not** add "face-scanned
maximum fidelity / skin pores / broadcast realism" — those pull it back to photo.

**CGI-enforcement block (append to any prompt that comes out too real):**
```
— rendered as a 3D CGI video-game character, NOT a photograph, NOT photorealistic. Real-time game-engine render (PS5 / Unreal Engine cutscene). Smooth waxy subsurface-scattering skin with a subtle plastic sheen, slightly simplified pores, clean CG geometry, rendered hair, ambient occlusion. The subject must read as a stylized computer-generated character model, obviously CGI — like a playable video-game character, not a real person.
```

**Tags:** `[style · scene · look]`. **look** = `full-render` (all in-engine) or
`cgi-in-scene` (stylized character on a photoreal backdrop). Full style detail in
`skills/nba2k-style/` and `skills/wwe2k-style/`.

> v2 — tuned to scraped refs in `creators/zion-clark/refs/`.

---

## NBA 2K  (`skills/nba2k-style/`)

**[nba2k · gym · full-render]**
```
2K Sports video game cutscene screenshot. Zion, a muscular Black adaptive athlete born without legs with medium-length dreadlocks pulled back and a short beard, powerful defined upper body and core, supporting himself on his hands mid-training on the gym floor, chalked palms, gold chain, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting. Real-time 3D render, plastic sheen and sweat specular on forehead, shoulders, and arms, decal tattoos, simplified dreadlock texture, warm amber skin. Low-angle hero framing, rim light, shallow DOF on background. Warm slightly desaturated palette, clean geometry, no grain. 9:16 vertical. NBA 2K cutscene aesthetic. Based on the likeness and framing of the provided reference photo. Represent his body authentically — no fabricated legs.
```

**[nba2k · gym · full-render — back / NO EXCUSES tattoo]**
```
2K Sports cutscene screenshot. Zion, a muscular Black adaptive athlete born without legs, seen from behind seated on the gym floor, powerful back and shoulders showing the bold "NO EXCUSES" tattoo across his upper back, medium-length dreadlocks, in a bright modern gym with heavy bags and equipment blurred behind. Real-time 3D render, sweat specular on skin, plastic subsurface sheen, decal tattoos, clean geometry. Contemplative hero framing, rim light. Warm slightly desaturated palette, no grain. 9:16 vertical. NBA 2K aesthetic. Based on the provided reference photo. Authentic body — born without legs, no fabricated legs.
```

**[nba2k · gym · cgi-in-scene]**
```
NBA 2K / 2K Sports style. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and a short beard, supporting himself on his hands during an upper-body workout, gold chain. Subject rendered as a stylized 2K game character — plastic sheen, sweat specular, decal tattoos — composited into a photorealistic real-world gym backdrop with racks and equipment. Warm even light, low-angle hero framing. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Represent his body authentically — no fabricated legs.
```

**[nba2k · training-facility · full-render]**
```
2K Sports cutscene screenshot. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back, training with battle ropes, gripping and slamming them from a seated hand-supported position, powerful shoulders and back, gold chain, turf floor, branded padded walls, staff in athletic wear at low detail behind, bright facility lighting. Real-time 3D render, heavy sweat specular, plastic sheen, decal tattoos, clean geometry, warm amber skin. Hero framing, rim light. 9:16 vertical. NBA 2K aesthetic. Based on the provided reference photo. Authentic body — no fabricated legs.
```

**[nba2k · training-facility · cgi-in-scene]**
```
NBA 2K style. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, in an intense training moment, upper body straining, on a performance turf floor. Subject rendered as a stylized 2K game character composited into a photorealistic real-world training-facility backdrop with branded padding and equipment. Sweat specular, plastic sheen, decal tattoos. Low-angle hero framing, rim light. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Represent his body authentically — no fabricated legs.
```

**[nba2k · track · full-render]**
```
2K Sports video game cutscene screenshot. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, in a racing wheelchair on an outdoor stadium track, gripping the push rims mid-sprint, powerful arms and shoulders, aerodynamic racing gloves and helmet, red synthetic track lanes with crisp white lines, lightly populated grandstands at reduced detail, bright natural daylight, blue sky, sponsor banners. Real-time 3D render, sweat specular, plastic sheen, decal tattoos, clean geometry, broadcast-quality lighting. Low-angle hero framing down the lane. 9:16 vertical. NBA 2K aesthetic. Based on the provided reference photo. Authentic adaptive athlete — racing wheelchair, no fabricated legs.
```

**[nba2k · track · full-render]**
```
2K Sports cutscene screenshot. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and a short beard, at the start line in his racing wheelchair, coiled and ready, intense focus, gold chain, stadium track and grandstands behind, bright daylight. Real-time 3D render, plastic sheen and sweat specular, decal tattoos, clean geometry. Dramatic low-angle hero framing. 9:16 vertical. NBA 2K aesthetic. Based on the provided reference photo. Racing wheelchair, authentic body, no fabricated legs.
```

**[nba2k · track · cgi-in-scene]**
```
NBA 2K style. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, sprinting in his racing wheelchair, arms driving the push rims. Subject rendered as a stylized 2K game character — plastic sheen, sweat specular, decal tattoos — composited into a photorealistic real-world stadium-track backdrop, red lanes, grandstands, daylight. Low-angle hero framing down the lane. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Racing wheelchair, no fabricated legs.
```

**[nba2k · portrait · full-render]**
```
2K Sports broadcast close-up portrait. Zion, a muscular Black adaptive athlete with medium-length dreadlocks pulled back, short beard, and gold chain, at maximum rendering fidelity, intense determined expression, plastic sheen and sweat specular on forehead and shoulders, decal tattoos on arms and neck, black "No Excuses" compression top, shallow depth of field with a blurred facility behind, dramatic broadcast lighting. 9:16 vertical. NBA 2K aesthetic. Based on the provided reference photo. Upper-body hero portrait, authentic representation.
```

**[nba2k · portrait · cgi-in-scene]**
```
NBA 2K style. A powerful upper-body hero portrait of Zion — dreadlocks pulled back, short beard, gold chain, determined gaze. Subject rendered as a stylized 2K game character — plastic sheen, sweat specular, decal tattoos — composited onto a photorealistic real-world gym backdrop with shallow depth of field. Dramatic rim light. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Authentic representation.
```

### Signature moments (exact-gesture, photoreal-leaning)
_Model on your Brunson-celebration prompt: name the pose precisely, add `(see ref images)`,
lean photoreal. Replace `<<<ZION>>>` with your Higgsfield token._

**[nba2k · signature · chalk-clap · photoreal]**
```
NBA 2K broadcast close-up. <<<ZION>>>, a muscular Black adaptive athlete born without legs with medium-length dreadlocks in a top-knot, full short beard, and a gold chain with a cross pendant, clapping both chalked hands together in front of his chest to explode a burst of white chalk dust into the air, arms flexed, mouth open in an intense fired-up yell, eyes locked forward (see ref images). Chest and collarbone tattoos visible, shirtless or in a black "No Excuses" cutoff, sweat specular sheen on shoulders and forehead. Gym backdrop blurred into shallow depth of field, dramatic rim light. Rendered as a 3D CGI video-game character, NOT a photograph — real-time game-engine cutscene render, smooth waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion; obviously computer-generated, like a playable NBA 2K character model. Warm slightly desaturated palette, no film grain. 9:16 vertical. NBA 2K26 MyCAREER cutscene aesthetic. Authentic body — no fabricated legs.
```

**[nba2k · signature · double-flex · photoreal]**
```
NBA 2K broadcast close-up. <<<ZION>>>, a muscular Black adaptive athlete born without legs with dreadlocks pulled back and a full beard, supported on one hand while raising the other arm in a hard double-take flex — bicep peaked, veins showing, fist clenched, jaw set in a roaring intense expression (see ref images). "NO EXCUSES" tattoo across his upper back catching the light, gold cross chain, sweat specular on skin. Dark moody gym, hard rim and key light, shallow depth of field. Rendered as a 3D CGI video-game character, NOT a photograph — real-time game-engine cutscene render, smooth waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion; obviously computer-generated, like a playable NBA 2K character model. Clean geometry, no film grain. 9:16 vertical. NBA 2K26 MyCAREER cutscene aesthetic. Authentic body — no fabricated legs.
```

---

## WWE 2K  (`skills/wwe2k-style/`)

**[wwe2k · entrance · full-render]**
```
WWE 2K video game screenshot, 2K sports engine, in-game render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back and a short beard, powerful oiled upper body, entering on his hands onto the entrance stage, arms mid-stride, intense heroic face, custom "No Excuses" entrance gear, gold chain. Giant LED video wall glowing behind (purple and gold), cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail. Oiled muscular specular sheen, plastic face sheen, decal tattoos, simplified dreadlock texture. Hard colored stage lighting, strong rim light against black arena, high contrast. Low-angle hero framing, poster-like. Clean geometry, no grain. 9:16 vertical. WWE 2K aesthetic. Based on the likeness and framing of the provided reference photo. Authentic body — no fabricated legs.
```

**[wwe2k · entrance · full-render — silhouette]**
```
WWE 2K screenshot, 2K sports engine, in-game render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, backlit in silhouette at the top of the entrance ramp, arms raised, the "NO EXCUSES" back tattoo catching the rim light, purple-and-gold pyro erupting, LED wall blazing, haze and follow-spots, roaring dark crowd below at low detail. Oiled muscle rim light, plastic sheen, decal tattoos. Epic low-angle hero framing. High contrast, saturated stage beams against black. 9:16 vertical. WWE 2K aesthetic. Based on the provided reference photo. Authentic body, no fabricated legs.
```

**[wwe2k · entrance · cgi-in-scene]**
```
WWE 2K style. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, making a dramatic entrance, powerful oiled upper body, arms raised, gold chain. Subject rendered as a stylized WWE 2K game character composited into a photorealistic real-world arena backdrop — LED wall, purple/gold pyro, spotlight haze, dark crowd. Oiled specular sheen, decal tattoos, strong rim light. Low-angle hero framing. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Authentic body — no fabricated legs.
```

**[wwe2k · ring · full-render]**
```
WWE 2K screenshot, 2K sports engine, in-game render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back, center-ring on the canvas, supported on his hands in a commanding heroic pose, ropes and padded turnbuckles around, championship logos on the mat, dark arena crowd at reduced detail, overhead truss lighting. Oiled muscular sheen catching the lights, plastic face sheen, decal tattoos including "NO EXCUSES" across the back, clean geometry. Dramatic framing, strong rim light. 9:16 vertical. WWE 2K aesthetic. Based on the provided reference photo. Authentic body, no fabricated legs.
```

**[wwe2k · ring · cgi-in-scene]**
```
WWE 2K style. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, in a commanding pose on the ring canvas, powerful upper body. Subject rendered as a stylized WWE 2K game character composited into a photorealistic real-world ring-and-arena backdrop — ropes, turnbuckles, dark crowd, truss lighting. Oiled specular, decal tattoos, dramatic rim light. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Authentic body, no fabricated legs.
```

**[wwe2k · victory · full-render]**
```
WWE 2K screenshot, 2K sports engine, in-game render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, raised on top of a turnbuckle balanced on his hands, arms and torso in a triumphant victory pose, "NO EXCUSES" back tattoo visible, backlit by purple-and-gold stage lighting and pyro, dark roaring crowd below at low fidelity, championship belt on the mat. Oiled muscle rim light, plastic sheen, decal tattoos, clean geometry. Epic low-angle hero framing. 9:16 vertical. WWE 2K aesthetic. Based on the provided reference photo. Authentic body — no fabricated legs.
```

**[wwe2k · victory · cgi-in-scene]**
```
WWE 2K style. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, in a triumphant victory pose, arms raised, backlit by pyro. Subject rendered as a stylized WWE 2K game character composited into a photorealistic real-world arena backdrop with a dark roaring crowd and purple/gold stage lighting. Oiled specular, decal tattoos, dramatic rim light, saturated colored beams. Epic low-angle hero framing. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Authentic body, no fabricated legs.
```

**[wwe2k · dramatic-gym · full-render]**
```
WWE 2K screenshot, 2K sports engine, in-game render. A dark, moody gym lit like a WWE 2K scene — hard rim and colored spotlights on Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, mid-lift supported on his hands, gold chain, equipment in deep shadow, saturated purple accent lighting, high-contrast heroic framing. Oiled specular sheen, plastic face sheen, decal tattoos, clean geometry. 9:16 vertical. WWE 2K aesthetic. Based on the provided reference photo. Authentic body, no fabricated legs.
```

**[wwe2k · portrait · full-render]**
```
WWE 2K broadcast close-up. Zion, a muscular Black adaptive athlete with medium-length dreadlocks pulled back, short beard, and gold chain, at maximum fidelity, intense expression, oiled skin with strong specular and sweat highlights, decal tattoos, championship belt over the shoulder, dark arena bokeh behind with purple/gold stage-light glow, dramatic lighting. 9:16 vertical. WWE 2K aesthetic. Based on the provided reference photo. Upper-body hero portrait, authentic representation.
```

**[wwe2k · portrait · cgi-in-scene]**
```
WWE 2K style. A dramatic upper-body hero portrait of Zion — dreadlocks pulled back, short beard, gold chain, intense gaze, championship belt over the shoulder. Subject rendered as a stylized WWE 2K game character composited onto a photorealistic real-world dark-arena backdrop with purple/gold stage-light bokeh. Oiled specular, decal tattoos, dramatic rim light. 9:16 vertical. Based on the likeness and framing of the provided reference photo. Authentic representation.
```

---

_~21 prompts, tuned to Zion's real look. Add more by mixing any scene modifier from the skill
files with a new pose. Every prompt must represent Zion's body authentically (no fabricated
legs) and keep the tone heroic and motivational._

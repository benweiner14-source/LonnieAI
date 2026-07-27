# Prompt Pack — Zion Clark

Paste-ready Higgsfield **GPT Image 2** prompts. Styles: **NBA 2K** and **WWE 2K**.
Grounded sports-game realism (see `creators/zion-clark/profile.md`).

**Authentic representation (read first — exact anatomy):** Zion was **born without legs**
(caudal regression syndrome). **His body ends at/just past his belly button** — there is no
hip, pelvis, thigh, or leg structure below that, not even partial/"stump" legs. Depict him
**authentically and heroically** — powerful upper body and core, moving on his **hands** or in
a **racing wheelchair**. **Do NOT generate fabricated legs, stump legs, hips, or a standing
figure.** He is the hero of every frame: elite, dignified, motivational.

**His real look (from `refs/`, woven into the prompts below):** a muscular Black adaptive
athlete, **medium-length dreadlocks often in a top-knot**, full short beard, **gold chain with
a cross pendant**, **chest/collarbone tattoos**, and a bold **"NO EXCUSES" tattoo across his
upper back/shoulders**; often in his own **"Z" lightning "No Excuses"** branded gear
(purple/gold/black), or shirtless training.

**One look: FULL CGI RENDER.** Every prompt renders the **entire frame — character AND
environment — in the game engine** (an in-game cutscene). We dropped the "CGI character
composited into a photoreal scene" look — GPT Image 2 couldn't hold it.

**⚠️ Brand safety — no real logos/trademarks.** Earlier prompts named real properties (e.g.
"NBA 2K", "WWE 2K") and the model started rendering **real NBA/2K/WWE logos, league text, and
team branding** into outputs — not usable for a commercial page. All prompts below are
genericized to describe the *aesthetic* (polished sports-sim CGI render) without naming a real
league, studio, or game title, and each ends with an explicit **no real logos/trademarks**
clause. If you write new prompts, keep this rule: describe the *look*, never the *brand*.

**How to run each prompt**
1. Higgsfield → **Nano Banana** (current best quality/consistency per testing) or GPT Image 2 →
   aspect ratio **9:16**, resolution 2k, quality high.
2. **Bind his identity:** attach 1–2 clean reference photos from `refs/soul-id/` directly
   (Nano Banana handles this well). **Soul 2.0 tested worse than Nano Banana / GPT Image 2** —
   skip training a Soul ID for now; use direct reference photos instead.
3. Generate 2–3 variants, keep the best. Verify the body is represented authentically.

**If it still renders too photoreal:** see `docs/higgsfield-cgi-playbook.md`. Do **not** add
"face-scanned maximum fidelity / skin pores / broadcast realism" — those pull it back to photo.
Append the **CGI-enforcement block** below to any prompt that comes out too real:
```
— rendered as a 3D CGI video-game character, NOT a photograph, NOT photorealistic. Real-time game-engine render (PS5 / Unreal Engine cutscene). Smooth waxy subsurface-scattering skin with a subtle plastic sheen, slightly simplified pores, clean CG geometry, rendered hair, ambient occlusion. The subject must read as a stylized computer-generated character model, obviously CGI — like a playable video-game character, not a real person.
```

**Tags:** `[style · scene]`. Full style detail in `skills/nba2k-style/` and `skills/wwe2k-style/`.

> v3 — all full CGI render; tuned to scraped refs in `creators/zion-clark/refs/`.

---

## NBA 2K  (`skills/nba2k-style/`)

**[nba2k · gym]**
```
Polished sports-simulation video game cutscene screenshot, full 3D game-engine render of both character and environment. Zion, a muscular Black adaptive athlete born without legs with medium-length dreadlocks pulled back and a short beard, powerful defined upper body and core, supporting himself on his hands mid-training on the gym floor, chalked palms, gold chain, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — all rendered in-engine. Plastic sheen and sweat specular on forehead, shoulders, and arms, decal tattoos, simplified dreadlock texture, warm amber skin, clean CG geometry, ambient occlusion. Low-angle hero framing, rim light. No film grain. 9:16 vertical. modern sports-sim story-mode cutscene aesthetic — no real league, team, or studio logos, no readable brand text. Based on the likeness of the provided reference / Soul ID. Represent his body authentically — his body ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · gym — back / NO EXCUSES tattoo]**
```
Sports-sim video game cutscene screenshot, full in-engine render. Zion, a muscular Black adaptive athlete born without legs, seen from behind seated on the gym floor, powerful back and shoulders showing the bold "NO EXCUSES" tattoo across his upper back, medium-length dreadlocks, in a bright modern gym with heavy bags and equipment — all rendered in-engine. Sweat specular on skin, plastic subsurface sheen, decal tattoos, clean CG geometry, ambient occlusion. Contemplative hero framing, rim light. No grain. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · gym — parallette hold]**
```
Polished sports-simulation video game cutscene screenshot, full 3D game-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and a short beard, supporting himself on his hands in a strength hold on the gym floor, arms and core engaged, gold chain, determined face. Bright modern gym with cable machines and dumbbells behind, rendered in-engine. Plastic sheen, sweat specular, decal tattoos, clean CG geometry. Dramatic low-angle hero framing, rim light. No grain. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · training-facility]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back, training with battle ropes from a seated hand-supported position, powerful shoulders and back, gold chain, on a turf floor with branded padded walls and staff at lower detail behind — all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Hero framing, rim light. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · training-facility — sled]**
```
Polished sports-simulation video game cutscene screenshot, full 3D game-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, in an intense training moment driving a weight sled with his arms across a performance turf floor, branded padding and equipment behind — all in-engine. Sweat specular, plastic sheen, decal tattoos, ambient occlusion. Low-angle hero framing, rim light. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · track]**
```
Polished sports-simulation video game cutscene screenshot, full in-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, in a racing wheelchair on an outdoor stadium track, gripping the push rims mid-sprint, powerful arms and shoulders, aerodynamic racing gloves and helmet. Red synthetic track lanes with crisp white lines, grandstands, bright natural daylight, blue sky, sponsor banners — all rendered in-engine. Sweat specular, plastic sheen, decal tattoos, clean CG geometry, broadcast-quality lighting. Low-angle hero framing down the lane. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Authentic adaptive athlete — racing wheelchair, body ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · track — start line]**
```
Sports-sim video game cutscene screenshot, full 3D game-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and a short beard, at the start line in his racing wheelchair, coiled and ready, intense focus, gold chain. Stadium track and grandstands behind, bright daylight — all in-engine. Plastic sheen and sweat specular, decal tattoos, clean CG geometry. Dramatic low-angle hero framing. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Racing wheelchair, authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · portrait]**
```
Sports-sim broadcast close-up portrait, full in-engine render. Zion, a muscular Black adaptive athlete with medium-length dreadlocks pulled back, short beard, and gold chain, intense determined expression, plastic sheen and sweat specular on forehead and shoulders, decal tattoos on arms and neck, black "No Excuses" compression top. Shallow depth of field with a blurred in-engine facility behind, dramatic broadcast lighting, clean CG geometry. 9:16 vertical. sports-sim cutscene aesthetic — no real league/team logos or brand trademarks. Upper-body hero portrait — body ends at/just past the belly button, no legs, no hips, no stump legs.
```

### Multi-image role-tagged (Nano Banana Pro — up to 14 refs, one job per image)
_Full technique + how to extend it: `docs/multi-image-role-tagging.md`. Attach images in this
exact order — the text numbering must match the actual upload order._

**[nba2k · gym · multi-ref role-tagged]** — single style ref (simplest, start here)
_Attach: 1) `refs/zion_gym_parallette.jpg` (face) 2) `refs/zion_back_noexcuses_tattoo.jpg` (tattoo)
3) `refs/soul-id/soul_12.jpg` (body) 4) `reference-material/2k-screenshots/2k_02.jpg` (style)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific gym and background in this image.

REFERENCE IMAGE 4: use ONLY for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in this reference — style/rendering-technique only, nothing else from this image.

Now render: a muscular Black adaptive athlete born without legs, medium-length dreadlocks in a top-knot, short beard, gold chain with a cross pendant, supporting himself on his hands mid-training on a gym floor, chalked palms, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — the entire frame (character AND environment) rendered in a polished sports-simulation CGI game-engine style, obviously computer-generated, NOT a photograph. No real league, team, studio, or brand logos or trademarks anywhere in the output; no readable brand text. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

**[nba2k · gym · multi-ref role-tagged — MULTI-STYLE variant]** — several style refs for a
stronger style "consensus." **14-image cap math:** 3 non-style refs (face/tattoo/body) leaves
**up to 11** style slots. Below uses **6** (a good balance — more than 6 tends to dilute focus
without adding much). Swap in more of `reference-material/2k-screenshots/` (up to 11) if you
want to go further; all 14 minus the 3 non-style refs would only leave room for 11, not 14.
_Attach: 1) `refs/zion_gym_parallette.jpg` (face) 2) `refs/zion_back_noexcuses_tattoo.jpg` (tattoo)
3) `refs/soul-id/soul_12.jpg` (body) 4–9) `reference-material/2k-screenshots/2k_01.jpg`,
`2k_02.jpg`, `2k_04.jpg`, `2k_06.jpg`, `2k_07.jpg`, `2k_10.jpg` (style, 6 images)_
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — his exact face shape, eyes, nose, beard. Ignore the pose and background in this image.

REFERENCE IMAGE 2: use ONLY for the "NO EXCUSES" tattoo artwork and its exact placement across the upper back and shoulders. Ignore the pose and background in this image.

REFERENCE IMAGE 3: use ONLY for body proportions, muscular build, and the authentic hand-supported pose/composition. His body ends at/just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Ignore the specific gym and background in this image.

REFERENCE IMAGES 4 THROUGH 9: use these ONLY, collectively, for the rendering STYLE — polished sports-simulation CGI game-engine look: waxy subsurface-scattering skin, plastic sheen, clean CG geometry, simplified hair, ambient occlusion, consistent character-render quality. Ignore and do NOT reproduce any logos, team names, league marks, jersey text, or watermarks visible in ANY of these reference images — style/rendering-technique only, nothing else from them.

Now render: a muscular Black adaptive athlete born without legs, medium-length dreadlocks in a top-knot, short beard, gold chain with a cross pendant, supporting himself on his hands mid-training on a gym floor, chalked palms, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — the entire frame (character AND environment) rendered in a polished sports-simulation CGI game-engine style, obviously computer-generated, NOT a photograph. No real league, team, studio, or brand logos or trademarks anywhere in the output; no readable brand text. His body ends at/just past the belly button — no hips, no legs, no stump legs. 9:16 vertical.
```

### Signature moments (exact-gesture, full CGI render)
_Name the pose precisely, add `(see ref images)`. Replace `<<<ZION>>>` with your Soul ID token._

**[nba2k · signature · chalk-clap]**
```
Sports-sim broadcast close-up, full 3D game-engine render. <<<ZION>>>, a muscular Black adaptive athlete born without legs with medium-length dreadlocks in a top-knot, full short beard, and a gold chain with a cross pendant, clapping both chalked hands together in front of his chest to explode a burst of white chalk dust into the air, arms flexed, mouth open in an intense fired-up yell, eyes locked forward (see ref images). Chest and collarbone tattoos visible, shirtless or in a black "No Excuses" cutoff, sweat specular sheen on shoulders and forehead. In-engine gym backdrop, shallow depth of field, dramatic rim light. Rendered as a 3D CGI video-game character, NOT a photograph — real-time game-engine cutscene render, smooth waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion; obviously computer-generated, like a playable sports-sim character model. No film grain. 9:16 vertical. modern sports-sim story-mode cutscene aesthetic — no real league, team, or studio logos, no readable brand text. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[nba2k · signature · double-flex]**
```
Sports-sim broadcast close-up, full 3D game-engine render. <<<ZION>>>, a muscular Black adaptive athlete born without legs with dreadlocks pulled back and a full beard, supported on one hand while raising the other arm in a hard double-take flex — bicep peaked, veins showing, fist clenched, jaw set in a roaring intense expression (see ref images). "NO EXCUSES" tattoo across his upper back catching the light, gold cross chain, sweat specular on skin. Dark moody in-engine gym, hard rim and key light, shallow depth of field. Rendered as a 3D CGI video-game character, NOT a photograph — real-time game-engine cutscene render, smooth waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion; obviously computer-generated, like a playable sports-sim character model. No film grain. 9:16 vertical. modern sports-sim story-mode cutscene aesthetic — no real league, team, or studio logos, no readable brand text. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

---

## WWE 2K  (`skills/wwe2k-style/`)

**[wwe2k · entrance]**
```
Pro-wrestling-sim video game screenshot, modern sports-sim engine, full in-engine render of character and stage. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back and a short beard, powerful oiled upper body, entering on his hands onto the entrance stage, arms mid-stride, intense heroic face, custom "No Excuses" entrance gear, gold chain. Giant LED video wall glowing behind (purple and gold), cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail — all rendered in-engine. Oiled muscular specular sheen, plastic face sheen, decal tattoos, simplified dreadlock texture, clean CG geometry. Hard colored stage lighting, strong rim light against black arena, high contrast. Low-angle hero framing. No grain. 9:16 vertical. wrestling-sim cutscene aesthetic — no real promotion/league logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[wwe2k · entrance — silhouette]**
```
Wrestling-sim screenshot, modern sports-sim engine, full in-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, backlit in silhouette at the top of the entrance ramp, arms raised, the "NO EXCUSES" back tattoo catching the rim light, purple-and-gold pyro erupting, LED wall blazing, haze and follow-spots, roaring dark crowd below at low detail — all in-engine. Oiled muscle rim light, plastic sheen, decal tattoos, clean CG geometry. Epic low-angle hero framing. High contrast, saturated stage beams against black. 9:16 vertical. wrestling-sim cutscene aesthetic — no real promotion/league logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[wwe2k · ring]**
```
Wrestling-sim screenshot, modern sports-sim engine, full in-engine render of character and arena. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back, center-ring on the canvas, supported on his hands in a commanding heroic pose, ropes and padded turnbuckles around, championship logos on the mat, dark arena crowd at reduced detail, overhead truss lighting — all rendered in-engine. Oiled muscular sheen catching the lights, plastic face sheen, decal tattoos including "NO EXCUSES" across the back, clean CG geometry. Dramatic framing, strong rim light. 9:16 vertical. wrestling-sim cutscene aesthetic — no real promotion/league logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[wwe2k · victory]**
```
Wrestling-sim screenshot, modern sports-sim engine, full in-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, raised on top of a turnbuckle balanced on his hands, arms and torso in a triumphant victory pose, "NO EXCUSES" back tattoo visible, backlit by purple-and-gold stage lighting and pyro, dark roaring crowd below at low fidelity, championship belt on the mat — all in-engine. Oiled muscle rim light, plastic sheen, decal tattoos, clean CG geometry. Epic low-angle hero framing. No grain. 9:16 vertical. wrestling-sim cutscene aesthetic — no real promotion/league logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[wwe2k · dramatic-gym]**
```
Wrestling-sim screenshot, modern sports-sim engine, full in-engine render. A dark, moody gym lit like a wrestling-sim cutscene — hard rim and colored spotlights on Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, mid-lift supported on his hands, gold chain, equipment in deep shadow, saturated purple accent lighting — all rendered in-engine. Oiled specular sheen, plastic face sheen, decal tattoos, clean CG geometry. High-contrast heroic framing. 9:16 vertical. wrestling-sim cutscene aesthetic — no real promotion/league logos or brand trademarks. Authentic body — ends at/just past the belly button, no legs, no hips, no stump legs.
```

**[wwe2k · portrait]**
```
Wrestling-sim broadcast close-up, full in-engine render. Zion, a muscular Black adaptive athlete with medium-length dreadlocks pulled back, short beard, and gold chain, intense expression, oiled skin with strong specular and sweat highlights, decal tattoos, championship belt over the shoulder. Dark in-engine arena bokeh behind with purple/gold stage-light glow, dramatic lighting, clean CG geometry. 9:16 vertical. wrestling-sim cutscene aesthetic — no real promotion/league logos or brand trademarks. Upper-body hero portrait — body ends at/just past the belly button, no legs, no hips, no stump legs.
```

---

_All full CGI render, tuned to Zion's real look. Add more by mixing any scene modifier from the
skill files with a new pose. Every prompt must represent Zion's body authentically — his body
ends at/just past the belly button, no legs, no hips, no stump legs — and keep the tone heroic
and motivational._

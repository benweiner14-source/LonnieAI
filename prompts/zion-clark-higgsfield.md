# Prompt Pack — Zion Clark (Higgsfield, simple single-paragraph format)

**This is the "just mess around in Higgsfield" version.** No `REFERENCE IMAGE 1 / 2 / 3...`
role-tagging — just one flowing descriptive paragraph per scene, modeled on the prompt Ben got
decent results with in Higgsfield Nano Banana. For the full-control version with explicit
multi-image role assignment (Comfy Cloud / Nano Banana Pro), use `prompts/zion-clark.md` instead
— same 16 scenes, same guardrails, just wired for a tool that actually honors multiple tagged
reference images.

**Why this is simpler on purpose:** Higgsfield's img2img/Nano Banana flow doesn't reliably use
more than what you attach directly, and earlier testing found GPT Image 2 in particular **only
honors one input image and silently drops the rest** — so writing "REFERENCE IMAGE 2: use ONLY
for..." text here would just be dead weight. Instead:
- **Attach one photo** — `creators/zion-clark/refs/zion_face_agt.jpg` (sharp, well-lit, front-facing
  red carpet photo) and `zion_gym_parallette.jpg` (clear face + shows arm/chest tattoos) are both
  good face-fidelity options; since Higgsfield typically only honors one attached photo reliably,
  try either and see which reads truer to his likeness.
- If the scene is specifically about a tattoo or a different body context, swap in the more
  relevant photo instead: `zion_chest_arm_tattoo.jpg` or `zion_chest_tattoo_closeup_alt.jpg`
  (chest/arm ink), `zion_back_noexcuses_tattoo.jpg` (back tattoo scenes), `zion_plyobox_bodycomp.jpg`
  or `soul-id/soul_12.jpg` (general body composition), `zion_track_noexcuses.jpg` (track/wheelchair),
  `zion_boxing_ring.jpg` (WWE/combat).
- Paste the prompt text below unmodified. Generate a few seeds and pick the best — same advice
  as the Comfy pack: discard any variant with a leg/foot/stump visible or with real-logo leakage.

**Non-negotiable in every prompt (same hard rules as the Comfy pack):** exact anatomy (body ends
at/just past the belly button, no hips/legs/stump legs/feet/shoes anywhere in frame), no real
league/team/studio/brand logos or trademarks, 9:16 vertical, obviously CGI/in-engine — not a
photograph, and not a Disney/Pixar/animated-movie look.

**Camera variety:** every scene ends with a specific angle + lens/focal-length + framing note
(low/high/Dutch angles, 20mm wide through 135mm telephoto, off-center framing) instead of a
generic centered "hero shot" — Ben flagged everything was reading too flat and symmetrical.

---

## NBA 2K

**[nba2k · gym]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. He has medium-length dreadlocks in a top-knot, short beard, gold chain with a cross pendant, supporting himself on his hands mid-training on a gym floor, chalked palms, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: low-angle hero shot, 24mm wide lens, subject positioned slightly left-of-center with exaggerated foreground-to-background perspective. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[nba2k · gym — back / NO EXCUSES tattoo]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, seen from behind, seated on a gym floor. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Powerful back and shoulders showing the bold "NO EXCUSES" tattoo across his upper back, medium-length dreadlocks. Bright modern gym with equipment in the background, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoo linework, clean CG geometry, warm amber skin. Camera: eye-level angle shot from directly behind, 50mm lens, subject placed in the lower third of frame with negative space above toward the gym ceiling. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[nba2k · gym — parallette hold / reclined]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Dreadlocks in a top-knot, reclined with his torso flat against the gym floor, resting up on his forearms in a relaxed pose between sets, gold chain, relaxed confident expression looking toward camera. Bright modern gym with cable machines and dumbbells in the background, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: high overhead angle looking down at a slight tilt, 28mm wide lens, asymmetrical framing with negative space to one side. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[nba2k · training-facility — battle ropes]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. He has dreadlocks pulled back, training with battle ropes from a seated hand-supported position, powerful shoulders and back, gold chain, on a turf floor with branded-free padded walls and staff at lower detail behind, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: Dutch angle (12° tilt), 35mm lens, dynamic diagonal composition. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[nba2k · training-facility — sled pull]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Dreadlocks pulled back, leaning low with his torso close to the ground, pulling a resistance sled backward by a strap with both arms, powerful shoulders engaged, on a performance turf floor with equipment visible in the background, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: extreme low angle looking up, 20mm wide lens, dramatic foreshortening. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[nba2k · track]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, in a racing wheelchair on an outdoor stadium track. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Gripping the push rims mid-sprint, powerful arms and shoulders, aerodynamic racing gloves and helmet, gold chain. Red synthetic track lanes with crisp white lines, grandstands, bright natural daylight, blue sky, banners, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: wide establishing shot, 24mm lens, subject framed off-center to the right with the track receding into the distance. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin. Racing wheelchair, authentic adaptive athlete.
```

**[nba2k · track — start line]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, at the start line in his racing wheelchair, coiled and ready, intense focus, gold chain. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Stadium track and grandstands in the background, bright daylight, all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: telephoto compression, 85mm lens, flattened background, subject framed left-of-center. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin. Racing wheelchair, authentic adaptive athlete.
```

**[nba2k · portrait]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, broadcast close-up portrait, intense determined expression, sweat specular on forehead and shoulders, chest and left arm tattoos visible, black "No Excuses" compression top. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point; upper-body hero portrait only. Shallow depth of field with a blurred facility in the background, dramatic broadcast lighting, all rendered in-engine. Plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: telephoto close-up, 100mm lens, extremely shallow depth of field, eyes positioned on the upper-left third of frame. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. No feet or shoes visible anywhere in frame.
```

### Signature moments

**[nba2k · signature · chalk-clap]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, seated upright on the gym floor, torso vertical, clapping both chalked hands together in front of his chest to explode a burst of white chalk dust into the air, mouth open in an intense fired-up yell, eyes locked forward. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Chest and left arm tattoos visible, shirtless or in a black "No Excuses" cutoff, sweat specular sheen on shoulders and forehead. Gym backdrop, shallow depth of field, dramatic rim light, all rendered in-engine. Plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: Dutch tilt (15°), 28mm wide lens, dynamic broadcast-camera energy. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[nba2k · signature · double-flex]**
```
Sports-sim video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, supported on one hand while raising the other arm in a hard double-take flex — bicep peaked, veins showing, his left arm tattoo visible on the flexed arm, fist clenched, jaw set in a roaring intense expression. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. "NO EXCUSES" tattoo across his upper back catching the light, gold cross chain, sweat specular on skin. Dark moody gym, hard rim and key light, shallow depth of field, all rendered in-engine. Plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: low three-quarter angle, 35mm lens, subject off-center with negative space to the right. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

---

## WWE 2K

**[wwe2k · entrance]**
```
Professional wrestling video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, positioned low at the front edge of the entrance stage, torso reclined and propped up on his forearms, surveying the crowd with an intense heroic expression, custom "No Excuses" entrance gear leaving his arms and chest tattoo visible, gold chain. Both his hands/forearms are clearly planted on the stage floor supporting his upper body; nothing below his torso is in frame. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Giant LED video wall glowing behind (purple and gold), cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail, all rendered in-engine. Heavy sweat/oil specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: extreme low angle looking up from the crowd, 24mm wide lens, dramatic scale, subject framed off-center. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[wwe2k · entrance — silhouette]**
```
Professional wrestling video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, torso reclined flat and silhouetted against a glowing LED wall at the top of the entrance ramp, propped up on both forearms with one arm lifting slightly in a triumphant gesture, the "NO EXCUSES" back tattoo catching the rim light. Only his torso, arms, and head are silhouetted — nothing below his torso is in frame. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Purple-and-gold pyro erupting, haze and follow-spots, roaring dark crowd below at low detail, all rendered in-engine. Plastic sheen, clean CG geometry, warm amber rim light. Camera: slight high angle from a side platform, 35mm lens, subject offset to one side of the ramp, not centered. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[wwe2k · ring]**
```
Professional wrestling video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, center-ring on the canvas, supported on his hands in a commanding heroic pose, ropes and padded turnbuckles around, bold graphic mat design, dark arena crowd at reduced detail, overhead truss lighting. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. Oiled muscular sheen catching the lights, "NO EXCUSES" tattoo visible across the back, all rendered in-engine. Heavy oil/sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: high three-quarter angle from the turnbuckle, 50mm lens, subject in the lower half of frame. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[wwe2k · victory]**
```
Professional wrestling video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, supporting himself with both hands gripping the middle turnbuckle ropes, torso raised and chest out in a triumphant victory pose, "NO EXCUSES" back tattoo visible, backlit by purple-and-gold stage lighting and pyro, dark roaring crowd below at low fidelity, a championship-style belt on the mat. His hands are clearly gripping the ropes/turnbuckle pad supporting his weight; nothing below his torso is in frame. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. All rendered in-engine. Plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: low Dutch angle (10° tilt), 28mm lens, dynamic tilted horizon. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[wwe2k · dramatic-gym]**
```
Professional wrestling video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, in a dark moody gym lit dramatically — hard rim and colored spotlights, mid-lift supported on his hands, gold chain, equipment in deep shadow, saturated purple accent lighting. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point. All rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: side-profile angle, 50mm lens, subject framed left-of-center, deep shadow filling the right side of frame. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. Authentic body — no fabricated legs, no stump legs, no feet or shoes visible anywhere in frame. His shorts, trunks, or shirt hem drape loosely and naturally past the end of his torso — empty, unfilled fabric, not shaped like a leg underneath — matching his real reference photos, rather than his torso ending abruptly in bare exposed skin.
```

**[wwe2k · portrait]**
```
Professional wrestling video game cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs, intense expression, oiled skin with strong specular and sweat highlights, chest and left arm tattoos visible, a championship-style belt over the shoulder. His body ends at just past the belly button — no hips, no thighs, no legs, no stump legs, nothing below that point; upper-body hero portrait only. Dark arena bokeh in the background with purple/gold stage-light glow, dramatic lighting, all rendered in-engine. Plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Camera: telephoto, 135mm lens, extremely shallow depth of field, off-center framing with negative space to one side. 9:16 vertical. sports sim video game aesthetic, obviously computer-generated, not a photograph — not a Disney/Pixar or animated-movie style, realistic human proportions. No real league, team, studio, or brand logos or trademarks anywhere in the output. No feet or shoes visible anywhere in frame.
```

---

_16 scenes matching `prompts/zion-clark.md` 1:1, reformatted as single-paragraph prompts for
Higgsfield. If a scene keeps coming out too photorealistic (this happened on the plainest gym
shot), try a few different seeds before rewriting the prompt — that axis is seed-sensitive._

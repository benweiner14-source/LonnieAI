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

**One look: FULL CGI RENDER.** Every prompt renders the **entire frame — character AND
environment — in the game engine** (an in-game cutscene). We dropped the "CGI character
composited into a photoreal scene" look — GPT Image 2 couldn't hold it.

**How to run each prompt**
1. Higgsfield → GPT Image 2 → aspect ratio **9:16**, resolution 2k, quality high.
2. **Bind his identity:** best path is a trained **Soul ID** on his `refs/soul-id/` used with
   **text-to-image** (no photo attached — that's what forces the CGI look instead of a photo).
   Where a prompt says `Zion`, replace it with your Soul ID `<<<token>>>`.
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
NBA 2K video game cutscene screenshot, full 3D game-engine render of both character and environment. Zion, a muscular Black adaptive athlete born without legs with medium-length dreadlocks pulled back and a short beard, powerful defined upper body and core, supporting himself on his hands mid-training on the gym floor, chalked palms, gold chain, focused intense expression, black "No Excuses" branded tee. Modern weight room with power racks, rubber flooring, motivational wall typography, bright even overhead lighting — all rendered in-engine. Plastic sheen and sweat specular on forehead, shoulders, and arms, decal tattoos, simplified dreadlock texture, warm amber skin, clean CG geometry, ambient occlusion. Low-angle hero framing, rim light. No film grain. 9:16 vertical. NBA 2K26 MyCAREER cutscene aesthetic. Based on the likeness of the provided reference / Soul ID. Represent his body authentically — no fabricated legs.
```

**[nba2k · gym — back / NO EXCUSES tattoo]**
```
NBA 2K cutscene screenshot, full in-engine render. Zion, a muscular Black adaptive athlete born without legs, seen from behind seated on the gym floor, powerful back and shoulders showing the bold "NO EXCUSES" tattoo across his upper back, medium-length dreadlocks, in a bright modern gym with heavy bags and equipment — all rendered in-engine. Sweat specular on skin, plastic subsurface sheen, decal tattoos, clean CG geometry, ambient occlusion. Contemplative hero framing, rim light. No grain. 9:16 vertical. NBA 2K aesthetic. Authentic body — born without legs, no fabricated legs.
```

**[nba2k · gym — parallette hold]**
```
NBA 2K video game cutscene screenshot, full 3D game-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and a short beard, supporting himself on his hands in a strength hold on the gym floor, arms and core engaged, gold chain, determined face. Bright modern gym with cable machines and dumbbells behind, rendered in-engine. Plastic sheen, sweat specular, decal tattoos, clean CG geometry. Dramatic low-angle hero framing, rim light. No grain. 9:16 vertical. NBA 2K aesthetic. Authentic body — no fabricated legs.
```

**[nba2k · training-facility]**
```
NBA 2K cutscene screenshot, full in-engine render of character and environment. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back, training with battle ropes from a seated hand-supported position, powerful shoulders and back, gold chain, on a turf floor with branded padded walls and staff at lower detail behind — all rendered in-engine. Heavy sweat specular, plastic sheen, decal tattoos, clean CG geometry, warm amber skin. Hero framing, rim light. 9:16 vertical. NBA 2K aesthetic. Authentic body — no fabricated legs.
```

**[nba2k · training-facility — sled]**
```
NBA 2K video game cutscene screenshot, full 3D game-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, in an intense training moment driving a weight sled with his arms across a performance turf floor, branded padding and equipment behind — all in-engine. Sweat specular, plastic sheen, decal tattoos, ambient occlusion. Low-angle hero framing, rim light. 9:16 vertical. NBA 2K aesthetic. Authentic body — no fabricated legs.
```

**[nba2k · track]**
```
NBA 2K video game cutscene screenshot, full in-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, in a racing wheelchair on an outdoor stadium track, gripping the push rims mid-sprint, powerful arms and shoulders, aerodynamic racing gloves and helmet. Red synthetic track lanes with crisp white lines, grandstands, bright natural daylight, blue sky, sponsor banners — all rendered in-engine. Sweat specular, plastic sheen, decal tattoos, clean CG geometry, broadcast-quality lighting. Low-angle hero framing down the lane. 9:16 vertical. NBA 2K aesthetic. Authentic adaptive athlete — racing wheelchair, no fabricated legs.
```

**[nba2k · track — start line]**
```
NBA 2K cutscene screenshot, full 3D game-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks and a short beard, at the start line in his racing wheelchair, coiled and ready, intense focus, gold chain. Stadium track and grandstands behind, bright daylight — all in-engine. Plastic sheen and sweat specular, decal tattoos, clean CG geometry. Dramatic low-angle hero framing. 9:16 vertical. NBA 2K aesthetic. Racing wheelchair, authentic body, no fabricated legs.
```

**[nba2k · portrait]**
```
NBA 2K broadcast close-up portrait, full in-engine render. Zion, a muscular Black adaptive athlete with medium-length dreadlocks pulled back, short beard, and gold chain, intense determined expression, plastic sheen and sweat specular on forehead and shoulders, decal tattoos on arms and neck, black "No Excuses" compression top. Shallow depth of field with a blurred in-engine facility behind, dramatic broadcast lighting, clean CG geometry. 9:16 vertical. NBA 2K aesthetic. Upper-body hero portrait, authentic representation.
```

### Signature moments (exact-gesture, full CGI render)
_Name the pose precisely, add `(see ref images)`. Replace `<<<ZION>>>` with your Soul ID token._

**[nba2k · signature · chalk-clap]**
```
NBA 2K broadcast close-up, full 3D game-engine render. <<<ZION>>>, a muscular Black adaptive athlete born without legs with medium-length dreadlocks in a top-knot, full short beard, and a gold chain with a cross pendant, clapping both chalked hands together in front of his chest to explode a burst of white chalk dust into the air, arms flexed, mouth open in an intense fired-up yell, eyes locked forward (see ref images). Chest and collarbone tattoos visible, shirtless or in a black "No Excuses" cutoff, sweat specular sheen on shoulders and forehead. In-engine gym backdrop, shallow depth of field, dramatic rim light. Rendered as a 3D CGI video-game character, NOT a photograph — real-time game-engine cutscene render, smooth waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion; obviously computer-generated, like a playable NBA 2K character model. No film grain. 9:16 vertical. NBA 2K26 MyCAREER cutscene aesthetic. Authentic body — no fabricated legs.
```

**[nba2k · signature · double-flex]**
```
NBA 2K broadcast close-up, full 3D game-engine render. <<<ZION>>>, a muscular Black adaptive athlete born without legs with dreadlocks pulled back and a full beard, supported on one hand while raising the other arm in a hard double-take flex — bicep peaked, veins showing, fist clenched, jaw set in a roaring intense expression (see ref images). "NO EXCUSES" tattoo across his upper back catching the light, gold cross chain, sweat specular on skin. Dark moody in-engine gym, hard rim and key light, shallow depth of field. Rendered as a 3D CGI video-game character, NOT a photograph — real-time game-engine cutscene render, smooth waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion; obviously computer-generated, like a playable NBA 2K character model. No film grain. 9:16 vertical. NBA 2K26 MyCAREER cutscene aesthetic. Authentic body — no fabricated legs.
```

---

## WWE 2K  (`skills/wwe2k-style/`)

**[wwe2k · entrance]**
```
WWE 2K video game screenshot, 2K sports engine, full in-engine render of character and stage. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back and a short beard, powerful oiled upper body, entering on his hands onto the entrance stage, arms mid-stride, intense heroic face, custom "No Excuses" entrance gear, gold chain. Giant LED video wall glowing behind (purple and gold), cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail — all rendered in-engine. Oiled muscular specular sheen, plastic face sheen, decal tattoos, simplified dreadlock texture, clean CG geometry. Hard colored stage lighting, strong rim light against black arena, high contrast. Low-angle hero framing. No grain. 9:16 vertical. WWE 2K aesthetic. Authentic body — no fabricated legs.
```

**[wwe2k · entrance — silhouette]**
```
WWE 2K screenshot, 2K sports engine, full in-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, backlit in silhouette at the top of the entrance ramp, arms raised, the "NO EXCUSES" back tattoo catching the rim light, purple-and-gold pyro erupting, LED wall blazing, haze and follow-spots, roaring dark crowd below at low detail — all in-engine. Oiled muscle rim light, plastic sheen, decal tattoos, clean CG geometry. Epic low-angle hero framing. High contrast, saturated stage beams against black. 9:16 vertical. WWE 2K aesthetic. Authentic body, no fabricated legs.
```

**[wwe2k · ring]**
```
WWE 2K screenshot, 2K sports engine, full in-engine render of character and arena. Zion, a muscular Black adaptive athlete born without legs with dreadlocks pulled back, center-ring on the canvas, supported on his hands in a commanding heroic pose, ropes and padded turnbuckles around, championship logos on the mat, dark arena crowd at reduced detail, overhead truss lighting — all rendered in-engine. Oiled muscular sheen catching the lights, plastic face sheen, decal tattoos including "NO EXCUSES" across the back, clean CG geometry. Dramatic framing, strong rim light. 9:16 vertical. WWE 2K aesthetic. Authentic body, no fabricated legs.
```

**[wwe2k · victory]**
```
WWE 2K screenshot, 2K sports engine, full in-engine render. Zion, a muscular Black adaptive athlete born without legs with dreadlocks, raised on top of a turnbuckle balanced on his hands, arms and torso in a triumphant victory pose, "NO EXCUSES" back tattoo visible, backlit by purple-and-gold stage lighting and pyro, dark roaring crowd below at low fidelity, championship belt on the mat — all in-engine. Oiled muscle rim light, plastic sheen, decal tattoos, clean CG geometry. Epic low-angle hero framing. No grain. 9:16 vertical. WWE 2K aesthetic. Authentic body — no fabricated legs.
```

**[wwe2k · dramatic-gym]**
```
WWE 2K screenshot, 2K sports engine, full in-engine render. A dark, moody gym lit like a WWE 2K scene — hard rim and colored spotlights on Zion, a muscular Black adaptive athlete born without legs with dreadlocks and short beard, mid-lift supported on his hands, gold chain, equipment in deep shadow, saturated purple accent lighting — all rendered in-engine. Oiled specular sheen, plastic face sheen, decal tattoos, clean CG geometry. High-contrast heroic framing. 9:16 vertical. WWE 2K aesthetic. Authentic body, no fabricated legs.
```

**[wwe2k · portrait]**
```
WWE 2K broadcast close-up, full in-engine render. Zion, a muscular Black adaptive athlete with medium-length dreadlocks pulled back, short beard, and gold chain, intense expression, oiled skin with strong specular and sweat highlights, decal tattoos, championship belt over the shoulder. Dark in-engine arena bokeh behind with purple/gold stage-light glow, dramatic lighting, clean CG geometry. 9:16 vertical. WWE 2K aesthetic. Upper-body hero portrait, authentic representation.
```

---

_All full CGI render, tuned to Zion's real look. Add more by mixing any scene modifier from the
skill files with a new pose. Every prompt must represent Zion's body authentically (no fabricated
legs) and keep the tone heroic and motivational._

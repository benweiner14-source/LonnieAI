---
description: Transform photos or scene descriptions into the NBA 2K / 2K Sports in-game cutscene aesthetic, generalized to fitness and athletics. Use for any "2K style," "2K render," or sports-game cutscene look for an athlete.
---

# NBA 2K / 2K Sports Style — Image Prompt Generator (Athletics)

Transform real photos or scene descriptions into the **2K Sports in-game cutscene**
aesthetic using Higgsfield GPT Image 2 — here generalized from basketball to a single
**fitness/athlete hero character** (gym and track/stadium contexts) and retargeted to
**9:16 vertical**.

> Ported from Ben's original `2K_Cutscene_Style_Skill.md` (see `reference-material/`).
> The rendering DNA is unchanged — the proven 2K "polished-CG, identifiably rendered" look —
> with basketball-specific scenes swapped for gym + track/stadium.

---

## When to Use

User says: "apply the 2K look," "make this look like a 2K cutscene," "2K style," or provides
an athlete photo and asks for the in-game cinematic treatment.

---

## Core Style DNA

The 2K look is **polished CG — better than last-gen but still identifiably rendered, not
photographed.** Every element reads as "high-end game engine," not real life.

### Rendering
- Real-time 3D game-engine quality — high polygon, smooth clean surfaces.
- Subsurface scattering on skin: slightly polished/waxy quality, with a distinct **plastic
  sheen** on foreheads, cheekbones, shoulders.
- **Sweat rendering** for training/competition moments: specular highlights on forehead,
  scalp, shoulders, and defined muscle — a key athletic tell.
- **Tattoo rendering:** visible on arms/chest/neck as flat **decal textures** that follow
  skin contours cleanly.
- No film grain, no noise, no lens artifacts — clean digital render.
- Athletic-wear fabrics show detailed mesh texture and micro-perforations; clean uniform
  folds, not photoreal cloth simulation.
- Clean geometry on all objects and equipment; brand logos (Nike, Jordan, Under Armour) crisp
  and readable.

### Characters
- High-fidelity **face-scanned** look for the hero athlete: detailed but smooth skin, realistic
  proportions, accurate facial hair volume with a slightly painted-on quality.
- Warm amber skin tones, smooth complexion, defined and slightly glossy musculature.
- **Simplified hair** is a key tell: buzz cuts render as a stippled texture map (dots, not
  strands); short hair as clean volumetric shapes — never strand-level.
- Foreground hero at high detail with expressive face; background figures (spotters, crowd) at
  noticeably lower fidelity, repeated models, flat texture-card faces at distance.

### Lighting
- Soft, diffused, even — no harsh shadows; subtle ambient occlusion under objects and in corners.
- **Rim lighting** on the main character to separate from background.
- Gym: bright even overhead with clerestory window light. Arena/stadium: broadcast-style even
  lighting on the hero, darker crowd. Track: bright natural daylight.

### Camera
- **Low-angle hero shots** looking up at the athlete for dramatic effect.
- Extreme close-ups on the face/muscle with shallow DOF; detail/insert shots on gear.
- Wide establishing shots for the full environment.
- Eye-level or slightly below standard.
- Vertical **9:16** by default (retargeted from the original 16:9) — compose tall: subject
  centered, headroom, foreground equipment or track.

### Color
- Warm, slightly desaturated palette overall; muted athletic-wear tones (blacks, grays, navy)
  with allowed saturated brand accents.
- Neutral/warm environments: wood floor, rubber gym flooring, gray equipment, painted walls.
- Stadium/track scenes allow saturated banners and brand colors.
- No heavy color grading — clean and balanced.

---

## Base Prompt Template

Replace `[SCENE DESCRIPTION]` with the specific content.

```
2K Sports video game cutscene screenshot. [SCENE DESCRIPTION]. Real-time 3D rendered, high-polygon game engine quality. Smooth subsurface scattering on skin, slightly polished complexion with plastic sheen on forehead, cheekbones, and shoulders; sweat specular highlights on muscle. Soft diffused lighting, subtle ambient occlusion, rim light on the athlete. Warm amber skin tones. Simplified hair rendered as texture maps, not individual strands. Tattoos as clean decal textures. Low-angle hero framing, shallow depth of field on background. Warm slightly desaturated palette. Clean geometry, no film grain or noise. 9:16 vertical aspect ratio. Unreal-quality NBA 2K / 2K Sports cutscene aesthetic.
```

---

## Scene Type Modifiers

### Gym / Weight Room
```
Modern strength-training gym, rubber flooring, power racks and dumbbells, cable machines and benches, chalk dust in the air, motivational wall typography, bright even overhead lighting with clerestory windows, brand banners (Nike/Under Armour) at lower detail behind, a few background figures training at reduced fidelity. Sweat sheen on the athlete's skin and shoulders.
```

### Training Facility (Brand)
```
Indoor athletic performance facility, turf or hardwood floor, sleds and battle ropes, branded padded walls, bright gym lighting, scattered staff/spotters in branded athletic wear at lower detail in the background, clean institutional environment.
```

### Track / Stadium (Day)
```
Outdoor running track in a stadium, red synthetic track lanes with crisp white lines, empty or lightly populated grandstands at reduced detail, bright natural daylight, blue sky, stadium light rigs and sponsor banners, clean broadcast-quality lighting on the athlete, low-angle hero framing down the lane.
```

### Stadium Tunnel / Walkout
```
Athlete emerging from a stadium tunnel into the light, concrete corridor with overhead fluorescent panels transitioning to bright daylight or arena glow, sponsor signage on the walls, dramatic rim light and lens-free clean render, tight framing in the corridor.
```

### Broadcast Portrait (Close-Up)
```
2K Sports broadcast close-up portrait, hero athlete at maximum rendering fidelity, plastic sheen and sweat specular on forehead and shoulders, decal tattoos on arms and neck, branded compression top, shallow depth of field with a blurred facility or crowd behind, dramatic broadcast-quality lighting.
```

---

## How to Use with a Reference Photo (Zion)

1. Describe the athlete from the reference photo (build, pose, wardrobe, expression).
2. Plug that into `[SCENE DESCRIPTION]` plus the appropriate scene modifier.
3. In Higgsfield GPT Image 2, attach the reference photo (image-to-image), set 9:16.
4. Add: `Based on the composition, likeness, and framing of the provided reference photo.`
5. Keep the athletic, motivational tone — clean and heroic.

### The two looks
- **full-render:** everything is the 2K engine (athlete + environment).
- **cgi-in-scene:** stylize the *athlete* as a 2K game character composited into a photoreal
  gym/track backdrop. Add: `photorealistic real-world background, subject rendered as a
  stylized 2K Sports game character.`

---

## Example Prompts

**Gym hero, full-render:**
```
2K Sports video game cutscene screenshot. A muscular athlete mid-workout gripping a loaded barbell, chalked hands, focused expression, in a black branded compression top. Modern weight room with power racks, rubber flooring, motivational wall type, bright even overhead light. Real-time 3D render, plastic sheen and sweat specular on forehead and shoulders, decal tattoos, simplified hair texture map, warm amber skin. Low-angle hero framing, rim light, shallow DOF on background. Warm slightly desaturated palette, clean geometry, no grain. 9:16 vertical. NBA 2K cutscene aesthetic.
```

**Track walkout, cgi-in-scene:**
```
2K Sports style. An athlete at the start line of a stadium track, determined pose, branded kit. Subject rendered as a stylized 2K game character — plastic sheen, sweat specular, decal tattoos — composited into a photorealistic real-world stadium track backdrop. Bright daylight, red track lanes, low-angle hero framing down the lane. 9:16 vertical. Based on the likeness and framing of the provided reference photo.
```

---

## Tool Guidance

- **Tool:** Higgsfield GPT Image 2. **Aspect ratio:** 9:16, resolution 2k, quality high.
- **Reference photo:** attach it (image-to-image); add the "based on the provided reference
  photo" line for likeness.
- **Generate 2–3 variants** per prompt — the CG look has natural variation.
- **DO keep:** plastic sheen, sweat specular, decal tattoos, simplified hair, clean geometry.
- **AVOID:** film grain, lens flare, chromatic aberration, bokeh circles, photographic artifacts.

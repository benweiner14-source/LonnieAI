---
description: Transform photos or scene descriptions into the Cyberpunk 2077 (Night City, RED Engine) in-game look. Use for any "Cyberpunk style," "Cyberpunk 2077 look," "Night City render," or neon-noir cyberpunk treatment.
---

# Cyberpunk 2077 Style — Image Prompt Generator

Transform real photos or scene descriptions into the **Cyberpunk 2077** in-game aesthetic
(CD Projekt RED Engine, Night City) using Higgsfield GPT Image 2.

> A fork of the NBA 2K cutscene skill's method — codified rendering *tells*, a base template,
> and scene modifiers — retargeted to Cyberpunk's neon-noir look and **9:16 vertical**.
>
> **Reference library:** drop in-game screen grabs / photo-mode shots into `reference/` to
> sharpen accuracy. `cp2077_boxart` is included as a starter (confirms the yellow/teal/magenta
> brand palette).

> **⚠️ Brand safety:** this file references the real game internally as the aesthetic we're
> describing — fine for OUR understanding. But the actual **prompt text sent to the image model
> must never name a real game, studio, or engine** — doing so has caused real logos/branding to
> leak into outputs elsewhere in this project. **Use the already-genericized, paste-ready prompts
> in `prompts/kazumi.md`** for actual generation. New prompts built from this file should describe
> the *aesthetic* (neon-noir cyberpunk look) — never the brand — and end with "no real studio/game
> logos or brand trademarks."

---

## When to Use

User says: "make this Cyberpunk," "Cyberpunk 2077 style," "put her in Night City,"
"neon-noir cyberpunk," or provides a photo and asks for the augmented/high-tech treatment.

---

## Core Style DNA

The Cyberpunk 2077 look is **photoreal geometry drowned in stylized neon lighting** — a
high-tech, high-contrast, rain-slick dystopia. The lighting and color grade do most of the
stylistic work; unlike the clean 2K look, this aesthetic **embraces photographic artifacts**
(bloom, lens flare, subtle chromatic aberration, film grain).

### Rendering
- RED Engine fidelity with **ray-traced reflections and neon global illumination** — every
  surface picks up colored light from signage and holograms.
- **Wet, rain-slick streets** with mirror-like reflective puddles doubling the neon.
- Heavy **volumetric fog** glowing with neon; light shafts through steam and rain.
- Strong **bloom** on all light sources; **anamorphic lens flares** (horizontal streaks) on
  bright neon; subtle **chromatic aberration** at frame edges; fine film grain.
- Chrome and metallic **cybernetic implants** with sharp specular highlights.
- High contrast — deep crushed blacks against blown-out neon.

### Characters
- **Augmented humans:** chrome jaw/cheek plates, subdermal implants, glowing **Kiroshi optic**
  eyes (faint colored glow + lens reflection), cyberware ports on temples/neck, LED tattoos.
- Edgerunner **techwear:** neon-trimmed jackets, tactical harnesses, techno-mesh, latex,
  holographic fabrics, utility straps, statement boots.
- **Vivid hair** — undercuts, mohawks, slick styles in electric teal, magenta, acid green,
  platinum; realistic strand detail.
- Bold makeup with metallic and neon accents, face tattoos, chrome nails.
- Confident, edgy posing; the character owns the frame like a poster.

### Lighting
- **Neon-noir:** the dominant light is colored — cyan/teal from one side, magenta/hot-pink
  from the other, with electric-yellow (the Cyberpunk brand accent) as a highlight.
- Strong **rim/edge lighting** separating the subject from a dark, foggy background.
- Holographic advertisements and signage cast moving colored light on skin and surfaces.
- Underlit and top-down practical sources (floor LEDs, ceiling strips, car headlights).

### Camera
- Cinematic third-person hero framing; **dramatic low angles** against megabuildings and holo-ads.
- Shallow depth of field with **neon bokeh** in the background (allowed here — it's core to
  the look, unlike the 2K skill which forbids it).
- Dutch tilts and reflective-puddle framing for mood.
- Vertical **9:16** by default — tall Night City verticality, holo-signage above, wet street below.

### Color
- Dominant **teal/cyan + magenta/hot-pink**, punctuated by **electric yellow** and deep blue.
- Deep blacks, high saturation on light sources, desaturated mid-tones.
- Occasional acid green and orange sodium accents.
- Overall: cold, electric, high-contrast — the opposite of warm/muted.

---

## Base Prompt Template

Replace `[SCENE DESCRIPTION]` with the specific content.

```
Cyberpunk 2077 video game screenshot, CD Projekt RED Engine, Night City in-game render. [SCENE DESCRIPTION]. Photorealistic geometry under stylized neon-noir lighting. Ray-traced reflections, wet rain-slick streets with mirror puddles, volumetric neon fog, strong bloom and anamorphic lens flare, subtle chromatic aberration and film grain. Augmented character with chrome cyberware and glowing Kiroshi optic eyes, vivid techwear, electric-colored hair. Teal-and-magenta neon lighting with electric-yellow accents, deep crushed blacks, high contrast. Dramatic low-angle cinematic framing, shallow depth of field with neon bokeh. 9:16 vertical aspect ratio. High-tech dystopian Night City aesthetic.
```

---

## Scene Type Modifiers

Append to the base template depending on the environment.

### Night City Street (Neon Alley)
```
Rain-slick Night City back alley at night, dense holographic advertisements in Japanese and English glowing overhead, neon signage in teal and magenta reflected in puddles, steam rising from vents, tangled cables and satellite dishes, distant megabuilding silhouettes, a lone flickering sign — moody neon-noir with deep shadow and colored fog.
```

### Megabuilding / Vertical Skyline
```
Towering Night City megabuildings at night, brutalist concrete stacked with thousands of lit windows and giant animated holo-billboards, flying AV cars with light trails, a walkway or balcony high above the neon canyon, dramatic vertical composition emphasizing scale, teal-and-magenta city glow.
```

### Cyber Bar / Ramen Stall (Nightlife)
```
Neon cyberpunk bar or street ramen stall, warm sodium and cold neon mix, holographic menu boards, LED-lit counter, patrons with cyberware in the blurred background, steam and smoke catching colored light, intimate underlit framing, reflective wet counter surface.
```

### Cosplay Hero Splash (Character Card)
```
Hero character splash / key-art framing, subject centered and lit like a Cyberpunk 2077 character-select portrait, dramatic teal rim light on one side and magenta on the other, electric-yellow accent, dark foggy background with faint holo-signage bokeh, chrome cyberware highlights, confident direct pose — poster-quality cosplay hero shot.
```

### Corpo / High-Tech Interior
```
Sleek corpo Night City interior — glass, brushed metal, holographic UI panels floating in the air, cool blue and cyan ambient light with magenta accents, floor-to-ceiling windows onto the neon skyline, minimalist high-tech furniture, reflective polished floor.
```

### Neon Car / Motorcycle
```
Posed with a cyberpunk sports car or neon-underlit motorcycle on a wet Night City street, chrome and carbon bodywork reflecting teal and magenta neon, headlight glare and light trails, holo-ads overhead, low-angle hero framing — edgerunner energy.
```

---

## How to Use with a Reference Photo (Kazumi)

1. Describe the subject from the reference photo (pose, wardrobe, hair, expression).
2. Plug that into `[SCENE DESCRIPTION]` plus a scene modifier; layer in cyberware details
   (glowing optics, a chrome jaw plate, LED tattoo) to sell the augmentation.
3. In Higgsfield GPT Image 2, attach the reference photo (image-to-image), set 9:16.
4. Add: `Based on the composition, likeness, and framing of the provided reference photo.`
5. Keep it **SFW** — techwear/latex styling is fine as fashion; no nudity or explicit posing.

### Look: full CGI render
Everything is the Cyberpunk 2077 engine — subject *and* Night City environment (an in-game
shot). (The composited-into-a-photo look was dropped — GPT Image 2 couldn't hold it.)

---

## Example Prompts

**Neon alley, full-render:**
```
Cyberpunk 2077 video game screenshot, RED Engine, Night City in-game render. A woman with a slick teal-and-magenta undercut, chrome cheek implant and faintly glowing cyber-eyes, in a neon-trimmed techwear jacket, standing in a rain-slick alley. Holographic ads glow overhead, puddles mirror the neon, steam rises from vents. Ray-traced reflections, volumetric fog, bloom, anamorphic flare, subtle chromatic aberration and grain. Teal-and-magenta lighting, electric-yellow accents, deep blacks, high contrast. Low-angle cinematic framing, neon bokeh. 9:16 vertical.
```

**Cosplay hero splash, full-render:**
```
Cyberpunk 2077 video game screenshot, RED Engine, character-select splash, full in-game render. A woman in glossy techwear with chrome nails and an LED face tattoo, confident direct pose — stylized Cyberpunk 2077 game character with chrome cyberware and glowing Kiroshi optics, against a dark in-engine neon-city background with holo-signage bokeh. Teal rim light one side, magenta the other, electric-yellow accent, bloom. 9:16 vertical. Based on the likeness / Soul ID. SFW.
```

---

## Tool Guidance

- **Tool:** Higgsfield GPT Image 2. **Aspect ratio:** 9:16, resolution 2k, quality high.
- **Reference photo:** attach it (image-to-image); add the "based on the provided reference
  photo" line for likeness.
- **Generate 2–3 variants** per prompt — pick the best.
- **DO keep:** teal/magenta neon, glowing optics, chrome cyberware, wet reflections, bloom,
  lens flare, subtle chromatic aberration + grain (these are core here, unlike the 2K look).
- **AVOID:** warm/muted palettes, daylight flatness, cartoon proportions, anything NSFW.

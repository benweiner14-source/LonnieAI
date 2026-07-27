---
description: Transform photos or scene descriptions into the WWE 2K in-game / entrance presentation aesthetic. Use for any "WWE 2K style," "2K wrestling look," or theatrical sports-entertainment game render for an athlete.
---

# WWE 2K Style — Image Prompt Generator

Transform real photos or scene descriptions into the **WWE 2K** in-game aesthetic (Visual
Concepts' 2K sports engine, theatrical entrance/ring presentation) using Higgsfield GPT
Image 2, retargeted to **9:16 vertical**.

> Same 2K-engine rendering DNA as the NBA 2K skill (`../nba2k-style/`), turned up for
> **sports-entertainment theater**: heavy sweat/oil sheen on muscle, dramatic stage lighting,
> pyro, and hero entrance framing. Use this when you want a more cinematic, high-drama look
> for the athlete than the clean gym look.
>
> **Reference library:** drop WWE 2K character renders / entrance screen grabs into `reference/`.

> **⚠️ Brand safety:** this file references the real "WWE 2K" game internally as the aesthetic
> we're describing — fine for OUR understanding. But the actual **prompt text sent to the image
> model must never name a real game, league, promotion, or studio** — doing so caused real
> NBA/2K/WWE logos and league branding to leak into outputs elsewhere in this project. **Use the
> already-genericized, paste-ready prompts in `prompts/zion-clark.md`** for actual generation.
> New prompts built from this file should describe the *aesthetic* (theatrical wrestling-sim CGI
> render) — never the brand — and end with "no real promotion/league logos or brand trademarks."

---

## When to Use

User says: "WWE 2K style," "2K wrestling render," "entrance look," or provides an athlete
photo and asks for the dramatic sports-entertainment treatment.

---

## Core Style DNA

WWE 2K shares the **polished-CG, identifiably-rendered** 2K-engine base, but pushes
**muscular definition, oiled-skin specular, and theatrical arena lighting** — the athlete is
a hero on a stage, not in a gym.

### Rendering
- Real-time 3D game-engine quality — high polygon, clean surfaces, PBR materials.
- **Oiled/sweaty muscle sheen** is the signature tell: strong specular highlights raking
  across shoulders, chest, arms, and back; wet skin catching stage lights.
- Face-scanned hero fidelity: detailed but smooth skin, slightly waxy subsurface scattering,
  plastic sheen on forehead and cheekbones.
- **Tattoos as clean decal textures** following the body's contours.
- Ring/entrance gear (spandex, leather, mesh, chrome studs, championship belt plates) with
  crisp material detail and metallic specular on the belt.
- Clean geometry; no film grain or photographic noise (this is a game render).
- **Simplified hair** as volumetric shapes / texture maps, not strand-level.

### Characters
- Hyper-defined, **oiled musculature**; heroic, powerful posing.
- Warm skin tones with strong highlight rolloff; expressive, intense face.
- Entrance gear, wrist tape, kneepads, custom boots; optional championship belt over the shoulder.
- Background crowd rendered as a lower-fidelity mass — thousands of small figures, phone-light
  sparkles, gradual detail falloff into a dark blur.

### Lighting
- **Theatrical stage lighting:** hard colored spotlights, follow-spots, LED stage wash,
  strobe/beam effects, backlit silhouette moments at the entrance.
- Strong **rim and edge light** carving the athlete out of a dark arena.
- Ring is bright and evenly lit for action; entrance ramp is dramatic and high-contrast.
- Optional **pyrotechnics** — sparks, flame jets, cold-spark fountains casting warm light.

### Camera
- **Entrance walkout hero shot:** low angle looking up at the athlete against the stage/LED
  screen, dramatic and poster-like.
- Ring-action medium shots; turnbuckle pose; dramatic close-ups on the intense face.
- Broadcast replay framing.
- Vertical **9:16** by default — tall stage/LED behind, athlete centered, ramp/foreground below.

### Color
- High-contrast and saturated on the stage lighting (colored beams — often team/brand colors),
  deep black arena around it.
- Warm skin against cool or colored stage wash; metallic gold/silver on the belt.
- More dramatic and saturated than the clean NBA 2K gym look.

---

## Base Prompt Template

Replace `[SCENE DESCRIPTION]` with the specific content.

```
WWE 2K video game screenshot, 2K sports engine, in-game render. [SCENE DESCRIPTION]. Real-time 3D rendered, high-polygon game engine quality. Oiled muscular skin with strong specular sheen on shoulders, chest, and arms; plastic subsurface sheen on the face; sweat highlights. Tattoos as clean decal textures. Theatrical arena stage lighting with hard colored spotlights and strong rim light carving the athlete out of a dark arena. Simplified hair as texture maps. Low-angle hero entrance framing, dramatic and poster-like. High contrast, saturated stage color against deep black. Clean geometry, no film grain. 9:16 vertical aspect ratio. WWE 2K sports-entertainment cutscene aesthetic.
```

---

## Scene Type Modifiers

### Entrance Walkout / Stage
```
Athlete walking out onto the entrance stage, giant LED video wall behind glowing with light, pyro fountains shooting cold sparks, follow-spot beams cutting through haze, dark packed arena crowd with phone lights sparkling at low detail, entrance ramp leading to the ring, dramatic low-angle silhouette-into-light hero framing.
```

### In the Ring
```
Inside a brightly lit wrestling ring, ropes and turnbuckles with padded covers, canvas mat, championship logos, dark arena crowd surrounding at reduced detail, overhead truss lighting, athlete in a heroic pose center-ring, sweat sheen catching the lights.
```

### Turnbuckle / Victory Pose
```
Athlete standing on the turnbuckle arms raised in a victory pose, backlit by stage lighting and pyro, dark roaring crowd below at low fidelity, dramatic rim light and lens-flare-free clean render, epic low-angle hero framing.
```

### Gym (Dramatic 2K)
```
Dark, moody strength gym lit like a WWE 2K scene — hard rim and spotlights on the oiled, muscular athlete mid-lift, equipment and background in deep shadow, saturated accent lighting, high-contrast heroic framing (more theatrical than the clean NBA 2K gym look).
```

### Broadcast Portrait (Close-Up)
```
WWE 2K broadcast close-up, hero athlete at maximum fidelity, intense expression, oiled skin with strong specular and sweat highlights, decal tattoos, championship belt over the shoulder, dark arena bokeh behind with colored stage-light glow, dramatic lighting.
```

---

## How to Use with a Reference Photo (Zion)

1. Describe the athlete from the reference photo (build, pose, wardrobe, expression).
2. Plug that into `[SCENE DESCRIPTION]` plus the appropriate scene modifier.
3. In Higgsfield GPT Image 2, attach the reference photo (image-to-image), set 9:16.
4. Add: `Based on the composition, likeness, and framing of the provided reference photo.`
5. Keep it heroic and SFW — powerful, intense, aspirational.

### Look: full CGI render
Everything is the WWE 2K engine — athlete *and* arena/stage (an in-game shot). (The
composited-into-a-photo look was dropped — GPT Image 2 couldn't hold it.)

---

## Example Prompts

**Entrance walkout, full-render:**
```
WWE 2K video game screenshot, 2K sports engine, in-game render. A powerful muscular athlete in custom entrance gear walking onto the stage, arms slightly raised, intense focused face. Giant LED wall glowing behind, cold-spark pyro fountains, follow-spot beams through haze, dark packed crowd with phone lights at low detail. Oiled skin with strong specular sheen, plastic face sheen, decal tattoos, simplified hair. Hard colored stage lighting, strong rim light against black arena, high contrast. Low-angle hero framing, poster-like. Clean geometry, no grain. 9:16 vertical. WWE 2K aesthetic.
```

**Turnbuckle victory, full-render:**
```
WWE 2K video game screenshot, 2K sports engine, full in-engine render of character and arena. An athlete on the turnbuckle, arms raised in victory, backlit by stage lighting and pyro — oiled muscular sheen, decal tattoos, plastic face sheen, clean CG geometry. Dark roaring crowd and arena all rendered in-engine. Dramatic rim light, saturated colored beams, epic low-angle hero framing. 9:16 vertical. Based on the likeness / Soul ID.
```

---

## Tool Guidance

- **Tool:** Higgsfield GPT Image 2. **Aspect ratio:** 9:16, resolution 2k, quality high.
- **Reference photo:** attach it (image-to-image); add the "based on the provided reference
  photo" line for likeness.
- **Generate 2–3 variants** per prompt — pick the most heroic.
- **DO keep:** oiled muscle specular, sweat, theatrical stage lighting, pyro, decal tattoos,
  strong rim light, clean geometry.
- **AVOID:** film grain and photographic artifacts (it's a game render), flat/even daylight,
  cartoon proportions, anything that reads as un-heroic.

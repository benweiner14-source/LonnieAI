---
description: Transform photos or scene descriptions into the Grand Theft Auto VI (Rockstar RAGE engine) in-game look. Use for any "GTA VI style," "GTA 6 look," "Vice City render," or Rockstar cinematic treatment.
---

# GTA VI Style — Image Prompt Generator

Transform real photos or scene descriptions into the **Grand Theft Auto VI** in-game
aesthetic (Rockstar's modern RAGE engine, Vice City / Leonida setting) using Higgsfield
GPT Image 2.

> Built as a fork of the NBA 2K cutscene skill. Same method — codified rendering *tells*,
> a base template, and scene modifiers — retargeted to Rockstar's photoreal-satirical look
> and **9:16 vertical** for Snapchat/Facebook.
>
> **Reference library:** drop in-game screen grabs (GTA VI Trailer 1 & 2, cover art, GTA V
> photo-mode) into `reference/` to sharpen accuracy. `gtav_keyart` is included as a starter.

---

## When to Use

User says: "make this GTA VI," "GTA 6 style," "put her in Vice City," "Rockstar render,"
or provides a photo and asks for the in-game open-world treatment.

---

## Core Style DNA

The GTA VI look is **grounded photorealism with a heightened, glossy, sun-soaked edge** —
it reads as a very high-end modern game engine, not a photograph and not a cartoon.
Rockstar's signature is "reality, but 10% more saturated, cinematic, and satirical."

### Rendering
- Modern RAGE-engine fidelity: high geometric detail, physically based materials, dense
  environment detail (foliage, wet asphalt, chrome, glass).
- Skin is realistic with visible pores and fine detail, but carries a subtle **humid sheen**
  — Florida heat: a light sweat/oil specular on foreheads, collarbones, shoulders.
- Strong **screen-space reflections** on wet roads, car paint, glass, water.
- Volumetric light and atmospheric haze — golden-hour god rays, humid air, heat shimmer.
- Cinematic **teal-and-orange color grade**, slightly crushed blacks, punchy HDR bloom on
  neon and sun highlights.
- Mild film-like softness (TAA), gentle lens flare on bright sources. Not clinically clean —
  a touch of cinematic grain is acceptable (unlike the 2K look).
- Realistic cloth simulation — fabric drapes and wrinkles naturally (more than the 2K look).

### Characters
- **Realistic human proportions** — grounded, not stylized or exaggerated. This is the key
  difference from cartoonish game looks.
- Detailed, expressive faces; realistic modern hair with strand-level detail (a big step up
  from older GTA — do NOT render hair as flat texture maps here).
- Tattoos rendered realistically on skin; jewelry, gold chains, and grills catch specular.
- Wardrobe leans Miami: swimwear, crop tops, linen, athleisure, streetwear, gold accents,
  designer sunglasses, acrylic nails.
- Slightly **poster-like confidence** in posing — Rockstar characters are always framed like
  they belong on the cover.
- Background NPCs at lower detail; crowds on the beach/strip render with variation but less
  crispness than the foreground hero.

### Lighting
- **Golden-hour and sunset** are the signature: warm orange/pink/purple skies, long shadows,
  rim light on subjects.
- Night scenes are **neon-lit** — Vice City signage in hot pink, cyan, and purple reflecting
  off wet surfaces and car paint.
- High dynamic range: bright blown-highlight sun, deep shadow, strong contrast.
- Practical light sources everywhere (neon, headlights, phone screens, club lighting).

### Camera
- Cinematic and **poster-forward** — bold, confident framing like GTA cover art and loading
  screens.
- **Low hero angles** looking up at the subject against sky or neon.
- Wide establishing shots of Vice City skyline, beach, causeway, Everglades.
- Medium and full-body fashion framing (this is a lifestyle/fashion use case).
- Vertical **9:16** by default — compose for a tall phone frame (subject centered, headroom
  for sky/neon, foreground road/sand).

### Color
- **Daytime:** saturated tropical — turquoise water, white sand, coral and mint pastels,
  palm green, chrome, hot car-paint colors.
- **Sunset:** orange → magenta → violet gradient skies, golden skin.
- **Night:** neon pink + cyan + electric purple, deep blue shadows, warm sodium streetlights.
- Overall grade is warm, saturated, and cinematic — never muted or gray.

---

## Base Prompt Template

Replace `[SCENE DESCRIPTION]` with the specific content.

```
Grand Theft Auto VI video game screenshot, Rockstar RAGE engine, in-game render. [SCENE DESCRIPTION]. Grounded photorealistic 3D render with realistic human proportions and detailed strand-level hair. Physically based materials, wet specular reflections, humid Florida sheen on skin. Cinematic teal-and-orange color grade, saturated tropical palette, golden-hour bloom. Volumetric light and atmospheric haze. Poster-like confident composition, low hero camera angle. 9:16 vertical aspect ratio. High-end modern open-world game engine, Vice City aesthetic — heightened, glossy, satirical realism, not photographic and not cartoon.
```

---

## Scene Type Modifiers

Append to the base template depending on the environment.

### Vice City Nightlife (Neon Strip)
```
Vice City nightlife on Ocean Drive, art-deco hotels with hot-pink and cyan neon signage, wet reflective asphalt, palm trees strung with lights, convertibles and neon-underlit supercars parked at the curb, distant skyline glow, warm humid night air with neon bloom, club entrance with velvet rope. Deep blue night shadows cut by saturated neon.
```

### Vice Beach / Daytime Coast
```
South Beach / Vice City coastline at golden hour, turquoise ocean, white sand, art-deco pastel buildings (mint, coral, cream), lifeguard towers, palm trees, parked convertible, jet skis on the water, warm low sun casting long shadows and rim light, saturated tropical color, atmospheric heat haze.
```

### Luxury / Exotic Car
```
Posed with a glossy exotic supercar (convertible or low sports car) in Vice City, chrome and candy car paint catching neon or sunset reflections, gas station or palm-lined boulevard backdrop, gold jewelry glinting, classic GTA cover-art energy — confident low-angle hero framing of subject leaning on or beside the car.
```

### Penthouse / Rooftop
```
Vice City luxury penthouse or rooftop pool at dusk, floor-to-ceiling glass overlooking the neon skyline, infinity pool reflecting purple sky, modern designer furniture, palm plants, warm interior practical lighting, city lights bokeh in the distance, glamorous lifestyle staging.
```

### Everglades / Backcountry
```
Leonida backcountry / Everglades at humid golden hour, airboat or lifted truck, tall saw-grass wetlands, cypress trees, warm hazy light, distant thunderheads, muddy earth tones contrasting with a saturated sky — Rockstar's rural satirical Americana.
```

### Downtown / Skyline Establishing
```
Wide establishing shot of the Vice City skyline at sunset or night, causeway and palm-lined boulevards, glass towers with neon crowns, traffic light trails, dramatic tropical sky, cinematic scale — subject small in a grand poster-like composition or foreground on a rooftop.
```

---

## How to Use with a Reference Photo (Kazumi)

1. Describe the subject from the reference photo (pose, wardrobe, hair, expression).
2. Plug that into `[SCENE DESCRIPTION]` plus the appropriate scene modifier.
3. In Higgsfield GPT Image 2, attach the reference photo (image-to-image) and set 9:16.
4. Add: `Based on the composition, likeness, and framing of the provided reference photo.`
5. Keep it **SFW / glam-but-clothed** — swimwear/streetwear is fine; no nudity or explicit posing.

### Look: full CGI render
Everything is the GTA VI engine — subject *and* environment (an in-game shot). Emphasize
"in-game render, stylized game character." (The composited-into-a-photo look was dropped.)

---

## Example Prompts

**Vice City neon night, full-render:**
```
Grand Theft Auto VI video game screenshot, Rockstar RAGE engine, in-game render. A confident young woman with long dark hair in a cropped designer top and gold hoops, leaning against a neon-underlit convertible on Ocean Drive at night. Art-deco hotels with hot-pink and cyan neon, wet reflective asphalt, palm trees with lights, distant skyline glow. Grounded photorealistic render, realistic proportions, strand-level hair, humid sheen on skin, wet specular reflections. Cinematic teal-and-orange grade, neon bloom, deep blue night shadows. Low hero camera angle, poster-like composition. 9:16 vertical. Vice City aesthetic — glossy satirical realism.
```

**Luxury car sunset, full-render:**
```
Grand Theft Auto VI video game screenshot, RAGE engine, full in-game render of character and environment. A young woman in a linen set and designer sunglasses seated on the hood of a glossy candy-orange supercar at golden hour, palm-lined Vice City boulevard behind — all rendered in-engine. Rockstar render look — humid skin sheen, saturated grade, gold jewelry catching sunset light, long shadows, atmospheric haze. Confident low-angle hero framing. 9:16 vertical. Based on the likeness / Soul ID. SFW.
```

---

## Tool Guidance

- **Tool:** Higgsfield GPT Image 2. **Aspect ratio:** 9:16, resolution 2k, quality high.
- **Reference photo:** attach it (image-to-image) for likeness; add the "based on the
  provided reference photo" line.
- **Generate 2–3 variants** per prompt — pick the best.
- **DO keep:** cinematic grade, humid sheen, neon bloom, realistic hair, wet reflections.
- **AVOID:** cartoon/stylized proportions, flat texture-map hair, muted gray palettes,
  anything NSFW.

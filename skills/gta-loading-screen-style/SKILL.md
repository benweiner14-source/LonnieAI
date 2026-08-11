---
description: Painted, illustrated key-art style — like official open-world crime-saga loading-screen and promotional artwork (visible brushwork, bold contour lines, dramatic saturated lighting, poster composition). A DIFFERENT RENDERING MEDIUM from the other styles — painted 2D illustration, not a 3D game-engine render. Use for "loading screen art," "key art," "painted GTA style," or "artwork diffusion" style requests.
---

# GTA Loading-Screen Art Style — Image Prompt Generator

> **⚠️ This is a genuinely different medium than every other style in this repo, not just a
> different look.** `gta6-style`, `cyberpunk-2077-style`, `nba2k-style`, `wwe2k-style`, and
> `iphone-selfie-style` are all **3D real-time game-engine renders** — that's the project's
> locked "full CGI render" decision. This style is **painted digital illustration** — the kind of
> semi-realistic, painterly key art used for official open-world crime-saga loading screens and
> promotional artwork. There is no 3D render happening in the fiction of the image at all; it's a
> painting. Built at Ben's explicit request as a deliberate new style option, the same way
> `iphone-selfie-style` was — not a reversal of the CGI-render decision for the other 4 styles,
> just a new one that happens to use a different medium. **Don't blend this with the "obviously
> computer-generated, in-engine" language used everywhere else** — that phrasing is specifically
> wrong for this style; use the painted-illustration language below instead.

> **⚠️ Brand safety — same standing rule.** Never name the real game, franchise, or studio this
> art style is associated with in the prompt text, and never reproduce any readable in-world text
> (game titles, location names) even if it's visible in a reference image — describe the
> *aesthetic only* ("painted, stylized open-world crime-saga key art").

---

## When to Use

User asks for "loading screen art," "key art," "painted [game] style," "artwork diffusion," or
references an art-style LoRA/model built on official game key-art (as opposed to in-game
screenshots) — a strong signal they want the painted-illustration look, not another 3D render.

---

## Core Style DNA

### Medium
- **Semi-realistic painted digital illustration** — NOT a 3D game-engine render, NOT a
  photograph. Think painted movie-poster/key-art, not an in-game cutscene screenshot.
- **A clear rendering-detail hierarchy from figure to background.** The hero character's skin and
  face are the most refined element — smooth, semi-realistic painted/airbrushed shading, not
  heavily-textured brushstrokes. The environment (buildings, vehicles, foliage) is noticeably
  more simplified and flat-shaded by comparison — bold color-blocked shapes with less painterly
  detail than the figure gets. Don't render the background at the same fidelity as the character.
- **Hair rendered in chunky, defined locks/strands with painted highlight strokes** — not
  individually-rendered fine CG hair strands, and not a flat solid shape either.
- **Clothing has crisp, bold contour linework** defining fold shapes, filled with painted gradient
  shading rather than fabric texture or photographic detail.
- Bold contour linework separating the figure from the background generally — a graphic,
  illustrated edge, not a soft photographic falloff.

### Lighting & Color
- **Signature lighting move: a warm backlight/rim light from a dramatic dusk or sunset sky**
  (orange-gold or purple-pink gradient) — glows the hair and shoulders from behind/above while the
  figure's front, facing camera, often reads at slightly lower contrast. This rim-lit-against-a-
  gradient-sky move is the single most identifiable trait of this look — lead with it.
- **A soft glowing light disc (sun or an equivalent strong source) directly behind or near the
  head** creates a radiant halo — a distinct atmospheric device on top of the rim-light, not the
  same thing. Worth naming separately since it reads as a specific "tell" of this style.
- **Color grading is vivid and punchy, not muted** — this is a real point of contrast against
  this project's 3D-render styles, which explicitly use muted/desaturated broadcast grading. This
  style should say the opposite: bold, saturated, poster-vivid color.

### Composition
- Poster/key-art composition: strong visual hierarchy, a clear hero subject, a confident dynamic
  pose — direct gaze or a knowing expression toward camera, marketing-poster energy rather than a
  candid in-game moment.
- **Confident "prop in hand" body language** — a deliberately posed item held at a specific angle
  (bag, phone, drink, sunglasses — whatever fits the scene) reads as on-style; an empty, relaxed
  hand reads as more generic. Give her something to hold/gesture with when the scene allows it.
- **Eyewear, when present, gets a couple of sharp painted highlight strokes on flat-colored
  lenses** rather than photoreal reflections — same painted-illustration logic as the rest of the
  face.
- **Optional alternate composition:** the hero figure isolated against a plain dark background,
  with the environment shown as a separate framed "inset" behind/beside her, like a poster
  layout — not the default, but a legitimate variant worth having in the back pocket for a
  portrait-style scene.
- Realistic human anatomical proportions rendered in the painted technique — **not**
  Disney/Pixar/animated-movie cute-and-rounded, and not photoreal either. This is its own third
  lane between those two failure modes.

### Camera
- Same 9:16 vertical and off-center/varied framing discipline as every other pack — no two scenes
  centered the same way.

---

## Base Prompt Template

```
[SCENE / CHARACTER DESCRIPTION]. Rendered as painted, stylized open-world crime-saga key art — a semi-realistic painted digital illustration, NOT a 3D game-engine render, NOT a photograph. The character's skin and face are rendered with smooth, semi-realistic painted/airbrushed shading — the most refined element in the image — while the surrounding environment is noticeably more simplified, flat-shaded, and graphic by comparison. Hair rendered in chunky defined locks with painted highlight strokes; clothing has crisp bold contour linework filled with painted gradient shading. Warm backlight/rim light from a dramatic dusk or sunset sky glows the hair and shoulders, with the figure's front reading at slightly lower contrast facing camera. Vivid, saturated, poster-punchy color grading — not muted or desaturated. Confident, dynamic hero pose with a direct or knowing gaze toward camera, poster/key-art composition with strong visual hierarchy. Realistic human anatomical proportions in the painted technique — NOT a Disney/Pixar/DreamWorks animated-movie style, NOT cartoon-stylized or cute/rounded. No real game, studio, brand logos, or readable text/signage anywhere in the output. 9:16 vertical.
```

---

## Tool Guidance

- Same multi-image role-tagging approach as the other styles for Comfy Cloud / Nano Banana Pro —
  face reference(s) + any relevant body/tattoo refs + a style reference, each with one explicit
  job. The **style role text must say "painted illustration," not "CGI game-engine render"** —
  reusing the wrong style-role block is the most likely mistake when forking a scene from another
  pack into this one.
- Same guardrail discipline as everywhere else: 3–4 seed variants per prompt, discard anything
  that leaks a real logo/title or drifts toward photoreal/Disney instead of painted key-art.

### Style reference images

`reference/` holds 5 official key-art stills, cropped by Ben to remove the studio wordmark/logo,
used purely to anchor the rendering *technique* (never the specific character/pose — always
role-tag "ignore the character/likeness in this reference, use ONLY for rendering technique"):

- **`cinema_doppler.jpg`** — recommended primary. Clean single-character composition, clearest
  example of the signature rim-light + halo-glow lighting move and the painted skin/hair/clothing
  technique all in one frame. Carries readable fictional signage ("Cinema Doppler," "Tsunami") —
  standard "do not reproduce readable text" instruction applies, same as every other style ref.
- **`arrest_scene.jpg`** — clean, no logo or readable studio text at all. Two-character
  composition, good for scenes needing that.
- **`franklin_gun.jpg`** — clean. Good example of the isolated-hero-on-dark-background composition
  variant (see Composition section above).
- **`flapper_couple.jpg`** — clean of the studio logo, but has a partial fictional landmark sign
  ("...EW OO D") visible in the background — same "ignore readable text" handling applies.
- **`couple_car_LOGO_NOT_CROPPED.jpg`** — **⚠️ do not use as-is.** Still has a visible studio star
  logo in the bottom-right corner; needs a tighter crop before it's usable as a style reference.

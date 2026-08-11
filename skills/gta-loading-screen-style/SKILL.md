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
- Visible painterly brushwork and texture; simplified, confidently-rendered forms rather than
  photoreal or CG-smooth detail.
- Bold contour linework separating the figure from the background — a graphic, illustrated edge,
  not a soft photographic falloff.

### Lighting & Color
- Dramatic directional lighting: deep, contrasty shadows and a strong rim/backlight, the way
  poster art exaggerates light for impact.
- Vibrant, saturated color grading — sunset oranges, hot magentas, cool teals — more graphic and
  poster-like than the muted broadcast grading used in the 3D-render styles.

### Composition
- Poster/key-art composition: strong visual hierarchy, a clear hero subject, confident dramatic
  pose — built to read instantly at a glance, the way marketing key art is designed to.
- Realistic human anatomical proportions rendered in the painted technique — **not**
  Disney/Pixar/animated-movie cute-and-rounded, and not photoreal either. This is its own third
  lane between those two failure modes.

### Camera
- Same 9:16 vertical and off-center/varied framing discipline as every other pack — no two scenes
  centered the same way.

---

## Base Prompt Template

```
[SCENE / CHARACTER DESCRIPTION]. Rendered as painted, stylized open-world crime-saga key art — a semi-realistic painted digital illustration, NOT a 3D game-engine render, NOT a photograph. Visible painterly brushwork and simplified confident forms, bold contour linework separating the figure from the background, dramatic directional lighting with deep contrasty shadows and a strong rim light, vibrant saturated color grading. Poster/key-art composition with strong visual hierarchy. Realistic human anatomical proportions in the painted technique — NOT a Disney/Pixar/DreamWorks animated-movie style, NOT cartoon-stylized or cute/rounded. No real game, studio, brand logos, or readable text/signage anywhere in the output. 9:16 vertical.
```

---

## Tool Guidance

- Same multi-image role-tagging approach as the other styles for Comfy Cloud / Nano Banana Pro —
  face reference(s) + any relevant body/tattoo refs + a style reference, each with one explicit
  job. The **style role text must say "painted illustration," not "CGI game-engine render"** —
  reusing the wrong style-role block is the most likely mistake when forking a scene from another
  pack into this one.
- No dedicated style-reference screenshot exists yet — carried by prompt text alone for now. If a
  clean example of this painted key-art look turns up (without real game-title text baked into
  it), add it as a style ref the same way the other packs do.
- Same guardrail discipline as everywhere else: 3–4 seed variants per prompt, discard anything
  that leaks a real logo/title or drifts toward photoreal/Disney instead of painted key-art.

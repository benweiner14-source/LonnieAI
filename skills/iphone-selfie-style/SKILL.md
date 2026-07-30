---
description: Transform a CGI game-character scene into an iPhone-selfie-camera aesthetic — wide-angle lens distortion, close framing, on-camera flash, chaotic energy — while the ENTIRE frame (character and environment) stays a full CGI render, same as the other styles. Use for any "selfie style," "phone camera," or "iPhone selfie" look.
---

# iPhone Selfie Style — Image Prompt Generator

This is a **camera/photography style**, not a look-category change. Like the gta6, cyberpunk,
nba2k, and wwe2k styles, the **entire frame renders in the CGI game engine — character AND
environment together, in one unified style.** What's different here is *what kind of shot it
is*: instead of a cinematic game-cutscene camera, it's shot like a real iPhone front-facing
selfie — close, wide-angle-distorted, flash-lit, chaotic.

> **This project already locked "full CGI render" as the only look** — we dropped compositing
> a CGI character into a real photoreal background because the model couldn't hold it cleanly.
> This style does not reverse that. Nothing in the frame is a real photograph; the crowd, the
> lights, the background, the skin — all of it renders in-engine. Only the *camera language*
> (lens distortion, flash falloff, motion blur, framing) borrows from real selfie photography,
> the same way the other styles borrow their camera language from broadcast or cinematic
> photography. If an output reads as "CGI person pasted onto a real photo," that's a miss —
> re-render, don't ship it.

> **⚠️ Brand safety:** never name real teams, leagues, games, or people in the prompt text, and
> never reference a real event (a specific championship, a specific date/team win). Describe the
> *aesthetic only* — a generic celebratory crowd, generic city night scene — same rule as every
> other style in this repo.

---

## When to Use

User says "iPhone selfie style," "selfie cam," "phone camera look," or wants the character
shooting a selfie of themselves in a chaotic/high-energy moment, still fully CGI.

---

## Core Style DNA

### Rendering
- Still a real-time 3D game-engine render, top to bottom — no real photographic elements
  anywhere in the frame. Skin, crowd, background, light sources: all CGI.
- The "iPhone camera" is simulated digitally: barrel-distortion wide-angle lens warp (strongest
  at the frame edges), a hard on-axis flash light source that falls off sharply with distance
  (subject near-camera is blown-out bright, background falls to near-black between light
  sources), simulated sensor noise/grain and slight motion blur on fast-moving elements —
  all as a rendered *effect*, not an actual photo layered in.
- Everything the flash would hit (the hero character, anyone/anything close to camera) gets
  the same hard flash falloff — keeps the whole frame in one consistent rendered "shot," not
  two mismatched layers.

### Characters
- Face large and close to the lens, exaggerated slightly by the wide-angle warp — a genuine
  selfie framing, not a standard portrait crop.
- Same subsurface-scattering CGI skin / simplified rendered hair / clean CG geometry as the
  other styles — this is still obviously a rendered character, not a photoreal human.
- Expression should read as high-energy / mid-celebration / mid-reaction — the selfie is being
  taken *in the moment*, not posed.

### Lighting
- Hard, direct, on-camera flash as the dominant light source — flat, slightly blown-out on the
  near subject, falling off fast into darker midground and background.
- Ambient scene light (neon signs, streetlights, other flashes in the crowd) rendered as
  scattered secondary sources, out-of-focus and soft where the flash doesn't reach.

### Camera
- **This must be a true first-person POV shot — the render's own camera position IS the phone's
  front-facing lens, held at arm's length by the character themselves. There is no external
  observer or second camera in this scene; do NOT render a third-person view of the character
  holding up a phone.** This is the single most common failure mode for this style: the model
  defaults to a documentary-style shot of someone taking a selfie (full body visible, wide view
  of the whole crowd/scene from several feet back) instead of actually becoming the phone's lens.
- Frame accordingly: the character's face and upper torso/shoulders fill most of the frame; their
  extended arm and the top edge of the phone enter the frame in the foreground. **Nothing below
  the waist is visible, and the background is only the narrow slice of the scene the phone's lens
  would actually catch at arm's length** — not a wide establishing shot of the full environment
  or a crowd shot spanning many feet in every direction.
- Selfie framing by definition: close, arm's-length distance, subject slightly off-axis (not
  perfectly centered — a real arm-extended shot has natural tilt/asymmetry).
- Wide-angle lens distortion (roughly an 18–24mm-equivalent selfie lens): curved perspective,
  stronger warp near the frame edges — this widens the field of view somewhat, but does not turn
  it into a wide shot of the whole scene from a distance.
- Vertical **9:16** — this is a phone-native format already, so it should feel natural here.

### Color
- Slightly cool/blown-out highlights where the flash hits, deep contrasty shadows elsewhere —
  the classic hard-flash-at-night palette, rendered rather than photographed.
- Background color comes from rendered environment light sources (signage, other lights), kept
  soft/out-of-focus relative to the sharp flash-lit foreground.

---

## Base Prompt Template

```
This image IS the photo captured by the character's own phone front-facing camera, held at arm's length in their own hand — the render's camera position IS the phone's lens itself. This is NOT a third-person shot of someone else photographing the character; there is no external observer or second camera anywhere in this scene. A CGI video-game character taking a selfie, rendered entirely in a real-time 3D game engine — the character AND the environment behind them both render in the same CGI style, nothing photoreal anywhere in frame. [SCENE / CROWD / ENVIRONMENT DESCRIPTION, described only in generic terms — no real teams, leagues, games, or events]. Framing is a true arm's-length selfie: the character's face and upper torso fill most of the frame; their extended arm and the top edge of the phone enter the frame in the foreground; nothing below the waist is visible. The background is only the narrow slice of the scene the phone's lens would actually catch at arm's length — NOT a wide shot of the full environment or a crowd spanning many feet in every direction. Simulated wide-angle selfie-lens distortion, strongest at the frame edges. Hard, direct, on-camera flash lighting the character with sharp falloff into the darker background — anything within the phone's actual field of view catches the same flash. Slightly off-center with natural arm's-length selfie tilt, expressive mid-moment reaction. Simulated sensor grain and slight motion blur on the visible background sliver, all rendered as part of the CG shot, not composited from a real photo. Clean CG geometry, subsurface-scattering skin, simplified rendered hair. 9:16 vertical. No real logos, brand names, or trademarks anywhere in frame.
```

---

## Tool Guidance

- Works the same way as the other three styles: multi-image role-tagging in Comfy Cloud / Nano
  Banana Pro (face + body/tattoo + this style's cues folded into the scene description), or a
  single flowing paragraph for Higgsfield.
- No dedicated style-reference screenshot exists for this look yet (unlike the 2K/GTA/Cyberpunk
  packs, which point at real game screenshots) — the aesthetic is carried by prompt text alone
  for now. If a clean CGI-selfie-style reference image turns up later, add it as a style ref.
- Keep the "fully CGI, nothing photoreal" instruction explicit and early in the prompt — this is
  the detail most likely to drift toward a composited-onto-a-real-photo read if dropped.
- Generate 3–4 seed variants and discard anything that reads as a real photo with a CGI figure
  pasted in, same discipline as the other styles.

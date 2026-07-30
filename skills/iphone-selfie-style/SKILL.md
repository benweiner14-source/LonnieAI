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

> **⚠️ POV lesson (v2 fix — read before writing a new scene):** the first version of this style
> tried to force first-person POV with meta/technical instructions ("the render's camera position
> IS the phone's lens," "this is NOT a third-person shot") — it still rendered third-person: a
> documentary-style photo of the character holding up a phone, full body, wide crowd, several feet
> back. **Meta camera-position language and negations don't reliably steer composition.** What
> actually works (confirmed by Ben's own working Higgsfield prompt, which used this exact
> structure): **lead the prompt with the photographic genre itself** — "A real iPhone
> front-facing selfie photo of [character], taken in [scene]" — as the very first clause, before
> any rendering/CGI language. "Selfie photo" is such a strong, specific composition in the
> model's training data that naming the genre up front does more work than any amount of explicit
> camera-position instruction after the fact. Follow it with concrete, physical framing language
> ("face large and close to the lens, wide-angle selfie distortion, one arm extended holding the
> phone") rather than abstract instructions about where the camera "is." Don't add "not
> third-person" negations — describe the correct shot positively and let the genre anchor do the
> work.

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
- **Lead the prompt with the genre, not a camera-position instruction:** "A real iPhone
  front-facing selfie photo of [character], taken in [scene]." Say this before introducing any
  CGI/rendering language. This is what actually locks first-person POV — see the lesson box
  above. Meta instructions ("the camera IS the phone's lens") and negations ("NOT third-person")
  are weaker than genre-anchoring and shouldn't be relied on alone.
- Concrete, physical framing language, not abstract camera-position language: face large and
  close to the lens, one arm extended holding the phone, wide-angle selfie distortion. This reads
  the same as Ben's own proven wording — keep it that plain and physical.
- Selfie framing by definition: close, arm's-length distance, subject slightly off-axis (not
  perfectly centered — a real arm-extended shot has natural tilt/asymmetry). Nothing below the
  character's torso should be described or implied.
- The crowd/background should be described as physically close and cropped by the frame edges
  ("packed tightly right up against the camera, bodies overlapping and partly cropped") rather
  than as a wide establishing shot — this concrete imagery does more to keep the shot
  close-in than an abstract "limited to the phone's field of view" instruction does.
- **Rectangular frame, no circular vignette.** "Wide-angle lens distortion" alone has been
  misread as an actual fisheye action-cam look — a circular vignette with dark rounded corners.
  Real phone selfies are rectangular with only a subtle barrel/perspective stretch near the
  edges. Say so explicitly: no circular crop, no dark vignette corners, just the normal 9:16
  rectangular frame.
- **Phone screen must not be visible.** A second failure mode: the model renders the held phone
  showing its own screen with an image on it (a photo-within-a-photo / a second face), instead of
  using the phone as the camera taking this shot. If the phone enters frame at all, only its
  plain back or edge should show — never a lit screen, never a displayed photo, never a second
  phone.
- Wide-angle lens distortion (roughly an 18–24mm-equivalent selfie lens): curved perspective,
  stronger warp near the frame edges — but still within a normal rectangular photo, not a fisheye
  crop (see above).
- Vertical **9:16** — this is a phone-native format already, so it should feel natural here.

### Color
- Slightly cool/blown-out highlights where the flash hits, deep contrasty shadows elsewhere —
  the classic hard-flash-at-night palette, rendered rather than photographed.
- Background color comes from rendered environment light sources (signage, other lights), kept
  soft/out-of-focus relative to the sharp flash-lit foreground.

---

## Base Prompt Template

```
A real iPhone front-facing selfie photo of [CHARACTER], taken in [SCENE / CROWD / ENVIRONMENT DESCRIPTION, described only in generic terms — no real teams, leagues, games, or events]. [CHARACTER] is a CGI video-game character rendered in a real-time 3D game engine — smooth subsurface-scattering skin, a subtle polished sheen on the forehead and cheekbones, simplified rendered hair as a clean texture map — clearly a high-fidelity rendered character, not a real photoreal person. Rectangular 9:16 photo — no circular vignette, no dark corners, no fisheye lens crop, just the normal subtle wide-angle perspective of a real phone selfie camera. If the phone enters the frame, only its plain back or edge is visible — never its screen, never a photo displayed on it, never a second phone anywhere in the shot. Face large and close to the lens with wide-angle selfie-lens distortion, [expression], one arm extended holding the phone. Face lit by harsh, direct, on-camera flash with sharp falloff into a darker background — the same flat hard flash lighting anyone/anything near the camera. Behind [him/her], a dense crowd packed tightly right up against the camera, bodies overlapping and partly cropped, faces turned toward the lens, smeared with motion blur — rendered in the same CGI game-engine style as the character, nothing photoreal anywhere in frame. Further back, [environment] dissolves into out-of-focus light streaks and glow, also fully CGI-rendered. Simulated low-light phone-camera artifacts: motion blur, sensor noise, lens haze, slight overexposure where the flash hits — all rendered as part of the CG shot, not composited from a real photo. Clean CG geometry throughout. 9:16 vertical. No real logos, brand names, or trademarks anywhere in frame.
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

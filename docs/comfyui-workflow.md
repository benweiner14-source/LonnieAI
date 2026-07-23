# ComfyUI workflow — CGI character from a real photo (identity + style + pose)

**Why ComfyUI beats GPT Image 2 here:** GPT Image 2 gives one hidden "edit strength" knob and
treats every input image as content, so it either keeps the photo photoreal or drops your style
reference. ComfyUI lets you condition **identity, style, and pose separately, each with its own
weight** — exactly what "recognizably Zion, but obviously a CGI game character, in his real pose"
needs.

## The core idea (three independent controls)
1. **Identity** — lock the face from Zion's refs, strongly, *independent of render style*.
2. **Style** — push the base render toward CGI/game-engine with a LoRA and/or a style image.
3. **Pose/body** — hold his real composition (seated / on hands / racing chair — authentic, no
   fabricated legs) with ControlNet.

Tune each weight until it's clearly CGI *and* clearly him.

## Recommended stack

### Option A — SDXL (most plug-ins, easiest to source)
- **Checkpoint:** an SDXL model with a stylized/3D lean (e.g. a "3D render" / "CGI" SDXL
  checkpoint), or base SDXL + a style LoRA.
- **Identity:** **InstantID** (SDXL) or **IP-Adapter FaceID Plus v2**. Feed 3–6 of the
  `creators/zion-clark/refs/soul-id/` face shots. Weight ~0.6–0.85.
- **Style:** a **video-game / 3D-render / "GTA" / "NBA-2K-ish" LoRA** (search Civitai for
  "videogame", "3d render", "GTA", "PS2/PS5 render", "unreal engine character"). Weight ~0.6–1.0.
  *Optionally* add an **IP-Adapter (style)** pointing at a faceless
  `reference-material/2k-screenshots/textures/` crop, weight ~0.3–0.5.
- **Pose/body:** **ControlNet OpenPose + Depth** from his real photo (preserves the exact
  composition — critical for authentic representation). Depth weight ~0.5–0.7.
- **Sampler:** img2img with **denoise ~0.55–0.75** (high enough to restyle, low enough to keep
  him) — or pure txt2img if identity + pose ControlNet are doing the anchoring.

### Option B — Flux (higher base fidelity)
- **Checkpoint:** Flux.1 dev.
- **Identity:** **PuLID (Flux)** — excellent face lock with heavy stylization.
- **Style:** a Flux game-render/3D LoRA + prompt.
- **Pose:** Flux ControlNet (Union / depth).
- Flux holds identity under strong stylization better; needs more VRAM.

## Node graph (Option A, sketch)
```
Load Checkpoint ─┐
Load Style LoRA ─┤→ Model ─┐
                 │         ├→ KSampler → VAE Decode → Save
InstantID/FaceID ┘         │
  (Zion soul-id refs) → conditioning ┘
ControlNet OpenPose ┐
ControlNet Depth    ┤→ conditioning (from his real photo)
Positive/Negative prompt (CGI-enforcement block from forcing-the-cgi-look.md)
[optional] IP-Adapter(style) ← textures/ crop
```

## Prompt (positive)
Reuse the CGI-enforcement wording: `3D CGI video-game character, NBA 2K / Unreal Engine render,
waxy subsurface skin, plastic sheen, clean CG geometry, rendered hair, ambient occlusion,
not a photograph`.
**Negative:** `photograph, photorealistic, real skin pores, DSLR, film grain`.

## Dials to turn if it's...
- **Too photoreal** → raise LoRA weight, raise denoise, lower IP-Adapter identity a touch.
- **Not enough like Zion** → raise InstantID/FaceID weight, add more face refs, lower denoise.
- **Wrong pose / body** → raise ControlNet depth/openpose weight (keep his real composition).

## Hardware / running it
ComfyUI needs a GPU. Options: local NVIDIA (≥12 GB VRAM for SDXL, ≥24 GB comfortable for Flux),
or a cloud GPU (RunPod, Vast.ai, or a hosted ComfyUI). Not runnable in this repo's container
(no GPU), but the workflow above is portable.

## Tradeoff vs Higgsfield
More setup and a GPU, but **decisive control** — this is the standard pipeline for "keep the
person, change the render." If you want, I can author an importable ComfyUI **workflow JSON**
(Option A) wired to Zion's `soul-id/` refs and the CGI prompt as a starting point.

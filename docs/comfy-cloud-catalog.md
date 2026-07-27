# Comfy Cloud catalog — what's available + chosen path

_From `search_models` on Ben's authenticated Comfy Cloud MCP (36 tools)._

## Available
- **Checkpoints:** `realvisxlV50` (SDXL 1.0, **photoreal by default**), `Illustrious-XL` (anime SDXL),
  **`flux1-dev-fp8`** ✓, `flux1-schnell-fp8` (4-step), `pony-diffusion-v6-xl`.
- **Identity:** `ip-adapter-faceid-plusv2_sdxl` (+ companion LoRA) ✓ **SDXL only**; portrait variants.
  **PuLID ❌, InstantID ❌.**
- **Style LoRAs (SDXL):** `sdxl-cyberpunk_anime_style`, `sdxl-midjourney_mimic`, `sdxl-aesthetic_anime`.
  **No GTA / NBA 2K / Unreal / 3D-render LoRA.**
- Note: `Qwen-…-Pixar-Inspired-3D` LoRA exists but needs a **Qwen** checkpoint (not in the checkpoint
  list) → unusable for now.

## The knot
- **Identity is SDXL-only; strong CGI style is easiest on Flux.** They don't currently meet.
- **Custom LoRA upload:** no MCP path (`upload_file` = images only, `/api/upload/image`). Must use the
  Comfy Cloud **web dashboard** (tier-dependent). `get_billing_status` tool does not exist — check the
  dashboard directly.

## STYLE baseline (promising, but NOT the finished output)
Two **no-identity, no-pose** txt2img baselines produced a plausible SDXL CGI look
(`RealVisXL + CGI prompt`, and `+ sdxl-cyberpunk_anime_style @0.45`). Ben's read: **generic and
"pretty bad"** on their own — expected, because FaceID (identity) and ControlNet (body/pose) were
OFF. So the *look* is reachable on SDXL, but the real test is the full pipeline below.

**Note (asked + answered):** GPT Image 2 CAN be called inside ComfyUI (API nodes / `partner_generate`)
but gives **no** stronger face lock or CGI control — it's a closed model; FaceID/ControlNet/LoRA only
attach to open models (SDXL/Flux). So there's no reason to route GPT Image 2 through Comfy.

## Identity: FaceID is BLOCKED on Comfy Cloud — use IP-Adapter Plus Face
**FaceID (any variant) fails**: `IPAdapterFaceID` needs InsightFace `buffalo_l`, which can't
download/initialize in the Comfy Cloud runtime (sandboxed). Dead end.
**Working identity path (confirmed):** `IPAdapterAdvanced` + `ip-adapter-plus-face_sdxl_vit-h`
+ `CLIPVisionLoader` (CLIP-ViT-H) — CLIP-vision face conditioning, no InsightFace.
- Feed it **clean, frontal FACE shots** (not action/body shots) — best from `refs/soul-id/`
  (the tight face angles); **3 refs as a batch** = stronger composite identity. Crop to the face if easy.
- **Weight ~0.75–0.85.** Caution: Plus-Face borrows the photo's face *texture*, so pushing weight
  too high drags back toward PHOTOREAL. If likeness is weak, add more/better face refs rather than
  cranking weight to 1.0; let the LoRA + CGI prompt carry the stylization.

## Remaining path (in order)
1. **Identity** — IP-Adapter Plus Face (above), 3 clean face refs, ~0.8.
2. **⚠️ Authentic body (no legs) — hard rule.** Baselines generated full legs + sneakers. For Zion,
   enforce: prompt "born without legs, torso ending at hips, supported on both hands, no legs";
   negatives "legs, thighs, knees, sneakers, standing, crouching, full body"; and **ControlNet
   Depth/OpenPose from a real hand-support photo** (`refs/zion_gym_parallette.jpg` or a `soul-id`
   hand-balance shot) to guarantee the composition. Prompt alone may leak legs.
3. **Then:** lock full recipe into `prompts/`, batch Zion's scenes, repeat for Kazumi (her Cyberpunk
   already suits the anime LoRA).
- **Flux.1-Dev** remains a backup for style, but SDXL already delivers and keeps FaceID identity, so
  no reason to switch bases now.

## Constraints (unchanged)
Zion: authentic body, **no fabricated legs**. Both: 9:16, SFW (Kazumi strict).

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
2. **⚠️ Authentic body — hard rule, exact anatomy.** His body ends **at/just past the belly
   button** — no hips, pelvis, thighs, or any leg/stump structure below that. Baselines generated
   full legs + sneakers (wrong) — enforce: prompt "born without legs, body ends at the belly
   button, nothing below that point, supported on both hands"; negatives "legs, thighs, hips,
   pelvis, stump legs, knees, sneakers, standing, crouching, full body"; and **ControlNet
   Depth/OpenPose from a real hand-support photo** (`refs/zion_gym_parallette.jpg` or a `soul-id`
   hand-balance shot) to guarantee the composition. Prompt alone may leak legs/stumps.
3. **Then:** lock full recipe into `prompts/`, batch Zion's scenes, repeat for Kazumi (her Cyberpunk
   already suits the anime LoRA).
- **Flux.1-Dev** remains a backup for style, but SDXL already delivers and keeps FaceID identity, so
  no reason to switch bases now.

## RESULT: full-pipeline SDXL test was a downgrade — pivoting
`ip-adapter-plus-face @0.85 + cyberpunk LoRA @0.45 + img2img(parallette, denoise 0.75)` produced a
**standing figure with full legs and bare feet** (hard-rule violation), a warped/generic face, and
garbled tattoos — worse than the Higgsfield GPT Image 2 baseline on every axis except "not a plain
photo," and it didn't even read as clean CGI (read as a damaged photo instead).
**Root cause of the legs:** this was **img2img at high denoise**, not real ControlNet — at
denoise 0.75, img2img only loosely nudges toward the source image's structure, so the model was
free to invent a standing pose. Real pose lock needs an actual ControlNet Depth/OpenPose node.

## PIVOT: use ComfyUI's official "GPT Image 2" partner node instead of SDXL/LoRA/IP-Adapter
Ben's ask: same models as Higgsfield, but with real control sliders. **This exists.** ComfyUI /
Comfy Cloud has an official **GPT Image 2 node** (same underlying OpenAI model Higgsfield calls)
reachable via the `partner_generate` MCP tool. Two fixes over Higgsfield's black-box UI:
- **True multi-image input** (up to ~9 refs per ComfyUI docs) — Higgsfield silently kept only one
  and dropped the rest; this may let "identity photo + 2K style screenshot" actually work together.
- **A structural-fidelity / input-fidelity control** — the missing "denoise knob": low = let the
  prompt restyle more (push toward CGI); high = cling closer to the reference (push toward photo).

**Next test (simpler than SDXL — no LoRA/IP-Adapter/ControlNet needed):**
`partner_generate` with provider **openai / gpt-image-2**, inputs: Zion identity ref(s) from
`refs/soul-id/` + a 2K screenshot from `reference-material/2k-screenshots/` as a **second** image,
**input fidelity LOW**, the CGI prompt from `prompts/zion-clark.md`, 9:16. Check whether both
images are actually honored (identity AND style) — that's the thing to verify first.
See https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2 for the exact param names.

## Constraints (unchanged)
Zion: exact anatomy — body ends **at/just past the belly button**, no hips/legs/stump legs.
Both: 9:16, SFW (Kazumi strict), no real brand/game/league logos or trademarks in output.

# Candidate LoRAs to upload to Comfy Cloud (SDXL 1.0)

Comfy Cloud's catalog has **no** game/3D-render LoRA and only a photoreal base (RealVisXL V5.0),
so we upload our own. **All must be SDXL 1.0** to work with RealVisXL — do NOT use Illustrious,
Pony, or SD1.x LoRAs (they won't load). Grab each `.safetensors` from Civitai (free account),
then upload to Comfy Cloud once custom uploads are confirmed on the plan.

## For Zion — NBA 2K / realistic 3D-CGI human (priority)
- **Semi-Realistic 3D Render Style (Iray/Daz)** — https://civitai.com/models/467293
  Daz/Iray render look = polished, slightly-plastic 3D humans. Closest to the "2K CGI player"
  vibe. **Top pick for Zion.** Start weight ~0.6–0.8.
- **3D [Style] LoRA XL (v3)** — https://civitai.com/models/128353
  Versatile "simple → hyper-real 3D render." Good general CGI pusher for either creator. ~0.5–0.8.
- **3D.Redmond – 3D Render Style for SDXL** — https://civitai.com/models/194138
  (Use the **SDXL** version, not the ZImage one.) Strong 3D-render stacker. ~0.5–0.7.

## For Kazumi — GTA VI look
- **GTA-ish (SDXL)** — https://civitai.com/models/391833
  GTA character-art style. **Top pick for Kazumi's GTA scenes.** ~0.6–0.9.
- **GTA IV Loading Screen Art Style (SDXL)** — https://civitai.com/models/525633
  Stylized GTA cover/loading-screen render — bold, poster-like. Alt for cover-art shots.

(Kazumi's Cyberpunk scenes are already served by the catalog `sdxl-cyberpunk_anime_style` +
a 3D-render LoRA above.)

## Usage notes
- **Get the trigger word** from each Civitai model page (e.g. "3d render", "gtaish style") and put
  it in the positive prompt — LoRAs often need their trigger to activate.
- **Stack sparingly:** one 3D/game LoRA + FaceID (+ its companion LoRA) is plenty. Two style LoRAs
  can fight; if stacking, keep each ≤0.5.
- **Skip (won't work with RealVisXL):** any "Illustrious", "Pony", or "SD 1.x" LoRA
  (e.g. the "Unreal Engine 5 Render" SD1.x one, and the Illustrious "GTA Style" ones).
- **Downloads may need a Civitai login / API token** — that's on Ben's side.

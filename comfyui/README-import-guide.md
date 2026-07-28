# ComfyUI — beginner import & run guide (Zion CGI)

Goal: turn a real photo of Zion into an obvious **CGI game character** using ComfyUI, which
(unlike Higgsfield GPT Image 2) lets you control *how much* it restyles vs. keeps the person.

This first workflow (`zion-cgi-img2img.json`) is intentionally simple — **only built-in nodes,
nothing to install** — so it just works. Once it runs, we level it up (stronger face lock).

---

## What you need first
1. **ComfyUI running** (your Comfy Cloud account, or the desktop app).
2. **One SDXL checkpoint model.** In ComfyUI Manager → "Model Manager", or from Civitai,
   download an **SDXL** checkpoint. For a CGI/3D look, search Civitai for an SDXL checkpoint
   tagged **"3D"**, **"CGI"**, or **"render"** (e.g. a "3D render" style SDXL model). If you
   only have base `sd_xl_base_1.0.safetensors`, that's fine to start.
   - Local install path: `ComfyUI/models/checkpoints/`. On Comfy Cloud, use its model uploader.

---

## Step 1 — Import the workflow
1. Open ComfyUI.
2. Drag **`zion-cgi-img2img.json`** from this folder onto the ComfyUI canvas (or top-left
   menu → **Workflow → Open**, and pick the file).
3. You'll see 4 labeled colored groups: **Load model → Your Zion photo → Prompts → Render+Save**.

> If any node shows up red, it means a value doesn't match your files — that's expected; fix it
> in Step 2. Red because of a *missing node type* shouldn't happen here (all nodes are built-in).

## Step 2 — Point it at your files
1. **Load model group** (top-left, "Load Checkpoint"): click the model dropdown and pick **your**
   SDXL checkpoint. (The file name in the workflow is just a placeholder.)
2. **Your Zion photo group** ("Load Image"): click **choose file to upload** and upload one of
   his refs from `creators/zion-clark/refs/` (a clear one like `zion_face_agt.jpg` or
   `zion_stage_visor.jpg`). Use a photo whose pose you want to keep.

## Step 3 — Run it
1. Click **Queue Prompt** (or press **Ctrl+Enter**).
2. First run downloads/loads the model (can take a minute). The result appears in the
   **Save Image** node and saves to your `output/` folder.

That's a working CGI-ish render with **zero custom nodes**. Now tune it.

---

## The one dial that matters most: **denoise**
In the **KSampler** node (Render group) there's a **`denoise`** value (default **0.65**).
This is the photoreal↔CGI slider GPT Image 2 hid from you:
- **Higher (0.75–0.85):** restyles harder → more clearly CGI, but drifts further from the exact photo.
- **Lower (0.45–0.55):** stays closer to the real photo → more photoreal.
Start at 0.65 and nudge up until it reads as a game character while still looking like Zion.

Other KSampler knobs: `steps` 30 is fine; `cfg` 7 is fine; `seed` set to "randomize" gives a new
variation each run.

---

## Level-up 1 — add a CGI/game LoRA (bigger style push)
The workflow already has a **Load LoRA** node, currently **bypassed** (greyed out) so it doesn't
error.
1. Download an SDXL **style LoRA** for the look you want (Civitai search: "videogame", "3D render",
   "GTA", "PS2/PS5 render"). Put it in `ComfyUI/models/loras/`.
2. Click the **Load LoRA** node → set its LoRA dropdown to that file.
3. **Un-bypass it:** click the node and press **Ctrl+B** (bypass toggles off; node turns normal).
4. Re-queue. Adjust its `strength` (0.6–1.0) for more/less style.

## Level-up 2 — lock his face harder (IP-Adapter FaceID)
When you're comfortable, we add **IP-Adapter FaceID** (one custom-node pack via ComfyUI Manager)
fed by the 20 images in `creators/zion-clark/refs/soul-id/`. That keeps his face locked even at
high denoise — the best of both worlds. Ping me and I'll extend this workflow into
`zion-cgi-faceid.json` with exact install steps. See `../docs/comfyui-workflow.md` for the
full plan (identity + style + pose).

---

## If something breaks
- **Red node / "missing"**: tell me the node name; for this file it should only be a mismatched
  model/LoRA/image filename → reselect it in the dropdown.
- **Output looks like the plain photo**: raise `denoise`, and/or enable the LoRA (Level-up 1).
- **Doesn't look like Zion**: lower `denoise`, or do Level-up 2 (FaceID).
- Send me a screenshot of the result + your denoise value and I'll tell you exactly what to change.

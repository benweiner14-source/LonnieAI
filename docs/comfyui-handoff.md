# Handoff brief — ComfyUI CGI-character generation (for the MCP-connected Claude)

You are picking up one slice of a larger project: generating **CGI game-character** imagery of a
real creator. Everything you need is in the repo below; this brief is self-contained.

## Repo & assets
- **Repo:** `benweiner14-source/lonnieai`  **Branch:** `claude/repo-setup-biy7uf`
- Clone/pull that branch first — it contains all reference images and the starter workflow:
  - `creators/zion-clark/refs/` — 8 curated reference photos (identity)
  - `creators/zion-clark/refs/soul-id/` — **20 clean face/body shots** (use these for FaceID /
    identity training)
  - `reference-material/2k-screenshots/` — 14 real NBA 2K in-game frames (CGI **style** target);
    `…/textures/` has faceless CGI skin/jersey/court crops
  - `comfyui/zion-cgi-img2img.json` — a minimal SDXL img2img starter (built-in nodes only)
  - `docs/comfyui-workflow.md` — the full node-graph plan
  - `docs/forcing-the-cgi-look.md` — what failed and why
  - `prompts/zion-clark.md` — ready prompts;  `creators/zion-clark/profile.md` — his look + rules

## The goal
Render the creator as an **obvious 3D CGI video-game character** (think NBA 2K / Unreal Engine
cutscene — the Lil Miquela "CGI character" effect), while keeping him **recognizable**. Output
is for Snapchat/Facebook, **9:16 vertical**, SFW.

## Hard constraints (do not violate)
- **Authentic representation:** the subject, **Zion Clark**, was **born without legs**. Depict
  him truthfully — powerful upper body, moving on his **hands** or in a **racing wheelchair**.
  **Never generate fabricated/prosthetic legs or a standing figure.** He is the hero of the frame.
- **SFW**, heroic, motivational tone.
- His look: muscular Black athlete, **medium dreadlocks (often a top-knot)**, short beard,
  **gold chain w/ cross pendant**, chest/arm tattoos, **"NO EXCUSES" tattoo across the upper back**.

## What we already learned (so you don't repeat it)
- **Higgsfield GPT Image 2 fails here:** in img2img it "retouches" the real photo and stays
  **photoreal**; it has no real style-slot and **drops** a 2K style screenshot (reads it as a
  different person). Prompt words alone can't override a strong photo reference.
- **The fix is ComfyUI**, because it separates **identity + style + pose** into independently
  weighted controls. That's your job.

## Your task via the ComfyUI MCP
Build/queue a workflow that combines:
1. **Identity** — IP-Adapter **FaceID** (or **InstantID**) on SDXL, or **PuLID** on Flux, fed by
   `refs/soul-id/`. Weight ~0.6–0.85.
2. **Style** — a **game/3D-render LoRA** (Civitai: "videogame", "3D render", "GTA", "PS5 render")
   + the CGI prompt. Optionally an IP-Adapter *style* input from a faceless `…/textures/` crop.
3. **Pose/body** — **ControlNet OpenPose + Depth** from one of his real photos, to hold his
   authentic composition (no fabricated legs).
4. **Sampler** — img2img denoise ~0.6–0.75 (or txt2img if identity+pose anchor it).

Start from `comfyui/zion-cgi-img2img.json` and extend it. Full plan + exact dials in
`docs/comfyui-workflow.md`.

## Prompt to use
Positive: `3D CGI video-game character render, NBA 2K / Unreal Engine cutscene, waxy
subsurface-scattering skin, plastic sheen, clean CG geometry, rendered hair, ambient occlusion,
[scene], obviously computer-generated, NOT a photograph` + his look details above.
Negative: `photograph, photorealistic, real skin pores, DSLR, film grain, fake legs, prosthetic
legs, standing, deformed, text, watermark`.

## Tuning (report back with the result + these values)
- Too photoreal → raise LoRA weight / denoise; lower identity weight slightly.
- Not like Zion → raise FaceID/InstantID weight; add refs; lower denoise.
- Wrong pose/body → raise ControlNet depth/openpose weight.

## Definition of done
A 9:16 image that reads clearly as a **CGI game character** AND is recognizably Zion, with his
body represented authentically (no fabricated legs). Save outputs and report the settings used so
they can be baked into a repeatable workflow.

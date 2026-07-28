# Handoff brief — ComfyUI CGI-character generation (for the MCP-connected Claude)

You are picking up one slice of a larger project: generating **CGI game-character** imagery of a
real creator via ComfyUI / Comfy Cloud. Everything you need is in the repo below; this brief is
self-contained. **Read `CLAUDE.md` at the repo root too** — it's the fuller project memory.

## Repo & assets
- **Repo:** `benweiner14-source/lonnieai`  **Branch:** `claude/repo-setup-biy7uf`
- Clone/pull that branch first — it contains all reference images and docs:
  - `creators/zion-clark/refs/` — 8 curated reference photos (identity)
  - `creators/zion-clark/refs/soul-id/` — **20 clean face/body shots** for identity conditioning
  - `reference-material/2k-screenshots/` — 14 CGI-style sports-sim frames (style target);
    `…/textures/` has faceless CGI skin/jersey/court crops
  - `docs/comfy-cloud-catalog.md` — **read this first**: what's in the Comfy Cloud model
    catalog, what was tried, what failed, and why
  - `docs/comfyui-workflow.md` — the general node-graph plan (identity+style+pose)
  - `docs/higgsfield-cgi-playbook.md` — parallel non-ComfyUI track, useful context
  - `prompts/zion-clark.md` — ready prompts (already genericized, brand-safe — reuse this wording)
  - `creators/zion-clark/profile.md` — his look + the exact-anatomy rule below

## The goal
Render Zion as an **obvious 3D CGI video-game character** (polished sports-sim cutscene look —
do NOT name real games/leagues, see Brand Safety below), while keeping him **recognizable**.
Output is for Snapchat/Facebook, **9:16 vertical**, SFW.

## Hard constraints (do not violate)
- **Exact anatomy:** Zion was born without legs. **His body ends AT/JUST PAST THE BELLY
  BUTTON** — no hips, no pelvis, no thighs, **no partial/"stump" legs**, nothing below that point
  at all. Saying "no legs" alone is not enough — a prior test produced full standing legs, and
  another produced stump legs, because this wasn't stated precisely. Say it exactly, every time,
  and prefer ControlNet/pose-lock from a real hand-support photo over prompt text alone.
- **Brand safety:** do NOT name real games, studios, leagues, or engines in the prompt ("NBA 2K",
  "WWE 2K", real team/league names, "Unreal Engine" by name, etc.) — doing so previously caused
  **real NBA/2K/WWE logos and league branding** to render into outputs, which is unusable for a
  commercial page. Describe the *aesthetic only* (see `prompts/zion-clark.md` for the genericized
  wording already in use) and add a "no real logos/trademarks, no readable brand text" clause.
- **SFW**, heroic, motivational tone.
- His look: muscular Black athlete, **medium dreadlocks (often a top-knot)**, short beard,
  **gold chain w/ cross pendant**, chest/arm tattoos, **"NO EXCUSES" tattoo across the upper back**.

## What's already been tried (don't repeat failed paths — see `docs/comfy-cloud-catalog.md`)
1. **Higgsfield GPT Image 2 (non-Comfy):** img2img "retouches" the real photo and stays
   photoreal; only honors ONE input image (drops a style-reference screenshot). Root problem this
   whole project is solving.
2. **SDXL + IP-Adapter Plus Face + LoRA + img2img(denoise 0.75):** style baseline (no identity/pose)
   looked promising, but the **full pipeline FAILED** — produced a standing figure with full legs
   (img2img at high denoise doesn't lock pose like real ControlNet does), a warped/generic face,
   and garbled tattoos. Worse than the Higgsfield baseline on every axis. **Root cause of the legs:
   img2img ≠ ControlNet — img2img only loosely nudges toward the source image.**
3. **FaceID (any variant) is BLOCKED on Comfy Cloud** — needs InsightFace `buffalo_l`, which can't
   init in that sandboxed runtime. Use **IP-Adapter Plus Face** (`ip-adapter-plus-face_sdxl_vit-h`
   + CLIPVisionLoader) instead — CLIP-vision based, no InsightFace.
4. **Catalog gap:** no game/3D-render LoRA in Comfy Cloud's SDXL catalog; base checkpoint
   (RealVisXL) is photoreal by default; custom LoRA upload has no MCP path (`upload_file` is
   images only) — would need the web dashboard.

## Current recommended path — try this first
**ComfyUI's official GPT Image 2 partner node**, via the `partner_generate` MCP tool. Same
underlying model as Higgsfield, but with real parameters Higgsfield hides:
- **True multi-image input** (~9 refs per ComfyUI docs, vs Higgsfield's silent 1-image limit) —
  try identity photo(s) + a sports-sim style screenshot together.
- **An input-fidelity control** (low = let the prompt restyle more toward CGI; high = cling to
  the reference) — the "denoise knob" Higgsfield never exposed.

Test: `partner_generate`, provider openai/gpt-image-2, images = 1–2 identity refs from
`refs/soul-id/` + optionally one frame from `reference-material/2k-screenshots/`, fidelity LOW,
prompt from `prompts/zion-clark.md` (already brand-safe + anatomy-correct), 9:16. See
https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-image-2

## Fallback — proper SDXL pipeline (if the above underperforms)
Fix what failed in attempt #2 above, don't repeat it:
1. **Identity** — IP-Adapter Plus Face (`ip-adapter-plus-face_sdxl_vit-h` + CLIPVisionLoader),
   3 clean **frontal face** refs from `refs/soul-id/` as a batch, weight ~0.75–0.85 (not higher —
   it pulls back toward photoreal).
2. **Style** — `sdxl-cyberpunk_anime_style` LoRA @0.45 (confirmed good CGI push in baseline
   testing) + the genericized CGI prompt.
3. **Pose/body** — **real ControlNet Depth or OpenPose** (NOT img2img) from a hand-support photo
   (e.g. `refs/zion_face_agt.jpg`), to actually lock the composition and prevent legs/stumps.
4. Negative prompt must include: `legs, thighs, hips, pelvis, stump legs, knees, sneakers,
   standing, crouching, full body` in addition to the standard photoreal negatives.

## Tuning
- Too photoreal → raise LoRA weight / lower input fidelity; lower identity weight slightly.
- Not like Zion → raise identity weight; add/improve face refs; don't over-rely on one lever.
- Wrong body (legs/stumps/hips appearing) → this is a **hard-rule failure**, not just quality —
  fix via ControlNet/pose-lock and the explicit anatomy phrasing above, re-test before batching.

## Definition of done
A 9:16 image that reads clearly as a **CGI game character**, is recognizably Zion, has **no real
brand/logo leakage**, and represents his body exactly (ends at/just past the belly button, nothing
below). Save outputs and report the settings used so they can be baked into a repeatable workflow
and applied to Kazumi next.

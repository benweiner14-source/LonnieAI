# CLAUDE.md — project memory

## What this is
A proof of concept for **Lonnie Anthony Consulting** (social-media agency; monetizes Facebook +
Snapchat for ~300 creators). Goal: render two test creators as **CGI "video-game characters"**
(the Lil Miquela idea) as a new content avenue. If it works, it scales to Lonnie's other clients.

Owner: Ben (benweiner14@gmail.com). Repo: `benweiner14-source/lonnieai`, working branch
**`claude/repo-setup-biy7uf`**.

## The two creators (test set)
- **Zion Clark** (@zionclark) — adaptive athlete, **born without legs** (caudal regression).
  Look: muscular Black athlete, medium dreadlocks (often top-knot), short beard, gold chain w/
  cross pendant, chest/arm tattoos, **"NO EXCUSES" back tattoo**, "Z / No Excuses" purple-gold
  branding. **Styles: NBA 2K + WWE 2K** (sports-game realism). Scenes: gym, track.
  **HARD RULE — exact anatomy: his body ends AT/JUST PAST THE BELLY BUTTON.** No hips, no
  pelvis, no thighs, no partial/"stump" legs — nothing below that point at all. NEVER generate
  fabricated legs, stump legs, or a standing figure. Represent him via hands / racing wheelchair.
- **Kazumi** (@KazumisWorld) — Filipina-American lifestyle/OnlyFans creator. Look: hourglass,
  long wavy balayage (blonde w/ dark roots, often high ponytail), full glam (winged liner, glossy
  lips), gold hoops + green jade pendant. **Styles: GTA VI + Cyberpunk 2077** (stylized/cosplay).
  Scenes: Vice City nightlife, Night City, luxury car, penthouse/cosplay hero.
  **HARD RULE: keep ALL output strictly SFW / brand-safe (glam-but-clothed).**

## Locked decisions
- **Aspect ratio:** 9:16 vertical (Snapchat Story / Facebook).
- **One look: FULL CGI RENDER** — entire frame (character + environment) in the game engine.
  We DROPPED the "CGI character composited into a photoreal scene" look (GPT Image 2 couldn't
  hold it).
- **Volume target:** ~25–40 images per creator for the POC.
- **Delivery:** curate the best into two folders → push to Google Drive → show Lonnie.
- **Identity:** bind via a trained **Soul ID / FaceID** from each creator's `refs/`, used with
  **text-to-image** (NOT img2img off a real photo).

## Key learnings (don't relitigate)
- **Higgsfield GPT Image 2 stays photoreal.** img2img "retouches" a real photo and won't render
  a CGI character. It also honors **only ONE input image and silently drops the rest** (even a
  faceless texture crop) — so attaching a style-reference screenshot does nothing.
- **Soul ID 2.0 tested WORSE than Nano Banana and GPT Image 2** (Ben's direct feedback) — do
  NOT recommend training/using Soul 2.0 for now. Current best path: **Nano Banana** (or GPT
  Image 2) with 1–2 clean reference photos attached directly, no Soul ID training step.
- The fixes, in order: (1) Nano Banana / GPT Image 2 + direct ref photos, no Soul ID; (2) a 2K
  screenshot as the SOLE image + identity ref; (3) different model (Flux.2). Remove photoreal cue
  words ("face-scanned, skin pores, broadcast realism"). See `docs/higgsfield-cgi-playbook.md`.
- **Brand safety — prompts must not name real games/studios/leagues.** Naming real properties
  ("NBA 2K", "WWE 2K", "GTA VI", "Cyberpunk 2077", "Rockstar", "CD Projekt", "RAGE/RED Engine")
  in the prompt text caused the model to render **real NBA/2K/WWE logos, league text, team
  branding, and real game titles** into outputs — unusable for a commercial page. **Fixed:** all
  prompts in `prompts/*.md` are genericized to describe the *aesthetic only* (e.g. "polished
  sports-simulation video game cutscene", "neon-noir cyberpunk screenshot") with invented place
  names (e.g. "Bayview City", "Neo City") instead of real trademarked ones, each ending in a
  "no real logos/trademarks" clause. **Any new prompt must follow this rule too.**
- **Moving to ComfyUI (Comfy Cloud)** for real control: separate weighted **identity + style +
  pose** (IP-Adapter FaceID/InstantID + game/3D LoRA + ControlNet). This is the current path.

## Current status (update me as we go)
- Repo fully built: 4 style skills, 2 prompt packs (all full-render, tuned to real refs),
  2 profiles, refs + 20-image Soul ID set (Zion), 14 NBA 2K style frames + texture crops,
  starter ComfyUI workflow, and setup/handoff/playbook docs.
- **Ben's LOCAL Claude Code is connected to the Comfy Cloud MCP (authenticated, 36 tools).**
  Generation happens there; this web session is strategy/repo upkeep.
- **Catalog reality:** only SDXL identity tool is FaceID Plus v2 (no PuLID/InstantID); base is
  photoreal RealVisXL; no game LoRA; Flux.1-Dev available but no Flux identity adapter. Custom
  LoRA upload not possible via MCP (image-only). See `docs/comfy-cloud-catalog.md`.
- **Style baseline works** on SDXL (RealVisXL + CGI prompt + `sdxl-cyberpunk_anime_style @0.45`),
  but no-identity/no-pose baselines read generic. GPT Image 2 in Comfy = no gain (closed model,
  can't take FaceID/ControlNet).
- **Full SDXL pipeline test FAILED**: IP-Adapter Plus Face + LoRA + img2img(denoise 0.75) produced
  a standing figure with full legs (hard-rule violation — img2img ≠ ControlNet, didn't hold pose),
  warped face, garbled tattoos. Worse than Higgsfield's GPT Image 2 baseline on every axis.
- **PIVOTED:** use ComfyUI's official **GPT Image 2 partner node** (`partner_generate` MCP tool) —
  same model as Higgsfield but with real params: true multi-image input (~9 refs, vs Higgsfield's
  silent 1-image limit) + an input-fidelity slider (the missing "denoise knob"). Next test: identity
  ref + a 2K screenshot as a 2nd image, fidelity LOW, CGI prompt. See `docs/comfy-cloud-catalog.md`.

## Where things live
- `skills/{gta6,cyberpunk-2077,nba2k,wwe2k}-style/` — style DNA + scene modifiers (9:16).
- `prompts/{zion-clark,kazumi}.md` — paste-ready prompts (full CGI render).
- `creators/<name>/{profile.md, refs/}` — brand + guardrails + reference stills;
  `creators/zion-clark/refs/soul-id/` = 20-image identity set.
- `reference-material/2k-screenshots/` — NBA 2K CGI style frames + `textures/` crops.
- `comfyui/` — starter workflow JSON + beginner import guide.
- `docs/` — `comfyui-workflow.md` (node plan), `comfyui-mcp-setup.md` (Comfy Cloud MCP),
  `comfyui-handoff.md` (self-contained brief), `forcing-the-cgi-look.md`,
  `higgsfield-cgi-playbook.md`.

## Working notes
- Apify (Instagram scraping) available via API token Ben provides — session-only, never commit.
- Higgsfield CLI/API exists (Soul ID, GPT Image 2) but img2img limits pushed us to ComfyUI.
- Commit + push to `claude/repo-setup-biy7uf` after changes. Keep refs/tokens out of git.

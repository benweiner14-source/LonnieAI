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
  **HARD RULE: represent him authentically — moving on his hands or in a racing wheelchair;
  NEVER generate fabricated/prosthetic legs or a standing figure.**
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
- The fixes, in order: (1) Soul ID + text-to-image (no photo); (2) a 2K screenshot as the SOLE
  image + Soul ID token; (3) different model (Flux.2). Remove photoreal cue words
  ("face-scanned, skin pores, broadcast realism"). See `docs/higgsfield-cgi-playbook.md`.
- **Moving to ComfyUI (Comfy Cloud)** for real control: separate weighted **identity + style +
  pose** (IP-Adapter FaceID/InstantID + game/3D LoRA + ControlNet). This is the current path.

## Current status (update me as we go)
- Repo fully built: 4 style skills, 2 prompt packs (all full-render, tuned to real refs),
  2 profiles, refs + 20-image Soul ID set (Zion), 14 NBA 2K style frames + texture crops,
  starter ComfyUI workflow, and setup/handoff/playbook docs.
- **Ben's LOCAL Claude Code is connected to the Comfy Cloud MCP (authenticated, 36 tools).**
  Generation now happens there; this web session is strategy/repo upkeep.
- **Next:** in local Claude Code — `search_models` (SDXL checkpoint + IP-Adapter FaceID/InstantID
  + game/3D LoRA), build a workflow, run ONE Zion CGI test, tune, then batch. Then repeat for
  Kazumi. Bake the winning recipe into `prompts/` and (later) automate the full batch via the API.

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

# Seedance 2.0 in Comfy Cloud — Working Notes

Ben's working notes on using ByteDance's Seedance 2.0 (via Comfy Cloud's `ByteDance2ReferenceNode`)
for Project Chimera and related tests, shared here as the reference for animating this project's
CGI-character renders into video. Covers the settings that work, the reference-image patterns that
hold up, and a trademark boundary discovered through repeated testing (relevant since this project
has its own, separate brand-safety rule — see `CLAUDE.md`).

## The node

`ByteDance2ReferenceNode` — a partner-API node (`api_node: true`), meaning it's a sealed black box: no ControlNet, no per-image weight sliders, no intermediate steps to inspect. Everything is controlled through its inputs:

- `model.prompt` — plain text
- `model.resolution` — 480p / 720p / 1080p / 4k
- `model.ratio` — 16:9, 9:16, etc.
- `model.duration` — 4 to 15 seconds, hard API limit. Longer needs multiple generations stitched together.
- `model.generate_audio` — true/false
- `model.reference_images.image_1` through `image_9` — up to 9 reference images (documented max, fully usable in practice)
- `model.reference_videos.video_1` through `video_3`
- `model.reference_audios.audio_1` through `audio_3` — this is how lip-synced talking-head content gets built, no separate video reference needed
- `seed`, `watermark`

## Settings to default to

- **Resolution:** 1080p for most tests. 4K works but ByteDance silently switches the output codec to HEVC 10-bit (`hev1` tag) at that tier — it plays back as "corrupted" in QuickTime, Photos, and a lot of browsers that don't decode 10-bit HEVC. Every 1080p/720p output comes back as standard H.264 and plays everywhere. **Always re-encode 4K output before sending it anywhere:**
  ```
  ffmpeg -i input.mp4 -c:v libx264 -pix_fmt yuv420p -crf 16 -preset slow -c:a aac -b:a 192k output.mp4
  ```
- **Duration:** 7 seconds for most single-shot tests, 10-11 for talking-head clips timed to a specific voiceover (match it to the actual audio length via `ffprobe`, round up).
- **Ratio:** 9:16 for Reels/Shorts-style talking-head content (matches this project's locked 9:16), 16:9 for broadcast-style or landscape shots.
- **`generate_audio`:** true — doesn't hurt, and is required when feeding a real audio reference for lip-sync.

## How to actually build the workflow

Don't use `run_template`'s `slot_overrides`/`input_overrides` on subgraph-based templates — they silently no-op and run the template's stock demo content instead. The reliable method: `get_template` → hand-edit the raw JSON directly (`widgets_values` on the LoadImage/LoadAudio nodes) → `save_workflow` → `run_saved_workflow`. Never `submit_workflow` on a save-format graph — it only accepts already-converted API format.

## Reference images: the pattern that works

One reference image plus a good text prompt is the baseline and it just works. Once multi-reference, there's exactly one rule that matters: **every reference image has to be used affirmatively.** Describe what each one contributes ("match this image's X") — never "copy this reference but ignore/replace part of what it shows." That specific instruction pattern is what breaks generation, not the image count.

Roles that have worked well across tests, in the order typically wired:

1. **Identity** — face/hair/body reference
2. **Location/environment** — the set the character stands in
3. **Product** (if relevant) — an item being held or worn
4. **Skin/render-fidelity closeup** — a different image, purely for matching skin rendering and lighting quality, doesn't need to be the same person
5. **Crowd/atmosphere** — for energy and background density
6. **Wardrobe texture** — if the outfit needs to match a specific design

At 9 references there's no hard image-count wall. The only thing that breaks it is content, covered below.

## The trademark boundary (from Ben's separate testing — different project, still worth knowing)

**Real environments are always safe**, no matter how much real branding is in them — environment/background branding is not an identity claim and doesn't get blocked. **Wearing a real NBA team's jersey is categorically blocked**, no prompt-engineering workaround found. **A real player as the prominent subject of a reference image is also blocked**, even for lighting/crowd reference only. This turned out to be **NBA-specific, not a general real-trademark rule** — real non-NBA trademarks, and even a real ad persona, render fine.

This project's own brand-safety rule (see `CLAUDE.md`) is stricter by default — no real games/leagues/teams/studios named or shown, full stop — so this NBA-specific nuance is background context, not a reason to relax our own guardrails.

**One more separate trigger:** explicitly instructing the model to spell out exact trademarked text breaks generation on its own, independent of the trademark itself. Generic phrasing survives fine.

## Talking-head / lip-sync

Single identity reference image + a real audio file wired into `reference_audios.audio_1`, with a prompt describing a lip-synced shot. No driving video needed. Validate by actually watching the output with sound — the lip-sync genuinely matches the words, not just a visual guess from stills.

## Gotchas worth remembering

- Rate limits (`error_type: api.rate_limit`) are transient — wait a couple minutes and resubmit the identical job.
- The opaque `error_type: unknown` is the default failure mode for content-moderation blocks. It gives no diagnostic detail — isolate the cause by changing one variable at a time and retrying, not by reading the error.
- Comfy Cloud's uploaded input files can become unresolvable after a few hours — re-upload fresh right before running rather than reusing an old upload filename from a prior session.

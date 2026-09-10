# Photoreal Motion-Transfer Pilot — Kazumi

A separate, deliberately different pilot from the CGI-avatar work that makes up the rest of this
repo. Documenting scope and consent basis clearly since this is a meaningfully different product
category from everything else here.

## What this is

1. Generate a **photorealistic character sheet** of Kazumi — NOT stylized, NOT a CGI/game render
   — using the same identity refs (`creators/kazumi/refs/`) that drive the rest of her CGI-avatar
   content, but rendered as a real photographic likeness instead.
2. Use a **motion-transfer / motion-control tool** to have that photoreal likeness perform motion
   pulled from a reference clip, interpolated onto her figure. Candidates, in order of how
   promising they look so far:
   - **Higgsfield Genjutsu** — the tool actually built for this exact workflow (character +
     motion-source-video in, character performing that motion out). Surfaced from researching a
     YouTube walkthrough of a similar AI-influencer pipeline (transcript reviewed, not the video
     itself) — this project already has Higgsfield touchpoints, so check access here first.
   - **Seedance 2.0** (`ByteDance2ReferenceNode` in Comfy Cloud) — has a `reference_videos` input,
     but it's not confirmed whether that does true motion/pose transfer or just video-style
     reference. See `docs/seedance-comfy-handoff.md`.
   - **Kling motion control** — Ben's original suggestion; not yet confirmed to exist in this
     project's Comfy Cloud catalog at all.

## Why this needed its own conversation, not just a new style

Every other pack in this repo (`prompts/kazumi.md`, `-higgsfield.md`, the GTA Loading-Screen Art
test) renders Kazumi as a **stylized CGI character** — that's the concept this project's "Locked
decisions" section describes as approved. A photoreal likeness performing motion-transferred video
is a different category of synthetic media: it produces footage of her real appearance physically
doing something she didn't actually do. That's not covered by "we're making her a game character,"
and treating it as just another style variant would have been the wrong call.

## Consent basis

**Ben confirmed directly: Kazumi is Lonnie's client and has signed off on this specific pilot** —
the photoreal-likeness + motion-transfer concept, as distinct from (and in addition to) the
CGI-avatar work. This is the sign-off this pilot proceeds on. It does not automatically extend to
any other photoreal use of her likeness beyond this pilot's scope (a motion-transfer identity
reference) — confirm separately if the scope changes.

## Motion reference sourcing

`creators/kazumi/motion-refs/motion-test-01.mp4` — a 6.74s, 1080×1920, 30fps clip of a woman
dancing, provided by Ben. Source/rights basis not specified; raised once, Ben's direction was to
proceed without further discussion of it. Noted here for an accurate record.

## Technical plan (needs Ben's local Comfy Cloud session — not runnable from this web session)

1. **Photoreal character sheet** — `prompts/kazumi-photoreal-charactersheet.md`: 3 separate
   Nano Banana Pro generations (front / three-quarter / profile), same identity refs as the rest
   of Kazumi's content, explicitly photoreal (not CGI/illustration) styling, plain studio
   backdrop/outfit held consistent across all three so they read as a matching identity set.
2. **Motion-control tool check** — from Ben's local session: check Higgsfield for Genjutsu access
   first (see candidates list above). If unavailable, `search_models` (or equivalent) on Comfy
   Cloud to confirm whether a Kling motion-control node exists in the catalog (not yet confirmed —
   don't assume it's available the way it was assumed for other partner nodes earlier in this
   project, that assumption has been wrong before). Seedance 2.0's `ByteDance2ReferenceNode`
   exposes `model.reference_videos.video_1` through `video_3` per `docs/seedance-comfy-handoff.md`,
   but that doc doesn't confirm exactly how those inputs drive generation (straight video-reference
   style transfer vs. actual motion/pose extraction) — verify against the node's real docs/schema
   rather than assuming, the same way the GPT Image 2 `input_fidelity` param name had to be
   confirmed off the real schema rather than guessed.
3. **Motion-transfer test** — once the character sheet is rendered: wire the photoreal identity
   images + `motion-test-01.mp4` into whichever tool checks out in step 2, run a short test clip,
   and validate identity holds up under motion (this is a much harder identity-lock test than a
   static image — expect this to need iteration).

## Status

Character sheet prompts written, not yet rendered. Motion reference clip in hand
(`motion-test-01.mp4`). Motion-control tool selection not yet researched — check Higgsfield
Genjutsu access first. Next: render the character sheet, then check tool access, then test.

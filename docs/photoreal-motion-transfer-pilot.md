# Photoreal Motion-Transfer Pilot — Kazumi

A separate, deliberately different pilot from the CGI-avatar work that makes up the rest of this
repo. Documenting scope and consent basis clearly since this is a meaningfully different product
category from everything else here.

## What this is

1. Generate a **photorealistic character sheet** of Kazumi — NOT stylized, NOT a CGI/game render
   — using the same identity refs (`creators/kazumi/refs/`) that drive the rest of her CGI-avatar
   content, but rendered as a real photographic likeness instead.
2. Use a **motion-transfer / motion-control tool** (candidates: Kling motion control, Seedance
   2.0's `reference_videos` input via Comfy Cloud's `ByteDance2ReferenceNode` — see
   `docs/seedance-comfy-handoff.md`) to have that photoreal likeness perform motion pulled from a
   dance reference clip, interpolated onto her figure.

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

**Not sourced by scraping a real creator's TikTok video** — that raises two separate problems:
downloading video off TikTok outside their own export tools violates their ToS regardless of the
content, and using someone else's specific choreography as a motion-capture source for a different
person's likeness is its own copyright question on top of that. The motion reference for this
pilot needs to be something Ben/Kazumi actually hold rights to — self-shot footage, a licensed
motion-capture clip, or choreography Kazumi performs herself on camera for this purpose.

## Technical plan (needs Ben's local Comfy Cloud session — not runnable from this web session)

1. **Photoreal character sheet** — `prompts/kazumi-photoreal-charactersheet.md`: 3 separate
   Nano Banana Pro generations (front / three-quarter / profile), same identity refs as the rest
   of Kazumi's content, explicitly photoreal (not CGI/illustration) styling, plain studio
   backdrop/outfit held consistent across all three so they read as a matching identity set.
2. **Motion-control tool check** — before committing to either tool: `search_models` (or
   equivalent) on Comfy Cloud to confirm whether a Kling motion-control node actually exists in
   this project's catalog (not yet confirmed — don't assume it's available the way it was assumed
   for other partner nodes early in this project, that assumption has been wrong before). Seedance
   2.0's `ByteDance2ReferenceNode` does expose `model.reference_videos.video_1` through `video_3`
   per `docs/seedance-comfy-handoff.md`, but that doc doesn't confirm exactly how those inputs
   drive generation (straight video-reference style transfer vs. actual motion/pose extraction) —
   verify against the node's real docs/schema rather than assuming, the same way the GPT Image 2
   `input_fidelity` param name had to be confirmed off the real schema rather than guessed.
3. **Motion-transfer test** — once the character sheet and a legitimately-sourced motion clip are
   both in hand: wire the photoreal identity images + the motion reference clip into whichever
   tool checks out in step 2, run a short test clip, and validate identity holds up under motion
   (this is a much harder identity-lock test than a static image — expect this to need iteration).

## Status

Character sheet prompts written, not yet rendered. Motion-control tool selection not yet
researched. Motion reference clip not yet sourced. This is the current blocking sequence, in
order — no point testing motion transfer before the character sheet and a legitimate motion clip
both exist.

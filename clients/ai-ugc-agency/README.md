# AI UGC production service — Ben's own agency, pitching DTC brands generally

**Parked for now — saved as context, not an active workstream.** Ben's current focus is Rocka
Moss (`clients/rocka-moss/`); this folder exists so the context isn't lost, not because there's
work in flight here. Don't pick anything up from this folder's "next steps" unless Ben asks.

**A third, distinct project from the Lonnie Anthony CGI-avatar POC and the Christian Brown /
Rocka Moss engagement.** This one is Ben building and pitching his *own* AI-generated-UGC ad
production service to DTC (direct-to-consumer) e-commerce brands broadly — not scoped to a single
client relationship. **Premier Sea Moss is the first warm lead/spec-ad target — a different
company from Rocka Moss** (premierseamoss.com vs. rockamoss.com), despite both being sea-moss
brands. Don't conflate the two: Rocka Moss is Christian Brown's own brand under a specific
consulting engagement; Premier Sea Moss is an unrelated prospective client for this
general-purpose service.

## What's here

- **`session-reference.md`** — the working session notes as handed off: outreach strategy for
  finding DTC brands, the Premier Sea Moss lead, a full 30s ad script, a GPT Image 2 character
  prompt, and 7 Seedance shot prompts. Saved verbatim.

## Status (as of the source doc, Sept 22 2026 — not touched since)

In progress on Ben's side, blocked on two research inputs, nothing rendered yet: the prompts and
script are based on general UGC ad structure + Premier Sea Moss's own brand research — not yet
grounded in "Frankie Shaw's" specific frameworks, which the source doc names as the intended
foundation (3 YouTube videos + an X/Twitter profile that couldn't be pulled at the time). Full
detail, including the source doc's own next-steps list, is in `session-reference.md`.

One thing worth flagging for whenever this picks back up: this repo now has a tool for the
YouTube half of that blocker — the `2k-yt-transcript` skill
(`.claude/skills/2k-yt-transcript/`, installed this session, confirmed working) pulls a clean
transcript from any YouTube link with no login/API key. The source doc only has video titles, not
links, so it can't be run yet — needs Ben to supply the actual URLs first.

## Cross-references to this repo's own proven Seedance/UGC work

This service is a generalized version of what `docs/seedance-comfy-handoff.md` and
`clients/rocka-moss/ai-ugc-playbook.md` already worked out for this repo's other projects. Worth
reading both if/when this picks back up — several details **agree** (validating both sources) and
one is worth testing rather than assuming:

- **Reference-count limits match exactly.** This repo's own Comfy Cloud node
  (`ByteDance2ReferenceNode`, documented in `docs/seedance-comfy-handoff.md`) caps at 9 reference
  images / 3 reference videos / 3 reference audio files — identical to this doc's "max 9 images,
  3 videos, 3 audio files (12 total)." Same underlying model, different access point (this doc's
  `@Image1`/`@Video1` tagging syntax reads as a different UI/API than the Comfy Cloud node's
  `reference_images.image_1..9` field names) — but the platform limits and the "every reference
  must be used affirmatively" role-tagging discipline are the same lesson twice, from two
  independent sources.
- **Lip-sync approach matches.** `reference_audios.audio_1` for talking-head lip-sync, confirmed
  working in this repo's own testing (Kazumi's rooftop-selfie lip-sync test) — same mechanism
  this doc's shot prompts rely on for voice-driven UGC delivery.
- **⚠️ "Seedance blocks realistic human faces in uploaded reference images" — worth testing
  against this project's own access point before assuming it applies, not blindly trusting it as
  a hard constraint.** This repo's Comfy Cloud `ByteDance2ReferenceNode` has *not* hit this
  restriction — it successfully used a real photoreal identity reference in Kazumi's
  motion-transfer pilot (`docs/photoreal-motion-transfer-pilot.md`) with no face-block issue
  reported. That doc's only confirmed restriction was the **NBA-specific** real-jersey/real-player
  block, not a general real-face block. Two explanations are both plausible: (a) this doc's
  source used a different, more restrictive Seedance access point (a consumer-facing app, not the
  Comfy Cloud partner node), or (b) it's model-wide and this project's own tests simply haven't
  triggered it yet. Don't assume either way if this picks back up.
- **Product-reference technique matches the Rocka Moss playbook's product-photography lesson.**
  Shot 3's `@Image2` (a real product label/jar photo, separately tagged from the character
  reference) is the same "protect the one real trademark you want reproduced faithfully by
  feeding it as a clean reference image, never a text description" technique documented in
  `clients/rocka-moss/ai-ugc-playbook.md`.
- **GPT Image 2 as the consistent-identity anchor** (regenerate 2-3 times, lock a face, reuse it
  across every shot) is the same purpose as this repo's own photoreal character-sheet technique
  (`prompts/kazumi-photoreal-charactersheet.md`).

## Not covered here

Outreach mechanics (Meta Ad Library scanning, Crunchbase/Similarweb prospecting, LinkedIn/Apollo
warm outreach, the outreach tracker) are business-development process, not AI generation — fully
documented in `session-reference.md`, no overlap with this repo's generation work.

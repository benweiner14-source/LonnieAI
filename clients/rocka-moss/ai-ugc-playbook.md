# AI UGC Production Playbook — Rocka Moss

Fills the gap the brief calls out directly: *"AI UGC production workflow is not covered by any
existing repo. This is the proprietary edge... the playbook Ben needs to build and own."*

This repo already built most of that edge — for Zion, Kazumi, and Selena's CGI-avatar content.
The techniques below are the ones that transfer **directly**, translated from "render a
stylized game-character avatar" to "generate a real-looking product/testimonial/lifestyle ad."
Every citation points at a file in this repo where the lesson was actually learned (usually the
hard way — read the linked section for the full failure/fix story before assuming the shortcut
version here is complete).

**Nothing in this doc has been run against a real Rocka Moss reference photo yet.** Treat it as
a starting recipe, not a locked one — validate 1-2 outputs before batching, same rule as every
other pack in this repo.

---

## The two content needs, and which engine fits each

Rocka Moss needs two different *kinds* of AI imagery, and this repo already learned (the hard
way, across dozens of tests) that they want different tools:

| Need | Right engine | Why |
|---|---|---|
| **Product photography** (5 styles: Studio, Floating, Ingredient, In Use, Lifestyle) | **Photoreal engine — GPT Image 2.5 Sunburst**, or Nano Banana Pro with no CGI-forcing language | A sea moss bottle needs to look like an actual photographed product, not a stylized render. This is the opposite problem from the rest of this repo (which spends most of its effort *fighting toward* CGI/stylized) — no fighting needed here, just don't add any "video-game," "CGI render," or style-reference language to the prompt. |
| **Testimonial / lifestyle UGC video ads** ("real-looking," per the brief) | **Photoreal engine — GPT Image 2.5 Sunburst for stills, then Seedance 2.0 / Higgsfield Genjutsu to animate** | This is exactly the "candid, authentic, iPhone creator look" this repo already solved for Selena's UGC pack (see below) — GPT Image 2.5 is the confirmed-photoreal path, Nano Banana Pro is the wrong tool here (it's the CGI-stylization engine). |

**Do not reuse the CGI-avatar skills (`skills/{gta6,cyberpunk-2077,nba2k,wwe2k,gta-loading-screen}-style/`)
for Rocka Moss.** Those are a deliberately different, stylized look for a different client's
different product. Rocka Moss wants the *opposite* of that — real, not gamified.

---

## 1. Product photography (the "5 styles" ask)

The brief's Phase 1 skill (`/ads photoshoot`, AgriciDaniel/claude-ads) names the 5 target styles:
Studio, Floating, Ingredient, In Use, Lifestyle. Whatever tool executes it, the identity-
consistency problem is the same one this repo already solved for people — just applied to a
bottle instead of a face:

- **Multi-image role-tagging** (`docs/multi-image-role-tagging.md`) — assign each reference
  image ONE explicit job in the prompt text ("REFERENCE IMAGE 1: the exact Rocka Moss bottle —
  match label design, cap color, glass shape, fill level. Do not alter the label text or logo.")
  instead of hoping the model infers it. This is the difference between a product shot that
  actually reproduces the real label/bottle and one that hallucinates a generic supplement
  bottle. Same lesson applies to swapping in Christian's likeness or a hand holding the bottle
  as a second, separately-tagged reference role.
- **Genericized brand-safety text still applies in reverse here** — this repo's standing rule
  (`CLAUDE.md`, "Key learnings") is *don't name real trademarked properties in the prompt text*
  because the model renders them into the scene. Here the direction flips: the Rocka Moss
  label/logo is the one trademark you *want* rendered faithfully, so it needs to come from a
  clean reference image (never described in text, which invites the model to improvise a
  label), while everything else in the scene (backgrounds, other products, gym equipment,
  kitchen counters) should stay generic to avoid a *different* logo leaking in unprompted — the
  same automaker-badge/real-signage leak found on Selena's GTA pack (`CLAUDE.md`, "Nano Banana
  Pro... real automaker logos/badges rendering unprompted") is just as possible with a random
  competitor supplement bottle or gym-brand logo showing up in a Lifestyle shot.
- **Source a clean bottle reference first.** Nothing here works without 1-2 sharp, well-lit
  photos of the actual current Rocka Moss bottle/label (front label legible, no glare) — the
  same "get a real reference photo before trying to prompt around its absence" lesson that came
  up repeatedly sourcing Zion's tattoo refs and Selena's face refs.

---

## 2. Testimonial / lifestyle UGC video ads ("real-looking... no shoot needed")

This is the closest one-to-one match to work already done in this repo: **Selena's photoreal
UGC pack (`prompts/selena-photoreal.md`)** was built for exactly this brief — Ben's own words on
that pack: *"I want the photoreal versions to be more like UGC, candid, and authentic... a
selfie vibe... an authentic iPhone creator/content creator look"* — which is the same "real-
looking testimonial and lifestyle" ask this brief makes for Rocka Moss. The recipe:

### Stills
- **Model: GPT Image 2.5 Sunburst**, not Nano Banana Pro — confirmed the only path in this
  project that stays photoreal without fighting the model (`CLAUDE.md`'s "GPT Image family
  closed for CGI... open for photoreal" conclusion — Nano Banana Pro would need to be *fought
  away* from stylization, GPT-2.5 defaults to real).
- **Recipe: face refs + product/body ref, no style ref** — a style reference image is what
  pushes toward a *look* (game-engine, painted key-art, etc.); UGC/candid wants no imposed look
  at all, just the subject and the product.
- **Three candid sub-genres, rotate per scene** (`prompts/selena-photoreal.md`):
  - **POV selfie** — genre-led: *"A real, candid iPhone front-facing selfie photo of [subject],
    taken in [scene]..."* — lead with the photographic genre as the very first clause, before any
    other instruction. This is the single most load-bearing lesson in this whole playbook — see
    the POV lesson box in `skills/iphone-selfie-style/SKILL.md`: meta camera-position
    instructions and "NOT third-person" negations reliably fail to produce first-person framing;
    naming the genre up front ("A real iPhone selfie photo of...") reliably does. Use this
    structure for "Christian testimonial selfie holding a bottle," "customer unboxing selfie,"
    etc.
  - **Mirror selfie** — phone visibly held in a mirror reflection, plain case, no screen content
    rendered. A real-Instagram staple this repo confirmed works for candid product-in-hand shots.
  - **Candid, friend-taken** — third-person, caught mid-motion/expression, not posed. Good for
    "someone mixing a Rocka Moss smoothie in their kitchen" type lifestyle shots.
- **If the subject is holding/using the phone as the camera (POV selfie genre):** the phone must
  never appear in frame — use the arm-fills-the-foreground-with-soft-focus technique
  (`skills/iphone-selfie-style/SKILL.md`, "no visible phone" section) instead of describing a
  held phone. If the shot needs a visible phone (mirror selfie, or someone else filming), that's
  the *mirror selfie* or *candid* sub-genre instead, not POV.
- **Override reference-photo expression and lighting explicitly, every time.** Two confirmed
  bugs from Selena's pack apply directly: (1) without an explicit "ignore this reference photo's
  expression, generate a fresh one matching the scene" instruction, every output copies the same
  static expression from whichever face photo was attached — kills the "authentic, in-the-
  moment" read a testimonial needs; (2) without an explicit "relight to the scene's actual light
  sources, not the reference photo's studio lighting" instruction, outputs read as a studio photo
  pasted into a different background. Both are one line of prompt text once you know to add them.
- **Multiple face reference photos beat one.** Spread identity across 2-3 different source
  photos of the same subject (different angle/expression each) rather than anchoring hard to a
  single photo — this is what fixed Selena's "every generation has the identical face and
  expression" bug.

### Video (animating stills into finished ad clips)
- **Seedance 2.0** (`docs/seedance-comfy-handoff.md`, `ByteDance2ReferenceNode` in Comfy Cloud)
  or **Higgsfield Genjutsu** — both confirmed working paths for taking a still and adding
  natural motion + ambient sound. Genjutsu came out ~8-16x cheaper per run in this repo's direct
  side-by-side (`CLAUDE.md`'s motion-transfer 3-way comparison) for comparable quality — default
  to Genjutsu unless Seedance's specific reference-image role system (below) is needed.
- **Lip-synced testimonial voiceover (the brief's ElevenLabs ask):** Seedance's
  `reference_audios.audio_1` input takes a voiceover file directly and lip-syncs the character to
  it — no separate video reference needed. This is the direct technical answer to "how to use
  ElevenLabs... for voiceover" and "stitch it into a 15-second video" from the brief's Gap note.
  Generate the ElevenLabs voiceover first, then feed it into this slot against a still of the
  testimonial subject.
- **Multi-shot ads (beyond one static testimonial clip):** chain each new shot off the *actual
  rendered output of the previous shot* (not the original reference photos) as the anchor image
  — this is the fix that killed visible style/identity drift between shots in Kazumi's
  multi-shot penthouse-party vignette (`CLAUDE.md`). Two gotchas that came with it, both relevant
  to a Rocka Moss ad that needs more than one shot: (1) chaining over-anchors composition too, so
  explicitly tell the model to ignore the chained reference's pose/composition/background and
  describe a genuinely different angle/sub-location per shot, or every shot looks like a near-
  duplicate; (2) watch for real place names rendering as legible signage in the background (the
  "MIAMI" neon-sign leak, same underlying issue as the CGI packs' "Ocean Drive"/"Bayview City"
  leaks) — keep locations generic in the prompt text unless the sign itself is a wanted detail.
- **Technical settings that already work** (`docs/seedance-comfy-handoff.md`): 1080p (4K silently
  switches codec to a format that "corrupted"-plays in QuickTime/Photos — always re-encode 4K
  output before sending anywhere), 9:16 for Reels/Shorts-style ad format, 7s for a single shot /
  10-11s timed to a specific voiceover length (match via `ffprobe`, round up), `generate_audio:
  true`.

---

## Brand-safety carryover

The same standing rule from the rest of this repo applies here without modification: **don't
name real brands/places/trademarks in prompt text, and instruct the model to ignore any it can
see in a reference image** — literal proper-noun-shaped text in a prompt (a real neighborhood
name, a real competitor brand) reliably gets rendered as legible on-screen signage/labeling even
when unintended (`CLAUDE.md`'s "Bayview City" / "Ocean Drive" / "MIAMI" signage leaks, and the
automaker-badge leak on Selena's vehicle scenes). For Rocka Moss specifically, watch for: real
competitor supplement brand logos leaking into Lifestyle/In-Use shots, real gym-chain branding in
background equipment, and real city/neighborhood names rendering as signage in Atlanta/Charlotte/
Chicago-set lifestyle scenes (describe the setting visually — a farmers market, a home kitchen, a
gym — without naming the city in the prompt text itself).

---

## What's not covered here

- **Influencer seeding (Phase 4 of the brief)** — that's real creators submitting real organic
  content, not AI-generated. No overlap with this repo's generation work; just collection/
  repurposing once it comes in.
- **Ad copy, campaign structure, Meta account setup/audit** — covered by the `/ads *` and
  `ads`/`cro` skills named in the brief, outside this repo's scope (image/video generation only).
- **Whether Christian Brown himself can be the AI-generated subject of Rocka Moss ad creative** —
  flagged as an open consent question in `README.md`, not resolved here.

## Next steps before running anything for real

1. Source 2-3 clean reference photos of the actual current Rocka Moss bottle/label.
2. Source face reference photos for whichever real person (Christian, a customer, a paid
   testimonial subject) will appear in the UGC content — confirm consent for AI-generated
   likeness use specifically, separate from any brand-deal-outreach permission already in place.
3. Validate one Studio product shot and one POV-selfie testimonial still before batching either
   direction — same discipline as every prompt pack in this repo.
4. Confirm ElevenLabs voice is ready before attempting a lip-synced Seedance clip — that step is
   blocked on having the actual audio file, same gating issue this repo already hit on Kazumi's
   lip-sync test (`CLAUDE.md`).

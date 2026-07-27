# Higgsfield-only playbook — getting a CGI character (no ComfyUI)

GPT Image 2 img2img **preserves whatever image you feed it** — feed it a real photo, you get a
real photo. So either (A) don't feed it a photo at all, or (B) feed it something that's *already
CGI*. Ranked techniques, best first.

> **Confirmed by testing:** GPT Image 2 honors **only ONE input image and silently drops the
> rest** — even a *faceless* texture crop gets discarded. So attaching a style reference
> alongside the identity photo does nothing. Use **exactly one** image and make it count.

> **Confirmed by testing:** **Soul ID 2.0 quality tested WORSE than Nano Banana and GPT Image 2**
> with direct reference photos. Don't bother training a Soul ID for now — attach 1–2 clean
> reference photos directly and use **Nano Banana** (current best) or GPT Image 2.

> **⚠️ Brand safety:** never name a real game/studio/league in the prompt ("NBA 2K", "WWE 2K",
> real team/league names) — this caused **real NBA/2K/WWE logos and team branding** to render
> into outputs. Describe the *aesthetic only* (see the genericized prompt below) and add a
> "no real logos/trademarks" clause.

> **⚠️ Exact anatomy for Zion:** his body ends **AT/JUST PAST THE BELLY BUTTON** — no hips, no
> pelvis, no thighs, no partial/"stump" legs, nothing below that point at all. State this
> explicitly in every prompt; don't just say "no legs" (that alone has produced stump legs).

---

## Technique A — direct reference photos + text-to-image  (primary fix)
No source photo fed as img2img → the model renders **fresh** and obeys the CGI prompt.

1. In Higgsfield, pick **Nano Banana** (or GPT Image 2).
2. Attach 1–2 clean reference photos of Zion directly (from `creators/zion-clark/refs/soul-id/`)
   for identity — as identity references, not as an img2img base to edit.
3. Prompt = the CGI wording below. Aspect **9:16**.
4. If still too real, escalate: raise style words, add "story-mode cutscene doll look", lower any
   "realism" wording.

This is the current highest-probability path in Higgsfield.

---

## Technique B — CGI-base img2img  (clever, great for close-ups)
Turn img2img's "keep the base" tendency into an advantage: make the **base image itself CGI**.

1. The **single** input image = a sports-sim CGI screenshot from
   `reference-material/2k-screenshots/` (e.g. `2k_01`, the upper-body close-up — no legs in
   frame, so it also sidesteps the anatomy issue). Do **not** also attach Zion's photo —
   GPT Image 2 would drop one of them anyway.
2. Supply Zion's identity via a reference photo or Soul ID token in the text, not a second image.
3. Prompt: "Polished sports-sim CGI render of Zion — dreadlocks top-knot, beard, gold cross
   chain, 'NO EXCUSES' tee — keep the 3D game-engine render look of the base image. No real
   league/team logos or brand trademarks."
4. Because the sole base is already CGI, the output **stays CGI** while the face shifts toward Zion.

Best for **portraits / upper-body / chalk-clap / flex** shots (pick a base frame with no legs so
his body isn't misrepresented). Avoid full-body bases that show legs.

---

## Technique C — low-strength img2img off his photo
If GPT Image 2 exposes an image-strength / similarity slider, drop it to **~0.4–0.5** so the
prompt's style dominates. If there's no slider, skip to A or B.

## Technique D — switch Higgsfield model
GPT Image 2 is edit-/photo-biased. Try **Flux.2** (or Recraft) on Higgsfield with the same
reference photos + CGI prompt — some stylize harder and honor references differently.

---

## Prompt (use in A / B)
**Positive:**
```
3D CGI video-game character, polished sports-simulation cutscene render, Unreal Engine. [SCENE]. A muscular Black adaptive athlete born without legs — his body ends at/just past the belly button, no hips, no thighs, no legs, no stump legs, nothing below that point — supported on his hands, medium-length dreadlocks in a top-knot, short beard, gold chain with cross pendant, "NO EXCUSES" back tattoo. Waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion. Obviously computer-generated game character, NOT a photograph, not photorealistic. No real league, team, or studio logos, no readable brand text. 9:16 vertical.
```
**Remove** any of: `face-scanned maximum fidelity`, `visible skin pores`, `broadcast realism`,
`photorealistic` — they pull it back to photo.

## Escalation ladder (stop when it looks CGI)
1. Technique A (direct ref photos + Nano Banana/GPT Image 2 text-to-image) + CGI prompt.
2. Add "story-mode cutscene doll look, smoother simplified features".
3. Technique B (CGI-base img2img off a sports-sim screenshot).
4. Technique C (lower strength) or D (Flux.2).

## Report back
For each try, note: technique used, model, (strength if any), and paste the result — we tune from
there and bake the winning recipe into `prompts/zion-clark.md`.

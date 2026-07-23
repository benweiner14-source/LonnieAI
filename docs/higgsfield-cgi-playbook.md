# Higgsfield-only playbook — getting a CGI character (no ComfyUI)

GPT Image 2 img2img **preserves whatever image you feed it** — feed it a real photo, you get a
real photo. So either (A) don't feed it a photo at all, or (B) feed it something that's *already
CGI*. Ranked techniques, best first.

> **Confirmed by testing:** GPT Image 2 honors **only ONE input image and silently drops the
> rest** — even a *faceless* texture crop gets discarded. So attaching a style reference
> alongside the identity photo does nothing. Use **exactly one** image and make it count:
> either **no photo** (Technique A) or **a CGI base as the sole image** (Technique B) with
> identity supplied by the Soul ID *token in text*, not a second attached image.

---

## Technique A — Soul ID + text-to-image  (primary fix)
No source photo to cling to → the model renders **fresh** and obeys the CGI prompt.

1. Create a **Soul ID** for Zion from `creators/zion-clark/refs/soul-id/` (20 images). Soul 2 tier.
2. Use **text-to-image** with the Soul ID (NOT img2img). Insert his `<<<soul-id token>>>`.
3. Prompt = the CGI wording below. Aspect **9:16**.
4. If still too real, escalate: raise style words, add "MyCAREER cutscene", lower any "realism".

This is the single highest-probability path in Higgsfield.

---

## Technique B — CGI-base img2img  (clever, great for close-ups)
Turn img2img's "keep the base" tendency into an advantage: make the **base image itself CGI**.

1. The **single** input image = an **NBA 2K screenshot** from `reference-material/2k-screenshots/`
   (e.g. `2k_01`, the Knicks #7 upper-body close-up — no legs in frame, so it also sidesteps the
   leg issue). Do **not** also attach Zion's photo — GPT Image 2 would drop one of them anyway.
2. Supply Zion's identity via his **Soul ID token in the text** (`<<<zion>>>`), not a second image.
3. Prompt: "NBA 2K CGI render of <<<zion>>> — dreadlocks top-knot, beard, gold cross chain,
   NO EXCUSES tee — keep the 3D game-engine render look of the base image."
4. Because the sole base is already CGI, the output **stays CGI** while the face shifts toward Zion.

Best for **portraits / upper-body / chalk-clap / flex** shots (pick a base frame with no legs so
his body isn't misrepresented). Avoid full-body 2K bases that show legs.

---

## Technique C — low-strength img2img off his photo
If GPT Image 2 exposes an image-strength / similarity slider, drop it to **~0.4–0.5** so the
prompt's style dominates. If there's no slider, skip to A or B.

## Technique D — switch Higgsfield model
GPT Image 2 is edit-/photo-biased. Try **Flux.2** (or Recraft) on Higgsfield with the same Soul
ID + CGI prompt — some stylize harder and honor references differently.

---

## Prompt (use in A / B)
**Positive:**
```
3D CGI video-game character, NBA 2K26 MyCAREER cutscene render, Unreal Engine. [SCENE]. A muscular Black adaptive athlete born without legs, seated/supported on his hands, medium-length dreadlocks in a top-knot, short beard, gold chain with cross pendant, "NO EXCUSES" back tattoo. Waxy subsurface-scattering skin with plastic sheen, simplified pores, clean CG geometry, rendered hair, ambient occlusion. Obviously computer-generated game character, NOT a photograph, not photorealistic. 9:16 vertical.
```
**Remove** any of: `face-scanned maximum fidelity`, `visible skin pores`, `broadcast realism`,
`photorealistic` — they pull it back to photo.

## Escalation ladder (stop when it looks CGI)
1. Technique A (Soul ID text2image) + CGI prompt.
2. Add "MyCAREER cutscene doll look, smoother simplified features".
3. Technique B (CGI-base img2img off a 2K frame).
4. Technique C (lower strength) or D (Flux.2).

## Report back
For each try, note: technique used, model, (strength if any), and paste the result — we tune from
there and bake the winning recipe into `prompts/zion-clark.md`.

# Forcing the CGI look (when GPT Image 2 stays too photoreal)

**Problem:** with a real reference photo, GPT Image 2 "lightly edits" the photo and keeps its
photographic texture — so the subject looks like the real person, not a CGI game character.

The goal (the Lil Miquela thesis) is a subject that clearly reads as a **rendered 3D
character** — computer-generated, game-engine look — even when the scene is photoreal.

Fix the **workflow first** (biggest levers), then the **prompt**.

---

## 1. Workflow levers (do these first — they matter more than words)

1. **Use Soul ID + text-to-image, NOT img2img of one photo.**
   Train a **Soul ID** on the creator's `refs/`, then generate with `text2image_soul_v2` +
   the style prompt. This *generates a fresh render* that obeys the style, while keeping the
   face — far more likely to be CGI than img2img, which clings to the source photo's realism.

2. **If you do use img2img, lower the input-image strength/influence.**
   Drop the reference adherence (aim ~0.4–0.6, not max) so the **style prompt dominates** and
   the model re-renders instead of retouching. High strength = photo stays a photo.

3. **Attach a game screenshot as an additional STYLE reference.**
   GPT Image 2 accepts multiple `--image-references`. Give it **two**: the creator (identity)
   *and* a real NBA 2K / GTA VI / Cyberpunk screenshot (the CGI target). Now the model has an
   actual "this is what CGI looks like" example to match. Use the frames in each skill's
   `reference/` folder or `reference-material/`.

4. **If GPT Image 2 still refuses to stylize, switch models.**
   Some Higgsfield models stylize harder than GPT Image 2 (which is edit-biased). Try a
   game-render / stylization model for the CGI pass, keeping the same prompt.

---

## 2. Prompt levers

**Remove the words that pull it back to photo.** Delete: `face-scanned maximum fidelity`,
`visible skin pores`, `broadcast realism`, `photorealistic`, `photo`. (These are the 2K
*photoreal* tier — the opposite of what we want here.)

**Front-load the render framing** — first words of the prompt, not buried at the end.

**Append this CGI-enforcement block** to any prompt that comes out too real:

```
— rendered as a 3D CGI video-game character, NOT a photograph, NOT photorealistic. Real-time
game-engine render (PS5 / Unreal Engine cutscene). Smooth waxy subsurface-scattering skin with
a subtle plastic sheen, slightly simplified pores, clean CG geometry, rendered hair, ambient
occlusion. The subject must read as a stylized computer-generated character model, obviously
CGI — like a playable video-game character, not a real person.
```

**Negations help** GPT Image 2: explicitly say *not a photograph, not photorealistic, not a
real person* — it responds to the contrast.

---

## 3. Quick escalation ladder

If a result is still too real, escalate in this order:
1. Add the CGI-enforcement block; remove photoreal words. →
2. Lower img2img strength. →
3. Add a game-screenshot style reference. →
4. Switch to Soul ID text-to-image. →
5. Switch models.

Stop at the first step that gives an obviously-CGI character. Log what worked per creator so we
can bake it into the defaults.

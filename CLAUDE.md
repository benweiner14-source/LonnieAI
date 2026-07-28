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
- **GPT Image 2 partner-node test (text-only vs 2-image) — style FAILED, identity inconclusive.**
  Both outputs were fully photoreal (no CGI tell at all) — GPT Image 2 has now failed to
  de-photoreal 3 separate ways (Higgsfield img2img, Higgsfield Soul ID, Comfy partner node).
  Also: text-only output contained a **real "NBA 2K" logo** baked in (model default association,
  not from our prompt) — reinforces that reference IMAGES can leak real logos even when the TEXT
  is genericized. Multi-image version misplaced the "NO EXCUSES" tattoo (chest, should be back).
- **PIVOTED AGAIN: Nano Banana Pro** (Google Gemini partner node, up to 14 ref images — the
  highest multi-image ceiling found) + **multi-image role-tagging**: assign each attached image
  ONE explicit job in the text ("REFERENCE IMAGE 1: use ONLY for X, ignore everything else"),
  since none of these partner nodes have a real role field. Ready-to-paste example in
  `prompts/zion-clark.md` ("multi-ref role-tagged"); full technique in
  `docs/multi-image-role-tagging.md`. **Style refs must also be told to ignore/not-reproduce any
  logos visible in the reference photo itself** — genericized text alone doesn't stop the model
  copying a logo it can see.
- **3-ref role-tagged test (face/body/style, no tattoo ref) — best result yet.** Identity: strong,
  specific likeness (not generic). Logo leakage: clean, none. Style: NOT flat photoreal this
  time — drifted to a **Disney/Pixar animated-movie** look instead of sports-game cutscene. This
  is a *different, more fixable* failure than the earlier flat-photoreal ones: "3D CGI, not a
  photograph" alone pulls toward animated-film associations (dominant in training data) rather
  than game-engine renders. **Fix applied:** added an explicit anti-Disney/Pixar/cartoon clause +
  "realistic proportions, muted broadcast color grading" to the style-role instructions in
  `prompts/zion-clark.md` and `docs/multi-image-role-tagging.md`. **Next test: re-run the same
  3-ref role-tagged prompt (now updated) and check whether it lands on sports-sim cutscene
  instead of animated-film.** This reopens Nano Banana Pro as a live style path — don't abandon
  it for the SDXL/LoRA fallback until this retest is judged.
- **✅ v2 retest CONFIRMED — RECIPE LOCKED.** Disney/Pixar drift gone; Ben called it "one of the
  best ones yet." Locked recipe: **Nano Banana Pro**, refs in order — face=`zion_face_agt.jpg`
  (always), tattoo=`zion_back_noexcuses_tattoo.jpg` (only when back is visible in-scene),
  body=`soul-id/soul_12.jpg` (gym/portrait) or `zion_track_noexcuses.jpg` (track) or
  `zion_boxing_ring.jpg` (WWE/combat), style=`2k_02.jpg` (always, anti-Disney wording locked in).
  **All 16 of Zion's scenes (NBA 2K + WWE 2K, incl. signature moments) are now built this way in
  `prompts/zion-clark.md`** — ready to run as a batch. Note: I initially misjudged the v1 image as
  "fully photoreal" when Ben confirmed it was actually a 3D render (just wrong style bucket,
  Disney-leaning) — be more careful/humble calling photoreal-vs-CGI from a compressed image;
  defer to Ben's full-resolution judgment on that specific axis.
- **Zion batch running** (local agent working through all 16 scenes in `prompts/zion-clark.md`).
- **Kazumi pack built in parallel** while waiting on Zion's renders: same multi-ref role-tagging
  technique, 15 scenes converted in `prompts/kazumi.md`. Face=`kazumi_yellow_polo_portrait.jpg`,
  body=`kazumi_olive_tank_denim.jpg`, style=real **gameplay** screenshots sourced fresh via Steam
  (`gtav_skyline_dusk.jpg`, `cp2077_neon_street.jpg`) — NOT the existing cover-art images
  (`gtav_keyart.jpg`, `cp2077_boxart.jpg`), which are dominated by the real logo/title itself and
  too risky even with an "ignore logos" instruction. **Not yet test-confirmed** — run one GTA
  scene + one Cyberpunk scene first, same validate-before-batch process as Zion.
- **3-scene cross-check (gym/track/wwe-entrance) — found a real anatomy violation + repetition
  issue, both fixed.**
  - `nba2k_gym`: Ben confirmed this one came out **too photorealistic** (the "plainest" scene —
    least dramatic lighting/environment to reinforce the CGI tell).
  - `nba2k_track`: anatomy correct (torso into the racing-chair seat, no legs), identity strong,
    clean logos. Proof the recipe works when the body ref is scene-matched.
  - `wwe2k_entrance`: **hard-rule violation** — a bent leg + sneaker was visible under his torso
    in a mid-air "diving/leaping" pose. Root cause: ambiguous dynamic-motion wording ("arms
    mid-stride") + no real reference photo of him airborne, so the model filled in a leg to
    complete a physically plausible flying-human silhouette. Grounded, static poses matched to
    real refs (gym, track) didn't have this problem.
  - Ben also flagged **pose repetition** — too many scenes were the same parallette/propped-on-
    hands shot; he specifically suggested torso-flat-on-ground as a valid alternative.
  - **Fixes applied to `prompts/zion-clark.md`:** (1) grounded the 3 riskiest WWE poses
    (entrance, entrance-silhouette, victory) — explicit "hands/forearms clearly planted,
    nothing below his torso is in frame" language, no more airborne/ambiguous-balance wording;
    (2) added real pose variety — parallette-hold → reclined flat-on-floor, sled → low/flat
    posture, chalk-clap → seated upright; (3) strengthened the universal anatomy closer on ALL
    16 scenes to explicitly include "no feet, no shoes visible anywhere in the frame — the
    composition must not require or imply a leg" (previously said "no legs" but not "no feet",
    which is exactly what leaked); (4) added guidance to generate **3–4 seed variants per
    prompt** (Ben's fix) since anatomy compliance and photoreal/CGI balance both vary
    noticeably by seed even with identical wording — discard bad-anatomy or logo-leak variants
    rather than trying to fix them after the fact.
  - **Not yet re-tested** — re-run `wwe2k_entrance` (and ideally the other 2 fixed WWE scenes)
    to confirm the grounding fix actually holds before resuming the remaining batch.
- **Arm/chest tattoos were "getting generated willy nilly" (Ben's report) — fixed.** Root cause:
  only the back tattoo had a photo reference; his chest/arm ink had no visual anchor at all, so
  the model improvised a different design every generation. Fix: Ben linked an Instagram post +
  a promiflash.de article; a **promo photo from the article**
  (`content.promiflash.de/article-images/video_1080/zion-clark-wrestler.jpg`) turned out to be a
  sharp, well-lit close-up of his real **"330 Clark" chest/collarbone script tattoo** and his
  **left arm/bicep tattoo** — clearer than any existing ref. Saved as
  `creators/zion-clark/refs/zion_chest_arm_tattoo.jpg`. Added as a new **always-included role**
  (like face and style) on every scene where his front/arms are visible; scenes shot from behind
  or in silhouette keep using only the back-tattoo ref. `prompts/zion-clark.md` is now v3 — all
  16 scenes renumbered with the new reference wired in (4 refs normally, 5 for `double-flex`
  which shows both tattoos). Also updated `docs/multi-image-role-tagging.md` and
  `creators/zion-clark/profile.md`. **Not yet test-rendered — this is the next thing to validate**
  before resuming the batch.
- **Also added a Higgsfield-only prompt pack per creator** (`prompts/{zion-clark,kazumi}-higgsfield.md`)
  — same scenes, single flowing paragraph, no `REFERENCE IMAGE N` tagging, for messing around
  directly in Higgsfield without the full role-tagging system.
- **Sourced 10 more Zion photos via a Google/Bing image search sweep (≥2MP, filtered by real
  resolution metadata), Ben approved 3 for specific roles — added as ADDITIONS, not replacements:**
  `zion_face_agt.jpg` (AGT red-carpet photo — now a **second face reference used alongside**
  `zion_gym_parallette.jpg`, not instead of it — both feed identity together on every prompt),
  `zion_plyobox_bodycomp.jpg` (approved alternate for body composition), and
  `zion_chest_tattoo_closeup_alt.jpg` (approved alternate second look at the chest tattoo).
  `prompts/zion-clark.md` is now **v4** — every scene carries both face refs (5–6 images total per
  prompt now). Also updated `docs/multi-image-role-tagging.md` and the Higgsfield pack.
- **Torso-cutoff was reading bare/exposed in some WWE renders (Ben flagged on `victory`).** His
  real reference photos never show bare skin right at the cutoff — a shirt hem or loose
  shorts/trunks typically drapes past it. Added a universal line to every full-body scene (both
  prompt packs): shorts/trunks/shirt hem drape loosely and *emptily* past the end of his torso
  (not shaped like a leg) instead of ending in bare skin. Upper-body-only portrait crops (framed
  above the waist) skip this since they don't reach that part of the frame.
- **Next up:** run one scene with the new refs (2 face images + tattoo ref) to confirm identity
  and tattoo both render consistently, re-test the fixed WWE scenes (esp. `victory` for the
  wardrobe-drape fix) + confirm gym's photoreal issue resolves with the seed-variant approach,
  then finish the remaining batch, curate best into `output/zion-clark/` (or push to Drive),
  validate Kazumi's recipe with a test scene, then batch her remaining 14.

## Where things live
- `skills/{gta6,cyberpunk-2077,nba2k,wwe2k}-style/` — style DNA + scene modifiers (9:16).
- `prompts/{zion-clark,kazumi}.md` — **Comfy Cloud / Nano Banana Pro** paste-ready prompts, full
  multi-image role-tagging (`REFERENCE IMAGE 1/2/3...`), full CGI render.
- `prompts/{zion-clark,kazumi}-higgsfield.md` — **Higgsfield** paste-ready prompts, same scenes,
  no role-tagging — single flowing paragraph per scene (Higgsfield's img2img/Nano Banana flow
  doesn't reliably use more than one attached photo, so explicit multi-image role text there is
  dead weight). Same hard rules (anatomy, brand safety, anti-Disney) baked into each paragraph.
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

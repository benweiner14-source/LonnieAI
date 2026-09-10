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
- **Zion batch mostly complete via Google Drive** (40 outputs uploaded across 16 scenes). Since
  the connected Google Drive tools can only search/read/copy/create (no rename, move, or delete),
  organized the 22 clearly-scene-named files into `Zion - organized/{NBA2K,WWE2K}/<scene>/` with
  clean filenames via copy — originals are still sitting in the top-level folder too (Ben needs to
  delete those manually once he's confirmed the copies). The other 18 files (opaque `hf_*`
  Higgsfield-timestamp names + `Untitled-*`) were dumped as-is into an `unsorted/` subfolder,
  not inspected, per Ben's call.
- **Kazumi's first test round (`nightlife` + `street`, 4 seeds each) — found real issues on both
  styles, both reworked in `prompts/kazumi.md` (now v6):**
  - `gta6_nightlife`: read too photoreal (real-world Miami, not a CGI screenshot — same "plainest
    scene" issue as Zion's gym) **and** 3/4 seeds got refused by Gemini's safety filter, traced to
    the body ref `kazumi_olive_tank_denim.jpg` combined with "cropped designer top" in the prompt.
    Checked all 8 Kazumi ref photos for a less-revealing replacement — none work (the covered ones
    are tight headshot crops, not figure shots; the figure shots are all similarly or more
    revealing than the current ref). **Fix:** dropped the image body ref for GTA scenes entirely
    (now 2-ref: face + style, figure carried by text only), added explicit "obviously
    computer-generated, NOT a real photograph" to the GTA style role, punched up `nightlife`'s
    environment with more exaggerated neon/lighting.
  - `cyberpunk_street`: passed the automated check (identity/logos/SFW clean 4/4) but Ben's direct
    look caught something the checklist missed — it read as a **CGI character composited onto a
    photoreal background**, exactly the look this project dropped early on (see "Locked
    decisions" above), plus the environments were busy/over-stylized (too many simultaneous
    neon/fog/bloom layers). **Fix:** added an explicit "character and environment must render in
    the SAME unified CGI style, not composited" instruction to the Cyberpunk style role, and
    trimmed the 4 busiest scene environments (`street`, `megabuilding`, `cyber-bar`,
    `cosplay-hero`) from 3-5 stacked elements down to 1-2 clean ones.
  - **Lesson:** an automated per-axis checklist (identity/style/logos/SFW) can still miss a
    composited-look failure that's obvious on direct look — keep having Ben eyeball results even
    when the checklist passes clean.
- **Everything was reading too centered/symmetrical — no camera variety in any pack.** Ben
  flagged both Zion's and Kazumi's renders as flat, always-centered hero shots. Root cause on
  inspection: the prompts genuinely had almost no camera-angle/lens language — most scenes ended
  in a generic "Hero framing, rim light." or nothing at all. **Fixed across all 4 prompt packs**
  (`zion-clark.md`, `zion-clark-higgsfield.md`, `kazumi.md`, `kazumi-higgsfield.md`): every one of
  the 62 scenes now ends with a distinct **Camera:** clause — angle (low/high/Dutch tilt/
  three-quarter/overhead), focal length (20mm wide through 135mm telephoto), and off-center/
  asymmetrical framing, no two scenes alike within a pack. One deliberate exception: Kazumi's
  `cyberpunk · cosplay-hero` stays centered on purpose (mimics a character-select screen). While
  touching Kazumi's Higgsfield pack, also ported over the Cyberpunk declutter/unified-style fix
  from the Comfy pack (it still had the old busy effect stack) so both packs stay in sync.
- **⚠️ "Extreme low angle looking up" auto-failed in Higgsfield (`kazumi cyberpunk · megabuilding`
  scene) — likely a safety-filter trigger, not a rendering issue.** Camera phrasing that frames a
  female subject from a low angle looking up at her is a known sensitive pattern for image-gen
  safety filters (reads as upskirt/creepshot-adjacent framing regardless of intent), separate from
  the Gemini-body-ref-image trigger found earlier on GTA nightlife. **Fixed:** replaced "extreme
  low angle looking up" on both Kazumi scenes that had it (`megabuilding`, `luxury-car`) in both
  prompt packs with angles that keep the scale/drama without literally looking up at her — eye-level
  wide with a large background environment, or a low three-quarter angle framed around the car
  instead of her body. **Rule of thumb going forward:** avoid "looking up at [her]" camera phrasing
  on Kazumi's prompts specifically; low angles emphasizing an object (a car, a building) she's
  merely standing near are fine, low angles whose subject is literally her body from below are not.
- **"Bayview City" / "Neo City" were rendering as literal signage in the output.** Ben noticed the
  invented placeholder city names kept showing up as readable text/signs in the generated images.
  Root cause: those names were literal words in the prompt text (e.g. "...9:16 vertical. Bayview
  City. Fully clothed, SFW."), so the model rendered them the same way it would any other text in
  a prompt — this is the same underlying mechanism that caused real logo leakage before, just with
  a fictional name instead of a trademarked one. **Fixed:** stripped every literal "Bayview City"
  and "Neo City" mention out of the actual scene prompt text in all 15 scenes across both
  `prompts/kazumi.md` and `prompts/kazumi-higgsfield.md` — the visual scene-setting (art-deco
  hotels, neon streets, marina, gas station, megabuildings, etc.) already establishes the setting
  without needing a place name spelled out. The explainer note in each file's header (documenting
  *why* invented names were chosen over real ones) still mentions them, but that text is never
  itself pasted into a generation. **Lesson:** any proper-noun-shaped phrase in a prompt — real or
  invented — risks getting rendered as literal on-screen text; only put a name in the prompt if you
  actually want it legible in the output.
- **Next up:** re-test `[gta6 · nightlife]` and `[cyberpunk · street]` once each against the v7
  Kazumi prompts to confirm the earlier photoreal/composited-look fixes AND the new camera variety
  hold, then batch the remaining 7 GTA + 6 Cyberpunk scenes. Separately: re-test the fixed Zion
  WWE scenes (esp. `victory` for the wardrobe-drape fix, now also carrying new camera angles) +
  confirm gym's photoreal issue resolves with the seed-variant approach, then finish the remaining
  Zion batch and have Ben delete the un-organized originals from the Drive folder once the
  organized copies are confirmed good.
- **Added a new "iPhone Selfie" style — a camera/photography variant, NOT a return to the dropped
  composited-into-a-real-photo look.** Ben's ask, with a worked example prompt (a real iPhone
  selfie of an NBA 2K MyPlayer avatar mid-celebration in a real crowd). My first pass mis-scoped
  this as a deliberate exception to the "full CGI render" locked decision — **Ben corrected that
  immediately: he only meant to hand over the iPhone-camera wording/technique (selfie framing,
  wide-angle lens distortion, hard on-camera flash, chaotic motion-blurred crowd), not the
  composited-onto-a-real-photo look itself.** The style stays inside the locked decision: the
  entire frame — character AND environment — still renders fully in the CGI game engine, same as
  GTA VI/Cyberpunk/NBA 2K/WWE 2K; only the *camera language* changes to mimic a real selfie shot.
  Ben's example also had real trademarks baked in (Knicks jersey, NBA Finals, "NBA 2K", "MyPlayer",
  a real person's handle "@Ronnie") — genericized out per the standing brand-safety rule, same as
  every other style. Built as a 5th style: `skills/iphone-selfie-style/SKILL.md` (Style DNA:
  simulated wide-angle selfie-lens distortion, hard flash with sharp falloff hitting everything
  near-camera identically, simulated sensor grain/motion blur — all rendered as part of the CG
  shot, never composited from a real photo). Added 2 scenes per creator to all 4 prompt packs
  (`prompts/zion-clark.md` v6, `prompts/zion-clark-higgsfield.md`, `prompts/kazumi.md` v8,
  `prompts/kazumi-higgsfield.md`) — Zion's use 4 refs (both face angles + arm/chest tattoo + a
  body/pose ref, grounded in his racing wheelchair or a forearm-propped floor pose to hold the
  exact-anatomy rule), Kazumi's use 1 ref (face only — no body ref, same lesson as her GTA rework,
  and the tight selfie crop keeps it modestly SFW by construction). No dedicated style-reference
  screenshot exists for this look yet, so the "fully CGI, nothing photoreal" instruction is carried
  entirely in prompt text — flagged as the detail most likely to drift if dropped.
- **iPhone Selfie's first test render (Kazumi, `nightlife`) failed on POV, not style.** Ben's
  output showed the CGI style and identity holding up fine, but the shot was framed as a
  **third-person documentary photo of her taking a selfie** — full body, several feet back, the
  whole crowd visible in a wide fisheye shot — instead of an actual first-person POV from the
  phone's own front-facing lens. Root cause: the prompts said "taking a selfie" and "face close to
  the lens" but never explicitly forbade an external observer's camera, so the model defaulted to
  the far more common "someone photographing a person taking a selfie" association. **Fixed** in
  `skills/iphone-selfie-style/SKILL.md` and all 8 scene prompts (both scenes × all 4 packs): every
  prompt now opens with an explicit "this image IS the photo captured by their own phone's
  front-facing camera — the render's camera position IS the phone's lens itself, NOT a third-person
  shot" clause, plus a hard framing constraint (face/upper torso fill most of the frame, nothing
  below the waist, background limited to the narrow slice actually within the phone's field of
  view at arm's length — not a wide shot of the whole scene/crowd). **v1 fix didn't hold** — Ben
  re-ran it and it was still third-person.
- **iPhone Selfie POV fix v2 — replaced meta camera-position language with genre-anchoring.** The
  v1 fix (explicit "the render's camera position IS the phone's lens... NOT a third-person shot"
  instructions) still rendered third-person on retest. Root cause: meta/technical camera-position
  instructions and negations don't reliably steer composition — the model still defaults to its
  strongest association. Ben pointed at his own working Higgsfield prompt (the original Knicks/
  MyPlayer example this style was built from) as a working reference: it never uses any camera-
  position or negation language at all. It just **leads with the photographic genre itself** — "A
  real iPhone front-facing selfie photo of [X], taken in [scene]" — as the very first clause,
  before any CGI/rendering language, then uses plain physical framing ("face large and close to
  the lens," "one arm extended holding the phone"). Naming the genre up front does more work than
  any amount of explicit instruction after the fact, because "selfie photo" is such a strong,
  specific composition in the model's training data. **Rewrote** `skills/iphone-selfie-style/
  SKILL.md` (Camera section + Base Prompt Template) and all 8 scene prompts to lead with the genre
  clause and drop the meta/negation language entirely; background crowd is now described with
  concrete physical imagery ("packed tightly right up against the camera, bodies overlapping and
  partly cropped") instead of an abstract "limited to the phone's field of view" instruction — kept
  fully CGI throughout per Ben's correction that this is a camera-language style, not a return to
  the dropped composited-into-a-real-photo look.
- **iPhone Selfie v2 test — POV genre-anchoring worked, two new artifacts found and fixed (v3).**
  Ben's retest confirmed the genre-lead fix: one output nailed real first-person POV (closest yet
  — face close, arm/hand in the foreground corner, background appropriately compressed). Two new
  issues showed up on the way there: (1) **circular fisheye vignette** — "wide-angle lens
  distortion" alone got misread as a literal fisheye action-cam look, complete with a dark
  circular crop, instead of the subtle rectangular-photo edge stretch a real phone selfie has;
  (2) **a visible second phone showing a photo on its screen** — one output showed her holding up
  a phone whose screen displayed an image of her face (a photo-within-a-photo), instead of using
  the phone as the camera taking the actual shot; this happened on an output that otherwise had
  correct POV framing, just with the phone rendered as a prop with content on it. **Fixed** in
  `skills/iphone-selfie-style/SKILL.md` and all 8 scene prompts: added an explicit "rectangular
  9:16 photo — no circular vignette, no dark corners, no fisheye lens crop" clause, and "if the
  phone enters frame, only its plain back or edge shows — never its screen, never a photo
  displayed on it, never a second phone."
- **Ben's call: the phone should never be visible at all, full stop** — not even its plain
  back/edge. It's a true POV shot; the phone IS the camera, so it can't also be an object in the
  frame, the same way a real person's own eye doesn't appear in what they're looking at.
  Tightened `skills/iphone-selfie-style/SKILL.md` and all 8 scene prompts again: replaced "one arm
  extended holding the phone" (which still implied a visible held object) with "one arm extended
  toward the camera, only the arm and hand visible — the phone itself is never shown in frame,
  since the camera taking this shot IS the phone's own lens," and hardened the "no phone" clause
  to explicitly rule out even the back/edge.
- **GPT Image 2 side-by-side comparison — same prompt, different result, confirms known
  tradeoffs and adds one new lesson.** Ben ran the exact same prompt text on GPT Image 2 (not a
  different/better prompt) and got noticeably better framing — the extended arm/sleeve filled
  most of the foreground in a natural soft-focus blur, cleanly cropping the hand/phone out of
  frame with no explicit instruction needed. But it confirmed the two known reasons this project
  isn't on GPT Image 2: fully photoreal (zero CGI tell, same failure mode as all 3 earlier GPT-2
  tests) and weaker facial fidelity (no FaceID/identity-adapter path on a closed model). **New
  lesson: Nano Banana Pro needs more explicit/redundant instruction than GPT-2 to land the same
  framing on identical text** — it's not more instruction-faithful, so constraints that GPT-2
  infers correctly from sparse wording need to be spelled out more concretely for Nano Banana.
  **Fixed:** added "arm and sleeve/forearm filling a large part of the foreground, soft and
  slightly out of focus from being this close to the lens, naturally cropping the hand and phone
  out of frame" to `skills/iphone-selfie-style/SKILL.md` and all 8 scene prompts — gives the "no
  visible phone" rule a physical/optical reason instead of a bare negation.
- **Wording fix: "arm and sleeve" → "arm (sleeved or bare, depending on the outfit)".** Ben caught
  that "sleeve" assumes every outfit has one — wrong for Zion's tanks and some of Kazumi's looks.
  Fixed across the skill file and all 8 scene prompts.
- **✅ iPhone Selfie CONFIRMED WORKING (Kazumi, rooftop-party nightlife scene).** Ben's retest on
  the v5 wording landed a clean result: true first-person POV, no phone visible anywhere in frame
  (just her bare arm + gold bangles filling the foreground, exactly the "arm blocks the phone via
  proximity blur" technique), no circular vignette/fisheye crop, correct CGI-not-photoreal
  identity, rooftop-party environment with string lights + skyline reading clearly in-engine. This
  is the recipe to reuse going forward for this style — don't re-litigate the POV/vignette/phone
  fixes above unless a *new* failure mode shows up. Still worth running the other 3 iPhone-Selfie
  scenes (Zion ×2, Kazumi's `penthouse-party`) to confirm the fix generalizes before calling the
  whole style locked.
- **New content avenue opened: animating these CGI-character stills into video with Seedance 2.0**
  (ByteDance's model, via Comfy Cloud's `ByteDance2ReferenceNode`), using Ben's own proven recipe
  from a separate project (Project Chimera) — saved as `docs/seedance-comfy-handoff.md`. Two tests
  currently handed off to Ben's local Claude Code session (this web session has no Comfy Cloud MCP
  access, can't run these directly):
  - **Broll motion test** — 3 already-rendered Comfy Cloud images (UUIDs `717356d8…`, `8628cfa2…`,
    `2d3ba387…`), animated with natural walking/body motion + ambient sound, max 10s each, single
    reference-image-per-generation pattern. Test plan sent as a file; not yet run/reported back.
  - **Lip-sync test** — the confirmed-good Kazumi rooftop-selfie render above, animated as a
    talking-head clip via `reference_audios.audio_1` + an ElevenLabs voiceover Ben is preparing.
    Test plan sent as a file; **blocked on the ElevenLabs audio file**, not yet run.
  - Both test plans carry forward the handoff doc's key gotchas: `slot_overrides`/
    `input_overrides` silently no-op on this node (must hand-edit the template JSON instead), and
    re-upload reference files fresh right before running (stale-upload risk after a few hours).
- **❌ GPT Image 2 retest FAILED — final answer, closing this thread.** The isolate-the-model test
  (`[nba2k · gym]`'s exact current prompt + full 5-image ref set, unmodified, run through the GPT
  Image 2 partner node instead of Nano Banana Pro) came back still too photoreal. This is the
  **4th confirmed failure** to de-photoreal GPT Image 2 (Higgsfield img2img, Higgsfield Soul ID,
  the earlier Comfy partner-node test, and now this one with the fully matured prompt language +
  complete role-tagged ref set) — the mature prompt and full identity refs didn't move the needle.
  Per the plan set going into this test: a closed model with no ControlNet/LoRA/FaceID path can't
  be pushed off its photoreal prior by reference images and prompt text alone. **Conclusion: GPT
  Image 2 is not a viable path for this project's CGI-render requirement, full stop — don't
  retest it for this purpose again.** Nano Banana Pro remains the only proven identity+style path.
- **Added a "GTA Loading-Screen Art" style — a genuinely different rendering MEDIUM, not just
  another look.** Ben's ask, referencing the Civitai "GTA5 Artwork Diffusion" model as inspiration.
  Every other style in this repo is a **3D real-time game-engine render** (the locked "full CGI
  render" decision); this one is **painted 2D digital illustration** — the semi-realistic painted
  key-art look used for official open-world-crime-saga loading screens/promotional art. Built as a
  5th style, `skills/gta-loading-screen-style/SKILL.md`, framed explicitly as a deliberate new
  style option (same pattern as iPhone Selfie) rather than a reversal of the CGI-render decision
  for the other 4. Style DNA sharpened across two passes from Ben sharing real official key-art
  images purely as visual reference for wording (not as generation inputs, so no logo-leakage risk
  at that stage): a clear rendering-detail hierarchy (skin/face most refined, environment flatter/
  more graphic), chunky painted hair locks, bold clothing contour linework, a signature warm
  dusk/sunset (or neon, for interior scenes) rim-light + soft glow-halo lighting move, vivid punchy
  color grading (a deliberate contrast against the other styles' muted broadcast grading),
  confident "prop in hand" body language, painted eyewear highlight technique, and an optional
  isolated-hero-on-dark-background composition variant. **Reference images:** Ben uploaded 5
  official key-art stills (cropped to remove the studio wordmark) via a GitHub web-UI upload
  directly to the branch — pulled in and organized into
  `skills/gta-loading-screen-style/reference/`. 4 of 5 are clean of the studio logo
  (`cinema_doppler.jpg` set as the recommended primary, plus `arrest_scene.jpg`,
  `franklin_gun.jpg`, `flapper_couple.jpg`); 1 (`couple_car_LOGO_NOT_CROPPED.jpg`) still has a
  visible studio star logo and is flagged not to use as-is. A `[gta-loading-screen · gaming-desk]`
  test scene (Kazumi at a neon gaming setup, environment ref from an image Ben pasted inline —
  not saved to the repo, he'll attach it himself locally) was drafted but **not yet run or added
  to the permanent `prompts/kazumi.md` pack** — validate before batching, same as every style.
- **New, separate pilot: photoreal character sheet + motion transfer for Kazumi — NOT part of the
  CGI-avatar work, its own consent basis.** Ben's ask: generate a photorealistic (not stylized)
  character sheet of Kazumi, then use a motion-transfer/motion-control tool (Kling motion control
  or Seedance 2.0's `reference_videos` input) to have that photoreal likeness perform motion from
  a dance reference clip. Flagged this as a meaningfully different product category before
  building anything — every other pack in this repo produces a *stylized CGI avatar*, which is
  the concept documented as approved in this project's locked decisions; a photoreal likeness
  performing motion-transferred video is different synthetic media entirely (footage of her real
  appearance doing something she didn't actually do), not automatically covered by that same
  approval. **Ben confirmed directly: Kazumi is Lonnie's client and has signed off on this
  specific pilot** — documented as the consent basis in `docs/photoreal-motion-transfer-pilot.md`.
  Also flagged (and Ben didn't push back on): the motion reference clip can't be scraped from a
  real creator's TikTok (ToS + choreography-copyright issues, same reasoning as declining to pull
  audio off a YouTube link earlier in this project) — needs to be footage Ben/Kazumi actually hold
  rights to. **Built so far:** `prompts/kazumi-photoreal-charactersheet.md` — 3 separate Nano
  Banana Pro generations (front / three-quarter / profile), same identity refs as her CGI content,
  explicitly photoreal styling (the opposite of every other prompt in this repo — "NOT a CGI/game
  render, NOT stylized" instead of "obviously computer-generated, NOT photoreal"), plain matching
  studio backdrop/outfit across all three so they read as one consistent identity set. **Not yet
  rendered.** Motion-control tool choice unresolved — Kling's availability in this project's Comfy
  Cloud catalog hasn't been checked (don't assume it's there, that assumption has burned this
  project before); Seedance's `reference_videos` input exists per the handoff doc but how exactly
  it drives generation isn't confirmed. Motion reference clip not yet sourced. Full plan and
  blocking sequence in `docs/photoreal-motion-transfer-pilot.md`.

## Where things live
- `skills/{gta6,cyberpunk-2077,nba2k,wwe2k,iphone-selfie,gta-loading-screen}-style/` — style DNA +
  scene modifiers (9:16, except `gta-loading-screen` which is a different rendering medium — see
  its own header note). `iphone-selfie-style` is a camera/photography variant, not a different
  look-category — still full CGI render, just shot like a real iPhone selfie.
  `gta-loading-screen-style` IS a different look-category — painted 2D illustration, not a 3D
  render — built as a deliberate additional style, not a reversal of the CGI-render decision for
  the other 4. Its `reference/` folder holds 5 real key-art stills (logos cropped, 4 clean/1
  flagged) as the style anchor.
- `prompts/{zion-clark,kazumi}.md` — **Comfy Cloud / Nano Banana Pro** paste-ready prompts, full
  multi-image role-tagging (`REFERENCE IMAGE 1/2/3...`), full CGI render.
- `prompts/{zion-clark,kazumi}-higgsfield.md` — **Higgsfield** paste-ready prompts, same scenes,
  no role-tagging — single flowing paragraph per scene (Higgsfield's img2img/Nano Banana flow
  doesn't reliably use more than one attached photo, so explicit multi-image role text there is
  dead weight). Same hard rules (anatomy, brand safety, anti-Disney) baked into each paragraph.
- `prompts/kazumi-photoreal-charactersheet.md` — **a different pilot, not part of the main CGI
  pipeline.** Photorealistic (NOT CGI/stylized) identity-reference generations for the
  motion-transfer pilot — see `docs/photoreal-motion-transfer-pilot.md` for scope/consent basis.
- `creators/<name>/{profile.md, refs/}` — brand + guardrails + reference stills;
  `creators/zion-clark/refs/soul-id/` = 20-image identity set.
- `reference-material/2k-screenshots/` — NBA 2K CGI style frames + `textures/` crops.
- `comfyui/` — starter workflow JSON + beginner import guide.
- `docs/` — `comfyui-workflow.md` (node plan), `comfyui-mcp-setup.md` (Comfy Cloud MCP),
  `comfyui-handoff.md` (self-contained brief), `forcing-the-cgi-look.md`,
  `higgsfield-cgi-playbook.md`, `seedance-comfy-handoff.md` (Ben's working notes on animating
  stills into video via Comfy Cloud's `ByteDance2ReferenceNode` — settings, reference-image
  patterns, lip-sync setup, gotchas).

## Working notes
- Apify (Instagram scraping) available via API token Ben provides — session-only, never commit.
- Higgsfield CLI/API exists (Soul ID, GPT Image 2) but img2img limits pushed us to ComfyUI.
- Commit + push to `claude/repo-setup-biy7uf` after changes. Keep refs/tokens out of git.

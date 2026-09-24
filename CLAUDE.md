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
  it drives generation isn't confirmed. Full plan and blocking sequence in
  `docs/photoreal-motion-transfer-pilot.md`.
- **Researched a YouTube walkthrough (transcript only) of a similar AI-influencer pipeline —
  surfaced the actual right tool: Higgsfield Genjutsu, not Kling or Seedance.** The video's
  workflow: generate a consistent character reference set (same idea as our photoreal character
  sheet), then use Higgsfield's **Genjutsu** motion-transfer feature to have that character
  perform motion from a source clip. Since this project already has Higgsfield touchpoints, check
  Genjutsu access there before chasing Kling (unconfirmed in the Comfy catalog) or Seedance's
  `reference_videos` (behavior unconfirmed). Updated `docs/photoreal-motion-transfer-pilot.md` to
  list Genjutsu as the primary candidate.
- **Ben provided a motion reference clip** — saved to
  `creators/kazumi/motion-refs/motion-test-01.mp4` (6.74s, 1080×1920, 30fps, a woman dancing).
  Source/rights basis not specified; raised once, Ben's direction was to proceed without further
  discussion of it — noted here for an accurate record, not revisiting unless something changes.
- **Motion-transfer 3-way comparison run: Kling rejected, Seedance and Genjutsu both landed the
  scene-placement fix, Genjutsu wins on cost.** All three run against the same GPT Image 2
  photoreal character sheet + `motion-test-01.mp4`:
  - **Kling Motion Control:** Ben's verdict — "useless... doesn't follow facial fidelity." Not
    pursued further. Also structurally limited to one reference image (hard node limit).
  - **Seedance 2.0 r2v:** first run kept the flat gray studio backdrop instead of the motion
    video's real scene (Ben: "I want her to be transposed into the motion reference scene, not
    this character reference gray background scene") — fixed by rewriting the prompt to
    explicitly say the real-world environment comes from the reference **video**, not the
    gray studio in the reference **images**. Retest confirmed the fix: correct room, strong
    identity, natural motion. First retry attempt was silent-audio-only because the provider
    auto-rejected the generated audio track as a possible copyright match (video itself
    unaffected) — succeeded on retry with `generate_audio` off.
  - **Higgsfield Genjutsu:** same fix (scene from the motion video, not the character sheet)
    confirmed working on the first run — correct room, strong identity, natural motion, audio
    came through intact (no copyright rejection).
  - **Cost: Genjutsu is ~8-16x cheaper.** Genjutsu = 45.5 Higgsfield credits per run. Seedance =
    365.49 Comfy credits per run — and the run that failed on the audio-copyright rejection
    still billed full price (bills on render completion, not on delivery), so the full
    Seedance test cost 730.98 credits across both attempts. Comfy Cloud doesn't expose a
    per-job dollar figure (invoiced at the account level), so this is a credit-unit comparison,
    not a dollar one. **Given comparable quality and the large cost gap, Genjutsu is the
    stronger default for this pilot going forward** — not yet a final call, Ben hasn't picked
    between them.

## New creator: Selena — GTA mockups, back to the core CGI-avatar thesis
- **Third POC creator, alongside Zion and Kazumi.** Ben's ask: build a GTA prompt pack for a new
  creator, Selena (`selenalenaxo` — Twitch/Kick affiliate streamer, Queens NYC, self-described
  "COD girly," Romanian/Turkish heritage per her IG bio). This is back on the main CGI-avatar
  thesis (full game-engine render), not the photoreal motion-transfer pilot above.
- **Reference sourcing hit real friction — two different blockers, two different fixes.**
  1. Most of her socials (Instagram directly, Twitter/X, Twitch, TikTok, Kick) are
     JS-rendered/auth-walled and blocked plain `WebFetch` (429/402/403). Spinning up a headless
     browser to force through them was explicitly denied by this environment's own safety
     classifier (flagged as circumventing platform scraping protections on a real person's
     images) — did not attempt to route around that block.
  2. Ben supplied his own Apify API token (session-only, never committed, per the standing
     `CLAUDE.md` working note) to run Apify's Instagram profile scraper properly. That worked —
     pulled her bio/follower data plus 12 recent post image URLs — but bulk-downloading the
     actual image files then hit a **second, separate** classifier block (flagged as PII
     handling on repeated bulk downloads of a real person's photos), intermittent at first then
     consistent. Per that block's own guidance, stopped rather than retried around it, and
     handed the decision to Ben rather than guessing at a workaround.
  3. **Actual fix: Ben pulled the rest himself and uploaded 15 screenshots directly via GitHub's
     web UI** (same upload-to-branch pattern used earlier for the GTA Loading-Screen Art
     reference images) — this is the reliable path for a new creator's reference photos going
     forward when scraping hits a wall; don't keep pushing on automated bulk-image pulls of a
     real person once the environment's classifier pushes back twice.
- **`creators/selena/refs/` built from 17 images total:** 1 Linktree avatar (direct CDN link, no
  scraping involved) + 1 Apify-sourced Instagram post + 15 of Ben's own uploads, all renamed from
  opaque `Screenshot ...png` filenames to descriptive ones (e.g.
  `selena_black_sweats_mirror.png`, `selena_car_daylight_portrait.png`,
  `selena_gaming_room_pink_chair.png`). `creators/selena/profile.md` documents her look (dark
  wavy hair, green eyes, full glam, nose stud, layered gold necklaces, no tattoos) and the
  sourcing trail above.
- **`prompts/selena.md` (Comfy/Nano Banana Pro, role-tagged) + `prompts/selena-higgsfield.md`
  (single-paragraph)** built: 7 GTA VI scenes (nightlife, club-entrance, beach, luxury-car,
  penthouse, casino, gaming-room — the last one nodding to her streamer identity). **Body ref
  chosen deliberately to dodge Kazumi's known GTA failure mode**: Kazumi's GTA scenes lost their
  body reference entirely after a revealing outfit + "cropped designer top" wording tripped
  Gemini's safety filter; Selena's body ref (`selena_black_sweats_mirror.png`) is a loose,
  modest oversized-sweats fit chosen specifically to avoid that — so this pack starts on the
  full 3-ref (face + body + style) recipe from scratch, instead of Kazumi's fallback 2-ref one.
  Reuses the existing `skills/gta6-style/reference/gtav_skyline_dusk.jpg` style ref (no new style
  ref sourced for her yet).
- **`[gta6 · nightlife]` test-rendered — Nano Banana Pro confirmed, GPT Image family (2 and 2.5)
  closed for this creator too.**
  - **Nano Banana Pro, first pass (2 seeds, 3-ref face+body+style):** both landed strong
    identity and correct CGI style (not photoreal). **Seed A had a real brand-safety leak:**
    it rendered "THE RIVIERA" and "OCEAN DRIVE" as legible signage — Ocean Drive is a real,
    famous Miami/South Beach street, never mentioned in our prompt text; the model pulled it
    from its own Vice-City associations, same underlying mechanism as the earlier "Bayview
    City" literal-signage issue. Seed B was clean (no real names). **Fixed:** added an explicit
    "do not render real-world neighborhood/street/place names as legible signage — invented,
    generic, or illegible text only" clause to the GTA style role in `prompts/selena.md` (all 7
    scenes) and a matching note in `prompts/selena-higgsfield.md`.
  - **Retest with the signage fix + 8 refs (3 standard + 5 additional identity photos of her,
    testing whether more refs help): clean.** No real place names this time (one scene had
    garbled non-word signage — not a real name, not a trademark leak, just imperfect text
    rendering). Identity and style both held. **The extra 5 refs didn't clearly improve
    anything over the original 3-ref recipe** — not worth the extra upload/wiring overhead
    for the rest of the batch. **Recipe locked: Nano Banana Pro, 3-ref (face + body + style),
    signage-fixed prompt.**
  - **GPT Image 2.5 (Flare/Sunburst tiers) tested as a live comparison — closed, same as GPT
    Image 2.** Discovered these tiers exist in Comfy Cloud's template catalog
    (`api_openai_gpt_image_25_sunburst_*`) even though `partner_generate`'s quick-reference
    registry doesn't list them yet — reachable via `run_template`/`submit_workflow` using the
    `OpenAIGPTImageNodeV2` node (`model: gpt-image-2.5-sunburst`, up to 16 ref images via
    `model.images.image_1..16`). First attempt (2 seeds, same wording as the working Nano
    Banana prompt): **both hard-rejected by OpenAI's own safety filter**
    (`safety_violations=[sexual]`) before rendering anything — traced to the body reference
    image combined with the "regardless of this reference's original styling" wording, same
    underlying issue as Kazumi's earlier GTA body-ref rejection. Reworded (softer body-role
    instruction explicitly forbidding bare-skin styling, "elegant... modest, full coverage"
    scene wording): **both seeds passed the filter this time, but came back fully
    photoreal** — indistinguishable from a real photo (visible pores, film grain, realistic
    depth of field), the same failure mode GPT Image 2 has now failed on 4 separate times.
    **Conclusion: GPT Image 2.5 is closed for this project's CGI-render requirement too — the
    entire GPT Image family (2 and 2.5) is a dead end here, don't retest either for this
    purpose again.** Nano Banana Pro remains the only proven path, now confirmed for Selena
    specifically as well as Zion and Kazumi.
- **Clarified: GPT Image 2.5's photoreal output is not a failure for every use — Ben wants it
  photoreal specifically, as a separate ask from the CGI-avatar requirement.** The "closed for
  this project's CGI-render requirement" conclusion above stands (never use it to try to hit the
  CGI-avatar look), but when Ben directly asks for a GPT-2.5 render, photoreal output is the
  correct/wanted result, not a defect to fix or resubmit.
- **5-scene / 2-seed comparison batch run: Nano Banana Pro vs. GPT Image 2.5 Sunburst, on
  club-entrance, beach, luxury-car, penthouse, casino (20 jobs total, 18 succeeded).**
  - **Nano Banana Pro (9/10 succeeded):** identity strong/consistent across every render; the
    signage fix held (no more real place names, only invented or garbled signage). **Found a
    new brand-safety leak, same underlying mechanism as the signage issue:** real automaker
    logos/badges rendering unprompted on vehicles — a legible Audi rings badge on
    `club-entrance` and a Ford Mustang running-horse grille emblem + real "Gulf" gas-station
    signage on `luxury-car`. **Fixed:** added an explicit "invented/generic vehicle design, no
    real automaker logos/badges/grille emblems" clause to the STYLE role in `prompts/selena.md`
    (all 7 scenes) and a matching note in `prompts/selena-higgsfield.md` — **not yet re-tested**.
    One outright failure: `beach` seedA — Gemini silently refused to generate an image.
  - **GPT Image 2.5 Sunburst (9/10 succeeded):** delivered exactly the photoreal look Ben wanted
    from it — zero CGI tell, clean identity, fully clothed/SFW, no logo issues spotted. One
    safety-filter rejection (`beach` seedB) even with the reworked prompt — confirms the fix
    reduces but doesn't eliminate the risk, scene/seed-dependent.
- **Face refs swapped after this batch, per Ben's direct call** (he flagged
  `selena_gaming_room_pink_chair.png` and `selena_skull_tank_vacation.png` as stronger likeness
  refs than the original `selena_car_daylight_portrait.jpg`). Recipe is now **4-ref: face ×2 +
  body + style** (same dual-face-ref pattern as Zion's pack) — updated in `prompts/selena.md`,
  `prompts/selena-higgsfield.md`, and `creators/selena/profile.md`. **Not yet re-tested with the
  new face refs.**
- **Next up:** re-run `[gta6 · nightlife]` and `[gta6 · luxury-car]` (the scene with the
  automaker-logo leak) with the new face refs + logo fix to confirm both hold, then batch the
  remaining scenes (club-entrance, beach, penthouse, casino, gaming-room) with the confirmed
  4-ref recipe.
- **Fixed a regression: `jet-ski-A` and `helicopter-A` had been accidentally dropped** from
  `prompts/selena.md` when the 48 remaining variants were expanded into self-contained blocks
  (excluded from that expansion on the mistaken assumption that already-validated scenes didn't
  need re-inserting into the file, which instead deleted them). Restored both using their
  confirmed-working text and the broadened watercraft/aircraft STYLE clause.
- **Built the parallel photoreal pack Ben asked for — `prompts/selena-photoreal.md`, same 13
  locations × 4 variants (52 scenes), GPT Image 2.5 Sunburst instead of Nano Banana Pro.** Ben's
  direction: he wants this pack to read as **UGC/candid/authentic — like her actual Instagram —
  not posed/stylized/professional** (that CGI-editorial quality is specifically what the Nano
  Banana pack should keep, and specifically what this pack should NOT have). Built around 3
  rotating candid sub-genres per location (picked per scene's plausibility): **POV selfie**
  (genre-led "A real, candid iPhone front-facing selfie photo of..." + the phone-never-visible /
  arm-blur technique from `skills/iphone-selfie-style/SKILL.md`, adapted from CGI to real-photo),
  **mirror selfie** (a new sub-genre for this project — phone IS visible held in the reflection,
  plain case, no screen content), and **candid, friend-taken** (third-person, caught mid-motion/
  mid-expression, not posed). Recipe: **2-ref only (face + body, no style ref)** — GPT-2.5 already
  defaults to photoreal, so there's nothing to fight toward unlike the CGI pack's Nano Banana
  wrangling. Carries forward the two GPT-2.5 photoreal-quality fixes already validated on this
  creator (gaze override to a natural candid angle instead of the reference photos' studio stare;
  full relighting to the scene's actual light sources instead of the references' studio lighting)
  plus the standing brand-safety clauses (no real place-name signage, no real vehicle/
  watercraft/aircraft logos). **Drafted only, not rendered** — same "prompts built, not run" rule
  Ben gave for the CGI expansion; validate 1-2 locations before batching if/when he asks to render.
- **New content avenue: Kazumi "penthouse party" 30-second vignette (multi-shot, Seedance 2.0
  img2video) — Ben's ask, shot-by-shot validation.** Not a prompt-pack scene, a standalone
  vignette: 7 shots moving through an upscale Miami Beach penthouse cocktail party (guests
  mingling, sophisticated ambient energy, explicitly NOT a rager), one consistent wardrobe
  throughout (blush-pink silk robe + camisole), **her hair deliberately black for this vignette
  only** (a one-off override from her canonical blonde balayage, via explicit "ignore the blonde
  hair in this reference" wording on the face-ref role — not a profile change). Output 9:16, 720p.
  **Chaining technique discovered mid-shoot and now the standing method for this vignette:** each
  new shot's still chains off the ACTUAL PREVIOUS SHOT'S RENDERED OUTPUT (not the original face/
  style refs) as the master anchor for identity/outfit/CGI-style continuity — this fixed visible
  style drift between shots. Two failure modes found and fixed while dialing this in: (1) chaining
  also over-anchored composition/pose/background, producing near-duplicate shots and one physics
  error (her feet rendering on the pool's water surface instead of the deck) — fixed by explicitly
  telling the model to ignore composition/pose/background from the chained reference and describing
  a genuinely different sub-location each shot; (2) a real place name ("MIAMI") rendered as legible
  neon signage in one background — same literal-signage mechanism as the earlier Bayview
  City/Ocean Drive leaks — fixed with an explicit no-real-place-name-signage clause, now standard
  in every shot's prompt going forward for this vignette.
  - **Shot 1 (Establishing)** — wide shot at the pool's edge, party mingling behind her. Confirmed
    and animated (slow push-in, ambient party sound). Locked as the vignette's anchor frame.
  - **Shot 2 (Walking hero)** — went through 3 iterations before landing: v1 (fresh refs, not
    chained) had good motion but style drifted slightly photoreal; v2 (chained off Shot 1) fixed
    style but broke physics (walking on water) and repeated Shot 1's exact composition; v3 fixed
    both (off-center framing, different sub-location — fire pit lounge) but leaked the real
    "MIAMI" signage; v4 fixed the signage. Confirmed and animated (low tracking shot retreating as
    she approaches, fire/party ambient sound).
  - **Shot 3 (originally planned as balcony turn/reveal) — descoped by Ben mid-shoot in favor of a
    mingling/interaction shot** ("her interacting and mingling with people at the party" instead of
    a solo turn-to-camera beat). The balcony version had gotten as far as a seed with visible face
    drift (caught by Ben, fixed by re-anchoring hard on the face ref for a second pass) before the
    scene concept itself was dropped — no loss, just superseded. New Shot 3: she's mid-conversation
    with two other guests at a bar-counter area, holding a champagne flute, genuine
    smiling/gesturing — confirmed working on Nano Banana Pro on the first chained attempt.
  - **GPT Image 2.5 Sunburst retested specifically for this vignette's CGI look, at Ben's request
    (he wanted to confirm whether 2.5 specifically — not just GPT Image 2 — could hit it, since
    2.5 is newer).** Same Shot 3 mingling scene, 3 escalating attempts: (1) plain prompt → fully
    photoreal, consistent with every prior GPT Image test on this project; (2) maximally aggressive
    CGI-forcing wording ("VIDEO GAME SCREENSHOT, NOT A PHOTOGRAPH", repeated CGI/in-engine language)
    → shifted noticeably toward smoother/waxier "next-gen game-engine" (Unreal/MetaHuman-style)
    shading, a real but partial move, still far from the stylized GTA/2K cutscene look the rest of
    the project uses, and identity fidelity dropped; (3) same aggressive wording + explicit
    identity-lock instructions and reordered refs (face ref first) → identity improved somewhat but
    hair partially reverted to blonde streaks, and Ben's direct judgment on this pass was that it
    still verged on photoreal. **Conclusion: reconfirms the standing "GPT Image family closed for
    this project's CGI-render requirement" finding — holds for 2.5 specifically, not just GPT Image
    2, even with best-effort aggressive prompt-forcing and identity-lock wording. Do not retest
    GPT Image (2 or 2.5) for the CGI-render look again**; Nano Banana Pro remains the only proven
    path. GPT-2.5 is still the right tool when photoreal output is explicitly wanted (Selena's UGC
    pack, Kazumi's character-sheet pilot) — this finding is about the CGI-render use case only.
  - **Next up:** animate Shot 3's still with Seedance, then continue the shot-by-shot vignette
    (originally-planned Shots 4-7: beauty close-up, jewelry detail, lounging, closing — subject to
    the same kind of on-the-fly rescoping Ben did to Shot 3) through to a full ~30s set of clips for
    Ben to edit together himself.

## New section: Christian Brown & Rocka Moss — separate client, shared AI-content playbook
- **A different engagement from the Lonnie Anthony Consulting CGI-avatar POC** — Ben acting as an
  independent brand/growth consultant to Christian Brown (pro basketball player, Kuwait) and
  Rocka Moss (sea moss wellness brand he co-owns), not Lonnie's agency. Added to this repo because
  one piece of it — Rocka Moss's need for AI-generated product photography and "real-looking"
  testimonial/lifestyle video ads, explicitly flagged in the brief as a gap with no existing
  playbook — is exactly the kind of AI image/video generation work this repo has spent months
  testing and hardening, just aimed at a different (photoreal, not CGI-stylized) output.
- **Two workstreams, per the brief:** Bucket 1 is pure brand-deal business development for
  Christian (Meta Ad Library prospecting, outreach, deal structuring) — no AI generation involved,
  out of scope for this repo. Bucket 2 is Rocka Moss growth marketing (Meta paid social + AI video
  ads + influencer seeding + reporting) — the AI video/photo piece is where this repo's work
  plugs in.
- **Built `clients/rocka-moss/`:** `PROJECT_BRIEF.md` (the full brief, saved verbatim for any
  agent coming in cold), `README.md` (orientation + scope boundary), and `ai-ugc-playbook.md` —
  the actual deliverable, mapping this repo's proven techniques onto Rocka Moss's two content
  needs. Key mappings: **product photography** → the multi-image role-tagging technique
  (`docs/multi-image-role-tagging.md`), applied to a bottle/label instead of a face, plus the
  standing brand-safety rule run in reverse (protect the real Rocka Moss label from being
  reinterpreted, while keeping everything else generic so no *other* real logo leaks in, same
  mechanism as the automaker-badge leak on Selena's pack). **Testimonial/lifestyle UGC video** →
  directly reuses Selena's photoreal UGC pack recipe (`prompts/selena-photoreal.md`: GPT Image 2.5
  Sunburst, not Nano Banana Pro — no CGI-fighting needed here since 2.5 already defaults
  photoreal; the three candid sub-genres — POV selfie, mirror selfie, candid friend-taken; the
  genre-anchoring POV lesson from `skills/iphone-selfie-style/SKILL.md`; the confirmed fixes for
  copied-expression and studio-lighting bugs), animated via Seedance 2.0 / Higgsfield Genjutsu
  (`docs/seedance-comfy-handoff.md`) — including `reference_audios.audio_1` as the direct answer to
  the brief's "how to use ElevenLabs for voiceover... stitch it into a video" ask, and the
  chain-off-the-previous-rendered-shot technique from Kazumi's penthouse-party vignette for
  multi-shot ads.
- **Not yet run against real Rocka Moss references — mapping only, not validated.** No Rocka Moss
  bottle/label reference photos sourced into the repo yet, no access to Shopify/Meta Business
  Manager confirmed, nothing generated for this client. Flagged an open consent question in
  `clients/rocka-moss/README.md`: if Christian Brown himself appears as an AI-generated subject in
  Rocka Moss ad creative, that needs its own explicit confirmation from him — the brief's
  Instagram-outreach permission (Bucket 1) doesn't automatically cover AI-likeness generation, same
  distinction already drawn for Kazumi's photoreal motion-transfer pilot.
- **Next up:** source real Rocka Moss bottle/label + testimonial-subject reference photos, validate
  one product shot and one POV-selfie testimonial still before batching either direction.
- **Added the creative-philosophy layer this playbook was missing: Frankie Shaw's (@frankyecom)
  AI UGC method, saved to `docs/frankie-shaw-ai-ugc-method.md`.** Ben's framing: context to use
  "when we craft the ideas and concepts before actually going into production" — this is concept/
  direction guidance (realism-as-the-product, environment-before-script, curiosity-before-product
  selling structure, the 5-beat transformational formula, a ranked format taxonomy, consumer
  archetypes, and V4 "realism law" POV/handheld/performance/audio rules), not a generation
  technique — sits alongside, not instead of, the existing how-to-render docs. **Applied directly
  to `clients/rocka-moss/ai-ugc-playbook.md`** as a new "Section 0" concept-direction layer ahead
  of the technical recipe: mapped Rocka Moss to founder/origin-story, in-car-confessional,
  street-interview, mirror-selfie/home-lifestyle, and fitness/physique formats specifically (and
  flagged podcast/keynote/engagement-bait formats as too high-production for a first validation
  round); flagged the no-bold/no-medical-claims rule as concretely relevant to sea moss
  marketing; mapped Rocka Moss's target audience to the Women <30 / general-wellness archetype,
  not the bold-claims-OK Men <30 one. **Independent confirmation, not new info:** the method's
  "front camera IS the camera" POV law matches exactly what this repo's own
  `skills/iphone-selfie-style/SKILL.md` arrived at the hard way (two failed fixes before
  genre-anchoring worked) — worth noting as validation, not treating as a new technique to layer
  on top.
- **Also unblocks part of the parked `clients/ai-ugc-agency/` context** (see below) — its
  session notes were explicitly waiting on "Frankie Shaw transcripts" to ground its own prompts.
  That folder stays parked/inactive per Ben's direction either way, but noted there for accuracy.
- **Enriched `docs/frankie-shaw-ai-ugc-method.md` with a second source doc (Ben's "AI UGC Style
  Bible," itself distilled from 3 Frankie Shaw video transcripts).** Mostly overlapping detail
  confirming the first pass, plus real new content: the direction-stack/motivation-buckets
  detail, expanded V4 realism-law specifics (zoom imperfection, artifact-prevention list), a
  V5.1/V5.2 funnel note, and — most consequential — a **Production Realities** section that
  resolves an open ambiguity from the parked ai-ugc-agency notes: **Seedance's real-face block on
  uploaded references isn't a case-by-case restriction to route around, it's why the whole
  Frankie Shaw method builds synthetic/fictional AI characters from the start** (via a locked GPT
  Image 2 character reference), never a real person's likeness. This surfaced a genuine
  strategic fork that didn't exist before: Rocka Moss testimonial content can either use a
  synthetic character (Frankie Shaw's proven method, sidesteps the Christian-consent question
  entirely) or Christian's real likeness via this repo's own already-working Comfy Cloud Seedance
  path (stronger authenticity, needs his explicit sign-off — the path hasn't hit a real-face
  restriction in this repo's own testing, per Kazumi's motion-transfer pilot). Flagged this
  explicitly in `clients/rocka-moss/README.md`, `ai-ugc-playbook.md` (both the open-question list
  and the "Next steps" concept-drafting step now call for deciding this up front), and
  `clients/ai-ugc-agency/README.md`. Also added a real worked Seedance prompt (a shoe-unboxing
  ad) as a concrete pattern to imitate — same "lock the product with multiple angle references"
  instinct as this repo's own multi-image role-tagging technique, independently arrived at.
- **Ben asked to go straight to source video transcripts for more learnings (not just the
  condensed style bible) before diving into Rocka Moss production.** The `2k-yt-transcript` skill
  is currently blocked in this environment for all 4 video URLs he sent — both the primary
  `youtube-transcript-api` path and the `yt-dlp` fallback are hitting a datacenter-IP block
  (429s, then "sign in to confirm you're not a bot" on yt-dlp itself). Didn't try to route around
  it with cookies/proxies — that starts to look like evading YouTube's bot detection rather than
  using a public API, same posture this project already took on the earlier Selena
  scraping-block decision. **Ben is pasting transcripts manually instead** (his own session's
  "Show transcript" workaround). **Reviewed 2 of 4 so far** (`FANWZjSbpdY`, `JCfun9lc2uY`) —
  genuinely new material folded into `docs/frankie-shaw-ai-ugc-method.md` (not just
  confirmation): the "storytelling problem, not a product problem" framing, the "curious ad" as
  an explicitly named soft-sell format, a fabricated-product prototyping technique (pressure-test
  a script/format with a placeholder product before real brand assets exist — directly useful for
  Rocka Moss), a CapCut production note (normalize for preview, export louder; the flash-cut
  effect is load-bearing, not decorative), the EU-market unsaturated-opportunity framing with its
  own honest non-guaranteed-transfer caveat, and a practical (not a recommendation) note on
  AI-content platform disclosure not clearly hurting CTR in his experience. **Not saving raw
  transcripts into the repo** — they're someone else's copyrighted spoken content; the doc's new
  "Direct video review" subsection under Sources tracks what's been reviewed and what's still
  pending (`vjAjDVOYLU4`, `1qZ42S_Z3bE`) without storing the transcript text itself.
- **Ben sent a 3-file transcript archive covering the remaining videos.** Two files
  (`FANWZjSbpdY`, `JCfun9lc2uY`) matched the pasted transcripts already reviewed almost exactly —
  no new material there. The third, `vjAjDVOYLU4` (realism thesis + 5 motivation buckets +
  environment-first), was genuinely new and added real content to
  `docs/frankie-shaw-ai-ugc-method.md`: "content converts on psychological response, not polish"
  as an explicit philosophy line, a relatable-not-intimidating casting principle generalized
  across archetypes (not just Women <30), a causal (not just sequential) framing of
  environment-drives-tonality in the direction stack, a new "brush-with-fame" hook (an unnamed
  high-status stranger implies endorsement — paired with an explicit brand-safety caveat that the
  technique works specifically by *not* naming or depicting a real identifiable person, consistent
  with this repo's own standing rule), and a note that he calls his structured prompting approach
  "JSON prompting" (name only, no actual template surfaced in this material). **`1qZ42S_Z3bE`
  remains the only outstanding video** — not part of this archive, still needs a transcript by
  whatever path is available (fetch tools remain blocked in this environment). Kept the same
  discipline throughout: no raw transcript text saved into the repo, only paraphrased new-beyond-
  what's-already-documented findings.
- **Ben brought a second creator's material — "Tay," a Shopify/dropshipping-focused channel —
  covering different ground than Frankie Shaw's creative philosophy.** Built a new,
  complementary doc, `docs/tay-ai-ugc-dropship-method.md` (same no-raw-transcript-storage
  discipline as the Frankie Shaw doc). Two videos: (1) a technique for reverse-engineering a
  competitor's already-proven static image ad into a video ad — source a similar/cheaper product,
  swap it into the competitor's proven composition via a Claude→Gemini→Canva→Kling AI tool chain,
  flagged with an explicit caution given this repo's own posture (lean on structure/composition,
  not a close copy of someone else's actual creative — this repo's own Meta-Ad-Library
  methodology already sources comparisons the safe way, via public screenshots); plus a simple
  CBO/broad-targeting/$50-a-day Meta ad-launch structure and concrete Omnisend retention-flow
  types (cart recovery, post-purchase cross-sell, high-value-customer segments) — real tactical
  detail the brief's generic mentions didn't have. (2) An AI agent (Manus) running an entire
  pipeline autonomously from one product link — deep multi-source research, TikTok viral-hook
  scraping, script drafting, a 3-view UGC character generation, and Kling 3.0's multi-shot video
  mode (a genuinely different capability from this repo's current Seedance/Genjutsu single-
  reference-set pattern) — flagged as worth evaluating, not adopting yet, and specifically called
  out one pattern (the agent taking over a live browser session to get past an access block) as
  the same shape of workaround this project has previously declined elsewhere, worth the same
  checkpoint-before-adopting caution even though the immediate use case (researching a public
  product listing) is lower-risk than the earlier real-person-scraping case it echoes. Added a
  short cross-reference to this new doc in `clients/rocka-moss/ai-ugc-playbook.md`'s Section 0.
- **Ben sent 4 more Tay videos (6 total now).** Substantially expanded
  `docs/tay-ai-ugc-dropship-method.md`. Highlights: (1) a granular, step-by-step Meta ad-account
  setup (CBO/$25-50 day/single-country/broad-targeting, a 3-format ad-copy technique, an
  "iterate within the same ad set via quick-duplicate" pattern, an explicit "don't 2x budget
  right after first sales" caution) — concrete enough to actually use when Rocka Moss's campaign
  launches; (2) an AI-assisted daily reporting pattern (Claude connected to Facebook
  Ads/Shopify/a profit app via MCP connectors, or a CSV-upload fallback) that maps directly onto
  the brief's "monthly reporting, plain numbers, no jargon" ask — flagged in
  `clients/rocka-moss/ai-ugc-playbook.md`; (3) **independent confirmation, from a second
  unrelated creator/platform, of the Seedance real-face-upload restriction** already documented
  from Frankie Shaw's material — cross-referenced into `docs/frankie-shaw-ai-ugc-method.md`
  directly, strengthening confidence it's a real platform behavior; (4) concrete Seedance
  production constraints (≤3 scenes per generation for quality, match scene duration to dialogue
  length) and a couple of tool capabilities worth evaluating later (an "enhance all" prompt-
  auto-expansion feature, an "extend" continuation mode flagged buggy by its own creator); (5) a
  product-page/landing-page generation workflow (Claude Design, modeled after a reference page —
  same reproduction caution as the ad-reverse-engineering technique — plus a genuinely new
  ad-to-landing-page message-consistency technique); and (6) **a real, standalone caution: that
  workflow fabricates fake customer reviews to fill an empty section, which is NOT something to
  carry over to Rocka Moss without Ben's explicit sign-off** — Rocka Moss has real customers and
  real reviews already, and fabricated testimonials are a meaningfully different risk category
  (deceptive social proof) than anything else flagged in this repo so far. Explicitly called out
  in `clients/rocka-moss/ai-ugc-playbook.md`. Same discipline throughout: no raw transcript text
  saved into the repo.
- **Ben asked directly whether there's a good grasp on Rocka Moss KPI targets (CTR, CAC).**
  Answered honestly rather than overclaiming: CAC/ROAS targets are solidly derivable straight
  from `PROJECT_BRIEF.md`'s own unit economics (breakeven ~$17–21 CAC / ~1.7–2.0x ROAS at 50–60%
  margin on a $34.99 bottle; a healthier target ~$9–11 CAC / ~3.5x+ ROAS, which isn't an outside
  number — it's what the brief's own "$3K spend → $10K+ incremental revenue" scaling scenario
  already implies). CTR is explicitly flagged as NOT grounded the same way — Rocka Moss has run
  zero paid ads, so any CTR figure is a generic benchmark (~1–2%+ healthy, <~0.8% flags a
  creative/hook problem per the Frankie Shaw hook material), not a validated target. Surfaced the
  single biggest variable that could move all of this: repeat-purchase/LTV data (sea moss is a
  daily-use consumable) isn't in the brief — if Rocka Moss reorders well, the $17–21 breakeven
  ceiling may be too conservative. Saved as `clients/rocka-moss/kpi-targets.md`, cross-referenced
  from `README.md`, and points at `docs/tay-ai-ugc-dropship-method.md`'s AI-assisted reporting
  pattern for tracking these live once the campaign launches.
- **Ben got Shopify admin access and pulled 3 real reports (Returning Customers, Customer Cohort
  Analysis, Net Sales Over Time) — found a real discrepancy that needs Christian's direct
  answer before finalizing any spend plan.** No Shopify MCP/connector exists in this session
  (checked via `ListConnectors` — full list has no Shopify entry); this was Ben's own admin
  login, data pulled manually and pasted as CSVs. **🚩 Actual net sales (Jan-Sep 2026, averaging
  ~$934/month, declining -63.5% from the Feb 2026 peak to the last full month) are roughly
  1/15th of `PROJECT_BRIEF.md`'s claimed "~$14K/month" — and June/July 2026 net sales were
  already far below $14K at the time the brief called that figure "current" (brief dated July
  2026), so "revenue declined since the brief" doesn't fully explain the gap.** Flagged directly
  rather than quietly worked around — the brief's own "$3K spend → $10K+ incremental revenue"
  scaling scenario (which the original CAC/ROAS targets were anchored to) assumes the $14K base;
  against ~$900/month actual, that scenario asks for 10x+ growth, not incremental. Possible
  explanations noted (a real but Shopify-invisible channel, e.g. the brief's own "product moves
  locally" line; an unverified claim; or it was simply wrong) — **not resolved, needs Christian's
  direct answer.** Separately, **real good news**: 63 returning customers / 198 total new
  customers in the trailing-12-month window ≈ **32% repeat-purchase rate** (solid for DTC
  wellness), averaging 2.86 orders per returner, and **real average order value among repeat
  customers is $46.96** — notably higher than the brief's flat $34.99 single-bottle assumption,
  which revises the breakeven CAC ceiling upward to ~$23–28/order (from the earlier $17-21
  estimate). Rewrote `clients/rocka-moss/kpi-targets.md` with all of this, marked the previous
  $9-11 CAC target as invalid until the revenue baseline is reconciled, and added a direct
  "ask Christian" next step. **Only aggregate numbers were saved — no customer names/emails
  went into the repo**, consistent with this project's standing PII-handling caution (same
  posture as the earlier Selena reference-photo scraping decisions).
- **Ben said to stop waiting on Christian and move forward on the real Shopify baseline — then a
  live Shopify MCP connector came online mid-session.** Rewrote `kpi-targets.md`'s framing: the
  $14K discrepancy is no longer a blocker (kept for the record, not chased further), and
  corrected a reasoning error from the previous pass — the brief's "$9-11 CAC / 3.5x ROAS"
  target is actually **valid as a per-unit economics target regardless of store size** (it's just
  a cost-benefit ratio), what was actually unrealistic was the **implied volume** (285-350
  orders/month against a store whose best month on record did ~34 real orders). Added a
  "Realistic Month 1 volume" target instead, benchmarked against the store's own historical
  acquisition range (15-44 new customers/month at its Oct 2025-Mar 2026 peak, now down to 4-8).
  **Confirmed live Shopify MCP access** (`get-shop-info`: store is Rocka Moss, rockamoss.com,
  base "Shopify" plan) and pulled real data directly via `run-analytics-query` (ShopifyQL): 285
  sessions/30d (thin, consistent with zero paid spend); a 90-day referrer breakdown showing
  Instagram as the clear #2 channel (8 orders/$456) meaningfully outperforming Facebook (1
  order/$79); and — genuinely new information not anywhere in `PROJECT_BRIEF.md` — **Rocka Moss
  actually sells 4 flavors** (Strawberry Shortcake, Mango Magic, Pineapple Breeze, Apple Pie),
  with Strawberry Shortcake the clear leader on both orders and revenue (worth featuring first in
  creative). Confirmed active discounting is already happening (gross ≠ net sales per flavor).
  Built `clients/rocka-moss/access-checklist.md` tracking what's done vs. still open (discount
  codes/terms, subscribe-and-save status, COGS-per-item, Meta Pixel/CAPI install status, email/SMS
  tool status, existing reviews) alongside the brief's still-outstanding non-Shopify access items
  (Meta Business Manager existence, Business Suite partner access, IG login, creative assets).
  Live MCP queries replace manual CSV pulls going forward for most Shopify data needs.

## Parked context: Ben's separate AI UGC agency (Premier Sea Moss) — not active, Rocka Moss is the focus
- Ben shared a working session doc from a **third, separate project**: his own general AI-UGC ad
  production service pitched to DTC brands broadly, with Premier Sea Moss (premierseamoss.com —
  **a different company from Rocka Moss**, despite both being sea-moss brands) as the first warm
  lead/spec-ad target. Saved to `clients/ai-ugc-agency/` (`session-reference.md` verbatim +
  `README.md` cross-referencing it against this repo's own Seedance/UGC findings) purely as
  context, per Ben's explicit direction: **"I'm not really interested in pursuing the new
  clients' stuff right now. I'm just focusing on the rocka seamoss. But I thought it was just
  important context to have."** Nothing here is active work — don't pick up its next-steps list
  (Frankie Shaw transcripts, character-image face-block test, spec-ad generation) unless Ben
  asks. Current focus stays Rocka Moss.

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
- `prompts/selena.md` (Nano Banana Pro, CGI/stylized) + `prompts/selena-photoreal.md` (GPT Image
  2.5 Sunburst, photoreal UGC/candid) — a matched pair covering the same 13 locations × 4 variants
  each, one stylized/posed, one candid/authentic-feeling. Different recipe (4-ref vs. 2-ref, no
  style ref on the photoreal side) and different guardrail emphasis (fighting toward CGI vs.
  fighting toward candid-not-editorial), same brand-safety rules.
- `creators/<name>/{profile.md, refs/}` — brand + guardrails + reference stills;
  `creators/zion-clark/refs/soul-id/` = 20-image identity set.
- `reference-material/2k-screenshots/` — NBA 2K CGI style frames + `textures/` crops.
- `comfyui/` — starter workflow JSON + beginner import guide.
- `docs/` — `comfyui-workflow.md` (node plan), `comfyui-mcp-setup.md` (Comfy Cloud MCP),
  `comfyui-handoff.md` (self-contained brief), `forcing-the-cgi-look.md`,
  `higgsfield-cgi-playbook.md`, `seedance-comfy-handoff.md` (Ben's working notes on animating
  stills into video via Comfy Cloud's `ByteDance2ReferenceNode` — settings, reference-image
  patterns, lip-sync setup, gotchas), `frankie-shaw-ai-ugc-method.md` (creative-philosophy
  reference for UGC-style ads — concept/structure/performance direction, not a rendering
  technique; apply before scripting any UGC ad, currently referenced by
  `clients/rocka-moss/ai-ugc-playbook.md`), `tay-ai-ugc-dropship-method.md` (a second, more
  tactical reference from a different creator — competitor-ad reverse-engineering, a
  Claude→Gemini→Kling production tool chain, a simple CBO Meta ad-launch structure, Omnisend
  retention-flow types, and notes on an AI-agent-driven end-to-end pipeline; complements rather
  than replaces the Frankie Shaw doc).
- `clients/rocka-moss/` — **a separate client engagement** (Christian Brown / Rocka Moss), not
  part of the Lonnie Anthony CGI-avatar POC. **Ben's current focus.** `PROJECT_BRIEF.md` (full
  context), `README.md` (scope/status), `ai-ugc-playbook.md` (this repo's CGI/photoreal
  generation lessons mapped onto Rocka Moss's product-photography and testimonial-video needs —
  see "New section" above).
- `clients/ai-ugc-agency/` — **parked context, not active work** (see "Parked context" section
  above). Ben's own separate AI-UGC agency pitch, Premier Sea Moss as the target lead — a
  different company from Rocka Moss. `session-reference.md` + `README.md`.

## Skills: installed 21 marketing skills from `coreyhaines31/marketingskills`
- **Ben asked what a getting-started to-do list would look like now that Shopify access exists,
  and separately whether any GitHub skills would make this a smarter paid-social/SEO/paid-search
  worker.** Proposed a phased plan (Pixel/CAPI confirmation + Shopify SEO/metadata + conversion-
  readiness in parallel first, since Pixel/CAPI is a harder blocker than SEO polish; creative
  production second; launch third) and pointed out the brief already names 4 skill repos never
  installed. Ben then linked `coreyhaines31/marketingskills` directly and asked which skills in
  it were worth pulling, then said to install everything judged helpful.
- **Cloned the repo, read all 49 skills' frontmatter, and installed a curated 21-skill subset**
  into `.claude/skills/` (MIT licensed — kept `THIRD_PARTY_LICENSE_marketingskills.txt` per the
  license's own terms; `.claude/skills/README.md` documents the full installed/excluded list and
  why). Installed: `ads`, `ad-creative`, `cro`, `seo-audit`, `schema`, `analytics`,
  `influencer-marketing`, `emails`, `sms`, `social`, `attribution`, `ab-testing`, `copywriting`,
  `copy-editing`, `competitor-profiling`, `marketing-psychology`, `offers`, `popups`, `video`,
  `image`, `ai-seo` — all map directly to Rocka Moss's actual situation (Meta ads, UGC/ad
  creative, Shopify SEO/CRO, the Pixel/tracking checklist item, Omnisend-style retention,
  Instagram being the real #2 channel, the discounting already happening, the 32% repeat rate).
  **Deliberately excluded ~28 SaaS/B2B-shaped skills** (onboarding, signup, paywalls, cold-email,
  prospecting, revops, sales-enablement, events, community-marketing, directory-submissions,
  programmatic-seo, launch, free-tools, lead-magnets, co-marketing, public-relations, aso, the
  SaaS-tier `pricing` skill — its own doc says single-product brands should use `offers`
  instead — plus the meta-planning skills `marketing-plan`/`marketing-ideas`/`marketing-council`/
  `marketing-loops`) that don't fit a single-brand DTC Shopify store — full reasoning in the
  README, and they're one copy-paste away if scope ever changes. `referrals` flagged as worth
  reconsidering later given the real 32% repeat-purchase rate, just not urgent now.

## Working notes
- Apify (Instagram scraping) available via API token Ben provides — session-only, never commit.
- Higgsfield CLI/API exists (Soul ID, GPT Image 2) but img2img limits pushed us to ComfyUI.
- Commit + push to `claude/repo-setup-biy7uf` after changes. Keep refs/tokens out of git.

## Ran a real SEO/metadata audit on Rocka Moss's Shopify store (2026-09-23)
- **Used the newly-installed `seo-audit` skill + live Shopify Admin GraphQL API + raw HTML pulls
  from rockamoss.com** — not guesses, every finding sourced. Real findings, most a same-day
  Admin fix: **all 4 products have `seo.title`/`seo.description` set to `null`**, so Shopify
  falls back to auto-truncated meta descriptions that literally cut off mid-sentence in the live
  render (confirmed on Strawberry Shortcake); **zero image alt text store-wide** on every product
  image; **`vendor` field says "My Store"** (Shopify's default placeholder) on 3 of 4 products,
  which leaks directly into the product's own JSON-LD schema (`"brand": {"name": "My Store"}`,
  confirmed live); **Pineapple Breeze is missing from the store's only collection**; and **zero
  `<h1>` tags anywhere on the site** (homepage and product pages both confirmed via raw HTML —
  this one needs theme/Liquid access, can't fix via the Admin API). Confirmed clean: robots.txt,
  sitemap.xml, canonicals, HTTPS, viewport, and baseline `ProductGroup` JSON-LD schema
  (price/availability per variant already present). Also confirmed no reviews exist yet on the
  product page checked, consistent with the standing don't-fabricate-reviews caution.
- **Method note, matches the skill's own guidance:** used raw `curl`+regex HTML parsing instead
  of relying solely on `WebFetch`'s summarized output, since the skill's own docs flag that
  `web_fetch`-style tools can silently miss JS-rendered or oddly-formatted elements — this is
  what caught the missing-H1 finding, which an LLM-summarized fetch had initially reported as
  "not shown in the provided content" (a false negative, not a real absence) before the raw-HTML
  pass confirmed it as a genuine, reproducible finding.
- Saved as `clients/rocka-moss/seo-audit.md`, cross-referenced from `README.md`, and folded the
  concrete fix list into `access-checklist.md`'s existing SEO/metadata section.

## Executed 6 of the SEO fixes directly via the Shopify MCP (2026-09-23, same session)
- **Ben asked whether any of the audit fixes could be driven directly rather than handed off as
  copy-paste instructions.** Checked each fix against the actual GraphQL schema rather than
  guessing: `productUpdate` mutation covers SEO title/description, vendor, productType, and tags;
  `fileUpdate` covers image alt text on existing media directly (no need to remove/re-upload);
  built-in `add-to-collection`/`update-collection` tools cover the last two. Only the missing-H1
  fix is genuinely blocked — it's a theme/Liquid change, and the Shopify MCP explicitly refuses
  writes to the live/published theme as a safety rail (allowed only on an unpublished theme copy).
- **Before executing, Ben asked for a "Day 0" baseline snapshot** so progress can be shown over
  time. Built `clients/rocka-moss/progress-log.md` — a dated, append-only changelog (distinct
  from `kpi-targets.md`/`seo-audit.md`/`access-checklist.md`, which get edited in place) — with
  the exact "before" state of everything about to change: live-confirmed title/meta description
  text for all 4 products (not just Strawberry Shortcake from the original audit), vendor values,
  blank alt text, missing collection membership, the stray meta-charset artifact.
- **Executed all 6 drivable fixes live**, verified each against a fresh page fetch after writing
  (not just trusting a successful mutation response): custom SEO title/description for all 4
  products, alt text on all 7 images, `vendor` corrected to "Rocka Moss" on 3 products,
  Pineapple Breeze added to the collection, the stray artifact removed, `productType`/`tags` set
  on all 4 products.
- **Ben asked mid-task to make sure the copy-editing/seo-audit skills' "avoid AI writing"
  reference was actually being used.** Ran all 8 product-facing strings (4 titles, 4
  descriptions) through a check against that reference's flagged list (em dashes, overused
  verbs/adjectives like "leverage"/"seamless"/"robust", filler words like "simply"/"truly", AI-tell
  phrases) — confirmed clean, all already written in plain, direct language with no hits. Good
  sign the copy was written right the first time, not that the check was skippable.
- **Caught and fixed a real mistake during execution, not after the fact:** the first attempt at
  cleaning up the collection description passed the replacement text HTML-escaped
  (`&lt;p&gt;...&lt;/p&gt;`) instead of as raw HTML, which would have made literal `<p>` tags show
  up as visible text on the live page — a worse problem than the stray artifact being fixed.
  Caught it by checking the mutation's own response (which echoed back the escaped text) before
  moving on, corrected immediately with proper raw HTML, verified live. Documented in
  `progress-log.md` for an accurate record, since Ben explicitly wants this log usable for
  external progress reporting.

## Parked (not active): full rebrand — logo, visual identity, website/theme redesign
- **Ben's own call, 2026-09-23:** "probably interested in changing the branding, logo, and
  website if we need to, considering it's all kind of basic and some of it's not great."
  Explicitly parked — no research, concepts, or design work started, and none should be without
  his go-ahead. Noted in `clients/rocka-moss/access-checklist.md` (new "Parked" section) and
  `README.md`'s Status, with the relevant context already on hand if/when it activates: the SEO
  audit's own findings (single generic collection, minimal nav, the now-fixed "My Store"
  placeholder leak, no content beyond 4 product pages + homepage) line up with Ben's "basic"
  read, though today's SEO/metadata fixes are a narrower scope (page data) and don't address
  this. `PROJECT_BRIEF.md`'s Phase 6 landing-page-quality mention is the closest existing
  precedent, broadened here to include logo/brand identity too.

## H1 investigation — root cause found, Ben fixing manually
- **Ben's ask:** "I'll fix the H1 manually. Let me know how to do it" (2026-09-23), after the SEO
  audit flagged zero `<h1>` tags site-wide as blocked by the Shopify MCP's live-theme-write safety
  rail. Investigated the live "Savor" theme's Liquid source directly (read-only theme-file access
  via GraphQL — the MCP can read theme files even though it can't write to the live/published one)
  to give precise, evidence-based instructions instead of generic Shopify advice.
- **Real root cause, more specific than "needs theme access":** `blocks/product-title.liquid` and
  `blocks/text.liquid` both delegate rendering to a shared `snippets/text.liquid` via a
  `type_preset` block setting (UI label "Preset," under each block's Typography section) whose
  options include `h1`-`h6`. But the snippet's actual element-selection logic only ever assigns
  `div` or `rte-formatter` to the rendered tag — the `h1`-`h6` preset values only add a CSS class
  for font sizing, never change the real HTML element. Confirmed this matches the live HTML found
  in the original audit (`<div class="text-block ... h2"><p>...</p></div>` — a styled `<div>`, not
  a real heading). **Meaning: switching the "Preset" dropdown to H1 in Shopify Admin — the fix
  Ben likely expected — does nothing to add a real `<h1>` tag, it only changes font size.** This
  is a genuine theme-code bug/limitation, not a misconfigured setting.
- **Instructions given to Ben:** duplicate the theme first (don't edit live), use Edit code to add
  an `elsif` branch to `snippets/text.liquid`'s element-assignment logic so `h1`-`h6` presets
  actually set `element` to that tag, then go into the block settings and set the Preset to H1 on
  exactly one block per page (homepage hero text block; product title block on product pages) —
  leaving everything else H2-H6 to avoid multiple H1s. Flagged the one real risk: a future
  Shopify theme-store update to "Savor" could overwrite this custom snippet edit.
- **✅ Fixed and confirmed live (2026-09-23), Ben executed both edits himself.** Ben pasted the
  full `snippets/text.liquid` file into chat himself (his own theme, his call to share it — kept
  to the established discipline of not proactively saving/reproducing large verbatim theme code
  in the repo either way). After the first fix (the `element`-assignment logic above) went live,
  the homepage hero got a real `<h1>` but the **product title block still didn't** — a second,
  separate bug in the same file: the product title renders through a `fallback_text` code path
  with its own hardcoded `<div>`, untouched by the first fix. Second small edit (same pattern —
  swap the hardcoded `<div>`/`</div>` for `<{{ element }}>`/`</{{ element }}>` in that branch)
  fixed it. **Confirmed live via raw HTML fetch after Ben published:** homepage has exactly one
  real `<h1>` (hero headline, rest `<h2>`); Strawberry Shortcake product page has exactly one
  real `<h1>` (product title). Noted a visual side effect (product title rendered larger, moving
  from its old H2-styled size to real H1 sizing) as expected theme behavior, not a bug — left
  as-is, tunable later via global Typography settings if needed. This closes out the last open
  item from the 2026-09-23 SEO audit — all 7 findings now live. Full detail in
  `clients/rocka-moss/progress-log.md`'s new Day 0 entry; `seo-audit.md` and
  `access-checklist.md` both updated to reflect the fix as done.

## Pulled the rest of the Shopify checklist items (2026-09-23) — none needed Meta Business Suite
- **Ben asked what else could move forward while still blocked on Meta Business Suite access.**
  Checked the already-fetched product page's own client-side JS first (Shopify's web pixel
  manager config) and found **a Facebook Pixel is already installed** — pixel ID
  `682325200982123`, via Shopify's own Facebook & Instagram sales channel app, confirmed firing
  standard events. Server-side Conversions API status still needs Business Suite to confirm, but
  this means whoever set the store up already has some Meta connection — worth searching for this
  exact pixel ID once access exists instead of starting fresh. Also found a second, unidentified
  marketing pixel (`D65JE4JC77U8VIJAA8H0`) — flagged for Ben/Christian to check in Admin.
- **Pulled the remaining 3 "still worth pulling" checklist items directly via GraphQL** (all
  Shopify-native, no Meta needed): **16 active discount codes** — mostly 20% off, including what
  look like **8 individual ambassador/seeding codes** already in informal circulation (short name
  fragments like `RMSWEAT`, `RMDEZ`, `RMTIM` etc., created Feb-Apr 2026) — real signal that
  informal influencer seeding may already be happening ahead of the brief's Bucket 2 "influencer
  seeding" workstream, worth asking Christian who these belong to. Also found `RMAP` at 100% off,
  worth confirming its purpose. **Zero selling plan groups exist** — confirmed no
  subscribe-and-save mechanism at all, the 32% repeat rate is fully organic; a real, confirmed
  open lever. **No COGS/unit cost entered anywhere** in Shopify (`null` on every variant) —
  margin math has to stay the brief's 50-60% estimate until Christian supplies real numbers.
  Checked the live page source for common email/SMS tool footprints (Klaviyo, Omnisend,
  Attentive, Postscript, Mailchimp) — found none, but flagged as inconclusive since some tools
  don't leave a client-side trace; a live discount code (`IG-EMAIL-1R9EMRC9`, time-limited)
  implies *some* automated flow exists, worth confirming directly in Admin → Settings → Apps.
- Updated `access-checklist.md` (all 4 items now resolved or clearly scoped) and `kpi-targets.md`
  (discount findings folded into the AOV/margin discussion, Next Steps checked off).

## Real Rocka Moss reference photos now exist in the repo (2026-09-23)
- **Ben asked "can you access this?" with a Google Drive folder link** ("Photography and Media,"
  owned by `rocka.moss0824@gmail.com`, folder ID `1fcSx7xcZ3jhA_m7_gbbqdB3exbyjDlC_`, shared just
  that day). Confirmed access via the Google Drive MCP connector and browsed it — the reference-
  photo source the checklist had been waiting on.
- **Found real product photography** (loose top-level files: Strawberry, Mango ×2, Apple Pie —
  real photos, not renders) and a **"Promo Photoshoots" folder with real, unbranded photos of a
  man holding product jars** (presumed Christian Brown, the co-founder) — exactly the testimonial-
  subject reference the "Decide synthetic vs. real Christian" open question needed. Also found
  **"Brand Campaign Visuals"**: 22 clean white-background 3D-rendered bottle mockups across **11
  flavors** (Strawberry, Mango, Apple, Pineapple, Peach, Mixed, Mixed-Blueberry, Soursop, Coconut,
  Blueberry, Passion Fruit) — **only 4 of which are live on Shopify today.** Flagged to Ben as
  worth asking Christian about (discontinued? seasonal? coming back?) since it changes what "the
  product line" means for creative and copy.
- **Flagged a likely misplaced folder, did not touch it:** `B Roll/` (owned by the photo studio,
  `officialeternalstudios@gmail.com`) contains several-GB ZIP archives named "Cross Family &
  Gravesite," "Family Pics," "Questionnaire," "Workout" — reads like an unrelated client's
  personal/family content, not Rocka Moss brand material. Never opened or downloaded; flagged for
  Ben to raise with the studio in case of a folder mix-up.
- **Technical constraint hit and worked around:** the Google Drive MCP's `download_file_content`
  tool returns full file content as inline base64 text — for the 10-17MB real photos, that would
  have flooded the conversation with tens of MB of unusable text for no benefit (can't visually
  inspect a base64 blob anyway). Rather than attempt that, asked Ben to re-send the useful subset
  directly, which landed as chat attachments **the session could read as actual images** (Read
  tool renders them) even though they weren't independently downloadable as clean files via the
  Drive tool. **First attempt to locate GitHub-web-UI-uploaded files failed** — checked both repo
  branches, all open PRs, and local git status, found nothing; the ask/answer mismatch was Ben
  uploading via chat attachment instead of GitHub, which is a valid alternate path this session
  can actually consume directly (found the files in the session's own scratchpad image directory).
- **Saved 5 real photos to the new `clients/rocka-moss/refs/` folder**, first of its kind for this
  client (previously only had `PROJECT_BRIEF.md`-level docs, no actual media):
  `rockamoss_strawberry_jar_bench.jpg`, `rockamoss_mango_jar_daylight.jpg`,
  `rockamoss_mango_jar_goldenhour.jpg`, `rockamoss_applepie_jar_mural.webp`,
  `rockamoss_founder_applepie_steps.jpg`. Full provenance/inventory in `refs/README.md`, including
  what was deliberately *not* pulled (Wellness Day event photos, the 22 flavor-render mockups,
  extra Founder Shot variants) and why. Ben also sent 4 white-background 32oz studio renders
  (Mango/Pineapple/Strawberry/Apple Pie) directly in chat — these arrived as inline content with
  no backing file this session could access on disk, but they're confirmed identical to files
  already cataloged in the Drive folder (`refs/README.md` records their Drive fileIds for
  re-pulling later if needed), so nothing was lost by not saving a separate local copy.
- **Consent note carried forward, not resolved:** having the founder's real photo on hand doesn't
  itself answer the standing "synthetic testimonial character vs. Christian's real likeness"
  question from `README.md` — storing his own existing marketing photos as reference material is
  a different, lower-risk act than generating new AI content of his likeness, which still needs
  his own explicit sign-off before any generation happens. Noted explicitly in `refs/README.md`
  and `access-checklist.md` so this doesn't get conflated later.
- Updated `README.md` (new refs entry, Status section) and `access-checklist.md` (Creative/content
  section — reference-photo sourcing now done, testimonial consent and validate-before-batch
  still open) to reflect all of this.

## First Rocka Moss test render — product-photo recipe confirmed working (2026-09-23)
- **Ben confirmed ("Yes, go ahead... using comfy")** to run the validate-before-batch product-shot
  test the playbook had been waiting on. Ran it directly via Comfy Cloud's `partner_generate`
  (this session does have Comfy Cloud MCP access, unlike earlier notes about the CGI-avatar
  Zion/Kazumi/Selena work needing Ben's local session) — uploaded
  `refs/rockamoss_strawberry_jar_bench.jpg` and generated via `openai/images-generations`
  (`gpt-image-2.5-sunburst`), a single role-tagged reference image plus a text-only Studio-style
  scene description, per `ai-ugc-playbook.md`'s product-photography recipe (photoreal engine, no
  CGI-forcing language).
- **Strong pass.** The front label reproduced with real fidelity — logo, wordmark, teal tagline
  bar, "STRAWBERRY" flavor tag, mineral claim, net weight, gold lid, mason-jar shape, gel color —
  on a clean plain studio background with a soft shadow, reading as a real photo. **One flaw
  found:** the side-panel ingredients/caution text rendered as illegible scribbles — a known
  GPT-Image-family limitation on small/dense text, doesn't affect the front label a Studio shot
  foregrounds anyway, but flagged for later (a second reference image of just that panel, or
  cropping it out of frame, would likely fix it if a future shot needs it legible).
- **Saved to `clients/rocka-moss/test-renders/`** (new folder, kept separate from `refs/` so real
  source photos and AI test outputs never get confused) — `strawberry_studio_v1.png` +
  `README.md` documenting the exact recipe/prompt approach and result. Sent to Ben directly as a
  file. Updated `access-checklist.md` (product-shot validation now done; POV-selfie testimonial
  still blocked on the synthetic-vs-real-Christian consent decision, unchanged).
- **This validates the recipe, not the whole style set** — only 1 of 5 product-photography styles
  (Studio) and 1 of 4 flavors tested. Worth running 1-2 more combinations before calling the
  direction locked, same standing discipline as every CGI-avatar pack in this repo.

## Fixed a real leak Ben caught: embossed "MASON" text copied from the reference photo
- **Ben looked closely at the first test render and caught something the initial review missed:**
  the jar's glass came out with "MASON" embossed into it — a real detail, not a hallucination.
  Checked the actual reference photo used (`refs/rockamoss_strawberry_jar_bench.jpg`) and
  confirmed "MASON" is genuinely embossed into the real jar's glass, just above the label — a
  generic canning-jar detail (not part of Rocka Moss's own brand identity) that the model
  faithfully reproduced from the source pixels. Same underlying mechanism as this repo's
  automaker-badge and real-signage leaks elsewhere: something genuinely present in a reference
  image that shouldn't make it into the output. Confirmed with Ben the jars themselves haven't
  changed — a prompt fix, not a stale-reference problem.
- **First fix attempt (a bare negation) only partially worked** — "the glass itself is plain, no
  embossed text" reduced the embossing but it was still faintly legible on close zoom. Confirms,
  in a new context, this repo's standing lesson from the iPhone Selfie POV fixes: negation
  instructions reliably lose to a strong visual signal already baked into a reference image's
  actual pixels.
- **Second fix attempt worked, confirmed via a zoomed-crop comparison of all 3 versions:** led
  with a positive physical description ("a completely smooth, plain glass body... clear unmarked
  glass") instead of a bare negation, and explicitly told the model the reference photo's glass
  differs from this jar's real glass ("this particular jar's glass is smooth and unmarked, unlike
  the reference photo's glass which happens to have embossed wording on it — do not copy that
  embossed wording"). Fully clean on inspection — completely smooth neck at any zoom level, front
  label still accurate. **This exact structure (positive description + explicit "reference photo
  differs from the real thing" framing) is now the standing fix, folded into
  `ai-ugc-playbook.md`'s product-photography section** for every future prompt using a real jar
  reference photo.
- Saved all 3 versions to `clients/rocka-moss/test-renders/` for the record
  (`strawberry_studio_v1.png`, `_v2_noemboss_partial.png`, `_v2_smoothglass.png` — the last one
  is the version to reuse), updated `test-renders/README.md` and `access-checklist.md` to match.

## Real gap found: Meta Ad Library competitor research was never on the working checklist
- **Ben asked directly whether competitor Ad Library research was already tracked — it wasn't.**
  Checked and confirmed: it's literally **step 1 of the 6-step pitch** in
  `PROJECT_BRIEF.md`'s "Key Messaging" section ("Pull every sea moss competitor ad running right
  now on Instagram/Facebook") and its own dedicated Phase 3 ("Competitor Research"), but it never
  got carried from the brief into `access-checklist.md`'s actual working to-do list — a real miss
  on my part, not something already covered elsewhere.
  - **Tried pulling it directly: blocked.** `facebook.com/ads/library` 403s on plain fetching —
    same JS-wall pattern this project hit repeatedly on Instagram/Twitter/TikTok/Kick during
    Selena's reference sourcing. Didn't push further, same standing posture as those blocks.
  - Added a new "Competitor research (Meta Ad Library)" section to `access-checklist.md` with the
    brief's own two paths forward: manual (Ben screenshots 10-15 winning ads himself, same
    upload pattern as every other image-sourcing block in this project) or Apify (reusing the
    session-only token pattern already established) if he wants it automated. Not yet started
    either way — his call which path.

## Ben asked for a full audit: what else from PROJECT_BRIEF.md never made it onto the checklist
- **Re-read the entire brief line by line and cross-referenced every actionable item against
  `access-checklist.md`.** Found two more real gaps plus one stale line, beyond the Ad Library
  item already caught:
  1. **Three of the brief's four named skill repos were never installed** — only
     `coreyhaines31/marketingskills` got pulled in. `AgriciDaniel/claude-ads` (an 8-command suite:
     `/ads dna`, `/ads photoshoot`, `/ads create`, `/ads generate`, `/ads meta`, `/ads math`,
     `/ads budget`, `/ads landing`), `tenfoldmarc/meta-ads-generator-skill`, and
     `hyperfx-ai/marketing-skills` were all named in the brief's "Skills Stack" section but never
     installed or tracked as missing. This had been mentioned once in passing in an earlier
     skill-install log entry ("pointed out the brief already names 4 skill repos never
     installed") but never turned into an actual checklist item or acted on.
  2. **The "other Rocka Moss co-founder" open question was never tracked anywhere** outside the
     raw brief text — it's in the brief's own "Open Questions" section and explicitly gates
     "committing to the full engagement" per the brief's wording, not just a Bucket-1 detail.
  3. **Stale checklist line found:** "existing creative assets Rocka Moss already has" was still
     showing as an open item even though the Google Drive photo folder (pulled 2026-09-23)
     already fulfilled it — checked off and corrected.
  - Confirmed several other brief items are correctly untracked, not missed: the financial-advisor
    referral lane, the black-truck business, agency-exclusivity check, and Christian's IG follower
    geography split are all Bucket 1 (personal brand deals), which `README.md` already scopes out
    of this repo's concern.
- Updated `access-checklist.md` with a new "Skills never installed" section and the co-founder
  open question, and fixed the stale creative-assets line. **Did not install the two new
  third-party skill repos without asking** — same consideration as the `coreyhaines31` install,
  which Ben explicitly greenlit; this is his call to make the same way.

# Photoreal Character Sheet — Kazumi (Motion-Transfer Pilot)

**⚠️ This is a different medium from every other prompt pack in this repo — read before using.**
Every other pack (`prompts/kazumi.md`, `prompts/kazumi-higgsfield.md`) renders Kazumi as a
**stylized CGI video-game character** — that's this project's core, client-approved concept. This
pack does the opposite on purpose: a **photorealistic likeness**, explicitly NOT stylized, NOT a
CGI/game render, NOT an illustration. It exists for one reason — to serve as a clean, consistent
identity reference for a motion-transfer pilot (Kazumi's real likeness performing motion from a
dance reference clip, via Seedance 2.0 / Kling motion control). It is not a new "style option" for
the main content pipeline; don't fold this into the regular batch process the other packs use.

**Consent basis:** Kazumi is Lonnie's client and has signed off on this specific pilot — a
photoreal-likeness + motion-transfer concept, distinct from the CGI-avatar work the rest of this
project covers. See `CLAUDE.md` and `docs/photoreal-motion-transfer-pilot.md` for the full context.
Don't extend this photoreal approach to any other use without confirming it's covered by that
same sign-off — the consent given for "stylize her as a game character" does not automatically
cover "generate a photoreal likeness," and vice versa; treat this pack's purpose (motion-transfer
identity reference) as the scope of what's been approved so far.

## Why 3 separate generations, not one grid image

A single "3 views in one image" character sheet asks the model to keep identity, outfit, and
lighting consistent across three separate figures inside one generation — a harder compositional
task than this project's proven pattern (one clean subject per generation, locked hard by
reference images). Generating **three separate images** — front, 3/4, profile — each pinned to
the same identity refs and near-identical style/lighting/outfit text, is more reliable and matches
how every other successful recipe in this repo works.

## Refs used in all three

- **Face (identity):** `creators/kazumi/refs/kazumi_yellow_polo_portrait.jpg`
- **Body (proportions/figure):** `creators/kazumi/refs/kazumi_olive_tank_denim.jpg`

## Reusable role blocks

```
FACE — REFERENCE IMAGE: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, skin tone. Ignore the clothing, pose, background, and makeup styling in this image.

BODY — REFERENCE IMAGE: use ONLY for body proportions and figure — her hourglass silhouette and natural proportions. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.
```

---

**[photoreal-sheet · front]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, skin tone. Ignore the clothing, pose, background, and makeup styling in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette and natural proportions. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

Now render: a real photographic studio portrait of the woman shown in the reference images, full body, facing directly toward camera, standing in a neutral relaxed pose with arms slightly away from her sides, weight even on both feet. She wears a simple fitted neutral-gray athletic top and leggings — plain, no logos, no text, no busy pattern — hair pulled back in a simple low ponytail so her silhouette reads clearly. Plain seamless light-gray studio backdrop, soft even studio lighting with no harsh shadows, a clean commercial-photography look. This must read as a REAL PHOTOGRAPH — natural skin texture and tone, natural fabric behavior, accurate human anatomy and proportions. NOT a CGI or video-game render, NOT an illustration or painting, NOT stylized in any way — photorealistic only. Full body visible head to feet, centered in frame. Vertical, 3:4 aspect ratio. Fully clothed, SFW.
```

**[photoreal-sheet · three-quarter]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, skin tone. Ignore the clothing, pose, background, and makeup styling in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette and natural proportions. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

Now render: a real photographic studio portrait of the woman shown in the reference images, full body, body turned three-quarters (about 45 degrees) with her face turned back toward camera, standing in a neutral relaxed pose, weight even on both feet. She wears the same simple fitted neutral-gray athletic top and leggings — plain, no logos, no text, no busy pattern — hair pulled back in the same simple low ponytail. Same plain seamless light-gray studio backdrop, same soft even studio lighting as a matching set with no harsh shadows, a clean commercial-photography look. This must read as a REAL PHOTOGRAPH — natural skin texture and tone, natural fabric behavior, accurate human anatomy and proportions. NOT a CGI or video-game render, NOT an illustration or painting, NOT stylized in any way — photorealistic only. Full body visible head to feet, centered in frame. Vertical, 3:4 aspect ratio. Fully clothed, SFW.
```

**[photoreal-sheet · profile]**
```
REFERENCE IMAGE 1: use ONLY for facial identity and likeness — her exact face shape, eyes, brows, lips, skin tone. Ignore the clothing, pose, background, and makeup styling in this image.

REFERENCE IMAGE 2: use ONLY for body proportions and figure — her hourglass silhouette and natural proportions. Ignore the specific outfit, pose, and background in this image. Keep the final output fully clothed and SFW regardless of this reference's original styling.

Now render: a real photographic studio portrait of the woman shown in the reference images, full body, in exact side profile (90 degrees to camera), standing in a neutral relaxed pose, weight even on both feet, looking straight ahead (not toward camera). She wears the same simple fitted neutral-gray athletic top and leggings — plain, no logos, no text, no busy pattern — hair pulled back in the same simple low ponytail. Same plain seamless light-gray studio backdrop, same soft even studio lighting as a matching set with no harsh shadows, a clean commercial-photography look. This must read as a REAL PHOTOGRAPH — natural skin texture and tone, natural fabric behavior, accurate human anatomy and proportions. NOT a CGI or video-game render, NOT an illustration or painting, NOT stylized in any way — photorealistic only. Full body visible head to feet, centered in frame. Vertical, 3:4 aspect ratio. Fully clothed, SFW.
```

---

## Notes

- Same plain outfit/backdrop/lighting language repeated deliberately across all three prompts —
  the "matching set" framing is meant to push the model toward consistency between the three
  separate generations, the same way this project's other packs repeat guardrail language
  verbatim across scenes rather than varying it.
- 3:4 vertical rather than this project's usual 9:16 — a full-body standing figure reads better
  in a less extreme aspect ratio, and this asset isn't meant for direct posting, just as an
  identity-lock reference for the motion-transfer step.
- Generate a few seed variants per angle and pick the one where identity is strongest and the
  photoreal read is cleanest (no CGI/illustration drift) — same discipline as every other pack.
- Once picked, save the 3 chosen images into `creators/kazumi/refs/photoreal-sheet/` so they're
  available as the identity reference for the Seedance/Kling motion-transfer test.

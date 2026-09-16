# Creator Profile — Selena

- **Handle:** `selenalenaxo` across platforms — [Instagram](https://instagram.com/selenalenaxo)
  (~19.8K followers), [Twitch](https://twitch.tv/Selenalenaxo) & [Kick](https://kick.com/selenalenaxo)
  (affiliate/partner streamer), [TikTok](https://tiktok.com/@ttvselenalenaxo),
  [X/Twitter](https://x.com/TTVselenalenaxo). Full link hub: https://linktr.ee/selenalenaxo
- **Who:** Twitch/Kick affiliate streamer and content creator, Queens NYC. Bio flags Romanian 🇷🇴
  and Turkish 🇹🇷 heritage. Self-described "COD girly" — Call of Duty–focused gaming content,
  IG business category tagged "Gamer." Launched her Twitch channel in 2018.
  New proof-of-concept creator for this project — third creator alongside Zion and Kazumi.
- **Brand:** Girl-next-door gamer glam — nightlife/going-out photos and casual mirror selfies
  mixed with a visible gaming-room presence (pink gaming chair/setup). Playful, confident,
  camera-aware; leans dressy/glam for going-out shots, casual and cozy for at-home content.

## Appearance (from `refs/`)
- Dark brunette, long wavy hair (natural black-brown with subtle warm highlights in some
  photos), worn down loose or in a half-up style.
- **Green/hazel-blue eyes**, full glam makeup — sharp winged eyeliner, long lashes, defined
  arched brows, glossy nude-pink lips.
- Fair-to-light-olive complexion with visible freckles/beauty marks on the cheeks.
- Slim, toned figure.
- Signature small details: a **nose stud**, gold hoop earrings, and layered dainty gold
  necklaces — an interlocking-ring pendant and a small sun/star charm pendant recur across
  multiple photos; no visible tattoos in any reference.
- Wardrobe split: black going-out fits (bodycon dresses, lace-up tops, strapless pieces) for
  nightlife/dining photos, and cozy loungewear (oversized sweats, tanks) for casual/at-home
  content. A pink gaming chair/gaming-room setup appears in one reference, tying to her
  streamer identity.

## Sourcing note
Reference photos pulled via two paths, both session-only (no scraping credentials committed):
1. **Linktree avatar** (`selena_linktree_avatar.jpg`) — direct CDN link, no scraping involved.
2. **Instagram** (`selena_ig_black_sweats_mirror.jpg` + 15 more screenshots Ben captured and
   uploaded directly via GitHub's web UI) — pulled via Apify's Instagram profile scraper using
   Ben's session-only API token (never committed) for the first image; the rest Ben sourced and
   uploaded himself after this session's environment restricted further automated bulk-image
   pulls of a real person (flagged by the platform's own PII-handling safeguard).

## Styles (this pack's focus)
- **GTA VI** (`skills/gta6-style/`) — full 3D CGI game-engine render, Vice City neon /
  daytime coast / luxury-car aesthetic. This is the primary ask for this creator — see
  `prompts/selena.md`.
- **Photoreal / UGC candid** — a parallel pack, `prompts/selena-photoreal.md`, same 13 locations
  × 4 variants but shot like her actual real Instagram content: candid, unposed, iPhone-camera
  quality (POV selfies, mirror selfies, friend-taken candids) instead of the GTA pack's
  posed/cinematic look. GPT Image 2.5 Sunburst, 2-ref (face + body). Drafted only, not rendered.
- Other styles (Cyberpunk, NBA 2K/WWE 2K, iPhone Selfie [CGI variant], GTA Loading-Screen) not yet
  built for her — add on request, following the same recipe as Zion/Kazumi.

## Look: FULL CGI RENDER
Same locked decision as the rest of this project — the entire frame (character *and*
environment) renders in the game engine, not a CGI character composited onto a real photo.
**Recipe (same technique as Zion/Kazumi, validated via `[gta6 · nightlife]` + a 5-scene/2-seed
batch):** Nano Banana Pro, multi-image role-tagging (face ×2 / body / style). Face refs:
`selena_gaming_room_pink_chair.png` + `selena_skull_tank_vacation.png` — swapped in after the
validation batch, replacing the original `selena_car_daylight_portrait.jpg` +
`selena_mirror_butterfly_case.jpg` pair once Ben judged these two as stronger likeness refs.
Body ref: `selena_black_sweats_mirror.jpg` (chosen specifically because it's a modest,
loose-fitting outfit — Kazumi's GTA body ref tripped Gemini's safety filter on a more revealing
outfit, so this one was picked to avoid that failure mode from the start). Style ref: reuse
`skills/gta6-style/reference/gtav_skyline_dusk.jpg` (same style ref as Kazumi's GTA scenes).
**Validation findings:** identity strong/consistent, the real-place-name signage leak (see
below) fixed and confirmed; found and fixed a new leak — real automaker logos/badges (Ford
Mustang emblem, Audi rings) rendering unprompted on vehicles in `luxury-car`/`club-entrance` —
now blocked by an explicit "invented/generic vehicle design" clause in the STYLE role. An
8-additional-ref experiment (12 face/body refs total) showed no clear improvement over the
standard recipe. Full prompts in `prompts/selena.md`.

**Real-place-name signage leak (found + fixed):** the first Nano Banana Pro test rendered
"Ocean Drive" (a real Miami street) as legible signage unprompted. Fixed with an explicit
"no real-world street/neighborhood names as legible signage — invented, generic, or illegible
only" clause in the STYLE role, confirmed clean on retest.

## Guardrails — SFW / brand-safe (same standard as Kazumi)
- Glam but clothed. Nightlife/going-out fashion is fine; NO nudity, NO explicit or overtly
  sexual posing, NO lingerie-as-subject.
- Confident and stylish, not pornographic — Snapchat/Facebook platform-safe.
- **Brand safety:** no real game/studio/logo names in prompt text (same standing rule as every
  other pack in this project) — describe the aesthetic only, invented place names, and every
  style role instructs the model to ignore/not-reproduce any logos visible in reference images.

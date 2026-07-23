# LonnieAI — CGI-Character Imagery POC

A proof of concept for **Lonnie Anthony Consulting**: turning social-media creators into
stylized **3D CGI / "video-game characters"** (in the spirit of Lil Miquela) as a new
content avenue for Snapchat Story + Facebook.

This repo produces **style skills** and **ready-to-paste prompt packs** for
[Higgsfield](https://higgsfield.ai) **GPT Image 2**. You run the prompts in Higgsfield
yourself (attaching each creator's reference photo); nothing here calls an API.

## Test creators

| Creator | Handle | Brand | Styles | Scenes |
|---|---|---|---|---|
| **Kazumi** | [@KazumisWorld](https://instagram.com/KazumisWorld) | Lifestyle / cosplay-adjacent | GTA VI, Cyberpunk 2077 | Vice City nightlife, Night City, luxury/exotic car, penthouse/cosplay hero |
| **Zion Clark** | [@zionclark](https://instagram.com/zionclark) | Fitness / athlete | NBA 2K, WWE 2K | Gym / weight room, track / stadium |

All output is **SFW / brand-safe**.

## Repo layout

```
skills/                     # style skills (one per game look), modeled on the 2K skill
  gta6-style/               #   Kazumi — GTA VI Vice City neon / cover-art
  cyberpunk-2077-style/     #   Kazumi — Night City neon-noir
  nba2k-style/              #   Zion — ported from the original 2K cutscene skill
  wwe2k-style/              #   Zion — WWE 2K broadcast realism
creators/                   # per-creator brand profile + reference stills (refs/)
prompts/                    # paste-ready prompt packs: kazumi.md, zion-clark.md
reference-material/         # the original 2K_Cutscene_Style_Skill.md (baseline)
```

## How to use a prompt pack

1. Open `prompts/<creator>.md`. Each entry is a copy-paste prompt tagged with **style** and **scene**.
2. In Higgsfield, pick **GPT Image 2**, set aspect ratio **9:16**, resolution 2k, quality high.
3. **Bind identity with a Soul ID** trained on the creator's `refs/`, used with **text-to-image**
   (no source photo). Feeding a real photo makes GPT Image 2 stay photoreal; a Soul ID text-to-image
   renders fresh and actually obeys the CGI style. Replace the creator name in a prompt with your
   Soul ID `<<<token>>>`.
4. Generate 2–3 variants per prompt and keep the best (the CG look has natural variation).

### The look: full CGI render

Every prompt renders the **entire frame — character *and* environment — in the game engine** (an
in-game cutscene): the cleanest "video-game character" read. We dropped the earlier
"CGI-character-composited-into-a-photo" look — GPT Image 2 couldn't hold it (it kept the photo
photoreal or ignored the style). See `docs/higgsfield-cgi-playbook.md`.

## Scaling later

The skills + packs are structured so an automation layer (Higgsfield CLI batch runner,
Soul ID per creator, delivery to Drive) can be added on top to roll this out to Lonnie's
other clients. Intentionally deferred for this POC.

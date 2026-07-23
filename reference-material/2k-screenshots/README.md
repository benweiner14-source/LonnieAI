# NBA 2K CGI style-reference screenshots

Real NBA 2K26 / 2K25 in-game screenshots (from Steam store media). Use these as a
**style reference** in Higgsfield to force the CGI game-character look — attach one of
these *alongside* the creator's identity photo so GPT Image 2 has a "this is what CGI
looks like" target to match. See `../../docs/forcing-the-cgi-look.md`.

## Best picks for a male athlete (Zion) — dramatic-lit CGI character renders
- `2k_01.jpg` — Knicks #7, spotlight broadcast close-up (**top pick**: hero framing + CG skin)
- `2k_02.jpg` — Thunder #2 close-up
- `2k_04.jpg` — Knicks #32, bearded medium shot
- `2k_06.jpg` — Celtics #0, bearded dribble
- `2k_07.jpg` — Raptors player close-up
- `2k_10.jpg` — Spurs player, motion close-up

Other character renders: `2k_03, 2k_05, 2k_08, 2k_09, 2k_11`.
Environment/City renders (for backgrounds): `2k_13` (skyline aerial), `2k_14` (City street),
`2k_15` (themed court).

## How to use (the CGI fix)
1. In Higgsfield GPT Image 2, attach TWO references: the creator's photo (identity) + one
   `2k_*` frame here (CGI style target).
2. Lower img2img strength (~0.5) so the style transfers instead of retouching the photo.
3. Keep the CGI-enforcement block from `docs/forcing-the-cgi-look.md` in the prompt.

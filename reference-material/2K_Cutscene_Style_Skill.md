---
description: Transform photos or scene descriptions into the NBA 2K in-game cutscene aesthetic. Use for any "2K style" or "cutscene look" image generation request.
---

# NBA 2K Cutscene Style — Image Prompt Generator

Transform real photos or scene descriptions into the NBA 2K in-game cutscene aesthetic using Higgsfield GPT Image 2.

**Reference library:** 28 MyCAREER cutscene screenshots + 39 broadcast/TV gameplay screenshots + 7 City aerial screenshots + 53 City storefront screenshots from NBA 2K26, all in `reference-screenshots/`.

---

## When to Use

User says: "apply the 2K cutscene look," "make this look like a 2K cutscene," "2K style," or provides a photo and asks for the in-game cinematic treatment.

---

## Core Style DNA

The NBA 2K cutscene look is **polished CG — better than last-gen but still identifiably rendered, not photographed.** Every element should read as "high-end game engine" not "real life."

### Rendering
- Real-time 3D game engine quality — high polygon, smooth clean surfaces
- Subsurface scattering on skin: slightly polished/waxy quality, with a distinct plastic sheen on foreheads and cheekbones
- Visible ear translucency in sidelit close-ups
- No film grain, no noise, no lens artifacts — clean digital render
- Clean geometry on all objects and architecture
- Jersey/uniform fabrics show detailed mesh texture patterns with visible micro-perforations
- Suit and formal fabric is unnaturally smooth with minimal wrinkles — very clean geometry
- **Sweat rendering** (broadcast/gameplay only): specular highlights on forehead, scalp, and shoulders during in-game moments; absent in MyCAREER story cutscenes
- **Tattoo rendering**: visible on arms, chest, and neck of scanned players; rendered as flat decal textures that follow skin contours cleanly

### Characters

**Two fidelity tiers exist:**
- **Face-scanned NBA players** (LeBron, Doncic, Durant, etc.): highest fidelity — detailed skin pores, wrinkles, realistic facial proportions, visible tattoos as decal textures, accurate facial hair volume. These look near-photorealistic up close.
- **MyCAREER/generic characters**: slightly smoother, more "CG doll" quality — less skin texture detail, simpler facial structure, more uniform amber skin tone. Still good but identifiably rendered.

**Common to both tiers:**
- Warm amber skin tones, smooth complexion
- **Simplified hair** is a key tell: buzz cuts render as a stippled texture map (individual dots, not strands); afros are volumetric simplified blobs; never strand-level rendering
- Facial hair (beards, mustaches) has a painted-on quality — volume without individual strand definition
- Foreground characters rendered at high detail with expressive faces
- Background NPCs noticeably lower fidelity — repeated models with clothing color variation, flat texture-card faces at distance
- Crowd members show varied postures (standing, sitting, arms raised) but limited animation; team jerseys with numbers visible in lower rows, gradual detail falloff into blurry color mass in upper deck
- Clothing has clean uniform folds — not photorealistic fabric simulation
- Screen-printed graphic logos on streetwear are sharp and fully readable
- Brand logos (Jordan Jumpman, Nike Swoosh) are crisp and prominently placed
- **Sideline reporter**: blonde female in white blazer, rendered at high detail, courtside positioning for postgame interviews
- **College uniforms** (Season 5+ content): Duke, UConn, Michigan, Ohio State, UCLA jerseys appear in Park/City — rendered at same quality as NBA uniforms with clean mesh texture, readable school names and numbers
- **MyTEAM card renders**: maximum fidelity player models against blurred arena backgrounds, same quality tier as face-scanned broadcast close-ups — used for digital card art

### Lighting
- Soft, diffused — no harsh shadows
- Warm practical light sources in interiors (pendant lights, window light, overhead fluorescents)
- Even overhead lighting in arena/gym scenes
- Subtle ambient occlusion in corners and under objects
- Rim lighting on main characters to separate from background
- European/Paris apartment scenes use strong directional sunlight through arched windows creating warm light shafts
- Locker rooms use flat overhead fluorescent with blue-tinted painted walls
- Empty arena practice scenes are darker and more industrial than game-day
- Interview/media set scenes use broadcast-style even front lighting

### Camera
- **Over-the-shoulder** is THE dominant conversation framing — one character's back-of-head in soft focus, other character sharp
- **Extreme close-ups** are frequent: tight face shots with very shallow DOF, environment almost entirely blurred (see frames 03, 15, 22, 23)
- **Wide establishing shots** for group/team scenes showing full environment (see frames 04, 07, 20, 25)
- **Two-shot medium** for 1-on-1 conversations, both characters visible waist-up
- **Low-angle hero shots** looking up at tall characters for dramatic effect
- **Detail/insert shots** on props (jersey numbers, desk items) for dramatic emphasis
- Eye-level or slightly below standard
- 16:9 widescreen (1920x1080)

### Color
- Warm, slightly desaturated palette overall
- Muted clothing colors: blacks, grays, olive, brown, navy dominate casual scenes
- Neutral/warm environments: wood floors, gray cabinets, white walls, marble counters
- Arena/gym scenes allow saturated brand colors and banners
- Team uniforms can be vibrant (purple/green, navy/red/white) — the muted rule applies to casual clothing, not uniforms
- European scenes tend warmer with more golden/amber tones from natural sunlight
- Blue-painted cinderblock walls in facility/locker room scenes provide cool contrast
- No heavy color grading — clean and balanced

---

## Base Prompt Template

Use this as the foundation. Replace `[SCENE DESCRIPTION]` with the specific content.

```
NBA 2K video game cutscene screenshot. [SCENE DESCRIPTION]. Real-time 3D rendered, high-polygon game engine quality. Smooth subsurface scattering on skin, slightly polished complexion with plastic sheen on forehead and cheekbones. Soft diffused lighting, no harsh shadows, subtle ambient occlusion. Warm amber skin tones. Simplified hair rendered as texture maps, not individual strands. Cinematic camera framing, shallow depth of field on background. Warm slightly desaturated color palette. Muted clothing tones. Clean geometry, no film grain or noise. 16:9 widescreen aspect ratio. Unreal Engine 5 quality, NBA 2K26 MyCAREER cutscene aesthetic.
```

---

## Scene Type Modifiers

Append these to the base template depending on the environment:

### Arena / Courtside (Game Day)
```
NBA arena environment, bright even overhead arena lighting, packed crowd in background with varied clothing colors at reduced detail, courtside media area visible, broadcast-quality lighting on foreground characters, sports banners and LED boards (Tissot, Nike) in background slightly out of focus, polished hardwood court floor with team logo at center.
```

### Arena / Practice (Empty)
```
Professional basketball arena during practice, empty bleacher seating visible, darker ambient lighting from overhead industrial rig, wooden court floor, Gatorade coolers and team bench visible courtside, scoreboard dark or showing zeros, coach in polo shirt uniform. More industrial and moody than game-day lighting.
```

### Interior / Rustic Home
```
Warm rustic family home interior, exposed wooden ceiling beams and support posts, dark wood bookshelves, warm pendant lighting, salmon/red-toned kitchen cabinets visible in background, wooden dining table, archway doorframes, cozy lived-in feeling with warm amber ambient light.
```

### Interior / Modern Apartment
```
Modern upscale city apartment interior, warm pendant lighting from above, marble countertops, hardwood flooring, white or gray cabinetry, tile backsplash, archway doorframes, clean contemporary furniture, city views through windows, warm golden ambient light.
```

### Interior / European Apartment (Paris)
```
Elegant Parisian apartment with tall arched windows, green trees visible outside, warm golden sunlight streaming in casting directional light shafts, beige/cream curtains, muted rose and sage furniture, dining table, hardwood floors, TV mounted on wall showing sports content. Bright and airy with European architectural details.
```

### Office / Business
```
High-rise office with floor-to-ceiling windows, city skyline visible through glass (LA or similar), natural daylight flooding in, modern minimal white desk with office props (desk phone, pen holder in bamboo cup, folders, binders), gray filing cabinets, floating shelves with framed photos and awards, blue and red file binders, clean corporate environment, neutral gray and white tones.
```

### Gym / Practice Facility (Nike/Brand)
```
Indoor basketball gym or practice facility, wooden court flooring, bleacher seating with scattered spectators in background at lower detail, Nike/brand banners prominent on walls, bright overhead gym lighting with clerestory windows, players and coaches in branded athletic wear.
```

### Outdoor / Park (Streetball)
```
NBA 2K Park outdoor basketball court, urban streetball environment, large colorful graffiti murals covering walls (bold reds, oranges, yellows, blacks), polished court surface, ambient overhead lighting, groups of players in streetwear (graphic tees, oversized fits, blue caps) standing at lower detail in background, vibrant but slightly muted colors.
```

### Outdoor / Hamilton Station Park
```
NBA 2K Hamilton Station Park outdoor basketball courts, train station-inspired architecture with grand stone/brick arched colonnades framing the courts. Subway/metro train cars visible behind the arches. Multiple basketball hoops with bright blue padded post stanchions. Colorful court surface in light blue and teal tones. City skyline with tall office buildings visible above the arches. Metal bleacher seating around courts. Players in college basketball uniforms (Duke blue, UConn navy, Michigan maize, Ohio State scarlet, UCLA blue/gold) — college jerseys render at same quality as NBA uniforms with clean mesh texture and readable numbers. Urban transportation-themed environment, brighter and more open than the graffiti-wall streetball park.
```

### Locker Room
```
Team locker room with wooden player cubbies/lockers, shoes and gear on shelves, colorful clothing hanging on racks, blue-painted cinderblock lower walls with white upper walls, overhead fluorescent lighting, team in matching uniforms (vibrant colors allowed), Jordan or Nike branding visible, slightly cramped group staging.
```

### Coach Film Room
```
Basketball facility film room or meeting space, blue-painted cinderblock walls, large whiteboard covered in play diagrams and handwritten strategy notes, coach or staff member in branded Jordan/Nike hoodie gesturing while explaining, overhead fluorescent lighting, utilitarian institutional environment.
```

### Restaurant / Diner
```
Casual restaurant or diner interior, dark wood-paneled ceiling with recessed can lights, condiment bottles (ketchup, mustard) on countertop, coffee equipment and menu boards partially visible in background, warm intimate lighting from overhead spots, wood and metal industrial aesthetic.
```

### Media Interview Set
```
Professional media or podcast interview setting, "Out of Bounds" style sports show branding visible in corner, character standing or seated addressing camera directly, well-lit broadcast-style front lighting, clean background with architectural interest (apartment or studio set).
```

### Postgame Hallway / Tunnel
```
Arena or facility hallway/corridor, wood-paneled or textured accent walls, overhead fluorescent panel lighting, security camera visible on ceiling, player in team jersey being interviewed, institutional clean environment, tight framing in narrow space.
```

### City / Neighborhood (The City)
```
NBA 2K The City open-world hub environment, massive futuristic plaza with concentric circular ground pattern in beige, blue, and maroon tones. Curved teal glass high-rise towers with giant LED screens showing NBA 2K26 player imagery. Oversized branded storefronts (Proving Grounds, Rec, Pro-Am, Theater, Legend) with angular concrete and metal architecture, each with distinct bold signage. Central landmark: large reflective globe/sphere with colorful landscape map texture. Interactive props scattered throughout — retro arcade gaming chairs (red/blue), digital leaderboard kiosks, glowing green waypoint markers on ground. Blimp overhead with promotional banners. Tiny NPC player avatars at very low detail scattered across the plaza. Bright overcast daylight, even ambient lighting, no dramatic shadows. All hard surfaces — polished concrete, brushed metal, glass — no vegetation. Theme-park scale with buildings towering over player figures. Elevated or aerial camera angle looking across the plaza.
```

### City Storefront Exterior
```
NBA 2K The City branded retail storefront, open-front design with no doors or glass — interior visible from plaza. Bold brand-color frame surround (unique per store), oversized 3D extruded metallic brand logo above entrance. Adjacent storefronts visible on either side in strip-mall arrangement. Clean concrete/stone plaza ground in front. Mannequins and product displays visible inside. Bright overcast daylight from outside contrasting with interior retail lighting.
```

### City Storefront Interior (Sneaker/Apparel)
```
NBA 2K The City retail store interior, brand-specific design language throughout. Shoes displayed on wall-mounted metal pegs or floating shelves organized by colorway. Gray or brand-colored mannequins on pedestals wearing full outfits. Brand logos repeated on walls, ceiling, and floor. Industrial-modern ceiling with grid panels, track spotlights, or fluorescent strips. Floor varies by brand (hardwood, red carpet, teal court lines, gray tile). Large lifestyle photography or player portraits on walls. Merchandise neatly arranged — sneakers, hoodies, jerseys, hats. Clean geometry, premium retail gallery feel.
```

### City Fitting Room (Shopping UI)
```
NBA 2K The City universal fitting room / dressing room. Warm reclaimed wood-paneled walls with horizontal slat pattern, small white potted plants on shelf above eye level, hardwood flooring, full-length mirror on back wall reflecting character from behind, warm pendant light overhead. Character stands center-frame wearing selected outfit. Semi-transparent dark shopping UI overlay on left side with product thumbnails, prices in virtual currency, SALE/OWNED tags, brand logo, and VC balance display bottom-right.
```

### Gatorade Training Facility
```
NBA 2K Gatorade Training Facility, large indoor gym with green basketball court (Gatorade "G" logo at center) surrounded by dark rubber flooring. Workout equipment zone — spin bikes, weight benches, dumbbells, pull-up rigs. Dark walls with bold white typography ("HYDRATES BETTER THAN WATER", "IS IT IN YOU?"), orange Gatorade Fuel Station service bar with NPC attendant in orange tee, Gatorade bottles on counter, gray metal stools. Overhead fluorescent panel lighting in grid ceiling. Orange and black brand color scheme throughout.
```

### Broadcast: Pregame / Matchup Intro
```
NBA TV broadcast presentation, 3D extruded metallic team logos flanking center frame, arena jumbotron/scoreboard visible above with team branding and stats, Crypto.com Arena (or equivalent venue) signage, dark arena ceiling with dramatic spotlighting, "Starting Lineups" graphic overlay at bottom, cinematic slow camera push toward court.
```

### Broadcast: Sideline Interview (Postgame)
```
NBA 2K postgame sideline interview, star player in team jersey with white towel draped over shoulder, visible sweat sheen on skin, blonde female sideline reporter in white blazer standing beside player, packed crowd celebrating in background with team jerseys visible, courtside Gatorade coolers and NBA branding, broadcast-quality even lighting on subjects.
```

### Broadcast: Player Portrait (Close-Up)
```
NBA 2K broadcast player close-up portrait, face-scanned real NBA player at maximum rendering fidelity, visible skin pores and sweat specular highlights, detailed beard/facial hair texture, tattoos rendered as clean decal textures on arms and neck, team jersey with sponsor patches (bibigo, Memorial, etc.), shallow depth of field with blurred crowd creating colorful bokeh behind, dramatic broadcast-quality lighting.
```

### Broadcast: Crowd Celebration
```
NBA 2K arena crowd celebration shot, hundreds of spectators standing and cheering, predominantly team-color clothing (gold/yellow for Lakers, etc.), visible jersey numbers and team logos on fans in lower rows, foam fingers, gradual detail falloff — lower rows show individual faces, upper deck becomes an impressionistic blur of team colors, dark arena ceiling above.
```

### Broadcast: Halftime Entertainment
```
NBA 2K halftime show on court, fan participants in matching team-color t-shirts with team logo, holding basketball, cheerleaders performing in background, "$10,000 HALF-COURT SHOT" banners on stanchion, bright arena lighting, packed crowd watching from stands, courtside sponsor signage (League Pass, Tissot) visible.
```

---

## Broadcast Graphics Package

The TV broadcast mode has a distinct visual language for its graphics overlays. Useful when creating content that mimics the full broadcast presentation:

| Graphic Type | Style | Reference |
|---|---|---|
| **Matchup Title Card** | 3D extruded metallic team logos (red/gold), 2K logo center, venue name below, dark arena BG | `broadcast_intro_00-00-03` |
| **Starting Lineups** | Semi-transparent overlay at bottom, player names + numbers, 3D team logos flanking, players walking on court behind | `broadcast_intro_00-00-23` |
| **Score Bug** | Bottom of screen, team colors (red/gold), abbreviated names (HOU/LAL), clean sans-serif | `broadcast_q1end_00-07-42` |
| **Quarter Break Card** | Small metal-framed scoreboard, "END OF 1ST QTR" / "START OF 3RD QTR" etc., 3D team logos | `broadcast_q1end_00-07-42` |
| **NBA Bumper Transition** | NBA logo centered on futuristic metallic/industrial background, blue LED left + red LED right, sci-fi server rack aesthetic | `broadcast_q1end_00-08-00` |
| **HALFTIME Title** | Yellow brush-stroke font on green panel, futuristic metallic mechanical frame with hex bolts, blue/red accent lighting | `broadcast_halftime_00-16-56` |
| **Halftime Report** | Split-screen stats card (team colors), 3D logos flanking, FG%/REB/AST/STL stats, "TOP PERFORMER" lower-third with player headshot | `broadcast_halftime_00-17-12` |
| **Player of the Game** | "PLAYER OF THE GAME" yellow text on red banner, 2K26 logo, player name below, shown over highlight replay footage | `broadcast_endgame_00-34-46` |
| **Final Score** | Same metal-framed card as quarter breaks, "FINAL" header, team scores, LED ribbon banners scrolling in BG | `broadcast_endgame_00-33-58` |

---

## How to Use with a Reference Photo

When the user provides a real photo (e.g., "make this photo of MSG look like a 2K cutscene"):

1. Describe what's in the photo (subjects, environment, action, composition)
2. Plug that description into `[SCENE DESCRIPTION]` in the base template
3. Add the appropriate scene type modifier
4. Specify that the output should match the composition/framing of the original photo
5. Add: `Based on the composition and framing of the provided reference photo.`

---

## Example Prompts

**Postgame interview at arena:**
```
NBA 2K video game cutscene screenshot. A female reporter in a coral blazer holding a microphone interviews a tall basketball player in a white team jersey, arms crossed, mid-conversation. NBA arena environment, bright even overhead arena lighting, blurred crowd cheering in background. Real-time 3D rendered, high-polygon game engine quality. Smooth subsurface scattering on skin, slightly polished complexion. Soft diffused lighting, subtle ambient occlusion. Warm amber skin tones. Simplified clean hairstyles. Over-the-shoulder camera angle, shallow depth of field on crowd. Warm slightly desaturated color palette. Clean geometry, no film grain. 16:9 widescreen. NBA 2K26 MyCAREER cutscene aesthetic.
```

**Family conversation in rustic kitchen:**
```
NBA 2K video game cutscene screenshot. Three people in a warm rustic kitchen — tall young man in black crewneck, woman in coral sweater seated at counter with laptop, older man in gray button-down standing opposite. Exposed wooden ceiling beams, salmon-red kitchen cabinets, hanging pans on wall rack, wooden dining table visible. Real-time 3D rendered, high-polygon game engine quality. Smooth subsurface scattering on skin. Warm pendant lighting, soft diffused shadows. Wide establishing shot showing full room layout. Warm amber color palette. Clean geometry, no film grain. 16:9 widescreen. NBA 2K26 MyCAREER cutscene aesthetic.
```

**Agent meeting in office:**
```
NBA 2K video game cutscene screenshot. Two men in a business meeting at a modern white desk. One leans forward in a brown suit, the other sits back in a black crewneck. High-rise office with floor-to-ceiling windows, LA city skyline visible. Natural daylight, desk phone and bamboo pen holder on desk. Real-time 3D rendered, high-polygon game engine quality. Smooth subsurface scattering on skin. Soft diffused lighting, subtle ambient occlusion. Medium two-shot, eye-level camera. Warm slightly desaturated color palette. Clean geometry, no film grain. 16:9 widescreen. NBA 2K26 MyCAREER cutscene aesthetic.
```

**Locker room team moment:**
```
NBA 2K video game cutscene screenshot. Team of basketball players in vibrant purple and green geometric-pattern uniforms standing in a locker room, some seated on benches, others standing. Wooden player cubbies with shoes and gear behind them, Jordan Jumpman logo visible on gear. Overhead fluorescent lighting, blue-painted lower walls. Player in foreground from behind looking at teammates. Real-time 3D rendered. Smooth subsurface scattering on skin. Slightly cramped group staging. Clean geometry, no film grain. 16:9 widescreen. NBA 2K26 MyCAREER cutscene aesthetic.
```

**Park court confrontation:**
```
NBA 2K video game cutscene screenshot. Group of five men in casual streetwear having an intense conversation on an outdoor basketball court. Central figure seen from behind in olive oversized t-shirt, others facing him in black graphic tees and casual fits. Large bold graffiti mural in red, orange, and black covering the wall behind them. Background players at lower detail. Real-time 3D rendered. Over-the-shoulder framing. Warm slightly desaturated colors. Clean geometry, no film grain. 16:9 widescreen. NBA 2K26 MyCAREER cutscene aesthetic.
```

**European arena cutscene:**
```
NBA 2K video game cutscene screenshot. Four basketball players on a European basketball court mid-conversation — two in white home uniforms, two in navy away uniforms with red/white/blue trim reading "Paris FC Basket." Dark empty arena seating in background, scoreboard visible, polished hardwood floor with team logo. Darker ambient lighting than NBA arenas. Real-time 3D rendered. Medium group shot at court level. Clean geometry, no film grain. 16:9 widescreen. NBA 2K26 MyCAREER cutscene aesthetic.
```

---

## Reference Screenshot Catalog

28 cutscene screenshots extracted from NBA 2K26 MyCAREER (PS5, 1080p). Located in `reference-screenshots/`.

> Frames 05 and 29 are **gameplay** (with HUD), not cutscenes — ignore for style reference.

| Frame | Timestamp | Scene Type | Camera | Key Details |
|-------|-----------|-----------|--------|-------------|
| 01 | 00:02:06 | Restaurant/Diner | Over-shoulder two-shot | Dark wood ceiling, recessed lights, condiments, white tee + black tee |
| 02 | 00:04:12 | Rustic Home | Medium single | Wooden beams, bookshelf, curtain rod, black crewneck |
| 03 | 00:06:18 | Kitchen (close-up) | Extreme close-up face | Shallow DOF, salmon cabinets blurred behind, skin sheen visible on forehead |
| 04 | 00:08:24 | Rustic Kitchen | Wide establishing | 3-person family scene, exposed beams, red cabinets, laptop on wooden counter |
| 06 | 00:12:36 | Park Court | Over-shoulder group | 5 characters, mural wall BG, streetwear (olive tee, black graphic tees, blue cap) |
| 07 | 00:14:42 | Indoor Gym | Wide establishing | Industrial ceiling, basketball court, black curtains, large NPC crowd, green Adidas tee |
| 08 | 00:16:48 | Park Court | Medium two-shot | Eye-level, mural BG, blurred crowd behind, olive tee + black tee, height difference |
| 09 | 00:18:54 | Modern Kitchen | Close-up face | White cabinets, tile backsplash, bright lighting, blonde buzz cut detail, black crewneck |
| 10 | 00:21:00 | Modern Apartment | Wide two-shot | City skyline through windows, floor lamp, gray couch, warm yellow walls, balcony door |
| 11 | 00:23:06 | Locker Room | Medium group | Purple/green uniforms, wooden cubbies, shoes on shelves, Jordan logo, blue wall |
| 12 | 00:25:12 | Coach Film Room | Close-up single | Jordan hoodie, whiteboard with play diagrams, blue cinderblock wall, hand gestures |
| 13 | 00:27:18 | Locker Room | Over-shoulder two-shot | Colorful clothes on hangers (orange, pink, blue), cubbies, shoes, blue/white walls |
| 14 | 00:29:24 | Nike Gym Facility | Low-angle two-shot | Nike banners on walls, bleacher crowd, brown suit agent + black crewneck player, jersey #6 walking away |
| 15 | 00:31:30 | Office (close-up) | Extreme close-up | Minimal BG, very shallow DOF, over-shoulder with blurred back-of-head foreground |
| 16 | 00:33:36 | Office Desk | Medium two-shot | City skyline, white desk, desk phone, pen holder, brown suit + black crewneck, classic agent meeting |
| 17 | 00:35:42 | Locker Room | Two-shot confrontation | "Union Elite" green/gold jerseys, blue cinderblock wall, electrical outlet visible, NPC in BG |
| 18 | 00:37:48 | Arena Court | Over-shoulder two-shot | Purple/green uniforms, blurred crowd behind, court-level, teammate conversation |
| 19 | 00:39:54 | Jersey Detail | Insert/detail shot | "HARRIS 16" jersey back, visible mesh texture perforations, blue/purple gradient, locker room BG |
| 20 | 00:42:00 | Nike Gym Court | Wide two-team shot | Two teams facing off, full crowd in bleachers, Nike branding, wide-angle at court level |
| 21 | 00:44:06 | Executive Office | Wide establishing | Navy suit man by window, photo shelves, file binders, TV on wall, gray walls, clean corporate |
| 22 | 00:46:12 | Office (close-up) | Extreme close-up face | Afro hair, navy suit, mustache detail (painted-on quality), bookshelves blurred behind |
| 23 | 00:48:18 | Office (close-up) | Over-shoulder reverse | Protagonist face with eyes downcast, subtle emotional expression, suit shoulder in foreground |
| 24 | 00:50:24 | Paris Apartment | Full-body standing | Arched windows, green trees outside, warm sunlight, "Out of Bounds" branding, dining area visible |
| 25 | 00:52:30 | European Arena | Wide group shot | "Paris FC Basket" uniforms (navy + white), empty dark arena, scoreboard, hardwood floor |
| 26 | 00:54:36 | European Arena | Over-shoulder coach | Practice scene, Gatorade coolers, empty bleachers, coach in polo, "ILIC 10" jersey back |
| 27 | 00:56:42 | Paris Apartment | Medium close-up | Arched windows, "Out of Bounds" badge, green trees, warm sunlight, black crewneck |
| 28 | 00:58:48 | Paris Apartment | Medium over-shoulder | TV showing game UI, gold chandelier fixture, warm sunlight, character leaning forward |
| 30 | 01:03:00 | Postgame Interview | Medium close-up | "Paris FC Basket 14" jersey, wood-panel hallway, "Out of Bounds" badge, overhead fluorescent |

### Broadcast / TV Gameplay (Lakers vs Rockets, Crypto.com Arena)

39 screenshots from NBA 2K26 TV Broadcast camera mode. Files prefixed `broadcast_`.

> `broadcast_q1end_00-08-06` is a black transition frame — ignore.

| File | Segment | Scene Type | Key Details |
|------|---------|-----------|-------------|
| `broadcast_intro_00-00-03` | Intro | Matchup title card | 3D HOU/LAL logos, 2K branding, Crypto.com jumbotron, dark arena ceiling |
| `broadcast_intro_00-00-08` | Intro | Arena overview | Title card foreground, full court warmups behind, packed crowd visible |
| `broadcast_intro_00-00-13` | Intro | Jersey logo close-up | Lakers logo on gold fabric, extreme macro, soft focus |
| `broadcast_intro_00-00-18` | Intro | Starting lineups + jumbotron | Stats on jumbotron, lineup graphic overlay, arena rafters |
| `broadcast_intro_00-00-23` | Intro | Player intro walk | Thompson #1 + Hachimura #28 from behind, lineup overlay, crowd blurred |
| `broadcast_intro_00-00-28` | Intro | LeBron face scan | Close-up during intro, beard detail, tattoos visible, "bibigo" patch |
| `broadcast_intro_00-00-33` | Intro | Two-player intro | Durant (Rockets red) + LeBron (Lakers gold), lineup overlay |
| `broadcast_q1end_00-07-36` | Q1 End | Wide court aerial | Full court overhead, end of quarter, players milling, full arena |
| `broadcast_q1end_00-07-42` | Q1 End | Score card | "END OF 1ST QTR" graphic, Durant #7 + Hachimura #28, LED banners |
| `broadcast_q1end_00-07-48` | Q1 End | Replay angle | Court-level action, score overlay, courtside crowd feet visible |
| `broadcast_q1end_00-07-54` | Q1 End | Doncic portrait | Luka #77 medium shot, high-angle, hardwood floor, crowd feet, wristband detail |
| `broadcast_q1end_00-08-00` | Q1 End | NBA bumper | NBA logo on futuristic metallic BG, blue/red LED split, sci-fi server aesthetic |
| `broadcast_q1end_00-08-12` | Q2 Start | Ultra-wide arena | Full arena from upper deck, jumbotron visible, "START OF 2ND QTR" card |
| `broadcast_q1end_00-08-19` | Q2 Start | Gameplay | Court-level, HUD visible, back to gameplay |
| `broadcast_halftime_00-16-08` | Halftime | Doncic walking off | Medium shot, Lakers #77 walking, score bug bottom, referee visible left |
| `broadcast_halftime_00-16-16` | Halftime | Jumbotron close-up | Crypto.com Arena scoreboard detail, half stats, dark ceiling, arena lights |
| `broadcast_halftime_00-16-24` | Halftime | Half-court shot contest | Two fans in yellow Lakers tees with basketball, cheerleaders behind, "$10,000" banners |
| `broadcast_halftime_00-16-32` | Halftime | Backboard close-up | NBA New Era logo, American flag sticker, hoop/net detail, crowd behind |
| `broadcast_halftime_00-16-40` | Halftime | Fan shooting | From-behind shot of fan on court, cheerleaders performing, Tissot scoreboard visible |
| `broadcast_halftime_00-16-48` | Halftime | Ball in air | Basketball mid-flight against blurred crowd, extreme shallow DOF |
| `broadcast_halftime_00-16-56` | Halftime | HALFTIME graphic | Yellow brush text "HALFTIME" on green panel, futuristic metallic frame, blue/red accents |
| `broadcast_halftime_00-17-04` | Halftime | Shot clock detail | Tissot shot clock + backboard, ball bouncing on rim, "LAKERS" LED banner above |
| `broadcast_halftime_00-17-12` | Halftime | Halftime Report | Stats split-screen (red/purple), 3D logos, FG%/REB/AST, Durant + Doncic headshots |
| `broadcast_halftime_00-17-20` | Halftime | Halftime Report alt | Same graphic, slightly zoomed, 2K logo center |
| `broadcast_halftime_00-17-28` | 3Q Start | Team huddle at bench | Doncic #77, Knight #4, LeBron #23 from behind, Gatorade towel, courtside fans visible at eye level |
| `broadcast_halftime_00-17-36` | 3Q Start | Jersey close-up | Durant ROCKETS #7, Nike swoosh, "Memorial" sponsor patch, extreme close-up fabric |
| `broadcast_halftime_00-17-44` | 3Q Start | Backboard action | Ball dropping through hoop, "GET THE App" stanchion, fan foam finger visible |
| `broadcast_halftime_00-17-56` | 3Q Start | Gameplay | Back to gameplay, 2K branding bar bottom |
| `broadcast_endgame_00-33-58` | Endgame | FINAL score card | "FINAL" HOU 62 - LAL 69, LED banners scrolling "LAKERS" in purple/gold |
| `broadcast_endgame_00-34-04` | Endgame | Crowd celebration | Close crowd shot, Lakers jerseys (#77, #24, #32), cheering, varied fidelity |
| `broadcast_endgame_00-34-10` | Endgame | Sideline interview | LeBron #23 + blonde reporter (white blazer), towel on shoulder, crowd celebrating behind |
| `broadcast_endgame_00-34-16` | Endgame | LeBron extreme CU | Maximum face detail — beard texture, skin pores, sweat sheen on forehead/scalp, bibigo patch |
| `broadcast_endgame_00-34-22` | Endgame | LeBron CU alt angle | Slightly different angle, mouth open, tattoo arm detail visible, crowd bokeh behind |
| `broadcast_endgame_00-34-28` | Endgame | LeBron CU 3rd angle | Wider frame, towel on shoulder, bibigo sponsor clearly visible, crowd at medium blur |
| `broadcast_endgame_00-34-34` | Endgame | Crowd wide | Upper/lower deck celebration, hundreds of fans in team colors, gradual detail falloff |
| `broadcast_endgame_00-34-40` | Endgame | Highlight replay | Court-level action shot, motion blur on players, Lakers/Rockets in contact, 2K watermark |
| `broadcast_endgame_00-34-46` | Endgame | Player of the Game | Doncic #77 driving to basket, "PLAYER OF THE GAME — LUKA DONCIC" lower-third |
| `broadcast_endgame_00-34-52` | Endgame | Aerial replay | High-angle court shot, Doncic shooting, Lakers floor logo visible, crowd at edges |

### City / Neighborhood Aerial Screenshots

7 aerial screenshots from NBA 2K26 The City open-world hub. Files prefixed `city_aerial_`.

| File | Camera | Key Details |
|------|--------|-------------|
| `city_aerial_01` | Wide aerial, slightly right | Central plaza with concentric circles, globe landmark center, Proving Grounds (right), Pro-Am gold logo (left), 2K26 billboards on teal towers, Warriors.com billboard, scattered NPCs |
| `city_aerial_02` | Wide aerial, center-left | Legend building (red/teal, left), Theater entrance (right of center), Dream basketball logo, central globe, arcade gaming chairs foreground, 2K26 banners on skyline buildings |
| `city_aerial_03` | Wide aerial, pulled back | Blimp visible in sky ("GET YOUR TICKETS NOW"), Starting5 building (left), Theater + Dream visible, gaming chairs foreground, broadest view of plaza layout, most NPCs visible |
| `city_aerial_04` | Medium aerial, right side | Closer angle on Proving Grounds entrance + Pro-Am basketball sign, central globe, gaming chairs midground, teal glass high-rise with 2K26 LED screen dominant right, clearest view of ground pattern detail |
| `city_aerial_05` | Medium aerial, left-center | Top Rep leaderboard kiosk prominent foreground, Rec building with basketball silhouette logo, Warriors-branded building with blue geodesic dome, Pro-Am globe and Theater visible center-right |
| `city_aerial_06` | Low aerial, upward angle | Central globe close-up with "Season 1" text, massive teal glass towers with 2K26 screens dominating frame, Rec silhouette logo right, most dramatic perspective — emphasizes tower scale |
| `city_aerial_07` | Low aerial, opposite angle | Similar to 06, CN Tower-style structure in skyline, "Season 1: SK..." text on globe, "Top Park" kiosk + "Entrance" sign visible, teal towers with multiple 2K26 screens, widest skyline view |

### City Storefront Screenshots

53 screenshots from NBA 2K26 The City storefronts — exteriors, interiors, and shopping UI. Files prefixed `city_storefront_`. Organized by brand.

**Brands covered:** Adidas, American Express, Coach, Converse, Gatorade, Jordan, New Balance, New Era, Nike, Puma, State Farm

> Fitting room / shopping UI frames (05–07, 12–13, 18, 27, 32, 37–38, 43, 48, 53) show the universal wood-paneled dressing room with UI overlay — useful for character outfit rendering but not environment style.

| File | Brand | View | Key Details |
|------|-------|------|-------------|
| `city_storefront_01` | Adidas | Exterior | Dark charcoal facade, 3D Adidas mountain logo, 4 player portrait posters (Lillard, Edwards, Harden, Mitchell) visible inside, green textured ground |
| `city_storefront_02` | Adidas | Interior left | Grid metal display panels with shoes on pegs, Adidas logo center, black hoodie hanging, hardwood court floor, "Streetball Park" neon visible outside left |
| `city_storefront_03` | Adidas | Interior back wall | 4 large player portraits (Lillard, Edwards, Harden, Mitchell), industrial grid ceiling with fluorescent strips, hardwood floor with court markings |
| `city_storefront_04` | Adidas | Interior right | Adidas Originals trefoil logo on grid panel, shoes + jacket display, Donovan Mitchell poster on right wall, hardwood floor |
| `city_storefront_05` | Adidas | Fitting room UI | Shopping categories (shirt, shoe), character in gray Adidas hoodie + joggers, VC balance 12.4M |
| `city_storefront_06` | American Express | Fitting room UI | Blue AmEx merch — bucket hats, oversize sweatshirts/tees, arm/leg sleeves, SALE tags, character in blue tee + shorts |
| `city_storefront_07` | American Express | Fitting room UI | AmEx arm/leg sleeves detail, blue patterned accessories, same character outfit |
| `city_storefront_08` | Coach | Exterior | Warm brown halftone-dot facade, "COACH" badge logo, oversized white sneaker with yellow taxi cab centerpiece, shoe wall visible inside |
| `city_storefront_09` | Coach | Interior close-up | Giant white sneaker + taxi cab display piece, Coach branding/sticker collage wall panels, curved shoe shelving behind |
| `city_storefront_10` | Coach | Interior shoe wall | All-white sneakers on dark wood shelves (5 rows, ~30 pairs), clean minimalist display, warm beige tones |
| `city_storefront_11` | Coach | Interior wide | Full interior — giant sneaker display, sticker/collage wall, curved shoe shelving, warm brown palette throughout |
| `city_storefront_12` | Coach | Fitting room UI | "COACH NEW YORK" varsity jacket, character in dark bomber + joggers, product preview overlay |
| `city_storefront_13` | Coach | Fitting room UI | Product grid — Coach Dinosaur, Soho shoes, Puffer Jacket, Hockey Shirt, Oversize Hoodies, Jersey (#41), prices in VC |
| `city_storefront_14` | Converse | Exterior | Yellow/gold frame, Converse star-chevron logo, gray stone surround, green dinosaur statue inside, SGA branding visible |
| `city_storefront_15` | Converse | Interior left | Large "SHAI GILGEOUS-ALEXANDER" typography wall, SGA logo, dark tees on rack, yellow shoe shelves, leather Chesterfield couch on round rug |
| `city_storefront_16` | Converse | Interior shoe wall | Yellow shelves with dark + lime sneakers (4 rows), Converse star-chevron logo above, gray concrete textured walls, exposed ceiling pipes |
| `city_storefront_17` | Converse | Interior gallery | Lifestyle photo grid wall (4 framed images), yellow shoe shelves left, gold dinosaur statue on pedestal right |
| `city_storefront_18` | Converse | Fitting room UI | Dark Converse tee + white shorts + lime green shoes, product preview overlay |
| `city_storefront_19` | Gatorade | Exterior | Massive curved silver/white/orange architecture, giant "G" logo dome, "GATORADE TRAINING FACILITY" text, "IS IT IN YOU?" tagline, city skyline behind |
| `city_storefront_20` | Gatorade | Interior wide (angle 1) | Green court with Gatorade logo, dark rubber surrounding floor, spin bikes, weight equipment, "HYDRATES BETTER THAN WATER" wall text, fluorescent grid ceiling |
| `city_storefront_21` | Gatorade | Interior wide (angle 2) | Opposite angle — pull-up rigs, weight benches, dumbbell racks in foreground, green court behind, "GATORADE TRAINING FACILITY" wall text |
| `city_storefront_22` | Gatorade | Fuel Station bar | Orange counter with Gatorade bottles, NPC attendant in orange tee, "REHYDRATE REPLENISH REFUEL" text, "GATORADE FUELSTATION" signage, dark brick wall, metal stools |
| `city_storefront_23` | Jordan | Exterior | Dark charcoal/black facade, large 3D Jumpman logo, angular granite column, red carpet floor inside, bright grid ceiling visible |
| `city_storefront_24` | Jordan | Interior shoe wall | 6 shelves of Jordans organized by colorway (reds top → blues bottom), gray stone panels, red carpet, marble display island |
| `city_storefront_25` | Jordan | Interior center | Red carpet, Jumpman logo on ceiling, B&W basketball photo art on back wall (player dunking), marble display islands with shoes, gallery feel |
| `city_storefront_26` | Jordan | Interior clothing | Clothing rack wall — tees, hoodies (white/orange/gray), folded items on marble table, B&W art visible, open to exterior right |
| `city_storefront_27` | Jordan | Fitting room UI | Categories: Shirts, Hoodies, Air Jordan Colorways, Pants & Shorts, Jordan Brand Colorways. Character in red hoodie + cream pants + Jordan 1s |
| `city_storefront_28` | New Balance | Exterior | Dark navy/black clean box facade, large 3D "NB" logo, sage/light blue interior walls, circular bench seating visible |
| `city_storefront_29` | New Balance | Interior left | Sage blue walls, wood shelf unit with mixed shoes/clothing on hangers, lifestyle photos on wall, warm wood accents |
| `city_storefront_30` | New Balance | Interior center | Large 3D "NB new balance" logo on sage wall, circular planter with green plant, curved wood bench, most lifestyle/organic of all stores |
| `city_storefront_31` | New Balance | Interior right | Sage walls, dark shelf unit with shoes on wood shelves + hanging clothes, 4 framed lifestyle photos, NB logo visible right |
| `city_storefront_32` | New Balance | Fitting room UI | Categories: Shirts, Colorways, Bottoms, Outerwear. Character in oversized graphic tee + jeans + NB sneakers |
| `city_storefront_33` | New Era | Exterior | Bold purple/blue frame, "NEW ERA" logo, colorful hat wall visible inside, warm wood floor, most product-dense store |
| `city_storefront_34` | New Era | Interior left | Wood shelving unit with caps sorted by team, "THE OFFICIAL CAP OF THE NBA" banner, track spotlights, warm wood floor |
| `city_storefront_35` | New Era | Interior center | Floor-to-ceiling cap wall (hundreds of colorful NBA team hats), rotating display stands on tables, wood flooring, most product-dense interior |
| `city_storefront_36` | New Era | Interior right | Cap wall continues, "THE OFFICIAL CAP OF THE NBA" plaque, purple/blue accent wall right, multiple display methods (peg wall, shelf, table) |
| `city_storefront_37` | New Era | Fitting room UI | OKC Thunder + Liberty caps previewed, character in white tee + jeans + Thunder cap |
| `city_storefront_38` | New Era | Fitting room UI | Thunder cap variants — Tip Off, standard, Two-Tone, prices 1,500–3,000 VC |
| `city_storefront_39` | Nike | Exterior | Orange/burnt orange frame, massive 3D Swoosh, mannequins in athletic wear flanking entrance, white shoe wall visible |
| `city_storefront_40` | Nike | Interior left | "WELCOME TO NIKE NBA2K" orange banner, player mural + abstract Swoosh graphic, mannequin in yellow jersey, shoes on grid pegs, gray floor with court lines |
| `city_storefront_41` | Nike | Interior center | Full shoe wall — dozens of colorful sneakers on metal pegs against white grid panels, dark speckled oval benches, "WELCOME TO NIKE NBA2K" banner |
| `city_storefront_42` | Nike | Interior right | Second player mural (red/cyan), two gray mannequins on pedestals, shoes on wall, industrial grid ceiling, most gallery-like Nike presentation |
| `city_storefront_43` | Nike | Fitting room UI | Categories: Shirts, Hoodies, Compression Shirts, Pants & Shorts, Colorways. Character in black Nike long-sleeve + athletic shorts |
| `city_storefront_44` | Puma | Exterior | Dark charcoal/black facade, 3D "PUMA" text + leaping cat logo, teal/turquoise floor visible, backlit white logo screen inside |
| `city_storefront_45` | Puma | Interior left | Diamond quilted texture wall panels, video screens showing gameplay, "All Pro Nitro 2" shoe display (pink), wooden bench, mannequin, teal court-pattern floor |
| `city_storefront_46` | Puma | Interior center | Large white backlit screen with Puma cat silhouette as centerpiece, teal floor with basketball court line pattern, black walls/ceiling, mannequin left |
| `city_storefront_47` | Puma | Interior right | Quilted walls with video screens, mannequin in pink outfit walking pose, clothing + shoes on display, teal floor continues |
| `city_storefront_48` | Puma | Fitting room UI | Categories: Shirts, Outerwear, Pants & Shorts, Socks, Colorways. Character in colorful patchwork #73 jersey + pink Puma sneakers |
| `city_storefront_49` | State Farm | Exterior | Bold red frame, "State Farm" triple-circle logo, "NGHBR GOODS" neon on gray brick back wall, mannequins in red outfits |
| `city_storefront_50` | State Farm | Interior left | Red + white branded display wall with oversized State Farm circles, mannequin in red suit, clothing rack with red/white items, gray brick wall |
| `city_storefront_51` | State Farm | Interior center | Gray brick walls, "NGHBR GOODS" red neon sign, dark ceiling with cross-shaped LED + round disc lights, mannequins in State Farm outfits |
| `city_storefront_52` | State Farm | Interior right | Lifestyle photography prints on walls, mannequins (red outfit, khakis, polo) on black pedestals, "NGHBR GOODS" neon text partially visible |
| `city_storefront_53` | State Farm | Fitting room UI | Categories: Shirts, Bottoms, Accessories. Character in red gradient tee + red shorts + headband |

---

## Tool Guidance

- **Primary tool:** Higgsfield GPT Image 2 (via `higgsfield-generate` skill)
- **Aspect ratio:** Always 16:9 (1920x1080) unless user specifies otherwise
- **If user provides a reference photo:** Use image-to-image mode, attach the reference, include the style prompt
- **Generate 2-3 variants** per request — the CG rendering style has natural variation that can be useful for picking the best result
- **Reference screenshots:** When building prompts, consult the catalog above to find the closest scene match, then read that reference frame for additional detail
- **Do NOT add:** film grain, lens flare, chromatic aberration, bokeh circles, or any photographic artifacts. The look is clean digital render.

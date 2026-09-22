# AI UGC Session Reference
**Date:** Sept 22, 2026 | **Status:** In progress

*Saved verbatim as handed off, for any agent coming in cold. See `README.md` in this folder for
how this connects to the rest of this repo's work.*

---

## 1. Project Context

Building an AI UGC production service targeting DTC (Direct-to-Consumer) brands. Full production stack using Seedance and related AI video tools. Goal: produce high-quality AI-generated UGC ad content and pitch to DTC e-commerce companies.

Primary deliverables in progress:
- A **30-second sizzle reel** for outreach
- A **spec ad for Premier Sea Moss** as first client proof-of-concept

---

## 2. Outreach Strategies

### Highest Intent Signals
- **Meta Ad Library** — Filter active ads. Look for brands running static images only (haven't cracked video) or low-quality UGC (easy upgrade pitch). Volume of impressions = real budget.
- **TikTok Creative Center** — Top performing ads by category. Brands there already understand creator content.

### Finding Companies
- **Minea / AdSpy / BigSpy** — Paid tools showing ad spend with product URLs
- **Crunchbase** — Filter "Direct to Consumer" + "Series A or Seed" — they just raised and need to spend on ads
- **Amazon Best Sellers** — Find niche category winners with their own DTC site
- **Similarweb** — Rising e-commerce sites

### Warm Outreach
- **LinkedIn** — "Head of Growth" or "Performance Marketing Manager" at 10–100 person e-commerce companies
- **DTC Communities** — DTC Newsletter, Operators Slack, DTC-focused Discords
- **Apollo.io / Reply.io** — Build a category list, find the marketing contact directly

> **Best pitch tactic:** Make a spec ad for the brand *before* contacting them. Eliminates the imagination gap and converts dramatically better than a cold deck.

---

## 3. Active Leads

### Premier Sea Moss ✅ Warm — They Replied

| Field | Detail |
|---|---|
| Website | premierseamoss.com |
| TikTok | @premierseamoss |
| Products | Sea moss gel — Mango Pineapple & Strawberry flavors |
| Key Claim | 92+ essential minerals, replaces multiple supplements |
| Usage | 2 tbsp on empty stomach each morning |
| Current Ads | Selfie-cam UGC style — casual, unpolished |
| Distribution | DTC website + Amazon storefront |

**Pitch angle:** Matches their existing selfie-cam aesthetic but with tighter scripting and pacing. Send finished spec with note: *"Here's what this looks like for your brand — ready to make 5 variations in a week."*

---

## 4. Missing Source Material

The following content was attempted but couldn't be retrieved. Needed before work can be grounded in Frankie Shaw's frameworks.

- 🎬 **YouTube Video 1** — "This AI UGC Framework Is Why My Ads Never Stop Scaling"
  - Fix: open video → three dots → "Show transcript" → copy/paste here

- 🎬 **YouTube Video 2** — "The Hidden Psychology Behind My AI UGC Ads"
  - Fix: same as above

- 🎬 **YouTube Video 3** — "How I Make AI UGC Videos That Look Real…"
  - Fix: same as above

- 𝕏 **@frankyecom — Recent Tweets**
  - X was behind login wall. Fix: log into X in Chrome, then re-read profile.

> **Impact:** Seedance prompts and ad script written so far are based on general UGC ad structure + Premier Sea Moss brand research — NOT on Frankie Shaw's specific archetypes. Once transcripts come in, prompts should be revised.

---

## 5. Skills & Constraints Loaded

### Seedance 2.0 — Key Rules
- Use `@Image1`, `@Image2`, `@Video1` etc. to assign roles to each uploaded asset
- Always state explicitly what each reference is for: `@Image1's character as the subject`
- Use time-segmented format for clips over 8s: `0–3s: ... 3–6s: ...`
- Include audio direction in every prompt — sound design improves output significantly
- Max 9 images, 3 videos, 3 audio files per generation (12 total)

### ⚠️ Critical Constraint
**Seedance blocks realistic human faces in uploaded reference images (platform compliance).** Your locked GPT character image may get blocked. If it does, prompts need to be rewritten as text-to-video with embedded character descriptions.

### Video Prompting — Global Rules
- Never include model name, duration, aspect ratio, or resolution inside the prompt text
- For image-to-video: treat the uploaded image as the visual anchor — focus prompt on **motion, camera, emotion/performance, and audio** only
- For i2v: do not re-describe the character's appearance

---

## 6. Premier Sea Moss — 30s Ad Script

**Format:** 9:16 vertical, selfie-cam style
**Character:** Woman, late 20s–early 30s, natural look, warm morning kitchen

**[0:00–0:03] HOOK**
> *"My doctor literally asked me what I changed. I said two tablespoons of this every morning."*

*Opens mid-delivery. She's already talking frame one. Direct eye contact, confident.*

**[0:03–0:08] PROBLEM**
> *"I was taking 6 different supplements — iron, magnesium, collagen, all of it. Spending $200 a month and still felt exhausted."*

**[0:08–0:14] PRODUCT INTRO**
> *"Then I found Premier Sea Moss. It's a gel — mango pineapple flavor — and it has 92 minerals in one. I just take it on an empty stomach before breakfast."*

*Holds up jar, tilts label to camera.*

**[0:14–0:22] BENEFITS**
> *"Week one my energy was just... steady. No crash. By week three my skin cleared up and I stopped reaching for coffee by 2pm."*

**[0:22–0:27] SOCIAL PROOF**
> *"I've been doing this for 60 days. I'm not going back."*

**[0:27–0:30] CTA**
> *"Link in bio — they have a starter bundle."*

*Points down to bottom of frame. Text overlay with link.*

---

## 7. GPT Image 2 — Character Reference Prompt

Paste into ChatGPT (GPT-4o image generation). Regenerate 2–3 times until you lock a face you like. Save that image — it's the `@Image1` reference for Seedance.

```
Photorealistic portrait of a woman, late 20s to early 30s, mixed complexion
with clear glowing skin, natural wavy dark brown hair pulled loosely back,
minimal makeup, warm almond-shaped brown eyes, slight smile, natural and
approachable. She is wearing a soft cream oversized crewneck. Shot in a
bright warm morning kitchen, natural window light hitting her face from
the left. Selfie-style framing, slight downward angle as if holding a phone.
No filters, no studio lighting — candid, authentic UGC feel.
Ultra-realistic, 4K, no AI artifacts.
```

---

## 8. Seedance 2.0 — Shot Prompts

Upload locked character image as `@Image1`, product jar/label shot as `@Image2`.
Shot 4 is text-to-video only — no character reference.

---

### Shot 1 — Hook | 3–4s | i2v

```
@Image1's character as the subject. Medium close-up selfie-cam, slight handheld drift. Character is already mid-delivery, speaking directly into camera with confident energy. Dialogue: "My doctor literally asked me what I changed... I said two tablespoons of this every morning." Expression is knowing, slight smile while speaking, eyes locked on camera the entire time. Audio: natural voice clear in mix, soft morning room tone underneath.
```

---

### Shot 2 — Problem | 5s | i2v

```
@Image1's character as the subject. Medium close-up handheld selfie-cam with natural micro-shake. 0–2s: woman speaks with mild animated frustration, free hand gestures expressively mid-sentence. 2–5s: expression softens into a small exhale and knowing headshake, settling into relief. Audio: natural ambient kitchen sound throughout.
```

---

### Shot 3 — Product Intro | 4s | i2v

```
@Image1's character as the subject, product label details reference @Image2. Medium close-up selfie-cam. 0–2s: woman raises sea moss gel jar into frame with her non-camera hand and rotates it so label faces forward. 2–4s: glances at jar then returns gaze to camera with a confirming nod and half-smile. Audio: soft glass clink, warm room tone.
```

---

### Shot 4 — Product B-roll | 4s | TEXT-TO-VIDEO (no character)

```
Static camera with slow push in toward a glass jar of golden translucent sea moss gel on a white marble counter in warm morning window light. 0–2s: wooden spoon enters from above and dips into the gel. 2–4s: spoon lifts slowly, thick viscous gel drips in a long satisfying strand. Audio: subtle ambient kitchen tone, soft wet texture sound. Food photography aesthetic, macro lens, no people.
```

---

### Shot 5 — Benefits | 5s | i2v

```
@Image1's character as the subject. Medium close-up handheld selfie-cam. 0–3s: woman leans slightly toward camera, eyes bright, nodding with growing energy as she speaks. 3–5s: free hand rises into a small emphatic point gesture, genuine smile breaks naturally. Audio: soft ambient room tone, upbeat conversational energy.
```

---

### Shot 6 — Social Proof | 4s | i2v

```
@Image1's character as the subject. Medium close-up selfie-cam drift slowly settles to near-static. 0–2s: expression softens from energized to sincere, speech pace slows visibly. 2–4s: holds direct eye contact, quiet exhale, single slow nod. Audio: quiet morning ambient, soft breath. Intimate warm frame.
```

---

### Shot 7 — CTA | 3s | i2v

```
@Image1's character as the subject. Medium close-up handheld selfie-cam. 0–1s: expression brightens into a full smile. 1–3s: index finger points downward off the bottom of frame twice with two deliberate nods, mouth forms a closing word. Audio: soft upbeat ambient energy, natural room tone.
```

---

## 9. Next Steps

1. **Get Frankie Shaw transcripts** — Copy from the 3 YouTube videos (three dots → Show transcript) and paste here. Archetypes need to be extracted before prompts are finalized.
2. **Log into X in Chrome** — Then revisit @frankyecom to pull recent posts and methodology.
3. **Test character image in Seedance** — If it gets blocked by face restriction, report back and i2v prompts will be rewritten as text-to-video.
4. **Generate Shot 4 (B-roll) first** — Text-to-video, no character reference, safest starting point to confirm product aesthetic.
5. **Build outreach tracker** — Premier Sea Moss is entry #1. Track brand, contact, status, follow-up date.
6. **Reply to Premier Sea Moss** — Once spec is generated, send with pitch note: *"Here's what this looks like for your brand — ready to make 5 variations in a week."*

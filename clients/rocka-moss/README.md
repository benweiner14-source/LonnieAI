# Christian Brown & Rocka Moss — separate client engagement

**This is a different client relationship from the Lonnie Anthony Consulting CGI-avatar POC
documented at the repo root** — Ben acting as an independent brand/growth consultant to a pro
athlete (Christian Brown) and the wellness brand he co-owns (Rocka Moss), not Lonnie's
social-media agency. It lives in this repo because **Bucket 2 of the engagement needs exactly
the kind of AI content-generation expertise this repo has spent months building and testing** —
see `ai-ugc-playbook.md`.

## What's here

- **`PROJECT_BRIEF.md`** — the full brief as handed off: who's involved, the two workstreams
  (personal brand deals for Christian; growth marketing for Rocka Moss), the brand-deal
  prospecting methodology, financials, access needed, open questions. Read this first.
- **`ai-ugc-playbook.md`** — **the actual deliverable this section exists to produce.** The
  brief flags "AI UGC production workflow" as a named gap ("not covered by any existing repo...
  this is the playbook Ben needs to build and own"). This repo already *is* that playbook for a
  different client — this doc maps the proven techniques (photoreal UGC prompting, the
  genre-anchoring/POV lessons, multi-shot video chaining, brand-safety guardrails) onto what
  Rocka Moss specifically needs: product photography and testimonial/lifestyle video ads,
  produced without a shoot.
- **`kpi-targets.md`** — CAC/ROAS targets, now grounded in **real Shopify data** (a live MCP
  connector came online 2026-09-23) rather than the brief's unverified $14K/month figure, which
  turned out not to match actual store revenue (~$934/mo average, declining) — see the doc for
  the full reconciliation and the decision to move forward on real numbers regardless. Also has
  the CTR sanity-check range (still not grounded — no Rocka Moss *ad* history exists yet).
- **`access-checklist.md`** — what's been pulled/confirmed from Shopify vs. still open, plus the
  non-Shopify access items still outstanding from `PROJECT_BRIEF.md`'s checklist.
- **`seo-audit.md`** — real SEO/metadata audit run 2026-09-23 against live Shopify data (not a
  guess): no custom SEO title/description on any product, zero image alt text store-wide, a
  "My Store" placeholder leaking into product schema, a product missing from the only collection,
  and no `<h1>` tag anywhere on the site. All 7 findings now fixed and confirmed live.
- **`refs/`** — real Rocka Moss reference photos (product shots + a founder photo), sourced
  2026-09-23. See `refs/README.md` for the full inventory and a couple of flagged open items
  (a flavor-count mismatch vs. the live Shopify catalog, and a founder-likeness consent question
  still separate from just having the photo on hand).
- **`competitor-research.md`** — real Meta Ad Library pull (2026-09-24, via Apify, run in 2
  passes — a narrow 3-term pass then a widened 8-term pass per Ben's "widen the search a little
  bit" ask): closes step 1 of the brief's 6-step pitch. **3 confirmed direct sea-moss competitors**
  (True Sea Moss — 6-Page whitelisting pattern; Infinite Age — subscription-first + heritage-
  storytelling hook; Aztlan Herbal Remedies) plus several adjacent wellness/Black-owned-brand
  references, including a cross-brand "personal confessional" hook pattern worth reusing and one
  fabricated-doctor-persona ad flagged as a caution, not a technique to copy.
- **`target-demo.md`** — real Shopify customer-geography analysis (2026-09-24): two independent
  data sources (real purchaser addresses + 90-day session geography) both show the customer base
  is Southeast-concentrated (South Carolina/Columbia metro + North Carolina/Charlotte metro
  dominant, Georgia/Atlanta secondary), not evenly national. Includes a data-quality catch
  (excluding bot/data-center traffic misread as real sessions) and a soft, flagged-as-unconfirmed
  hypothesis about the customer base's likely demographic skew (since confirmed by Ben directly).
  Built specifically to ground the AI UGC character sheet(s) — see Status below.
- **`ai-ugc-concepts.md`** — 2 concrete AI UGC character/ad concepts (2026-09-24), grounded in
  `target-demo.md`'s findings: a synthetic Black woman character, Southeast-coded everyday
  settings, Strawberry Shortcake as the lead flavor. Concepts only — nothing generated yet, ready
  to greenlight.

## The two buckets (from the brief)

1. **Bucket 1 — Christian's personal brand deals.** Pure brand/business development (Meta Ad
   Library prospecting, outreach, deal structuring). No AI content generation involved — not
   this repo's concern, covered fully in the brief.
2. **Bucket 2 — Rocka Moss growth marketing.** Meta paid social + AI-generated video ads +
   influencer seeding + reporting. **The AI-generated video ads and product photography line is
   where this repo's work plugs in directly.**

## Status

- **Parked, not active: a full rebrand (logo, visual identity, website/theme redesign)** — Ben's
  own call, noted 2026-09-23. Don't start research or concepts on this without his go-ahead; see
  `access-checklist.md`'s "Parked" section.
- Brief received and filed (2026-09-22). **Shopify admin access confirmed 2026-09-23**, with a
  live Shopify MCP connector now available in this session (see `access-checklist.md` and
  `kpi-targets.md` for what's been pulled). **Meta Business Suite access confirmed and fully
  walked through 2026-09-24** (Ben's own login, no MCP connector for it in this session, checked
  screen by screen) — all 5 setup checks came back clean: Business Manager/Page ownership, Ad
  Account (`RockaMossBTL`, billing healthy), Instagram (`@rockamoss`), Pixel + server-side CAPI
  (both connected, proven via real historical purchases), and domain verification. **Also found
  Rocka Moss has already run real paid Meta ads before** (4 campaigns, $463.48 total spend, 10
  real purchases) — corrected the "zero paid marketing" assumption that had been in the brief and
  `kpi-targets.md` — see that doc's correction section. Nothing left blocking infrastructure-wise
  for a new campaign launch. **Real Rocka Moss reference photos now exist in `refs/`** (sourced
  2026-09-23 from a Drive folder Ben shared, see `refs/README.md`) — no generations run for this
  client yet, but product-shot/testimonial validation is now unblocked.
- `ai-ugc-playbook.md` is a **mapping document** — it translates lessons already proven on
  Zion/Kazumi/Selena onto Rocka Moss's needs. It hasn't been validated against real Rocka Moss
  product/brand references yet. Treat every recipe in it as a starting point to test, not a
  locked recipe, the same discipline this repo uses everywhere else (see `CLAUDE.md`'s running
  log — nothing here gets called "confirmed" until Ben's eyes are on an actual output).
- **✅ Resolved 2026-09-24 (Ben's decision): synthetic AI UGC characters, NOT Christian's real
  likeness.** The open consent question above is closed — Rocka Moss's testimonial/UGC video
  content will use AI-generated character sheets built from Rocka Moss's actual Shopify customer/
  target-demo data, not any real person's identity. This is exactly the proven Frankie Shaw AI-UGC
  method already documented (`docs/frankie-shaw-ai-ugc-method.md`'s "Production realities"
  section) — a locked character reference (built here via this repo's existing photoreal
  character-sheet recipe, proven on Kazumi's pilot and Selena's photoreal pack), not a photoreal
  likeness of Christian. **Ben's stated pipeline:** target-demo data (from Shopify) → AI UGC
  character sheet(s) → apply the UGC ad philosophy/format "tent poles" from
  `docs/frankie-shaw-ai-ugc-method.md` and `docs/tay-ai-ugc-dropship-method.md` → draft concrete ad
  concepts → generate via Seedance 2.0 (`docs/seedance-comfy-handoff.md`). No consent question
  remains for this path — it never touches Christian's or anyone real's likeness.
- **Step 1 of that pipeline is done: real target-demo data pulled and written up in
  `target-demo.md` (2026-09-24).** Two independent Shopify data sources (real purchaser addresses
  + 90-day session geography) both show the customer base is concentrated in South Carolina
  (Columbia metro) and North Carolina (Charlotte metro), with Georgia (Atlanta-area) secondary —
  not evenly national. One hypothesis flagged for Ben/Christian to confirm before locking a
  character's specific look (a likely skew toward Black women customers, inferred cautiously from
  first-name patterns, cross-checked against `competitor-research.md`'s independent findings).
  Next: draft 1-2 concrete AI UGC character/ad concepts grounded in this profile.

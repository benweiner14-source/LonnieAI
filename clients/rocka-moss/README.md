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
  `kpi-targets.md` for what's been pulled). A Meta/Facebook Pixel was found already installed
  (found via page source, not Business Suite — see `access-checklist.md`). **Meta Business Suite
  access confirmed 2026-09-24** (Ben's own login, no MCP connector for it in this session — see
  `access-checklist.md`'s new section for the concrete next-check list: Business Manager
  ownership, both pixels' real status, domain verification, ad account existence, Instagram
  connection). **Real Rocka Moss reference photos now exist in `refs/`** (sourced 2026-09-23 from
  a Drive folder Ben shared, see `refs/README.md`) — no generations run for this client yet, but
  product-shot/testimonial validation is now unblocked.
- `ai-ugc-playbook.md` is a **mapping document** — it translates lessons already proven on
  Zion/Kazumi/Selena onto Rocka Moss's needs. It hasn't been validated against real Rocka Moss
  product/brand references yet. Treat every recipe in it as a starting point to test, not a
  locked recipe, the same discipline this repo uses everywhere else (see `CLAUDE.md`'s running
  log — nothing here gets called "confirmed" until Ben's eyes are on an actual output).
- **Open item carried over from the brief:** if Christian Brown himself appears as an AI-generated
  or AI-assisted subject in any Rocka Moss ad creative (not just real photos of him), that's a
  narrower consent question than "Ben has permission to post on his Instagram" (Bucket 1's
  permission). The same distinction this repo already drew for Kazumi's photoreal motion-transfer
  pilot (`docs/photoreal-motion-transfer-pilot.md`) applies here — confirm explicitly with
  Christian before generating any AI likeness content of him, don't assume the brand-deal
  outreach permission covers it.
  - **This is now a genuine two-path decision, not just a permissions checkbox** — see
    `docs/frankie-shaw-ai-ugc-method.md`'s "Production realities" section: the proven AI-UGC
    method this repo just added builds **synthetic, non-real testimonial characters** by design
    (a GPT Image 2-generated identity, not any real person's likeness), which sidesteps this
    consent question entirely at the cost of losing the "the co-founder said this himself"
    authenticity. Decide on purpose whether Rocka Moss testimonial content should feature a
    synthetic character (no consent question, matches the proven method) or Christian's real
    likeness via this repo's own already-working path (stronger authenticity, needs his explicit
    sign-off) — don't default to either.

# Rocka Moss — Access & Getting-Started Checklist

Tracks what's been pulled/confirmed vs. still open, now that both Shopify admin access and a live
Shopify MCP connector exist for this session.

## Shopify — done
- [x] Shopify collaborator/admin access (Ben, 2026-09-23)
- [x] Live Shopify MCP connector connected (2026-09-23 — confirmed via `get-shop-info`: store is
  Rocka Moss, rockamoss.com, base "Shopify" plan tier)
- [x] Returning Customers report → 32% repeat-purchase rate, 2.86 avg orders/returner
- [x] Customer Cohort Analysis → new-customer acquisition trend (peaked Feb 2026 at 44/mo, down
  to 4-8/mo by mid-2026)
- [x] Net Sales Over Time → real revenue baseline (~$934/mo average Jan-Sep 2026, declining)
- [x] Traffic/session data (30d) → 285 sessions, thin but real, consistent with zero paid spend
- [x] Referrer/channel breakdown (90d) → Instagram is the clear #2 channel after direct/
  unattributed; Facebook meaningfully underperforms IG (1 order vs. 8)
- [x] Product/flavor sales split (90d) → 4 flavors exist (Strawberry Shortcake, Mango Magic,
  Pineapple Breeze, Apple Pie); Strawberry Shortcake leads on both orders and revenue
- [x] Confirmed active discounting (gross ≠ net sales per flavor) — codes/terms not yet pulled
- [x] **Full SEO/metadata audit run (2026-09-23)** — see `seo-audit.md`. Found: no custom SEO
  title/description on any product (Shopify auto-fallback truncates mid-sentence), zero image
  alt text store-wide, `vendor` field says "My Store" on 3/4 products (leaks into product
  schema), Pineapple Breeze missing from the only collection, and no `<h1>` tag anywhere on the
  site (theme-level, needs Liquid/theme access to fix). Confirmed clean: robots.txt, sitemap.xml,
  canonicals, HTTPS, viewport, and baseline `ProductGroup` JSON-LD schema.
- [x] **Existing product-page reviews confirmed: none visible** (checked directly on the
  Strawberry Shortcake product page as part of the SEO audit) — no `aggregateRating`/`review` in
  the page's own schema either. Consistent with the standing caution in `ai-ugc-playbook.md`
  against fabricating reviews — when they do get added, use real ones.

All of the above is in `kpi-targets.md` and `seo-audit.md` with full detail.

## Shopify — still worth pulling
- [x] **Active discount codes/terms** — pulled live via GraphQL (2026-09-23): **16 active codes**.
  Two look like general-purpose site codes (`ROCKA10` 15% off since Oct 2025, `ROCKA15` $15 off
  flat since Mar 2026); one looks like a welcome/flow-triggered code with an actual expiry
  (`IG-EMAIL-1R9EMRC9`, 15% off, expires 2026-09-28 — implies *some* email/IG-triggered automation
  already exists, worth confirming what sends it); one is a flat local-pickup/in-person code
  (`LOCAL`, $6.50 off); and **8 look like individual ambassador/seeding codes** — each a short
  name fragment at 20% off (`RMSWEAT`, `RMDEZ`, `RMTIM`, `RMAVIBABY`, `RMRWU`, `RMTOYA`, `RMJAS`,
  `RMBRI`), all created between Feb-Apr 2026. **This means informal influencer/ambassador seeding
  is likely already happening** — worth asking Christian who these codes belong to and whether
  there's tracking on their performance, since the brief's Bucket 2 already names "influencer
  seeding" as a workstream and this may be a head start rather than a clean slate. Also found
  `RMAP` at **100% off** (free) — worth confirming its purpose (internal/testing/gifting) since an
  unrestricted 100%-off code is worth knowing about either way.
- [x] **Subscribe-and-save/reorder option status** — confirmed via GraphQL (`sellingPlanGroups`):
  **zero selling plan groups exist — no subscription mechanism at all today.** The 32%
  repeat-purchase rate is happening entirely organically, with no subscribe-and-save nudge. Real
  confirmation this is a genuine open lever, not already covered — worth raising with Christian on
  its own, separate from the ad-spend plan (Shopify's native Subscriptions feature or an app like
  Recharge/Skio would be the build).
- [x] **Cost-per-item / COGS entered on products** — confirmed via GraphQL
  (`InventoryItem.unitCost`): **`null` on every variant, all 4 products.** No COGS data exists in
  Shopify at all — margin has to stay the brief's 50-60% estimate until Christian/Ben supplies
  real per-unit cost numbers directly; this isn't pullable from Shopify itself.
- [~] **Meta Pixel / Conversions API install status** — partially answered via page-source
  scraping (2026-09-23): a Facebook Pixel is already installed, ID `682325200982123`, connected
  via Shopify's own Facebook & Instagram sales channel app (client-side/browser only confirmed).
  **Now that Meta Business Suite access exists (2026-09-24), the rest of this item — CAPI status,
  historical event data, and identifying the second unidentified pixel `D65JE4JC77U8VIJAA8H0` —
  moved to the new "Non-Shopify — Meta Business Suite access confirmed" section below, since it's
  checked in Business Suite/Events Manager, not Shopify Admin.**
- [ ] **Email/SMS tool connection status** — checked the live homepage and product page source
  for common tool footprints (Klaviyo, Omnisend, Attentive, Postscript, Mailchimp) — **no evidence
  found in the client-side page source**, but this isn't conclusive (some tools only load
  on-trigger, e.g. exit-intent, or run server-side/via Shopify Flow with no client script). The
  `IG-EMAIL-1R9EMRC9` discount code above implies *some* automated flow exists. Needs a direct
  check in Shopify Admin → Settings → Apps to confirm either way.

## SEO/metadata fixes — from the 2026-09-23 audit, see `seo-audit.md` for full detail, `progress-log.md` for the executed changes
- [x] **Write custom SEO title + meta description for all 4 products** — done 2026-09-23, driven
  directly via the Shopify MCP (`productUpdate`), confirmed live.
- [x] **Add alt text to every product image** — done 2026-09-23, all 7 images, confirmed live.
- [x] **Fix `vendor` field to "Rocka Moss"** on Strawberry Shortcake, Mango Magic, Apple Pie —
  done 2026-09-23, confirmed live.
- [x] **Add Pineapple Breeze to "Explore The Rocka Moss Collection"** — done 2026-09-23, collection
  now holds all 4 products, confirmed live.
- [x] **Clean up stray `<meta charset="utf-8">` artifact in the collection description** — done
  2026-09-23, confirmed live (see `progress-log.md` — a mistake mid-fix was caught and corrected
  in the same step).
- [x] **Set `productType` + `tags` on all 4 products** — done 2026-09-23, confirmed live.
- [x] **Missing `<h1>` tags — fixed and confirmed live (2026-09-23), Ben executed manually.**
  Root cause was a real theme-code bug in the shared `snippets/text.liquid` (two separate bugs,
  found one at a time): (1) the element-selection logic only ever assigned `div`/`rte-formatter`
  regardless of the `h1`-`h6` "Preset" setting; (2) even after fixing that, the product title
  block still rendered as a `div` because it renders through a separate `fallback_text` code path
  that had its own hardcoded `<div>`, unrelated to the `element` variable. Ben duplicated the
  theme, made both small Liquid edits directly in Edit code, set the Preset to H1 on the homepage
  hero block and the product title block, and published. **Confirmed live via raw HTML fetch**:
  homepage has exactly one real `<h1>` (hero headline, rest `<h2>`), Strawberry Shortcake product
  page has exactly one real `<h1>` (product title, was previously a styled `<div>`). Full
  investigation trail in `CLAUDE.md`'s "H1 investigation" entry.

## Non-Shopify — Meta Business Suite access confirmed 2026-09-24, next-check list below
- [x] **Meta Business Suite partner access** — Ben confirmed 2026-09-24. No Business Suite MCP
  connector exists in this session (`ListConnectors` confirmed only Gmail is connected) — this is
  Ben's own login access, same pattern as Shopify admin before the Shopify MCP came online. This
  session can't pull Business Suite data directly; the items below are what to check/report back,
  not things this session ran itself.
- [x] **Does Rocka Moss have a Meta Business Manager, and does it own the Page/Ad Account/Pixel?**
  **Confirmed 2026-09-24 — yes, cleanly.** Facebook Page (ID `674650849075325`) is owned directly
  by the "Rocka Moss" business portfolio, not a personal account. 4 people have access; Ben has
  full access, and a second person with full access — **"Darius Boyd"** — may be the "other Rocka
  Moss co-founder" flagged as an open question in the brief's Open Questions section (see below,
  not yet confirmed which).
- [x] **Does a Meta Ad Account already exist?** **Confirmed 2026-09-24 — yes: `RockaMossBTL`**
  (ID `721440597562823`), owned directly by Rocka Moss. **Real prior campaign history exists —
  this account is NOT cold-start.** 4 campaigns (all now inactive) ran ~$463.48 total spend with
  10 real purchases attributed via the pixel — full breakdown and open questions (why campaigns
  stopped, what the custom-conversion event was, why CPA varied 4x between the two purchase
  campaigns) in `kpi-targets.md`'s new correction section. **Billing confirmed healthy**: MasterCard
  on file, $0 balance owed, Meta-set daily spending limit $106.83 — not blocked on payment setup.
- [ ] **Identify both pixels found via page-source scraping (2026-09-23)** — the historical
  campaign data confirms pixel `682325200982123` has real, working purchase attribution (10 real
  conversions credited) — its health is no longer in question. Still open: identify the second,
  unidentified pixel (`D65JE4JC77U8VIJAA8H0`, app client ID `4383523`) via Business Settings →
  Data Sources, and confirm which pixel(s) fed the historical campaigns above.
- [ ] **Server-side Conversions API status on the primary pixel** — Events Manager → the pixel →
  "Overview"/"Diagnostics" tab, check whether a server-side connection exists alongside the
  browser pixel (client-side-only was confirmed via page source; the historical campaigns prove
  purchase attribution works via the browser pixel at minimum, but CAPI specifically still unknown).
- [ ] **Domain verification status** — Business Settings → Brand Safety → Domains — confirms
  rockamoss.com is verified, needed for iOS14.5+ event prioritization once campaigns run.
- [ ] **Rocka Moss Instagram — is it connected to this Business Manager, and does Ben have
  co-manager access?** Business Settings → Accounts → Instagram Accounts. Needed for organic
  posting, ad placements running "as" the IG account, and confirming the account itself (handle,
  follower count) since none of that has been pulled yet.
- [ ] **Who is "Darius Boyd"?** Found 2026-09-24 with full access to the Rocka Moss Facebook Page
  — may directly answer the brief's still-open "who is the other Rocka Moss co-founder" question
  (see the dedicated section below). Not yet confirmed either way.
- [ ] **Confirm the `IG-EMAIL-1R9EMRC9` discount code's source** — the Shopify-side discount pull
  (2026-09-23) found this code implies *some* automated email/IG flow already exists; Business
  Suite's Instagram/Messenger automation settings (or Shopify Admin → Settings → Apps, still
  separately open below) may show what's actually sending it.
- **Once the above is confirmed, the natural next question is ad-account setup itself** — this
  project already has concrete, ready-to-use structure for that step:
  `docs/tay-ai-ugc-dropship-method.md`'s CBO/$25-50-day/single-country/broad-targeting launch
  structure, and the `ads-meta` skill (installed 2026-09-24) for a full account-health audit once
  there's an actual account/pixel/campaign to point it at — its audit framework is evidence-based
  (Pixel install, CAPI, event dedup, domain verification, campaign structure, audiences,
  attribution) and explicitly avoids guessing at anything it can't confirm from real account data,
  so it's the right next step to run once Ben can hand over real screenshots/exports from the
  screens above, not before.
- [x] **Any existing creative assets Rocka Moss already has** — done 2026-09-24 (was stale/still
  showing open even though this was already fulfilled 2026-09-23): the Google Drive "Photography
  and Media" folder Ben shared *is* Rocka Moss's existing creative assets — real product photos,
  founder photos, and 22 brand-render mockups, see `refs/README.md`.

## Open question from the brief, never tracked: the other Rocka Moss co-founder
- [ ] **Who is the other Rocka Moss co-founder, and are they in the loop?** Flagged 2026-09-24 —
  this was in `PROJECT_BRIEF.md`'s "Open Questions" section the whole time
  ("Christian has part ownership. There's at least one other partner... The marketing decision
  likely involves them. Ben needs to get in the room with both before committing to the full
  engagement") but never made it into this working checklist. This isn't just a Bucket-1/personal
  detail — it directly gates committing to the full Bucket 2 engagement per the brief's own
  wording, and the `/ads math` skill's PPC reporting is explicitly meant to support "the
  conversation with the Rocka Moss co-founders" (plural) about what the ad spend is generating.
  Not something this repo can resolve — Ben's to confirm directly with Christian.
  - **Possible lead, not yet confirmed:** the Meta Business Suite Page-access check (2026-09-24)
    found a "Darius Boyd" with full access to the Rocka Moss Facebook Page alongside Ben — worth
    checking whether this is the co-founder the brief refers to, rather than treating this as
    fully separate/unresolved.

## Competitor research (Meta Ad Library) — done 2026-09-24, widened same day
- [x] **Pull every sea moss / Black-wellness competitor ad running right now.** Closes step 1 of
  the brief's 6-step pitch. Direct fetch was blocked (403, JS wall) same as prior scraping blocks
  — Ben provided an Apify token (already present in this session's environment), ran
  `curious_coder/facebook-ads-library-scraper` (Apify's most-used Ad Library actor) in 2 passes:
  a narrow 3-term pass (~$0.05, 14 unique ads), then a widened 8-term pass per Ben's "widen the
  search a little bit and run again" ($0.116, 71 unique ads across ~38 brands). Combined ~$0.17.
  **Full findings, ranked by days-running (a real performance proxy), in `competitor-research.md`.**
  - **Headline finding (strengthened by the widened pass):** **3 confirmed direct sea-moss
    competitors**, not just 1 — **True Sea Moss** (trueseamoss.com, the same ad whitelisted
    through 6 different Facebook Pages, longest variant 232 days, benefit-list structure),
    **Infinite Age** (infiniteage.com, "Sea Moss Advanced" — Sea Moss + Bladderwrack + Burdock —
    a **subscription-first** offer ("locked in for life, every month") plus a heritage/
    storytelling hook, a real head start on the subscribe-and-save lever this checklist already
    flags Rocka Moss is missing), and **Aztlan Herbal Remedies** (aztlanherbalremedies.com,
    "Wildcrafted Irish [Sea] Moss," 234 days, a colon-detox/cleanse framing). **Flagged a real
    caution on all three:** their copy leans into borderline-to-fabricated medical claims
    (Infinite Age: "no more meds"; one naturalrems.com ad used a fake "ENT Specialist" persona
    with an invented health timeline) — study the structure (offer/subscription mechanics,
    storytelling hooks), never the claims language, per this project's standing no-medical-claims
    rule for Rocka Moss.
  - **New cross-brand pattern found in the widened pass:** a "personal confessional" hook —
    several unrelated wellness brands (Alevia, American Health Support Community, Rosabella,
    Roots of Wellness) open ads with a first-person story about someone else, no product
    mentioned until well into the copy. Worth keeping as a third ad-angle type in the
    psychology-pillar-map toolkit alongside True Sea Moss's benefit-list and Infinite Age's
    heritage-narrative approaches — independent confirmation of Frankie Shaw's "curious ad" /
    storytelling-before-product-first principle already in `ai-ugc-playbook.md`.
  - Adjacent (non-sea-moss) references: **MuscleMax Nutrition**'s "stop taking 10 different
    supplements — just take these 2" consolidation-pain hook (178-520 days), **Culture Connection
    360** (Black-owned, real Chicago + Atlanta locations — 2 of Rocka Moss's 3 target cities,
    616-1389 days), and **Black Girl Vitamins** (491 days, same whitelisting tactic as True Sea
    Moss, plus a strong demographic-positioning reference: named medical advisor, community/equity
    angle) — all strong tonal/voice references even though the product category differs.
  - **Honest limitation, updated in the file:** the widened pass closed most of the gap — 3
    confirmed direct competitors instead of 1, ~38 brands surveyed instead of 3. What remains true:
    sea moss itself still appears to be a genuinely under-advertised niche on Meta relative to
    general wellness supplements — 3 direct competitors is a real, not just under-searched, number.
    Re-running the same widened search periodically (ads start/stop constantly) is the way to keep
    this current, not further keyword-widening within the category.
  - No scraped video/image files stored in the repo — every entry links to its real, public Meta
    Ad Library permalink instead, same reproduction-caution posture used elsewhere in this
    project.

## Skills the brief names — 2 of 3 gaps closed 2026-09-24
Only `coreyhaines31/marketingskills` (21 skills) had been installed as of 2026-09-23. Three other
skill repos `PROJECT_BRIEF.md`'s "Skills Stack" section names by name were missing — Ben asked to
install both installable ones on 2026-09-24:
- [x] **`AgriciDaniel/claude-ads`** — installed 2026-09-24, scoped down. The live upstream repo
  has grown into a full 12-platform "Claude Ads" operating system (way beyond what the brief
  describes) with live campaign-mutation commands — vendored only the Meta-only,
  non-account-mutating subset matching the brief's 8 named commands plus 3 more directly useful
  ones (`ads-dna`, `ads-photoshoot`, `ads-create`, `ads-generate`, `ads-meta`, `ads-math`,
  `ads-budget`, `ads-landing`, `ads-competitor`, `ads-creative`, `ads-plan`). Full
  installed/excluded reasoning in `.claude/skills/README.md`.
- [ ] **`tenfoldmarc/meta-ads-generator-skill`** — **not installed, blocked on licensing.**
  Checked 2026-09-24: this repo has no LICENSE file at all (unlike the other two, both MIT) — no
  explicit grant to redistribute its files. Its actual content wasn't vendored, consistent with
  this project's standing no-raw-copyrighted-content discipline (same as the Frankie Shaw/Tay
  YouTube material). One genuinely useful idea from it — the "psychology pillar map" technique
  (synthesize competitor/review research into 4-6 named purchase-driver pillars, each backed by a
  real customer quote, before drafting ad angles) — was captured in our own words and folded into
  `ai-ugc-playbook.md` instead. If the actual tool is wanted, needs either Ben's own permission
  from tenfoldmarc or building an equivalent using this project's own Comfy Cloud path.
- [ ] **`hyperfx-ai/marketing-skills`** (`meta-ads-library`) — still not installed, requires Hyper
  MCP setup at app.hyperfx.ai/mcp (not configured in this session) — the automated path for the
  competitor-research gap above; the manual/Apify paths there still stand as the current options.

## Creative/content — refs now exist, validate before batching
- [x] **Source reference photos of the actual bottle/label** — done 2026-09-23. Ben shared a
  Google Drive folder ("Photography and Media") with real Rocka Moss brand photography; 5 real
  photos saved to `refs/` (Strawberry, Mango ×2 lighting variants, Apple Pie, plus a founder
  photo). Pineapple Breeze still needs a real-photo ref (only a 3D render exists for it in Drive,
  not yet pulled). See `refs/README.md` for full inventory, including a flagged discrepancy: the
  Drive folder's brand renders show **11 flavors, only 4 of which are live on Shopify today** —
  worth asking Christian about before any creative decisions.
- [ ] Decide: synthetic testimonial character vs. Christian's real likeness (open consent
  question, flagged in `README.md` — needs his explicit sign-off if real). **Now has a real,
  usable reference photo on hand either way** (`refs/rockamoss_founder_applepie_steps.jpg`) —
  having the photo doesn't itself resolve the consent question, it just means testing can start
  the moment sign-off exists.
- [x] **Validate one product shot** — done 2026-09-23, confirmed clean after 2 fix iterations.
  GPT Image 2.5 Sunburst via Comfy Cloud, Strawberry Shortcake, Studio style — see
  `test-renders/README.md` for the full recipe and result. Front label reproduced accurately
  throughout; a real jar-embossing leak ("MASON," caught by Ben) needed a reworded fix (a bare
  negation only partially worked, a positive-description version fixed it fully) — now folded
  into the standing recipe in `ai-ugc-playbook.md`. Small-text side-panel legibility remains an
  open, lower-priority flaw. Recipe validated; the other 4 styles/3 flavors/testimonial recipe
  not yet tested.
- [ ] Validate one POV-selfie testimonial before batching that direction (per
  `ai-ugc-playbook.md`'s standing validate-before-batch discipline) — still needs Christian's
  consent decision (synthetic vs. real likeness) resolved first.

## Parked — not now, don't start on this without Ben's go-ahead
- [ ] **Full rebrand: logo, visual identity, and website/theme redesign.** Ben's own call
  (2026-09-23): "probably interested in changing the branding, logo, and website if we need to,
  considering it's all kind of basic and some of it's not great." Explicitly parked — **do not
  start competitor/brand research, logo concepts, or theme redesign work on this** unless Ben
  asks. Noted here so it doesn't get lost, and because the `seo-audit.md` findings are relevant
  context if/when this activates: single generic collection, minimal nav (Home/Shop/Contact/
  FAQ/About Us), a leftover "My Store" placeholder that had leaked into product data (now fixed),
  and no site content beyond the 4 product pages + homepage — consistent with Ben's "basic"
  read, though the SEO/metadata fixes already done are a different, narrower scope (page data,
  not visual identity) and don't resolve this. `PROJECT_BRIEF.md`'s Phase 6 (`/ads landing`
  skill — landing page quality assessment) already gestured at "Shopify theme refresh... could
  lift conversion rate" as a possibility; this is that idea, broadened to logo/brand identity
  too. When it activates: the `cro`, `copywriting`, and `image` skills (already installed) plus
  possibly a design-focused tool not yet in this repo's stack would be the relevant starting
  points — not scoped further than that until Ben says go.

## How to keep pulling Shopify data going forward
Live queries now work directly in this session via the Shopify MCP tools (`run-analytics-query`
for ShopifyQL, `search_products`, `list-orders`, `list-customers`, `get-shop-info`, etc.) — no
more manual CSV exports needed for most of the above. `docs/tay-ai-ugc-dropship-method.md`'s
AI-assisted daily reporting pattern (Claude connected to Facebook Ads + Shopify + a profit app)
becomes directly buildable once a Meta ad account/Pixel also exist.

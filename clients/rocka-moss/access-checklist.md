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
- [ ] **Active discount codes/terms** — so ad creative doesn't contradict a live offer, and so
  CAC math uses real average selling price, not list price.
- [ ] **Subscribe-and-save/reorder option status** — the 32% repeat rate is happening organically;
  confirm whether a subscription mechanism exists, since turning one on (if not) could be a
  high-leverage, non-ad-spend lever worth raising with Christian on its own.
- [ ] **Cost-per-item / COGS entered on products**, if any — would give a precise margin number
  instead of the brief's 50-60% estimate, tightening the CAC-ceiling math.
- [ ] **Meta Pixel / Conversions API install status** — not visible from Shopify sales/session
  data alone; check Settings → Customer events or installed sales channels/apps directly.
- [ ] **Email/SMS tool connection status** (Omnisend, Klaviyo, Shopify Email, or none) — tells us
  whether retention infra (see `docs/tay-ai-ugc-dropship-method.md`'s Omnisend flow types) is a
  green-field build or something to extend.

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

## Non-Shopify — still open from `PROJECT_BRIEF.md`'s access checklist
- [ ] Does Rocka Moss have a Meta Business Manager at all? (the brief's own "first check")
- [ ] Meta Business Suite partner access (Page, Instagram, Ad Account, Pixel — "Manage" level)
- [ ] Rocka Moss Instagram login/co-manager access (nice-to-have)
- [ ] Any existing creative assets Rocka Moss already has (nice-to-have)

## Creative/content — unblocked once refs exist
- [ ] Source 2-3 clean reference photos of the actual current bottle/label (all 4 flavors, if
  creative will differentiate between them — Strawberry Shortcake first, per the sales data)
- [ ] Decide: synthetic testimonial character vs. Christian's real likeness (open consent
  question, flagged in `README.md` — needs his explicit sign-off if real)
- [ ] Validate one product shot + one POV-selfie testimonial before batching (per
  `ai-ugc-playbook.md`'s standing validate-before-batch discipline)

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

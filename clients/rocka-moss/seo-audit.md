# Rocka Moss — SEO/Metadata Audit (2026-09-23)

Run with the `seo-audit` skill + live Shopify Admin GraphQL API + raw HTML pulls from the live
site (rockamoss.com). Not a guess — every finding below is confirmed against real data, sourced
per finding.

## Priority 1 — quick wins, Shopify Admin only, no developer needed

1. **All 4 products have `seo.title`/`seo.description` set to `null`** (confirmed via Admin
   GraphQL — `products { seo { title description } }`). Shopify falls back to the raw product
   title and a blunt truncation of body copy. Live example (Strawberry Shortcake):
   - Rendered `<title>`: "Rocka Moss Gel: Strawberry Shortcake"
   - Rendered meta description: "A deliciously sweet superfood fusion! Packed with 92 essential
     minerals and bursting with the nostalgic flavor of fresh strawberries and creamy vanilla,
     this gel delivers powerful health benefits and dessert-worthy taste. Perfect for boosting
     energy, supporting immunity, and nourishing your skin from within. Add it to" — **cuts off
     mid-sentence**, no CTA.
   - Fix: Admin → each product → "Search engine listing" → write custom title (~50-60 chars) +
     description (~150-160 chars, ending on a complete sentence with a reason to click).
2. **Zero image alt text, store-wide.** Confirmed via GraphQL (`media { image { altText } }`) —
   every image on every product (Apple Pie, Strawberry Shortcake, Mango Magic, Pineapple Breeze)
   returns `altText: ""`. Costs image-search traffic, real accessibility gap.
3. **`vendor` field is "My Store"** (Shopify's default placeholder) on 3 of 4 products —
   Strawberry Shortcake, Mango Magic, Apple Pie. Only Pineapple Breeze correctly says "Rocka
   Moss." This leaks directly into the product's JSON-LD schema — confirmed live:
   `"brand": {"@type": "Brand", "name": "My Store"}` on the Strawberry Shortcake page right now.
   Fix: set vendor to "Rocka Moss" on all 4.
4. **Pineapple Breeze is missing from the store's only collection** ("Explore The Rocka Moss
   Collection," handle `frontpage`) — confirmed via `get-collection`: `productsCount: 3`
   (Mango Magic, Strawberry Shortcake, Apple Pie only). Real lost internal linking/discoverability
   for a flavor that's already generating real orders (see `kpi-targets.md`).
5. Minor: the collection's `descriptionHtml` has a stray `<meta charset="utf-8">` tag pasted
   directly into the visible text — cosmetic cleanup, likely from a copy-paste.

## Priority 2 — needs theme/Liquid access — ✅ FIXED 2026-09-23, confirmed live

6. **No `<h1>` tag anywhere on the site — fixed, see resolution below.** Confirmed by pulling raw HTML from both the homepage
   and a product page (`rockamoss.com/`, `rockamoss.com/products/rocka-moss-gel-strawberry-
   shortcake`) and searching for heading tags directly — both return 0 `<h1>` matches (homepage
   does have `<h2>`/`<h3>`, so headings work generally, just not at the H1 level). Real on-page
   SEO miss — Google weights the H1 for topical relevance. Can't fix via the Admin API, needs
   theme code access.
   - **Root cause confirmed 2026-09-23 by reading the live "Savor" theme's actual Liquid source**
     (read-only theme-file access — the Shopify MCP can read theme files even though it blocks
     writes to the live/published theme). `blocks/product-title.liquid` and `blocks/text.liquid`
     both render through a shared `snippets/text.liquid`, which exposes a "Preset" dropdown
     (`type_preset`) with `h1`-`h6` options — but its element-selection logic only ever emits a
     `div` or `rte-formatter` tag, never the real heading element the preset name implies. The
     `h1`-`h6` values only add a CSS class for font sizing. **This means picking "H1" from the
     Preset dropdown in Shopify Admin does not add a real `<h1>` tag** — it's a genuine theme-code
     bug, not a misconfigured setting.
   - **Second bug found after the first fix went live:** the homepage hero got a real `<h1>`, but
     the product title block didn't — it renders through a separate `fallback_text` code path in
     the same snippet that had its own hardcoded `<div>`, independent of the element-selection fix.
     Needed a second small edit to the same file.
   - **Resolution: both fixed and confirmed live 2026-09-23.** Ben duplicated the theme, made both
     Liquid edits directly, set the "Preset" to H1 on the homepage hero block and the product
     title block, and published. Verified via raw HTML fetch: homepage has exactly one real
     `<h1>` (hero headline, rest `<h2>`); Strawberry Shortcake product page has exactly one real
     `<h1>` (product title). Full trail in `CLAUDE.md`'s "H1 investigation" entry.

## What's already working — confirmed clean, don't touch

- `robots.txt` — standard, correctly allows product/collection/page/blog crawling, blocks
  admin/cart/checkout, references the sitemap correctly.
- `sitemap.xml` — valid index with products/pages/collections/blogs sub-sitemaps, plus a
  `sitemap_agentic_discovery.xml` entry (a newer Shopify addition for AI-agent shopping).
- Canonical tags — self-referencing and correct on the product page checked.
- HTTPS, mobile viewport meta tag — both present and correct.
- Homepage title/meta description are custom-written, not auto-generated: `<title>` "Rocka
  Moss: Premium Wildcrafted Sea Moss", meta description a real 137-character sentence with no
  truncation. Someone already did this right on the homepage — it was just never extended to
  the product pages, which is exactly what Priority 1 item #1 fixes.
- Structured data (JSON-LD) is present: `Organization` schema site-wide, `ProductGroup` schema
  on product pages with per-variant `Offer` (price + `InStock` availability) — decent baseline.
  Only issue is the "My Store" brand name (Priority 1 #3). No `aggregateRating`/`review` present,
  which is expected — no reviews exist yet (see Priority 3 #3).

## Priority 3 — content depth, after Priority 1 is live

1. **No `productType` or `tags` set on any of the 4 products** (confirmed via `search_products`)
   — hurts internal search/filtering, gives Google less topical signal.
2. Descriptions are short (2-4 sentences per product) — fine as ad copy, thin for SEO. Worth
   expanding with ingredient/usage/benefit detail once Priority 1 is done.
3. **No visible reviews on the product page checked** (confirmed via direct page fetch) — matches
   the standing "don't fabricate reviews" caution already in `ai-ugc-playbook.md`. When reviews
   do get added, use real ones.
4. Navigation is minimal (Home, Shop, Contact, FAQ, About Us) — no blog/content section, so no
   organic-content growth lever exists yet beyond the 4 product pages + homepage.

## Method / sources
Shopify Admin GraphQL API (`search_products`, `get-collection`, and a custom
`ProductSEO` query pulling `seo`, `media { altText }`, `descriptionHtml` for all 4 products) via
the live Shopify MCP connector; raw HTML pulled directly (`curl`) from `rockamoss.com/` and
`rockamoss.com/products/rocka-moss-gel-strawberry-shortcake` and parsed for title/meta
description/canonical/heading tags/JSON-LD, since the `seo-audit` skill's own guidance notes
`WebFetch`/`web_fetch`-style tools can strip or miss JS-rendered elements — raw HTML parsing was
used specifically to get an accurate, non-false-negative read on heading tags and schema.

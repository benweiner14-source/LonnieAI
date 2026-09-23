# Rocka Moss — Progress Log

A running, dated record of changes made to the Shopify store and the broader engagement — meant
to be shareable with Christian/Rocka Moss to show what's been done since work started. Each entry
is a snapshot at a point in time; don't edit past entries, add new ones.

---

## Day 0 — 2026-09-23: Setup + baseline audit (before any changes)

**Access established:** Shopify collaborator/admin access confirmed; live Shopify MCP connector
connected for this session (`get-shop-info`: store is Rocka Moss, rockamoss.com, base "Shopify"
plan). Full detail in `access-checklist.md`.

**Business baseline established** (see `kpi-targets.md` for full detail, sourced from real
Shopify data, not the brief's unverified figures):
- Net sales: ~$934/month average (Jan-Sep 2026), declining — Feb 2026 peak ($1,610) down to
  Aug 2026 ($587), a -63.5% drop.
- Repeat-purchase rate: ~32% (63 returning customers / 198 total new customers, trailing 12mo),
  averaging 2.86 orders per returner. Real average order value among repeat customers: $46.96.
- Traffic: 285 sessions/30 days, ~8 completed checkouts — thin, consistent with zero paid spend.
- Channel mix (90d, 46 orders): 31 direct/unattributed, 8 Instagram, 3 Google organic, 1 Facebook.
- Product catalog: 4 flavors — Strawberry Shortcake (leads on orders/revenue), Mango Magic,
  Pineapple Breeze, Apple Pie.

**SEO/metadata audit run** (see `seo-audit.md` for full detail) — **exact "before" state of
everything about to change, for the record:**

| Product | Title tag (before) | Meta description (before — Shopify auto-fallback) | Vendor (before) |
|---|---|---|---|
| Apple Pie | "Rocka Moss Gel: Apple Pie" | "Discover the natural goodness of Rocka Moss Gel- Apple Pie, crafted with premium natural ingredients. Indulge in the delicious taste while nourishing your body with essential nutrients. Elevate your wellness routine with this exceptional product today. Average serving size: 2 tbsp Estimated serving duration for 16 oz j[…cut off]" | "My Store" |
| Strawberry Shortcake | "Rocka Moss Gel: Strawberry Shortcake" | "A deliciously sweet superfood fusion! Packed with 92 essential minerals and bursting with the nostalgic flavor of fresh strawberries and creamy vanilla, this gel delivers powerful health benefits and dessert-worthy taste. Perfect for boosting energy, supporting immunity, and nourishing your skin from within. Add it to[…cut off]" | "My Store" |
| Mango Magic | "Rocka Moss Gel: Mango Magic" | "Tropical Vibes in every spoonful! Mango Magic is bursting with juicy, sun-ripened flavor! Packed with 92 essential minerals, this tropical twist delivers both taste and nourishment. Refreshing, revitalizing, and irresistibly smooth—it's your daily wellness boost with island flair." | "My Store" |
| Pineapple Breeze | "Rocka Moss Gel: Pineapple Breeze" | "Bring a taste of the tropics to your wellness journey with our Pineapple Breeze Sea Moss Gel. Bursting with the bright, refreshing flavor of ripe pineapple, this blend combines island sweetness with the powerful nourishment of wildcrafted sea moss. It's a perfect balance of delicious indulgence and essential minerals y[…cut off]" | "Rocka Moss" (only correct one) |

All 4 products, before: **zero custom SEO title/description set** (`seo.title`/`seo.description`
both `null` via the Admin API — the table above is Shopify's raw auto-fallback), **zero image alt
text** on every product image, **no `productType` or `tags`** set. Collection ("Explore The Rocka
Moss Collection") held only 3 of 4 products — Pineapple Breeze missing. Collection description
had a stray `<meta charset="utf-8">` artifact pasted into the visible text. No `<h1>` tag found
anywhere on the site (homepage or product pages) — flagged as needing theme/Liquid access,
separate from the fixes below.

**Skills installed:** 21 marketing skills from `coreyhaines31/marketingskills` (ads, ad-creative,
cro, seo-audit, schema, analytics, influencer-marketing, emails, sms, social, attribution,
ab-testing, copywriting, copy-editing, competitor-profiling, marketing-psychology, offers,
popups, video, image, ai-seo) — see `.claude/skills/README.md`.

**From here on, this log tracks what actually changed, dated, against this baseline.**

---

## Day 0 — 2026-09-23: First changes made (same day, after the baseline above)

Executed directly via the live Shopify MCP connector — not a to-do list handed off, actually
done and verified live on the storefront. All 6 fixes below were checked with a fresh page fetch
after writing, so what's recorded is confirmed live, not just "the mutation returned success."

1. **Custom SEO title + description written for all 4 products** (previously `null`, falling
   back to auto-truncated body copy — see Day 0 baseline table above for the exact before state).
   Confirmed live on Strawberry Shortcake: title now "Strawberry Shortcake Sea Moss Gel | Rocka
   Moss", meta description now "Wildcrafted sea moss gel with real strawberry flavor and 92
   essential minerals for energy, immunity, and skin health. Dessert-worthy taste. Shop now." —
   a complete sentence with a CTA, not a mid-sentence cutoff. Same pattern applied to Apple Pie,
   Mango Magic, and Pineapple Breeze.
2. **Alt text added to all 7 product images** (previously blank on every one). Confirmed live —
   e.g. Strawberry Shortcake's image now carries "Rocka Moss Strawberry Shortcake sea moss gel,
   16oz jar" instead of an empty string.
3. **`vendor` field corrected to "Rocka Moss"** on Apple Pie, Strawberry Shortcake, and Mango
   Magic (previously "My Store," Shopify's default placeholder — Pineapple Breeze was already
   correct). This also fixes the brand name inside each product's JSON-LD schema.
4. **Pineapple Breeze added to "Explore The Rocka Moss Collection"** — the collection now holds
   all 4 active products (was 3). Confirmed live: the flavor is now linked from the collection
   page.
5. **Collection description cleaned up** — the stray `<meta charset="utf-8">` artifact pasted
   into the visible text is gone; the rest of the original description text was left untouched
   (not a rewrite, just the cleanup). Confirmed live: the artifact no longer appears on the
   collection page.
   - **Caught and fixed a mistake in this step during execution:** the first attempt at this fix
     passed the replacement text HTML-escaped (`&lt;p&gt;...&lt;/p&gt;`) instead of as raw HTML,
     which would have made literal `<p>` tags show up as visible text on the page — a worse
     problem than the one being fixed. Caught before moving on, corrected immediately, verified
     live. Noted here for an accurate record, not because it's still an issue.
6. **`productType` ("Sea Moss Gel") and `tags`** (`Sea Moss Gel`, `Wildcrafted`, `Wellness`, plus
   the flavor name) **set on all 4 products** — previously empty/unset on every one.

**Not done — still needs theme/Liquid access, can't be driven via the Shopify MCP's write
tools** (the connector explicitly blocks writes to the live/published theme as a safety rail):
the missing `<h1>` tag issue from the baseline audit. Still open.

**Copy quality check:** all SEO titles/descriptions and alt text written above were checked
against the `seo-audit`/`copy-editing` skills' AI-writing-detection reference (em dashes,
overused verbs/adjectives, filler words, AI-tell phrases) before use — confirmed clean, no
em dashes or flagged patterns in any of the 8 product-facing strings written today.

---

## Day 0 — 2026-09-23: The last fix, `<h1>` tags, done by Ben directly in Shopify Admin

The one fix that couldn't be driven via the MCP (live-theme-write safety rail) — Ben executed
this one himself, with instructions/root-cause investigation from this session, and it's now
confirmed live along with everything else on Day 0's list.

**Root cause turned out to be two separate bugs** in the theme's shared `snippets/text.liquid`,
found one at a time as each fix was tested live:
1. The snippet's element-selection logic only ever rendered a `div` or `rte-formatter` tag,
   regardless of the block's "Preset" setting (which offers `h1`-`h6` options) — so switching
   the Preset dropdown to "H1" in Shopify Admin, the obvious fix, only changed font size, not the
   actual HTML tag. Confirmed by reading the live theme's Liquid source directly.
2. After fixing that and publishing, the homepage hero picked up a real `<h1>` — but the product
   title block still didn't, because it renders through a separate `fallback_text` code path in
   the same file with its own hardcoded `<div>`, untouched by the first fix.

**Process:** Ben duplicated the "Savor" theme, made both small Liquid edits directly in Edit
code, set the "Preset" setting to H1 on the homepage hero block and the product title block
(everything else left H2-H6, so each page still has exactly one H1), previewed, and published.

**Confirmed live via raw HTML fetch after publishing:**
- Homepage: exactly one real `<h1>` tag (the hero headline "BUILT ON MINERALS. POWERED BY THE
  SEA."), rest of the headings are `<h2>`.
- Strawberry Shortcake product page: exactly one real `<h1>` tag (the product title) — previously
  a styled `<div class="... h1">`, confirmed via the same raw-HTML method used in the original
  audit.

**Side effect, expected not a bug:** the product title rendered visually larger after moving
from its old H2-styled size to real H1 — the theme's H1 typography preset is bigger by design.
Left as-is; adjustable later via the theme's global Typography settings if it ever looks too big,
without touching the tag fix.

**This closes out every item from the original 2026-09-23 SEO audit** — all 7 findings (6 driven
via the Shopify MCP earlier the same day, this H1 fix done by Ben directly) are now live and
confirmed.

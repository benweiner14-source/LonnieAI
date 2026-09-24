# Rocka Moss — KPI Targets

**Updated 2026-09-23 with real Shopify data.** Started from 3 manually-pulled reports (Returning
Customers 2025-09-23–2026-09-22, Customer Cohort Analysis 2025-09-01–2026-08-31, Net Sales Over
Time 2026-01-01–2026-09-23), then a **live Shopify MCP connector came online mid-session** — see
"Live Shopify MCP data" below for what that added. **Only aggregate numbers are recorded here —
no customer names/emails saved into this repo.**

## Decision (2026-09-23, Ben's call): work from the real Shopify baseline, not the brief's $14K figure

Not waiting on a reconciliation with Christian to move forward — planning against what the store's
own data actually shows from here on. Kept the discrepancy below for the record, since it still
matters for interpreting some of the numbers, but it's no longer a blocker.

### For the record: actual store revenue doesn't match `PROJECT_BRIEF.md`

The brief states Rocka Moss does **~$14K/month, ~400 bottles/month currently**. Actual Shopify net
sales tell a very different story:

| Month | Net sales |
|---|---|
| Jan 2026 | $1,006.82 |
| Feb 2026 (peak) | $1,609.82 |
| Mar 2026 | $1,377.60 |
| Apr 2026 | $812.84 |
| May 2026 | $1,165.25 |
| Jun 2026 | $828.83 |
| Jul 2026 | $648.86 |
| Aug 2026 (last full month) | $587.03 |
| Sep 2026 (partial) | $369.89 |

- **Average across Jan–Sep 2026: ~$934/month** — roughly **1/15th** of the brief's claimed $14K.
- **Declining, not flat:** -63.5% from the Feb 2026 peak to the last full month (Aug 2026).
- The brief was "last updated July 2026" and claims $14K/month as current *at that time* — but
  June ($829) and July ($649) net sales in this data were already far below that, so "revenue
  declined since the brief was written" doesn't fully explain the gap either.

**Plausible explanations, never resolved, not being chased further right now:**
- The brief mentions "product moves locally" — real in-person/wholesale/other-channel revenue
  that never touches this Shopify store could make $14K real even if this data doesn't show it.
- The $14K figure may have been Christian's own unverified claim, never checked against the
  store before now.
- It may simply have been wrong or aspirational.

**What this actually changes, now that we're planning off real numbers:** the brief's "$3K ad
spend → $10K+ incremental revenue" scenario set a cost-benefit bar ($6K total cost → $10K+ return)
that's mathematically fine on its own — but **the volume it implies (285–350 orders in a month)
is wildly unrealistic against a store whose best month on record did ~46 orders** (Feb 2026, at
$46.96 AOV ≈ 34 orders, actually — even the peak month doesn't get close). The **CAC/ROAS targets
below still hold as per-unit economics** — hitting a $23–28 CAC or better is good on any single
order, regardless of store size — but **the volume/revenue-in-a-month ambition needs to be reset
against actual scale**, not the brief's $10K figure. See "Realistic Month 1 volume" below.

## Repeat-purchase data — the genuinely good news

- **63 returning customers** (2+ orders) in the trailing 12 months, out of **198 total new
  customers** acquired in the same window (per the cohort report) → **~32% repeat-purchase rate.**
  Solid for a DTC wellness brand — real evidence the CAC ceiling can sit above single-order
  breakeven.
- **180 total orders** from those 63 returners (**117 of them repeat orders**), averaging
  **2.86 orders per returning customer**. A handful of genuinely loyal buyers: top of the list is
  9 orders, then 8, then three separate customers at 6 orders each.
- **Average order value among repeat customers: $46.96** — notably higher than the brief's flat
  $34.99 single-bottle assumption. People are evidently ordering multiple bottles or add-ons per
  order, at least once they're repeat buyers. **This revises the breakeven math below.**
- **New-customer acquisition has slowed sharply, tracking the same decline as net sales:** 44 new
  customers in Feb 2026 → 31 (Mar) → 9 (Apr) → 11 (May) → 8 (Jun) → 5 (Jul) → 4 (Aug).
- Month-1 cohort retention (returned the month right after first purchase) is noisy on small
  monthly cohort sizes — roughly 10–20% in most months, with a couple of high outliers (45%, 60%)
  on cohorts too small (n=11, n=5) to trust as a trend.

## ⚠️ Correction (2026-09-24): Rocka Moss has ALREADY run paid Meta ads — "zero paid marketing" was wrong

`PROJECT_BRIEF.md` and every doc in this repo up to now (including this one's own CTR section
below) assumed Rocka Moss has never run paid ads. **That's false.** Ben pulled a real Meta Ads
Manager campaign export (`RockaMossBTL` ad account, ID `721440597562823`, owned directly by the
Rocka Moss business) covering Aug 2025–present. 4 campaigns exist, **all currently inactive**:

| Campaign | Result | Result type | Cost/result | Spent | Impressions | Reach |
|---|---|---|---|---|---|---|
| Test2 | — | (no results) | — | $4.23 | 456 | 391 |
| TestOFF | 97 | custom conversion (event ID `24231000873195869`, not yet identified — likely a soft top-funnel event given the low cost) | $0.46 | $44.45 | 5,018 | 4,493 |
| Official-Campaign-2 | 1 | `fb_pixel_purchase` (real purchase) | $129.31 | $129.31 | 5,443 | 4,039 |
| Rocka-Campaign-2026 | 9 | `fb_pixel_purchase` (real purchase) | $31.72 | $285.49 | 15,907 | 6,229 |

**Totals: $463.48 spent, 26,824 impressions, 15,152 reach, 10 real purchases attributed via the
pixel.** Blended CAC across the two purchase-attributed campaigns: **$41.48/purchase** — above
the $23–28 breakeven ceiling below, but the two campaigns performed very differently
(Official-Campaign-2 at $129.31/purchase vs. Rocka-Campaign-2026 at $31.72/purchase, a 4x gap on
a small sample — worth understanding why before writing off either approach).

**What this actually confirms, positively:** the Facebook Pixel (`682325200982123`, found via
page-source scraping 2026-09-23) has real, working end-to-end purchase attribution — these aren't
hypothetical events, Meta credited 10 real conversions to it. That's a stronger pixel-health
signal than anything a Business Suite settings screen alone would show.

**Ben's call (2026-09-24): not chasing the "why" behind these old campaigns — treating this as a
fresh start.** Three real open questions came out of this table (why the campaigns went inactive,
what TestOFF's custom conversion event was, why CPA varied 4x between the two purchase campaigns)
but Ben decided not to pursue them. The data above stays on record as real historical reference —
useful context that the account and pixel aren't brand new and that a $31.72-$129.31 CPA range is
achievable in this category — but it's not being reverse-engineered or built on top of. New
campaign planning starts fresh rather than picking up Official-Campaign-2 or Rocka-Campaign-2026
where they left off.

**Technically not a cold-start account** (real spend/conversion history exists, which matters if
an `ads-meta` skill audit or Meta's own algorithm ever references account history) — but
**strategically being planned as a fresh start** per Ben's direction above. Both things are true
at once: don't assume zero history exists, but also don't treat the old campaigns as a foundation
to build the next one on.

## Revised CAC / ROAS targets

**Using the real repeat-customer AOV ($46.96) instead of the brief's flat $34.99 bottle price** —
at 50–60% margin:

**Breakeven line — the floor, not a target to operate at:**
- CAC ceiling: **~$23–28/order** (up from the earlier $17–21 estimate, now that real AOV is
  known to run higher than a single bottle)
- ROAS floor: **~1.7x–2.0x** (unchanged — this ratio depends only on margin %, not AOV)

**Aspirational per-order target, still valid on its own terms** (the brief's "$3K spend → $10K+
incremental revenue" scenario is really just a cost-benefit bar — spend $X, want a healthy
multiple back — and that logic doesn't depend on store size):
- CAC target: **~$9–11/order**
- ROAS target: **~3.5x+**
Hitting this on any given order/campaign is a good outcome at any scale. What's *not* realistic
anymore is expecting **$10K+ in a single month** — see below.

**Realistic Month 1 volume, reset against actual scale:** the store's best month on record (Feb
2026) did ~34 orders at the real $46.96 AOV. Recent months (Jun–Aug) are running 13–18 orders/mo.
A meaningful Month 1 win at $500–1,000 ad spend looks like **materially growing order count
relative to that — e.g., pushing new-customer acquisition back toward the Oct 2025–Mar 2026
range (15–44/month) it was already hitting organically before it slid to 4–8/month** — not
matching or exceeding a $10K/month revenue bar that the store has never actually hit.

**Month 1 test-budget bar:** CAC meaningfully under the ~$23–28 breakeven ceiling, order volume
trending up week over week toward the acquisition levels above — same "prove the system" framing
as before, now scaled to what this store's actual size can plausibly do in a month.

**The 32% repeat-purchase rate is real support for accepting a first-order CAC above the
$23–28 single-order breakeven**, if LTV over a customer's 2.86-order average clears it —
worth running the actual LTV math once ad spend starts and real CAC numbers exist to compare
against real customer value.

## Live Shopify MCP data (pulled directly, 2026-09-23)

A Shopify MCP connector came online mid-session (confirmed via `get-shop-info`: store is
**Rocka Moss, rockamoss.com, base "Shopify" plan tier**, not Plus/Advanced — worth knowing since
some analytics/reporting depth is plan-gated). Pulled live via `run-analytics-query` (ShopifyQL):

**Traffic (last 30 days): 285 sessions, ~8 completed-checkout sessions** — thin, but consistent
with zero paid spend to date. Most days show 0% session-to-purchase conversion with occasional
1-per-day completions; not enough daily volume yet to read a stable conversion-rate trend.

**Referrer breakdown (last 90 days, 46 orders, ~$2,254 total sales):**
| Source | Orders | Sales |
|---|---|---|
| Direct/unattributed | 31 | $1,372 |
| Instagram | 8 | $456 |
| Google (organic search) | 3 | $168 |
| Shopify network / Shop app | 3 combined | $180 |
| Facebook | 1 | $79 |

**Instagram is the clear #2 channel and meaningfully outperforms Facebook** (8 orders vs. 1) —
worth weighting creative/testing toward IG placements first, and matches the brief's own
Instagram-centric framing of the brand. Majority of orders are direct/unattributed, consistent
with an engaged existing audience (repeat customers, word of mouth) rather than discovery traffic.

**Product catalog — genuinely new information, not in `PROJECT_BRIEF.md` at all.** Rocka Moss
sells **4 flavors**, not a single SKU (last 90 days):
| Flavor | Orders | Gross sales |
|---|---|---|
| Strawberry Shortcake | 20 | $787.80 |
| Mango Magic | 14 | $635.84 |
| Pineapple Breeze | 11 | $352.39 |
| Apple Pie | 7 | $244.93 |

**Strawberry Shortcake is the clear leader** on both orders and revenue — the obvious first
flavor to feature in ad creative and product photography. Gross vs. net sales differ per flavor
(e.g. Strawberry: $787.80 gross → $671 net), confirming **discount codes are already in active
use** — confirmed and pulled in full (see `access-checklist.md`): 16 active codes, mostly 20% off,
including what look like 8 individual ambassador/seeding codes already in circulation. **Ad copy
going forward should account for these** — a "no discount" full-price framing would contradict
what's already live; worth deciding with Christian whether to formalize/replace the informal
codes once a real influencer program starts, or keep them running alongside it.

## CTR — real ad history exists now (see correction above), CTR itself still not pulled
The "no Rocka Moss ad history exists" line here was wrong — 4 real campaigns ran, see the
correction section above. **CTR specifically wasn't in the campaign CSV Ben pulled** (that export
covered results/cost/spend/impressions/reach, not clicks/CTR) — worth pulling a CTR-inclusive
report from Ads Manager if it's useful context for judging whether past creative's hooks worked,
separate from the CAC/purchase data already in hand. Until then, general Meta/DTC-wellness UGC
benchmark still applies as a fallback: roughly **1–2%+** is healthy for a resonant hook; **under
~0.8%** after real spend usually points at the hook/creative, not the targeting — see
`docs/frankie-shaw-ai-ugc-method.md`'s hook/format material. CTR doesn't determine profitability
on its own — CAC and ROAS do.

## How to track this once ads are live
`docs/tay-ai-ugc-dropship-method.md`'s AI-assisted daily reporting pattern (Claude connected to
Facebook Ads/Shopify/a profit-tracking app, or a CSV-upload fallback) is a direct way to check
actual CAC/ROAS against these targets without manual dashboard-reading.

## Next steps
- ~~Pull active discount codes/terms~~ — done 2026-09-23, see `access-checklist.md`: 16 active
  codes, ~8 of them look like individual ambassador/seeding codes already in circulation.
- ~~Confirm whether a subscribe-and-save/reorder option exists~~ — done 2026-09-23: confirmed
  **zero selling plan groups exist**, the 32% repeat rate is fully organic today. Real, confirmed
  open lever worth flagging to Christian on its own.
- ~~Confirm cost-per-item/COGS~~ — done 2026-09-23: confirmed **no COGS entered in Shopify at
  all**, margin stays the brief's 50-60% estimate until Christian supplies real numbers directly.
- **Meta Pixel/CAPI install status — fully resolved 2026-09-24.** Meta Business Suite access
  confirmed; ad account `RockaMossBTL` (ID `721440597562823`) exists, owned by Rocka Moss, with a
  payment method attached (MasterCard, $0 balance owed, $106.83/day Meta-set spending limit — not
  blocked on billing). "Rocka Moss's pixel" (ID `682325200982123`) is confirmed **receiving events
  from both Conversions API and Meta Pixel** — server-side CAPI is already connected, not just the
  browser pixel — combined with the real historical purchase attribution in the campaign CSV
  above, this pixel's setup is solid and ready to use for new campaigns.
- The $14K-vs-actual discrepancy is no longer blocking work (see "Decision" above) but is still
  worth asking Christian about eventually, since it may point at a real revenue channel this
  data doesn't see.
- **Meta Business Suite walkthrough complete (2026-09-24) — all 5 setup checks clean.** Business
  Manager/Page ownership, Ad Account (`RockaMossBTL`, billing healthy), Instagram (`@rockamoss`),
  Pixel + server-side CAPI (both connected and proven via real historical purchases), and domain
  verification (`rockamoss.com` verified) are all confirmed in good shape — see
  `access-checklist.md` for the full walkthrough. Nothing left blocking a new campaign launch from
  the infrastructure side.
- ~~Why the 4 historical campaigns went inactive, what TestOFF's custom conversion event was, why
  CPA varied 4x~~ — **not being pursued, per Ben's direction (2026-09-24): treating the ad account
  as a fresh start rather than investigating the old campaigns.** See the correction section above.
- ~~Who is the other Rocka Moss co-founder~~ — **resolved 2026-09-24: JaVon.** See
  `access-checklist.md`.

## Does the "$500-1,000/month" figure Ben told Christian still hold up? (2026-09-24)

**Yes — it holds up, and now with real data behind it instead of a guess.** Ben had told
Christian this was the ad-spend commitment level needed to make the engagement worthwhile.
Checked it against the real confirmed CAC range from the historical campaign data above (not the
aspirational $9-11 target, which was never actually hit):

| Monthly spend | Orders/mo at best-case real CAC ($31.72) | Orders/mo at blended real CAC ($41.48) | Orders/mo at worst-case real CAC ($129.31) |
|---|---|---|---|
| $500 | 16 | 12 | 4 |
| $750 | 24 | 18 | 6 |
| $1,000 | 32 | 24 | 8 |

**Read against the store's own organic baseline** (13-18 orders/month recently, ~34 at the Feb
2026 peak): **$500-1,000/month at anything close to Rocka-Campaign-2026's real efficiency
($31.72 CAC) would roughly match-to-double the store's best month ever, purely from paid.**
Even at the blended CAC across both real purchase campaigns ($41.48), $750-1,000/month lands in
the same range as the store's best organic month. That's a genuinely meaningful, achievable lift
— the number isn't undersized.

**One real caveat, not a reason to raise the budget, just a timeline expectation to set with
Christian:** at $500-1,000/month, weekly spend is roughly $115-230, which — even at the best real
CAC — produces only ~3-7 conversions/week. Meta's own guidance for an ad set to exit the learning
phase quickly wants closer to 50 conversions/week; well below that, campaigns typically take
longer to stabilize and Meta's auto-optimization has less signal to work with. **This doesn't mean
$500-1,000/month won't work** — it means expect a slower ramp-up/learning period than a
larger-budget account would see, not immediate steady-state performance from week one.

**Bottom line to tell Christian:** $500-1,000/month is a real, defensible number — grounded in
this account's own actual historical performance, not a guess — capable of meaningfully growing
order volume beyond what the store has ever hit organically. The honest caveat is patience during
the first few weeks while the algorithm has time to learn, not a concern about the budget being
too small.

## Sources
Three Shopify Analytics reports pulled manually before the connector came online (Returning
Customers, Customer Cohort Analysis, Net Sales Over Time) — aggregate figures only, individual
customer records not retained in this repo. Live Shopify MCP queries (`get-shop-info`,
`run-analytics-query`) pulled directly in this session once connected. `PROJECT_BRIEF.md`'s
stated unit economics (price, margin) for the original breakeven math.

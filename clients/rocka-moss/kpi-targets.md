# Rocka Moss — KPI Targets

**Updated 2026-09-23 with real Shopify data** (Ben pulled 3 reports after getting store admin
access: Returning Customers 2025-09-23–2026-09-22, Customer Cohort Analysis 2025-09-01–2026-08-31,
Net Sales Over Time 2026-01-01–2026-09-23). **Only aggregate numbers are recorded here — no
customer names/emails saved into this repo.**

## 🚩 Unresolved: actual store revenue doesn't match `PROJECT_BRIEF.md`

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

**Plausible explanations, not conclusions — this needs a direct answer from Christian/Rocka
Moss before any spend commitment is finalized:**
- The brief mentions "product moves locally" — real in-person/wholesale/other-channel revenue
  that never touches this Shopify store could make $14K real even if this data doesn't show it.
- The $14K figure may have been Christian's own unverified claim, never checked against the
  store before now.
- It may simply have been wrong or aspirational.

**Why this matters for everything below:** the brief's whole "$3K ad spend → $10K+ incremental
revenue" scaling scenario — which the original CAC/ROAS targets in this doc were anchored to —
assumes a $14K/month base. Against a store actually doing ~$900/month, that scenario asks for
10x+ growth, not incremental growth. **Don't plan Month 1 spend or targets against the brief's
$14K number until this is reconciled.**

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

## Revised CAC / ROAS targets

**Using the real repeat-customer AOV ($46.96) instead of the brief's flat $34.99 bottle price** —
at 50–60% margin:

**Breakeven line — the floor, not a target to operate at:**
- CAC ceiling: **~$23–28/order** (up from the earlier $17–21 estimate, now that real AOV is
  known to run higher than a single bottle)
- ROAS floor: **~1.7x–2.0x** (unchanged — this ratio depends only on margin %, not AOV)

**Target line — previously anchored to the brief's "$3K spend → $10K+ incremental revenue"
scenario. That scenario itself is now in question** (see the revenue-discrepancy flag above) —
**don't treat the old $9–11 CAC / ~3.5x ROAS target as valid until the $14K baseline is
reconciled.** Once Christian confirms whether $14K/month is real (and where, if not this store),
rebuild this target against whatever the actual revenue base turns out to be — the same "what
ad spend justifies the retainer" math still applies, just against a different starting number.

**Month 1 test-budget bar, largely unaffected by the revenue question:** CAC meaningfully under
the (now ~$23–28) breakeven ceiling, trending down week over week — same "prove the system"
framing as before, and arguably a lower-stakes bar now that it's being measured against a smaller
store, not a $14K/month one.

**The 32% repeat-purchase rate is real support for accepting a first-order CAC above the
$23–28 single-order breakeven**, if LTV over a customer's 2.86-order average clears it —
worth running the actual LTV math once ad spend starts and real CAC numbers exist to compare
against real customer value.

## CTR — still not grounded, unchanged
No Rocka Moss *ad* history exists (separate from the store data above, which is organic/existing
traffic, not paid). General Meta/DTC-wellness UGC benchmark: roughly **1–2%+** is healthy for a
resonant hook; **under ~0.8%** after real spend usually points at the hook/creative, not the
targeting — see `docs/frankie-shaw-ai-ugc-method.md`'s hook/format material. CTR doesn't
determine profitability on its own — CAC and ROAS do.

## How to track this once ads are live
`docs/tay-ai-ugc-dropship-method.md`'s AI-assisted daily reporting pattern (Claude connected to
Facebook Ads/Shopify/a profit-tracking app, or a CSV-upload fallback) is a direct way to check
actual CAC/ROAS against these targets without manual dashboard-reading.

## Next step
**Ask Christian directly whether the $14K/month figure is real, and if so, where it comes from**
(a channel outside this Shopify store, or a number that was never actually verified). Everything
above the "Repeat-purchase data" section depends on getting a real answer to this before
committing to a specific ad-spend target.

## Sources
Three Shopify Analytics reports (Returning Customers, Customer Cohort Analysis, Net Sales Over
Time), pulled by Ben on 2026-09-23 after getting store admin access — aggregate figures only,
individual customer records not retained in this repo. `PROJECT_BRIEF.md`'s stated unit economics
(price, margin) for the original breakeven math, now flagged as needing reconciliation on the
revenue-baseline side.

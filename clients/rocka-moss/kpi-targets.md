# Rocka Moss — KPI Targets

**Confidence level, stated plainly:** the CAC/ROAS targets below are solidly grounded — they're
derived directly from the unit economics already agreed in `PROJECT_BRIEF.md`, not an outside
benchmark. The CTR figure is *not* grounded the same way — Rocka Moss has run zero paid ads to
date (per the brief: "zero paid marketing infrastructure currently"), so there's no real
performance history to calibrate against. Treat CTR as a rough industry sanity-check, not a
validated target, until real campaign data exists.

## Unit economics (from `PROJECT_BRIEF.md`)
- Price: $34.99/bottle
- Product margin: 50–60% → **$17.50–$21 net per bottle**, before ad spend or Ben's retainer
- Current baseline: ~400 bottles/month, ~$14K/month revenue, zero paid marketing

## CAC / ROAS targets

**Breakeven line — the floor, not a target to operate at:**
- CAC ceiling: **~$17–21/bottle** (spend anything close to this and there's no real margin left)
- ROAS floor: **~1.7x–2.0x** (revenue ÷ spend, at this AOV and margin)

**Target line — what justifies scaling past the test month, derived from the brief's own math**
(its "$3K ad spend → $10K+ incremental revenue, 285–350 incremental bottles" scenario):
- CAC target: **~$9–11/bottle**
- ROAS target: **~3.5x+**

This range isn't an outside benchmark — it's the same math the brief already uses to define when
the full $3K retainer + $3K ad spend becomes "a no-brainer" for Rocka Moss. Hitting it is the
actual bar for justifying month 2+, not month 1.

**Month 1 (test budget, $500–1,000/mo) is a different, lower bar — per the brief's own framing:**
"prove the system, establish CPA baseline," not hit the $9–11 target yet. Reasonable pass/fail
line for the test month: CAC meaningfully under the $17–21 breakeven ceiling, trending down
week over week, not a hard number.

## CTR — diagnostic signal, not a validated target
No Rocka Moss ad history exists to calibrate against. General Meta/DTC-wellness UGC benchmark:
roughly **1–2%+** is healthy for a resonant hook; **under ~0.8%** after real spend usually points
at the hook/creative, not the targeting — see `docs/frankie-shaw-ai-ugc-method.md`'s hook/format
material before assuming a targeting fix is needed. CTR doesn't determine profitability on its
own — CAC and ROAS do; don't report CTR as a pass/fail metric, use it to diagnose a weak creative.

## The biggest open variable: repeat-purchase / LTV
Sea moss is a daily-use consumable — if Rocka Moss has any reorder-rate or subscription data,
**that changes the acceptable CAC ceiling substantially.** A first-order CAC above the $17–21
single-order breakeven can still be profitable if LTV over 2–3 orders clears it — common in DTC
wellness. **Ask Rocka Moss for repeat-purchase data before treating the $17–21 ceiling as a hard
line** — it may be too conservative if reorder rate is healthy.

## How to track this once live
`docs/tay-ai-ugc-dropship-method.md`'s AI-assisted daily reporting pattern (Claude connected to
Facebook Ads/Shopify/a profit-tracking app, or a CSV-upload fallback) is a direct way to check
actual CAC/ROAS against these targets without manual dashboard-reading — maps onto the brief's
"monthly reporting, plain numbers, no jargon" ask, at whatever cadence is useful.

## Sources
`PROJECT_BRIEF.md`'s own financial framework and unit-economics numbers (all figures above are
derived from it, not invented); general CTR benchmark is broad industry knowledge, not a Rocka
Moss-specific measurement.

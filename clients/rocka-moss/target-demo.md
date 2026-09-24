# Rocka Moss — Target Demo Profile (2026-09-24)

Built to ground the AI UGC character sheet(s) in real Rocka Moss customer data, per Ben's
direction: "build AI UGC character sheets based on their target demos from their data in
Shopify." Every finding below is sourced from live Shopify data pulled in this session — no
guessed persona. **Only aggregate figures are recorded here — no customer names, emails, or exact
addresses saved into this repo**, consistent with this project's standing PII discipline.

## Headline finding: the real customer base is Southeast-concentrated, not evenly national

Two **independent** Shopify data sources agree on this, which makes it a strong signal rather than
a small-sample fluke:

**1. Real purchaser addresses** (`defaultAddress` on the 36 most recent customers with ≥1 order,
pulled via GraphQL): **South Carolina is 58% of real purchasers** (21/36), concentrated
specifically in the **Columbia metro area** (Columbia itself, plus suburbs Irmo, Lexington,
Hopkins, Warrenville) with a secondary Charleston-area cluster (Summerville). North Carolina (3),
Georgia (3), and a long tail of single-customer states make up the rest. Order-weighted (repeat
customers counted per order, not per customer — a better proxy for real revenue-driving geography)
South Carolina rises to **57% of all orders in the sample**, and several of the highest-repeat
customers found earlier in this project's Shopify work (6 orders, 5 orders, 4 orders) are
specifically in the Columbia, SC area.

**2. Session geography, last 90 days** (`FROM sessions SHOW sessions GROUP BY session_region /
session_city`) — an independent signal (site visitors, not just converters) that lands on the same
place: **South Carolina is the #1 region by sessions (157), North Carolina is #2 (108)** — well
ahead of every other state. By city, **Columbia is the #1 city by sessions (78)**, with Charlotte
#3 (60), Atlanta #7 (18), and Irmo, Summerville, Simpsonville, Lexington, Savannah, and Hopkins all
appearing again — the same cities as the purchaser data, found independently.

**Combined read: South Carolina (Columbia metro core) + North Carolina (Charlotte metro) are the
real, dominant markets today — not a broad, even national footprint.** Georgia (Atlanta-area) is a
real secondary market. This is a materially different picture from treating Rocka Moss as
targeting broadly across the brief's mentioned expansion cities (Chicago, Atlanta, + a third) —
those may be *aspirational* future-expansion targets, but the **current, real customer geography**
is Carolinas-first.

## ⚠️ Data-quality catch: some "sessions" are bot/datacenter traffic, not real visitors

Before trusting the session data at face value, a few entries stood out as implausible for real
consumer traffic: **Council Bluffs, Iowa (42 of the region's 52 Iowa sessions)** and **Boardman +
Prineville, Oregon (36 of 40 Oregon sessions)** are well-known major cloud/data-center hub cities
(Google, Amazon, and Meta all operate large data centers in exactly these towns), and **Ashburn,
Virginia (10 of 36 Virginia sessions)** is the single largest data-center corridor in the US (AWS
us-east-1 and others). These read as automated/bot/crawler traffic or VPN exit nodes, not real
shoppers — excluded from the "clean" recalculation above (South Carolina still leads at ~32% of
non-datacenter-tainted sessions, North Carolina ~22%, combined ~55%). **Lesson for any future
traffic analysis on this store: always sanity-check top-session cities against known data-center
locations before reading them as real audience geography** — this wasn't previously flagged in
`kpi-targets.md`'s earlier session-data pull.

## Behavioral signals (already established elsewhere, restated here for the character-sheet brief)

- **32% repeat-purchase rate**, averaging 2.86 orders per returning customer (`kpi-targets.md`).
- **Real average order value among repeat customers: $46.96** — people buying more than one bottle
  or adding items, not just a single $34.99 jar (`kpi-targets.md`).
- **Strawberry Shortcake is the clear flavor leader** on both orders and revenue — the obvious
  flavor to feature first in any character-sheet/UGC concept (`kpi-targets.md`).
- **Instagram meaningfully outperforms Facebook as a referral channel** (8 orders vs. 1 in the
  original 90-day pull) — reinforces IG as the primary platform to design UGC creative for.

## Soft signal, flagged carefully: likely skews toward Black women customers

Scanning first names across the same 50-customer sample pulled for the geography analysis (not
saved to this repo — aggregate observation only), the customer base reads as **majority female**
and includes a real concentration of names commonly associated with Black American communities.
**This is explicitly a soft, inferred signal — not confirmed demographic data.** Shopify doesn't
capture age, gender, or ethnicity directly, and inferring identity from first names alone is
unreliable and shouldn't be treated as fact. It's worth noting for one reason: it's **directionally
consistent with independent evidence already gathered elsewhere in this project** —
`competitor-research.md` flagged Black Girl Vitamins and Culture Connection 360 (both
Black-owned/Black-audience-focused wellness and body-care brands) as strong positioning/tonal
references for Rocka Moss, and Culture Connection 360 specifically has real Chicago and Atlanta
locations that came up again in the geography analysis above via Canton, GA. Two independent
observations pointing the same direction is worth taking seriously as a hypothesis — **not**
worth locking in without Ben or Christian's direct confirmation.

## What this means for the AI UGC character sheet(s)

1. **Ground the environment/setting in the Southeast — Columbia, SC or Charlotte, NC-coded
   suburban/everyday settings** (a home kitchen, a car, a local gym, a porch) rather than a
   generic or coastal-city backdrop. This matches Frankie Shaw's own environment-drives-tonality
   principle already documented in `docs/frankie-shaw-ai-ugc-method.md`.
2. **Casting should be relatable, not aspirational-model** — per the same doc's
   relatable-not-intimidating casting principle, already mapped to Rocka Moss in
   `ai-ugc-playbook.md`'s Section 0.
3. **The likely-Black-women skew above is a hypothesis to confirm with Ben/Christian before
   locking a specific character's look** — if confirmed, casting should reflect that; if not
   confirmed or if Christian wants broader appeal, a neutral/varied casting approach is the safer
   default. Don't guess past what the data actually supports.
4. **Feature Strawberry Shortcake first** in whatever concept gets built, consistent with the real
   sales data above.

## Method note

`list-customers` (the built-in Shopify tool) doesn't return address fields — the geography pull
required a direct GraphQL query against `Customer.defaultAddress` (validated via
`validate_graphql_codeblocks` before running, per the Shopify MCP's own required workflow).
Session geography came from `run-analytics-query` (ShopifyQL) `GROUP BY session_region` and
`GROUP BY session_city`. Both pulls covered ~36-86 real customer records / 743 sessions — real but
moderate sample sizes; worth re-running periodically as more data accumulates, especially once any
paid campaign starts driving new geographic traffic.

## Next step

Draft 1-2 AI UGC character concepts grounded in this profile (per `ai-ugc-playbook.md`'s Section 0
framework and the Frankie Shaw/Tay tent-pole formats), confirm the Black-women-skew hypothesis
with Ben/Christian before locking a specific look, then generate and lock a character sheet via
GPT Image 2.5 (same approach as `clients/ai-ugc-agency/session-reference.md`'s character-reference
step) before drafting the first real ad concept.

# Skills in this repo

## `2k-yt-transcript`
Own skill, built this session — pulls a YouTube video's transcript via
`youtube-transcript-api` with a `yt-dlp` fallback. See its own `SKILL.md`.

## Marketing skills (from `coreyhaines31/marketingskills`)
21 of the repo's 49 skills, vendored in 2026-09-23 for Rocka Moss growth-marketing work — Ben
asked which were worth pulling, this is the curated subset. MIT licensed (Corey Haines, 2025) —
full license text kept in `THIRD_PARTY_LICENSE_marketingskills.txt` per the license's own terms.
Each skill's `evals/` folder (the upstream repo's own test suite) was left out; `SKILL.md` +
`references/` + `assets/` were kept.

**Installed — directly maps to active Rocka Moss work:**
`ads`, `ad-creative`, `cro`, `seo-audit`, `schema`, `analytics`, `influencer-marketing`, `emails`,
`sms`, `social`, `attribution`, `ab-testing`, `copywriting`, `copy-editing`,
`competitor-profiling`, `marketing-psychology`, `offers`, `popups`, `video`, `image`, `ai-seo`.

**Deliberately left out — SaaS/B2B-shaped, doesn't fit a single-brand DTC Shopify store:**
`aso` (App Store Optimization — no app), `churn-prevention` (subscription cancel-flows — no
subscription product yet), `co-marketing`, `cold-email`, `community-marketing`, `competitors`
(SaaS "vs" comparison pages), `directory-submissions` (startup/SaaS directories),
`events`, `free-tools`, `lead-magnets`, `launch` (Product Hunt-style launches), `onboarding`
(post-signup SaaS activation), `paywalls`, `pricing` (its own `SKILL.md` says single-product/
service brands should use `offers` instead), `product-marketing` (redundant with this repo's own
`PROJECT_BRIEF.md`/`profile.md` pattern), `programmatic-seo`, `prospecting` (B2B lead lists),
`public-relations`, `referrals` (worth reconsidering later — the 32% repeat-purchase rate found
in `clients/rocka-moss/kpi-targets.md` could support a referral program, just not urgent now),
`revops`, `sales-enablement`, `signup`, `site-architecture`, `marketing-plan`/`marketing-ideas`/
`marketing-council`/`marketing-loops` (meta-planning tools, lower priority than direct execution
skills right now).

Add any of the excluded ones later the same way if scope changes — they're all in the same
upstream repo, MIT licensed, same install pattern.

## `ads-*` skills (from `AgriciDaniel/claude-ads`) — 2026-09-24
`PROJECT_BRIEF.md` names 8 commands from this repo (`/ads dna`, `/ads photoshoot`, `/ads create`,
`/ads generate`, `/ads meta`, `/ads math`, `/ads budget`, `/ads landing`) — installed 2026-09-24
after an audit found they'd never actually been pulled in. MIT licensed (agricidaniel, 2026) —
full license text kept in `THIRD_PARTY_LICENSE_claude-ads.txt`.

**The live upstream repo has evolved into something much bigger than the brief describes** — a
full multi-platform ("Claude Ads") paid-media operating system covering 12 ad platforms (Google,
Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat, X) with a
Python backend, install/uninstall scripts, a control-plane, and live campaign-mutation commands
(`/ads launch --apply`, `/ads optimize --apply`) gated behind its own capability/credential system.
**Did not run the upstream `install.sh`** and did not vendor the master `ads/SKILL.md` orchestrator
or its Python core — that would pull in all 12 platforms and live-mutation tooling this project
doesn't need or have credentials for. Instead, vendored just the individual skill files (each is
self-contained, no dependency on the orchestrator to be useful as prompting/methodology guidance):

**Installed — the 8 brief-named commands, mapped to their current skill-folder names, plus 3
more that are directly useful and Meta-only/non-mutating:**
`ads-dna` (brand profile extraction — brief's `/ads dna`), `ads-photoshoot` (product photography
generation guidance — brief's `/ads photoshoot`, complements this repo's own
`ai-ugc-playbook.md` recipe rather than replacing it), `ads-create` / `ads-generate` (campaign
concepts → ad image assets — brief's `/ads create` / `/ads generate`), `ads-meta` (Meta platform
audit — brief's `/ads meta`), `ads-math` (CPA/ROAS/break-even calculator — brief's `/ads math`),
`ads-budget` (budget/bid planning — brief's `/ads budget`), `ads-landing` (landing-page quality
audit — brief's `/ads landing`, distinct from the parked full-rebrand item, a narrower
"run before spending ad budget sending traffic there" check), `ads-competitor` (competitor
paid-ad research methodology — directly supports the Meta Ad Library gap found 2026-09-24),
`ads-creative` (ad copy/creative audit — hooks, fatigue, format coverage), `ads-plan` (overall
paid-ad strategy document).

**Deliberately excluded:**
- All other-platform audits (`ads-google`, `ads-youtube`, `ads-linkedin`, `ads-tiktok`,
  `ads-microsoft`, `ads-apple`, `ads-amazon`, `ads-reddit`, `ads-pinterest`, `ads-snapchat`,
  `ads-x`) — `PROJECT_BRIEF.md` explicitly says "NOT in scope... this is a Meta-only play."
- `ads-launch`, `ads-optimize` — live campaign-mutation commands with `--apply` modes against a
  real connected ad account. Excluded on purpose, not an oversight: this project has no live Meta
  ad account write-access configured, and installing mutation-capable tooling isn't something to
  pull in quietly alongside a documentation-only skill batch.
- `ads-monitor` — daily/weekly live-account pacing monitoring, not useful until ads actually run.
- `ads-setup`, `ads-validate`, `ads-research`, `ads-report`, `ads-test`, `ads-audit`,
  `ads-attribution`, `ads-server-side-tracking` — orchestrator/control-plane infrastructure for
  the full "Claude Ads" system (installation safety, run-bundle JSON rendering, cross-platform
  attribution spanning platforms this project doesn't use) — narrower than what the brief
  actually asked for.
- Supporting `references/` files: kept the Meta-specific ones (`meta-audit.md`,
  `meta-creative-specs.md`, `meta-ai-stack.md`) plus platform-agnostic ones that generically
  support the installed skills (`benchmarks.md`, `bidding-strategies.md`, `budget-allocation.md`,
  `compliance.md`, `compliance-requirements.md`, `conversion-tracking.md`, `copy-frameworks.md`,
  `creative-source-registry.md`, `image-providers.md`, `prompt-patterns.md`,
  `thinking-framework.md`, `voice-to-style.md`) in a shared `claude-ads-references/` folder (not
  itself a skill). Left out the other-platform reference/creative-spec files and the
  control-plane plumbing docs (`automation-tier-classifier.md`, `status-contract.md`,
  `mcp-integration.md`, `scoring-system.md`).

## `meta-ads-generator-skill` (`tenfoldmarc/meta-ads-generator-skill`) — NOT installed, no license
The brief's other named repo. **Checked 2026-09-24: this repo has no LICENSE file and no license
mention anywhere** (unlike `coreyhaines31/marketingskills` and `AgriciDaniel/claude-ads`, both
MIT). Under default copyright, that means no explicit grant to redistribute/vendor its files —
so its actual `SKILL.md`/`backends/*.md` content was **not copied into this repo**, consistent
with the standing no-raw-copyrighted-content discipline already used for the Frankie Shaw/Tay
YouTube material (paraphrase the technique, don't store the source verbatim). Its actual pipeline
(URL → brand guidelines → competitor + customer-review research → a "psychology pillar map"
synthesizing 4-6 emotional/rational purchase drivers, each backed by a verbatim customer quote →
4 ad concepts → backend-routed image generation) substantially overlaps with what
`ai-ugc-playbook.md` and `docs/multi-image-role-tagging.md` already do for this project, with one
genuinely new idea worth capturing in our own words: **the "psychology pillar map" technique**
(synthesize competitor/review research into 4-6 named purchase-driver pillars, each with a real
customer quote as evidence, before drafting any ad angle) — not yet folded into
`ai-ugc-playbook.md`, worth doing since it's a real, useful structure distinct from what's there.
If Ben wants the actual tool (not just the technique), that needs either his own direct
relationship with tenfoldmarc/permission to vendor it, or building an equivalent from scratch
using this project's own Comfy Cloud generation path instead of its Higgsfield/kie.ai/OpenAI
backend options.

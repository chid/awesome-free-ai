# Free AI Resources — Project Guide

A self-updating directory of free AI tools, served as a static web page driven by a CSV, with a guide to following AI developments.

> **This file is the single source of truth for agent instructions in this repo.**
> It follows the cross-tool `AGENTS.md` convention, so Claude Code, Antigravity,
> Cursor and Codex all read the same conventions. `CLAUDE.md` is a pointer to this
> file — put changes here, never there, so the two cannot drift apart.
>
> More than one agent works in this repo at once. Before staging, re-check
> `git status` for edits that are not yours, prefer explicit paths over
> `git add -A`, and commit promptly rather than leaving work in the tree.

## Files

| File | Purpose |
|---|---|
| `resources.csv` | Source of truth — free tools, one row per tool |
| `paid_resources.csv` | Source of truth — paid-only tools (no genuine free tier) |
| `local_resources.csv` | Source of truth — local/self-hosted LLM runners, UIs, and engines |
| `index.html` | Web page; fetches and renders CSV data at load time |
| `STAY_CURRENT.md` | Curated guide to AI newsletters, blogs, podcasts, videos, research feeds, and communities |
| `history.csv` | Append-only log of every add/remove/edit to `resources.csv` |
| `paid_history.csv` | Append-only log of every add/remove/edit to `paid_resources.csv` |
| `local_history.csv` | Append-only log of every add/remove/edit to `local_resources.csv` |
| `CHANGELOG.md` | Human-readable summary of each refresh, newest first |
| `QUOTAS.md` | Notes on how paid AI plans meter usage — quota models, not prices |
| `quota_history.csv` | Append-only log of quantitative rate limits, credit pools, and quota transitions over time |
| `quotas.py` | CLI/library to query, filter, and compare quantitative quota histories |
| `README.md` | Markdown rendering of `resources.csv`, regenerated each refresh (keep the banner/live-site header block) |
| `assets/banner.svg` | README banner (also served by Pages) |
| `update.py` | Interactive CLI for manual changes (writes history automatically) |
| `sync_activity.py` | Syncs latest commit dates, stars, and model updates from GitHub/HuggingFace |
| `activity.json` | Cached metadata and live activity timestamps for GitHub/HuggingFace resources |
| `AGENTS.md` | Project guide and agent conventions — the source of truth |
| `CLAUDE.md` | Pointer to `AGENTS.md`, for Claude Code's auto-loading |
| `refresh_prompt.md` | Claude prompt for researching and adding free tools |
| `paid_refresh_prompt.md` | Claude prompt for researching and adding paid-only tools |
| `local_refresh_prompt.md` | Claude prompt for researching and adding local LLM tools |
| `watch_setup_prompt.md` | One-time prompt to build `check_tiers.py` + `watch_pages.csv` (local tier-change watcher) |
| `models_viz_prompt.md` | One-time prompt to build `models.html` + `model_releases.csv` (open-weights model release timeline, seeded from models.fyi) |
| `models.html` | Static model release timeline page; fetches `model_releases.csv` at load — serve via `python3 -m http.server` |
| `model_releases.csv` | Data for the timeline — notable releases, two-year rolling window plus `notable` classics. A row with `license` = `TBD` is a **placeholder** for an announced, unshipped model (e.g. the Qwen4 tiers): the page badges it and leaves it out of the region counts. When it ships, fill in the real date, specs and licence, and log an `edit` |
| `model_releases_history.csv` | Append-only seed/change log for `model_releases.csv` |
| `rumours.html` | Rumoured/announced-but-unshipped models ranked by prediction-market odds, plus filings (e.g. Anthropic's S-1); fetches `rumours.csv` |
| `rumours.csv` | Data for the rumour page: `item, lab, kind (model/filing), status (Rumoured/Announced/Confirmed), expected, probability, market_scope (blank = the market is for this exact model; otherwise what it resolves on, e.g. "any Qwen model"), notes, source_label, source_url, checked`. Once something ships, move it to `model_releases.csv` and delete it here. This file is a snapshot, not a log |
| `.github/workflows/pages.yml` | Deploys the site (both pages + CSVs) to GitHub Pages on every push to `main` |


> **Frontier model pricing & context windows:** see [models.dev](https://models.dev) — no need to track this ourselves.

## CSV schemas

`resources.csv` columns:
```
name, category, url, description, free_tier, requires_signup, tags
```

`paid_resources.csv` columns:
```
name, category, url, description, pricing, tags
```
(`pricing` replaces `free_tier`/`requires_signup` — paid tools are always paid and require accounts.)

`local_resources.csv` columns:
```
name, category, url, description, hardware_reqs, license, tags
```

`history.csv` / `paid_history.csv` / `local_history.csv` columns:
```
date, action, name, category, url, notes
```

`quota_history.csv` columns:
```
date, vendor, product, tier, feature_or_model, metric, limit_value, unit, window, change_type, notes
```


Valid `action` values: `add`, `remove`, `edit`, `init`.

## How to serve locally

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

The page uses `fetch('resources.csv')` so it needs a server (not file://).

The site is also published to GitHub Pages — <https://chid.github.io/awesome-free-ai/>
(includes the model timeline at `/models.html`). The deploy workflow runs on
every push to `main`; no build step, the artifact is just the tracked files.

## How to update

**Manually via CLI:**
```bash
python3 update.py
```
Supports add, remove, edit, list, and history view. All writes also log to `history.csv`.

**Manually via CSV editor:**
Edit `resources.csv` directly, then append a row to `history.csv` yourself.

**Via Claude (research refresh):**
Open a Claude Code session in this directory and paste the contents of `refresh_prompt.md` (free tools) or `paid_refresh_prompt.md` (paid-only tools). Claude will web-search for new tools, add any not already listed, and open a PR.

## How to run a refresh

Run both in the same session so everything lands in one `refresh/YYYY-MM` PR:

```bash
claude
# 1. paste refresh_prompt.md        → free tools
# 2. paste paid_refresh_prompt.md   → paid tools
```

Or trigger the scheduled agent if one is configured (check `claude schedule list`).

The model timeline (`models.html`) has its own monthly upkeep — at each refresh,
paste the "Monthly upkeep" section of `models_viz_prompt.md`.

## Monthly PR workflow

Each monthly refresh creates a branch `refresh/YYYY-MM`, commits all changes to
`resources.csv`, `paid_resources.csv`, their history files, `CHANGELOG.md`,
`QUOTAS.md` and `README.md`, then opens a PR against `main`. Merge the PR to publish the month's
updates.

## Maintenance rules

- Never delete rows from any `*history.csv` file — they are append-only
- Every refresh adds a dated section at the top of `CHANGELOG.md` summarising adds, removes, tier changes, and fixes
- When a vendor changes *how* it meters (credits, rolling windows, shared pools) rather than what it charges, record it in `QUOTAS.md` and date it — temporary boosts must never be written into a `free_tier` or `pricing` value undated
- `README.md` mirrors `resources.csv` — regenerate its resource sections when rows change, and update the snapshot month and count in the header
- Review the links and activity in `STAY_CURRENT.md` on a monthly refresh; update its review date when checking the recommendations
- Keep `requires_signup` as exactly `Yes` or `No` (free tools only)
- `tags` are lowercase, comma-separated, no spaces around commas
- `free_tier` should be specific (e.g. "Free tier with rate limits", "Completely free", "$5 credit on signup") not vague ("Free!")
- `pricing` should be specific (e.g. "$20/month", "from $0.015/1K tokens") not vague ("Paid")
- If a tool's free tier **changes** (tighter or more generous limits), update the row and log an `edit` in `history.csv` with old and new values in the notes
- If a tool's free tier disappears, move it from `resources.csv` to `paid_resources.csv` and log `remove` + `add` in the respective history files
- If a paid tool gains a genuine free tier, move it from `paid_resources.csv` to `resources.csv` and log accordingly
- Categories must match one of the existing values or be clearly justified as new

## Free-tool categories (current)

Audio / Music, Audio / Voice, Code / UI, Code Assistant, Image Generation,
LLM API, LLM Chatbot, LLM Router, LLM Client, Agent Framework, RAG Framework,
Prompt Optimization, Productivity, Search / Research,
Video Generation

### One tool, one pathway

`Local / Self-hosted` was retired from `resources.csv` on 2026-09-05. Anything that
runs on the reader's own hardware belongs in `local_resources.csv` — it has the
`hardware_reqs` and `license` columns that make a local tool useful, which the free
schema does not. Before adding a row to any pathway, check the other two for the same
name or URL.

Freemium tools are the deliberate exception: a genuinely free tier in `resources.csv`
alongside a separately-named paid plan in `paid_resources.csv` (e.g. `Claude (Anthropic)`
and `Claude Pro / Team / Max`) is correct and intended.

## Paid-tool categories (current)

Same set — pick the closest match.

## Local-tool categories (current)

Local Runner, Desktop Client, Serving Engine, Web UI, Code Assistant,
Agent Framework, Fine-tuning / Quant, Embeddings / RAG,
Image / Audio / Video, Hardware / Benchmarking

Local tools render in their own "Run It Yourself" section at the bottom of
`index.html` — they are deliberately excluded from the Free/Paid/All tier counts
and from the header total, so month-on-month resource counts stay comparable.
The page search filters both the main grid and the local section; the category
chips apply to the main grid only.

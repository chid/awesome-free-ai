# Open-Weights Model Timeline — Setup Prompt (one-time)

Use this prompt with a coding agent session to build the **model release
timeline**: a models.fyi-style visualisation of notable AI model releases —
frontier and open-weight — rendered as a static page driven by a CSV, in the
same style as `index.html`.

Data is seeded once from upstream trackers (models.fyi first), then maintained
monthly. The **rolling window rule**: keep releases from the last two years,
plus anything marked `notable` — those classics stay forever.

---

## Prompt (copy everything below this line)

You are working in a repository that maintains a CSV-driven directory of free,
paid and local AI tools rendered by `index.html`. Its conventions live in
`AGENTS.md` — **read it first**, and read `index.html` end-to-end before
writing any page code: your new page must match its visual language and
architecture exactly.

**Your task:** build `model_releases.csv` (data) and `models.html` (visualisation)
covering notable AI model releases, with open-weight status as the headline
dimension, then wire them into the repo docs.

### Step 1 — Research and seed `model_releases.csv`

Create `model_releases.csv` with columns:

```
date,name,lab,modality,weights,license,params,context,notable,notes,source_url
```

- `date` — release-to-public date, `YYYY-MM-DD` (`YYYY-MM` allowed if the exact
  day is unknown). Ascending order, oldest first.
- `weights` — one of: `Open` (downloadable weights today), `Open (announced)`
  (publicly committed, not yet shipped — e.g. FLUX 3 Dev), `API-only`, `Private`.
- `modality` — pick the dominant one: `text`, `vision`, `audio`, `video`,
  `image`, `code`, `robotics`; use `omni` when three or more modalities go in
  and/or out of one model (e.g. Qwen3-Omni).
- `notable` — `Yes` or empty. Marked rows survive the rolling window forever
  (think GPT-3, LLaMA 1, Stable Diffusion 1.5, Whisper). Be sparing: roughly
  15 pre-window classics total.
- `notes` — one clause, no hype. `params`/`context` may be empty when unknown.

Research pass — verify before you trust:

- **Primary upstream: [models.fyi](https://models.fyi)** — use it as the release
  census (every model, every effort tier). It is the feed the timeline mirrors;
  credit it in the page footer.
- **Cross-check every open-weight claim against the actual Hugging Face repo or
  GitHub release** (license file + downloadable weight files exist). Trackers
  routinely label API-only checkpoints as open; the repo's own `local_resources.csv`
  conventions apply — specific, dated, no vibes.
- Fallback sources for dates and specs: Epoch AI's model database
  (epoch.ai/data/ai-models), aireleasetracker.com, and the labs' own blogs
  (bfl.ai, qwen.ai, and similar) as tiebreakers.

Seed scope:

- Every notable release within the last two years (rolling from today) across
  text, vision, audio, video, image, omni and robotics — both open-weight and
  API-only, so the page can show the open/closed split over time. Target
  80–150 rows.
- Pre-window classics marked `notable=Yes`.
- These are already researched and verified (as of 2026-10-03) — include them
  with the dates and sources given:
  - **FLUX 3** (Black Forest Labs, bfl.ai/blog/flux-3) — multimodal flow-matching
    backbone, Early Access 2026-07-23; `FLUX 3 Action` 7B world-action model
    open-weight 2026-09-22; `FLUX 3 Dev` open-weight backbone `Open (announced)`
    for later 2026.
  - **Qwen3-Omni** (Alibaba, github.com/QwenLM/Qwen3-Omni) — 2025-09-22,
    30B-A3B MoE, Apache-2.0, text/image/audio/video in → text/real-time speech out.
  - **Qwen3.5-Omni** (Alibaba, huggingface.co/collections/Qwen/qwen35) —
    2026-03-29, `Open` Light variant; Plus tier and Qwen3.8-Omni-Flash
    (2026-09-18) are `API-only`.

### Step 2 — Build `models.html`

One static file, matching `index.html`'s conventions: same CSS variable palette
and dark card aesthetic, vanilla JS only, `fetch('model_releases.csv')` at load
(so it needs `python3 -m http.server 8080`, not `file://`), no build step, no
external dependencies.

- **Visualisation:** vertical timeline grouped by year (newest first). Each
  release is a row/card with date, name, lab, modality chip, weights badge
  (green = `Open`, amber = `Open (announced)`, muted = `API-only`/`Private`),
  params/context where known, one-line notes, and a link to `source_url`.
- **Filters:** text search; weights chips (All / Open / Open (announced) /
  API-only); modality chips; a lab dropdown. Header counts: total releases,
  open-weight count, window span.
- **Window rule, rendered:** rows older than two years are hidden unless
  `notable=Yes`, with a "show notable classics" toggle so they stay
  discoverable. State this rule in the page footer.
- **Footer credit:** "Seeded from models.fyi, Epoch AI and lab blog
  announcements; open-weight status verified against Hugging Face. Last
  seeded YYYY-MM-DD."

### Step 3 — History log and repo docs

- Create `model_releases_history.csv` (`date,action,name,notes` — append-only)
  and log every seeded row as `add` during the seed pass. This follows the
  repo's existing history-file convention; never delete from it.
- `AGENTS.md`: add `models.html`, `model_releases.csv`,
  `model_releases_history.csv` and `models_viz_prompt.md` to the **Files** table,
  plus a one-line pointer under **How to run a refresh** to the monthly upkeep
  below.
- `CHANGELOG.md`: add a dated section at the top describing the seed (row count,
  date range, open vs API split).

### Step 4 — Branch, commit, PR

Land it on the monthly refresh branch per repo convention:

```bash
git checkout -b refresh/$(date +%Y-%m) 2>/dev/null || git checkout refresh/$(date +%Y-%m)
git add models.html model_releases.csv model_releases_history.csv AGENTS.md CHANGELOG.md
git commit -m "viz: add open-weights model release timeline (models.html + model_releases.csv)"
git push -u origin refresh/$(date +%Y-%m)
```

If a PR for the branch already exists the push updates it; otherwise open one
with `gh pr create` summarising: row count, date range, open vs API-only split,
and the notable classics list.

### Monthly upkeep (recurring — paste just this section next month)

1. Add the past month's notable releases: models.fyi first, open-weight claims
   verified against Hugging Face, `add` rows logged in
   `model_releases_history.csv`. Work through any open "Review models.dev
   cross-check" issue (or run `python3 .github/scripts/check_models_dev.py`),
   and record skipped items in `.github/upstreams/models-dev-reviewed.txt`.
   Date a row by its first public release: the API, an app or a download that anyone
   can use, so not a waitlist or partner-only preview. When weights follow later,
   note their date in `notes`.
2. Flip `Open (announced)` → `Open` when weights actually ship (e.g. FLUX 3 Dev
   when it lands), noting the ship date in `notes`.
3. Prune rows older than two years that are not `notable=Yes`; log each prune
   as a `remove` row — never delete from the history file.
4. Update the footer's last-seeded date and add a `CHANGELOG.md` section.

---

## Running it

Open a coding agent session in this project directory and paste the prompt
above. One shot for the build; afterwards, paste the "Monthly upkeep" section
at each refresh.

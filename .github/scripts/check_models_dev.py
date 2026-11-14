#!/usr/bin/env python3
"""Cross-check model_releases.csv against models.dev (github.com/anomalyco/models.dev).

models.dev keeps one TOML file per model under models/<lab>/ with release_date, open_weights and a
weights link. This check reports two things for review, never edits our data:

  1. New: recent first-party models for labs we track that model_releases.csv doesn't have.
  2. Differences: rows we both have where the release date differs by more than a week, or the
     open-weights status disagrees.

models.dev is a cross-check, not ground truth (it can lag, e.g. on weights published after an API
launch), so every item needs checking against the lab's own announcement or Hugging Face.
Acknowledge an item you've reviewed by adding its line to .github/upstreams/models-dev-reviewed.txt.
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
import tarfile
from datetime import date, timedelta
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
TARBALL_URL = "https://codeload.github.com/anomalyco/models.dev/tar.gz/refs/heads/dev"
REPO_URL = "https://github.com/anomalyco/models.dev/blob/dev/models"
REVIEWED_PATH = ROOT / ".github" / "upstreams" / "models-dev-reviewed.txt"

# Our `lab` values -> models.dev lab folders. Labs missing here aren't in models.dev.
LABS = {
    "OpenAI": "openai", "Anthropic": "anthropic", "Google": "google", "Google DeepMind": "google",
    "xAI": "xai", "Meta": "meta", "DeepSeek": "deepseek", "Alibaba": "alibaba", "Moonshot AI": "moonshotai",
    "Zhipu AI (Z.ai)": "zhipuai", "MiniMax": "minimax", "Mistral AI": "mistral", "Xiaomi": "xiaomi",
    "StepFun": "stepfun", "NVIDIA": "nvidia", "Reflection AI": "reflection", "Tencent": "tencent",
}
# Serving variants and snapshots, not separate releases.
VARIANT_RE = re.compile(r"(latest|highspeed|ultraspeed|contributor|\b\d{4}\b$|-\d{4}$)", re.I)
DATE_TOLERANCE_DAYS = 7


def normalize(value: str) -> str:
    value = re.sub(r"\s*[\(\[].*?[\)\]]", "", value)  # drop "(announced)", "[dev]" and similar
    return re.sub(r"[^a-z0-9.]+", "", value.casefold())


def parse_model(text: str) -> dict:
    """Read the top-level scalars and [[weights]] urls we need, without a TOML dependency."""
    out: dict = {"weights": []}
    table = None
    for raw in text.splitlines():
        line = raw.split(" #", 1)[0].strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("["):
            table = line.strip("[] ")
            continue
        m = re.match(r'^([A-Za-z_]+)\s*=\s*(.+)$', line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val in ("true", "false"):
            val = val == "true"
        if table is None and key in ("name", "release_date", "open_weights", "family"):
            out[key] = val
        elif table == "weights" and key == "url":
            out["weights"].append(val)
    return out


def fetch_models() -> dict[str, dict]:
    request = Request(TARBALL_URL, headers={"User-Agent": "free-ai-upstream-check"})
    with urlopen(request, timeout=60) as response:
        data = response.read()
    models: dict[str, dict] = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        for member in tar:
            parts = member.name.split("/")
            # <root>/models/<lab>/<model>.toml
            if len(parts) == 4 and parts[1] == "models" and parts[3].endswith(".toml") and member.isfile():
                fh = tar.extractfile(member)
                if fh is None:
                    continue
                model = parse_model(fh.read().decode("utf-8"))
                model["lab"], model["id"] = parts[2], parts[3][:-5]
                models[parts[2] + "/" + model["id"]] = model
    return models


def load_reviewed() -> set[str]:
    if not REVIEWED_PATH.is_file():
        return set()
    return {
        line.split(" #", 1)[0].strip()
        for line in REVIEWED_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def to_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value) if len(value) == 10 else None
    except ValueError:
        return None


def compare(models: dict[str, dict], rows: list[dict], reviewed: set[str], since: date):
    # Explicit matches: "match <lab>/<id> = <our name>" in the reviewed file.
    aliases = {}
    for line in reviewed:
        m = re.match(r"^match\s+(\S+)\s*=\s*(.+)$", line)
        if m:
            aliases[m.group(2).strip()] = m.group(1)

    index: dict[tuple[str, str], str] = {}
    for key, m in models.items():
        for n in (m.get("name", ""), m["id"]):
            index.setdefault((m["lab"], normalize(n)), key)

    matched: dict[str, dict] = {}
    differences = []
    for row in rows:
        lab = LABS.get(row["lab"])
        if not lab or row.get("license") == "TBD":  # placeholders aren't released yet
            continue
        key = aliases.get(row["name"]) or index.get((lab, normalize(row["name"])))
        if not key or key not in models:
            continue
        matched[key] = row
        m = models[key]
        theirs, ours = to_date(str(m.get("release_date", ""))), to_date(row["date"])
        if theirs and ours and abs((theirs - ours).days) > DATE_TOLERANCE_DAYS:
            item = f"{key} release_date={m['release_date']}"
            if item not in reviewed:
                differences.append((row, m, key, item, f"date: ours {row['date']}, models.dev {m['release_date']}"))
        ow = m.get("open_weights")
        if isinstance(ow, bool) and row["weights"] in ("Open", "API-only", "Private") and ow != (row["weights"] == "Open"):
            item = f"{key} open_weights={'true' if ow else 'false'}"
            if item not in reviewed:
                differences.append((row, m, key, item, f"open weights: ours {row['weights']}, models.dev open_weights={str(ow).lower()}"))

    ours_by_lab = {(LABS.get(r["lab"]), normalize(r["name"])) for r in rows}
    new = []
    for key, m in models.items():
        if m["lab"] not in set(LABS.values()) or key in matched or key in reviewed:
            continue
        rd = to_date(str(m.get("release_date", "")))
        if not rd or rd < since or VARIANT_RE.search(m["id"]) or VARIANT_RE.search(m.get("name", "")):
            continue
        if (m["lab"], normalize(m.get("name", ""))) in ours_by_lab:
            continue
        new.append((key, m))
    new.sort(key=lambda km: (str(km[1].get("release_date")), km[0]), reverse=True)
    return new, differences


def render_report(new, differences, since: date) -> str:
    lines = [
        "## models.dev cross-check",
        "",
        f"Source: [anomalyco/models.dev](https://github.com/anomalyco/models.dev) (`models/<lab>/*.toml`, `dev` branch).",
        f"New: first-party models released since {since.isoformat()} that `model_releases.csv` lacks. "
        f"Differences: release dates more than {DATE_TOLERANCE_DAYS} days apart, or open-weights status disagreeing.",
        "",
    ]
    if not new and not differences:
        lines.extend(["Nothing needs review.", ""])
        return "\n".join(lines)
    if new:
        lines.extend([f"### New ({len(new)})", ""])
        for key, m in new:
            ow = m.get("open_weights")
            weights = f" · [weights]({m['weights'][0]})" if m.get("weights") else ""
            lines.append(
                f"- `{m.get('release_date')}` [{m.get('name', key)}]({REPO_URL}/{key}.toml) — {m['lab']}, "
                f"open_weights={str(ow).lower() if isinstance(ow, bool) else '?'}{weights} — ack: `{key}`"
            )
        lines.append("")
    if differences:
        lines.extend([f"### Differences ({len(differences)})", ""])
        for row, m, key, item, what in differences:
            lines.append(f"- **{row['name']}** vs [{key}]({REPO_URL}/{key}.toml): {what} — ack: `{item}`")
        lines.append("")
    lines.extend([
        "models.dev can lag or record an API date rather than the announcement, so check each item against the "
        "lab's announcement or Hugging Face. Add verified releases or fixes to `model_releases.csv` and log them in "
        "`model_releases_history.csv`. To stop an item reappearing (skipped, or our value is right), add its ack line "
        "to `.github/upstreams/models-dev-reviewed.txt`. If a row only fails to match because the names differ, add "
        "`match <lab>/<id> = <our name>` there instead.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path, help="write the Markdown report to this path")
    parser.add_argument("--github-output", type=Path, help="write has_findings to a GitHub Actions output file")
    parser.add_argument("--days", type=int, default=120, help="how far back to look for new releases (default 120)")
    args = parser.parse_args()

    try:
        models = fetch_models()
    except (OSError, URLError, tarfile.TarError, UnicodeError) as error:
        print(f"Could not fetch or read the models.dev archive: {error}", file=sys.stderr)
        return 2
    if len(models) < 100:
        print(f"Only {len(models)} models found in the models.dev archive; refusing a partial comparison.", file=sys.stderr)
        return 2

    with (ROOT / "model_releases.csv").open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    since = date.today() - timedelta(days=args.days)
    new, differences = compare(models, rows, load_reviewed(), since)
    report = render_report(new, differences, since)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write(f"has_findings={'true' if new or differences else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

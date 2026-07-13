#!/usr/bin/env python3
"""Fetch the authorized Codex Radar model-summary API and append history."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from radar.api import (  # noqa: E402
    DEFAULT_API_URL,
    append_history,
    fetch_current_payload,
    normalize_model_summary,
    token_from_environment,
)


HISTORY_PATH = ROOT / "data" / "api" / "model_iq_history.csv"


def main() -> None:
    url = os.environ.get("CODEX_RADAR_API_URL", DEFAULT_API_URL).strip() or DEFAULT_API_URL
    payload = fetch_current_payload(token_from_environment(), url=url)
    rows = normalize_model_summary(payload, source_url=url)
    added = append_history(HISTORY_PATH, rows)
    print(f"API snapshot {rows[0]['snapshot_id']}: {len(rows)} model summaries; {added} new rows")
    print(f"Updated {HISTORY_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

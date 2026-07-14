#!/usr/bin/env python3
"""Fetch the authorized Codex Radar model-summary API and append history."""

from __future__ import annotations

import json
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
STATUS_PATH = ROOT / "data" / "api" / "monitor_status.json"


def write_monitor_status(rows: list[dict[str, str]], added: int) -> None:
    """Write a public heartbeat without exposing credentials or the raw response."""
    status = {
        "last_successful_check_at": rows[0]["retrieved_at"],
        "snapshot_id": rows[0]["snapshot_id"],
        "source_observed_at": rows[0]["observed_at"],
        "source_date": max((row.get("source_date", "") for row in rows), default=""),
        "model_count": len(rows),
        "new_rows": added,
        "source_changed": added > 0,
    }
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        json.dumps(status, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    url = os.environ.get("CODEX_RADAR_API_URL", DEFAULT_API_URL).strip() or DEFAULT_API_URL
    payload = fetch_current_payload(token_from_environment(), url=url)
    rows = normalize_model_summary(payload, source_url=url)
    added = append_history(HISTORY_PATH, rows)
    write_monitor_status(rows, added)
    print(f"API snapshot {rows[0]['snapshot_id']}: {len(rows)} model summaries; {added} new rows")
    print(f"Updated {HISTORY_PATH.relative_to(ROOT)}")
    print(f"Updated {STATUS_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

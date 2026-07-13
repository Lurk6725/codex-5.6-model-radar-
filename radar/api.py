"""Codex Radar API retrieval and model-summary normalization."""

from __future__ import annotations

import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_API_URL = "https://codexradar.com/api/v1/current"
API_HISTORY_COLUMNS = [
    "snapshot_id", "observed_at", "retrieved_at", "source_date", "model", "effort",
    "label", "source_score", "passed", "tasks", "invalid", "valid_tasks",
    "total_tokens", "input_tokens", "cached_input_tokens", "output_tokens",
    "wall_seconds", "cost_usd", "provenance", "source_url",
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _as_csv_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _infer_effort(key: str) -> str:
    suffix = key.removeprefix("gpt_56_")
    for effort in ("xhigh", "medium", "high", "low", "max", "ultra"):
        if suffix.endswith(f"_{effort}"):
            return effort
    return "unknown"


def fetch_current_payload(token: str, *, url: str = DEFAULT_API_URL, timeout: int = 30) -> dict[str, Any]:
    """Fetch and validate the authorized current-summary response."""
    token = token.strip()
    if not token:
        raise ValueError("API token must not be empty")

    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "codex-5.6-model-radar/0.1",
        },
        method="GET",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read()
    except HTTPError as error:
        raise RuntimeError(f"Codex Radar API returned HTTP {error.code}") from error
    except URLError as error:
        raise RuntimeError(f"Codex Radar API request failed: {error.reason}") from error

    try:
        payload = json.loads(body)
    except json.JSONDecodeError as error:
        raise RuntimeError("Codex Radar API returned invalid JSON") from error
    if not isinstance(payload, dict):
        raise RuntimeError("Codex Radar API payload must be a JSON object")
    comparisons = payload.get("model_iq", {}).get("comparisons")
    if not isinstance(comparisons, dict) or not comparisons:
        raise RuntimeError("API payload does not contain model_iq.comparisons")
    return payload


def snapshot_id(payload: dict[str, Any]) -> str:
    """Create a stable ID from the model-summary portion of one API response."""
    model_iq = payload.get("model_iq", {})
    canonical = json.dumps(model_iq, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def normalize_model_summary(
    payload: dict[str, Any], *, source_url: str = DEFAULT_API_URL, retrieved_at: str | None = None
) -> list[dict[str, str]]:
    """Convert model_iq.comparisons into public, value-only CSV rows."""
    model_iq = payload["model_iq"]
    comparisons = model_iq["comparisons"]
    observed_at = str(payload.get("monitored_at") or model_iq.get("latest", {}).get("date") or "")
    retrieved_at = retrieved_at or utc_now_iso()
    current_snapshot = snapshot_id(payload)
    rows: list[dict[str, str]] = []

    for key, comparison in sorted(comparisons.items()):
        if not isinstance(comparison, dict):
            continue
        latest = comparison.get("latest")
        if not isinstance(latest, dict):
            continue
        model = str(latest.get("model") or comparison.get("model") or key)
        effort = str(latest.get("reasoning_effort") or comparison.get("reasoning_effort") or _infer_effort(key))
        rows.append({
            "snapshot_id": current_snapshot,
            "observed_at": observed_at,
            "retrieved_at": retrieved_at,
            "source_date": str(latest.get("date") or observed_at[:10]),
            "model": model,
            "effort": effort,
            "label": str(comparison.get("label") or f"{model} {effort}"),
            "source_score": _as_csv_value(latest.get("score")),
            "passed": _as_csv_value(latest.get("passed")),
            "tasks": _as_csv_value(latest.get("tasks")),
            "invalid": _as_csv_value(latest.get("invalid")),
            "valid_tasks": _as_csv_value(latest.get("valid_tasks")),
            "total_tokens": _as_csv_value(latest.get("total_tokens")),
            "input_tokens": _as_csv_value(latest.get("input_tokens")),
            "cached_input_tokens": _as_csv_value(latest.get("cached_input_tokens")),
            "output_tokens": _as_csv_value(latest.get("output_tokens")),
            "wall_seconds": _as_csv_value(latest.get("wall_seconds")),
            "cost_usd": _as_csv_value(latest.get("cost_usd")),
            "provenance": "authorized_api_model_iq_summary",
            "source_url": source_url,
        })
    if not rows:
        raise RuntimeError("API payload contains no normalizable model summaries")
    return rows


def append_history(path: Path, new_rows: list[dict[str, str]]) -> int:
    """Upsert rows by snapshot/model/effort and return the number of new rows."""
    existing: list[dict[str, str]] = []
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            existing = list(csv.DictReader(handle))

    combined: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in existing + new_rows:
        normalized = {column: row.get(column, "") for column in API_HISTORY_COLUMNS}
        key = (normalized["snapshot_id"], normalized["model"], normalized["effort"])
        combined[key] = normalized

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=API_HISTORY_COLUMNS)
        writer.writeheader()
        writer.writerows(combined.values())

    existing_keys = {(row.get("snapshot_id", ""), row.get("model", ""), row.get("effort", "")) for row in existing}
    return sum(1 for row in new_rows if (row["snapshot_id"], row["model"], row["effort"]) not in existing_keys)


def token_from_environment() -> str:
    token = os.environ.get("CODEX_RADAR_API_TOKEN", "").strip()
    if not token:
        raise RuntimeError("CODEX_RADAR_API_TOKEN is not configured")
    return token

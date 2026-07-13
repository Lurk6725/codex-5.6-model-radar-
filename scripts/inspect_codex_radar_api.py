#!/usr/bin/env python3
"""Safely inspect the shape of the Codex Radar API response.

This intentionally prints field names and JSON types only. It never prints
response values, request headers, or the bearer token.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_URL = "https://codexradar.com/api/v1/current"


def schema(value: Any, *, depth: int = 0, max_depth: int = 5) -> Any:
    """Return a value-free, bounded description of a JSON value."""

    if depth >= max_depth:
        return {"type": type(value).__name__, "truncated": True}
    if isinstance(value, dict):
        return {
            "type": "object",
            "keys": {str(key): schema(item, depth=depth + 1) for key, item in value.items()},
        }
    if isinstance(value, list):
        result: dict[str, Any] = {"type": "array", "length": len(value)}
        if value:
            result["item_schema"] = schema(value[0], depth=depth + 1)
        return result
    if value is None:
        return {"type": "null"}
    if isinstance(value, bool):
        return {"type": "boolean"}
    if isinstance(value, int) and not isinstance(value, bool):
        return {"type": "integer"}
    if isinstance(value, float):
        return {"type": "number"}
    return {"type": "string"}


def main() -> int:
    token = os.environ.get("CODEX_RADAR_API_TOKEN", "").strip()
    url = os.environ.get("CODEX_RADAR_API_URL", DEFAULT_URL).strip()
    if not token:
        print("CODEX_RADAR_API_TOKEN is not configured", file=sys.stderr)
        return 2

    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "codex-5.6-model-radar-api-inspector/0.1",
        },
        method="GET",
    )

    try:
        with urlopen(request, timeout=30) as response:
            body = response.read()
            content_type = response.headers.get("Content-Type", "")
            status = response.status
    except HTTPError as error:
        print(f"API request failed with HTTP {error.code}", file=sys.stderr)
        return 1
    except URLError as error:
        print(f"API request failed: {error.reason}", file=sys.stderr)
        return 1

    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        print(f"API returned a non-JSON response (HTTP {status}; {content_type})", file=sys.stderr)
        return 1

    print(json.dumps({"http_status": status, "content_type": content_type, "payload": schema(payload)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

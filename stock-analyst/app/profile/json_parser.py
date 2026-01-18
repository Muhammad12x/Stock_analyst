from __future__ import annotations

import json


class JSONParseError(ValueError):
    pass


def extract_json_block(text: str) -> dict:
    start = text.find("{")
    if start == -1:
        raise JSONParseError("No JSON object found")

    brace_count = 0
    end = None
    for idx in range(start, len(text)):
        char = text[idx]
        if char == "{":
            brace_count += 1
        elif char == "}":
            brace_count -= 1
            if brace_count == 0:
                end = idx
                break
    if end is None:
        raise JSONParseError("Unbalanced JSON braces")

    block = text[start : end + 1]
    try:
        return json.loads(block)
    except json.JSONDecodeError as exc:
        raise JSONParseError(f"Invalid JSON: {exc}") from exc

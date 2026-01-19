from __future__ import annotations


def build_profile_prompt(ticker: str, report_markdown: str) -> str:
    return f'''
You are an analyst extracting structured data from a markdown stock report.
Return ONLY valid JSON for the schema below with no extra commentary.

Schema:
{{
  "ticker": "{ticker}",
  "company_name": string or null,
  "sector": string or null,
  "thesis_bullets": ["..."],
  "key_drivers": ["..."],
  "risks": [{{"name": "...", "severity": "low|medium|high"}}],
  "price_targets": {{
    "bull": number or null,
    "base": number or null,
    "bear": number or null,
    "range_low": number or null,
    "range_high": number or null,
    "extraction_status": "found" or "not_found"
  }}
}}

Rules:
- Extract best-effort from the report.
- Never invent numbers. If targets not clearly present, set all to null and extraction_status to "not_found".
- Provide 3-6 thesis bullets and 3-8 drivers when possible.
- Provide 3-8 risks with severity.

Report:
\"\"\"
{report_markdown}
\"\"\"
""".strip()

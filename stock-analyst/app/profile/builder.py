from __future__ import annotations

from pathlib import Path

from pydantic import ValidationError

from app.llm.adapter import LLMAdapter
from app.obs.logger import EventLogger
from app.profile.json_parser import JSONParseError, extract_json_block
from app.profile.prompts import build_profile_prompt
from app.profile.schema import StockProfile
from app.profile.scoring import compute_risk_score


class ProfileBuilder:
    def __init__(self, llm: LLMAdapter, logger: EventLogger) -> None:
        self.llm = llm
        self.logger = logger

    def build(self, ticker: str, report_markdown: str) -> StockProfile:
        prompt = build_profile_prompt(ticker, report_markdown)
        response_text = self.llm.generate(prompt)
        try:
            payload = extract_json_block(response_text)
        except JSONParseError as exc:
            self.logger.log("profile_parse_error", {"ticker": ticker, "error": str(exc)})
            raise
        try:
            profile = StockProfile.model_validate(payload)
        except ValidationError as exc:
            self.logger.log(
                "profile_validation_error",
                {"ticker": ticker, "error": exc.errors()},
            )
            raise
        profile.overall_risk_score_0_10 = compute_risk_score(profile.risks)
        self.logger.log("profile_built", {"ticker": ticker})
        return profile


def write_profile(profile: StockProfile, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(profile.model_dump_json(indent=2), encoding="utf-8")

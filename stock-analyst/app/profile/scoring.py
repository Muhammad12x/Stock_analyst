from __future__ import annotations

from typing import Iterable

from app.profile.schema import RiskItem


WEIGHTS = {"low": 1, "medium": 2, "high": 3}


def compute_risk_score(risks: Iterable[RiskItem]) -> float:
    risks_list = list(risks)
    if not risks_list:
        return 5.0
    total = sum(WEIGHTS.get(risk.severity, 0) for risk in risks_list)
    score = round(total / 2, 1)
    return min(10.0, score)

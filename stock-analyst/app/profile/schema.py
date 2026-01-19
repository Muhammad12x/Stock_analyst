from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class RiskItem(BaseModel):
    name: str
    severity: str = Field(..., pattern="^(low|medium|high)$")


class PriceTargets(BaseModel):
    bull: Optional[float] = None
    base: Optional[float] = None
    bear: Optional[float] = None
    range_low: Optional[float] = None
    range_high: Optional[float] = None
    extraction_status: str = Field(..., pattern="^(found|not_found)$")


class StockProfile(BaseModel):
    ticker: str
    company_name: Optional[str] = None
    sector: Optional[str] = None
    thesis_bullets: List[str]
    key_drivers: List[str]
    risks: List[RiskItem]
    price_targets: PriceTargets
    overall_risk_score_0_10: float = 0.0

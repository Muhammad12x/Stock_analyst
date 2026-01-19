from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd

from app.profile.schema import StockProfile


def build_stocks_list(profiles: List[StockProfile]) -> pd.DataFrame:
    records = []
    for profile in profiles:
        targets = profile.price_targets
        record = {
            "ticker": profile.ticker,
            "sector": profile.sector,
            "target_bull": targets.bull,
            "target_base": targets.base,
            "target_bear": targets.bear,
            "target_range_low": targets.range_low,
            "target_range_high": targets.range_high,
            "risk_score": profile.overall_risk_score_0_10,
        }
        records.append(record)
    return pd.DataFrame(records)


def write_stocks_list(df: pd.DataFrame, json_path: Path, csv_path: Path) -> None:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_json(json_path, orient="records", indent=2)
    df.to_csv(csv_path, index=False)

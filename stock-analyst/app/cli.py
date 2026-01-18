from __future__ import annotations

import typer
from rich.console import Console

from app.core.config import load_config
from app.llm.ollama_client import OllamaClient
from app.obs.logger import EventLogger
from app.profile.builder import ProfileBuilder, write_profile
from app.profile.list_builder import build_stocks_list, write_stocks_list
from app.storage.loader import load_markdown

app = typer.Typer(help="Stock Analyst CLI")
console = Console()


@app.command()
def build(ticker: str) -> None:
    """Build stock profile and list outputs from a markdown report."""
    config = load_config()
    logger = EventLogger(config.logs_dir / "events.jsonl")
    llm = OllamaClient(config.ollama_url, config.ollama_model, logger)
    builder = ProfileBuilder(llm, logger)

    report_path = config.reports_dir / f"{ticker}.md"
    report_markdown = load_markdown(report_path)

    profile = builder.build(ticker, report_markdown)
    profile_path = config.profiles_dir / f"{ticker}.profile.json"
    write_profile(profile, profile_path)

    stocks_list_df = build_stocks_list([profile])
    json_list_path = config.outputs_dir / "stocks_list.json"
    csv_list_path = config.outputs_dir / "stocks_list.csv"
    write_stocks_list(stocks_list_df, json_list_path, csv_list_path)

    console.print(f"Profile written to {profile_path}")
    console.print(f"Stocks list JSON written to {json_list_path}")
    console.print(f"Stocks list CSV written to {csv_list_path}")


if __name__ == "__main__":
    app()

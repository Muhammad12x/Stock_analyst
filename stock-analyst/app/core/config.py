from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    repo_root: Path
    data_dir: Path
    reports_dir: Path
    outputs_dir: Path
    profiles_dir: Path
    logs_dir: Path
    ollama_url: str
    ollama_model: str


def load_config() -> AppConfig:
    load_dotenv()
    repo_root = Path(__file__).resolve().parents[2]
    data_dir = repo_root / "data"
    outputs_dir = data_dir / "outputs"
    profiles_dir = outputs_dir / "profiles"
    logs_dir = data_dir / "logs"
    reports_dir = data_dir / "reports"
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3.1")

    return AppConfig(
        repo_root=repo_root,
        data_dir=data_dir,
        reports_dir=reports_dir,
        outputs_dir=outputs_dir,
        profiles_dir=profiles_dir,
        logs_dir=logs_dir,
        ollama_url=ollama_url,
        ollama_model=ollama_model,
    )

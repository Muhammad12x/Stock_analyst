from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

import httpx

from app.llm.adapter import LLMAdapter
from app.obs.logger import EventLogger


@dataclass
class OllamaClient(LLMAdapter):
    base_url: str
    model: str
    logger: EventLogger

    def generate(self, prompt: str) -> str:
        payload: Dict[str, Any] = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        self.logger.log("llm_call_start", {"model": self.model})
        with httpx.Client(timeout=60.0) as client:
            response = client.post(self.base_url, json=payload)
            response.raise_for_status()
            data = response.json()
        self.logger.log("llm_call_end", {"model": self.model})
        return data.get("response", "")

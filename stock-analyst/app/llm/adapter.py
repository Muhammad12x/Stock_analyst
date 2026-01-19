from __future__ import annotations

from abc import ABC, abstractmethod


class LLMAdapter(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError

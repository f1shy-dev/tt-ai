from dataclasses import dataclass
from typing import Optional


class AnalysisProvider:
    def analyze(self, text):
        raise NotImplementedError("Subclasses must implement analyze method")


@dataclass
class AnalysisChunk:
    start: str
    end: str
    reason: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    hashtags: Optional[list[str]] = None

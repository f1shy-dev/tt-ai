from dataclasses import dataclass


class AnalysisProvider:
    def analyze(self, text):
        raise NotImplementedError("Subclasses must implement analyze method")


@dataclass
class AnalysisChunk:
    start: str
    end: str
    summary: str
    reason: str

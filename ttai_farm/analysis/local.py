from . import AnalysisProvider, AnalysisChunk
from dataclasses import dataclass
from os import path
import json


@dataclass
class LocalAnalysisProvider(AnalysisProvider):
    path: str

    def analyze(self, text):
        if not path.exists(self.path):
            raise FileNotFoundError(f"File not found: {self.path}")

        with open(self.path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON file: {e}") from e

            return [AnalysisChunk(**chunk) for chunk in data]

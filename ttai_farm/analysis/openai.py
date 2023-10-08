from . import AnalysisProvider, AnalysisChunk
from ttai_farm.utils import parse_timestamp_date
from dataclasses import dataclass
import openai
import os
from ttai_farm.console import status, console


@dataclass
class OpenAIAnalysisProvider(AnalysisProvider):
    openai_api_key: str = os.environ.get("OPENAI_API_KEY")
    model: str = "gpt-3.5-turbo-16k"

    def analyze(self, text):
        with status(f"Analyzing transcript with model {self.model}"):
            system_prompt = """You are an analyser, which looks at the transcripts of podcasts and selects a few (max three) high quality 10-30second (must be AT LEAST 10 seconds, dont pick out like 15 short segments, only a few high quality ones) segments which would engage the most largest audience and most amount of viewers in a video clip on social media - audience would be age of between 13 and 24, and dont forget to consider things such as the main hooks in the transcript, and stuff like controversial opinions or interesting facts which could attract attention

    You are to return a JSON array of objects, where in the object: "start" and "end" are the start/end points, "summary" is a one sentence (max 30word) summary of the clip section, and "reason" is a reason from you about why you picked this clip (max 15 words)

    example:
    [{
    "start":"0:00:28.300",
    "end": "0:00:45.620",
    "summary": "Freedom won't happen for the rest of the world, the divide will remain.",
    "reason": "Super controversial opinion - would engage audience/comments"
    }]"""
            openai.api_key = self.openai_api_key
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "system", "content": system_prompt},
                          {"role": "user", "content": text}]
            )
            usage = response["usage"]
            prompt = usage['prompt_tokens']
            comp = usage['completion_tokens']
            print(
                f"Used {prompt} prompt + {comp} completion ({usage['total_tokens']} total ~ ${(prompt/1000*0.0015) + (comp/1000*0.002)}) tokens.")
            items = response["choices"][0]["message"]["content"]
            og_length = len(items)

            items = [item for item in items if parse_timestamp_date(
                item["end"])[2] - parse_timestamp_date(item["start"])[2] >= 10]

            if len(items) == 0:
                raise ValueError(
                    "No segments were found that were longer than 10 seconds.")
            if og_length != len(items):
                print(
                    f"Filtered out {og_length - len(items)} segments that were too short.")

            return [AnalysisChunk(**item) for item in items]
from poe_api_wrapper import PoeApi
from dataclasses import dataclass
import os
import json
from . import AnalysisProvider, AnalysisChunk
from ttai_farm.utils import parse_timestamp_date
from ttai_farm.console import status, console


@dataclass
class PoeAnalysisProvider(AnalysisProvider):
    poe_api_token: str = os.environ.get("POE_API_TOKEN")
    bot_name: str = "a2_100k"

    def analyze(self, text):
        client = PoeApi(self.poe_api_token or os.environ.get("POE_API_TOKEN"))
        bot = self.bot_name or "a2_100k"

        prompt = """You are an analyser, which looks at the transcripts of podcasts and selects a few high quality 10-30second (must be AT LEAST 10 seconds, MAX 1ish minutes - give or take like 10secs, dont pick out like 15 short segments, only a few high quality ones) segments which would engage the most largest audience and most amount of viewers in a video clip on social media - audience would be age of between 13 and 24, and dont forget to consider things such as the main hooks in the transcript, and stuff like controversial opinions or interesting facts which could attract attention

    You are to return a JSON array of objects, where in the object: "start" and "end" are the start/end points, "summary" is a one sentence (max 30word) summary of the clip section, and "reason" is a reason from you about why you picked this clip (max 15 words)

    example:
    [{
    "start":"0:00:28.300",
    "end": "0:00:45.620",
    "summary": "Freedom won't happen for the rest of the world, the divide will remain.",
    "reason": "Super controversial opinion - would engage audience/comments"
    }]

    Please dont add anything else like "here is the ..." or anything that isnt part of the json to your response.

    Just to repeat, output MUST BE JSON array format, and ONLY give me the JSON in the message, and each segment should be 10+ seconds, max 1 or so minutes...\n\nTranscript:\n"""

        end_reminder = """Just so you don't forget, here are your instructions again:"""
        response = ""

        try:
            for chunk in client.send_message(bot, f"""{prompt}{text}\n\n{end_reminder}\n\n{prompt}""", timeout=20):
                pass
            response = chunk["text"]
            console.log("[green]Got response from bot!")
        except Exception as e:
            console.log(
                f"[red]Error sending message to bot: '{e}', trying to get response via alternative method...")
            chatCode = client.current_thread[self.bot_name][0]['chatCode']
            msgs = client.get_previous_messages(bot, chatCode=chatCode)
            bot_msgs = [msg for msg in msgs if msg["author"] == bot]
            if len(bot_msgs) > 0:
                console.log(
                    "[green]Got response from bot via alternative method!")
                response = bot_msgs[0]["text"]
            else:
                raise ValueError("No response from bot")

        if response == "":
            raise ValueError("No response from bot")
        parsed = '[' + response.split("[").pop().split("]")[0] + ']'
        items = json.loads(parsed)
        og_length = len(items)

        def seconds(x):
            return parse_timestamp_date(x)[1] * 60 + parse_timestamp_date(x)[2]

        items = [item for item in items if seconds(
            item["end"]) - seconds(item["start"]) >= 10]

        if len(items) == 0:
            raise ValueError(
                "No segments were found that were longer than 10 seconds.")

        if og_length != len(items):
            console.log(
                f"[grey46]Filtered out {og_length - len(items)} segments that were too short.")

        return [AnalysisChunk(**item) for item in items]

from poe_api_wrapper import PoeApi
from dataclasses import dataclass
import os
import json
import re
from . import AnalysisProvider, AnalysisChunk
from ttai_farm.utils import parse_timestamp_date
from ttai_farm.console import status, console


@dataclass
class PoeAnalysisProvider(AnalysisProvider):
    """
    `prompt` = prompt to use for the analysis. The string "`{transcript}`" will be replaced with the transcript of the video.
        * If starting with `@`, it will be treated as a file path from `./prompts/`
        * If starting with `#`, it will be treated as a file path as-is
        * Otherwise, it will be treated as a string literal

    `bot_name` = name of the bot to use for the analysis
        * `a2_100k` = Claude instant (100k)
        * `a2_2` = Claude 2 (100k)
        * `a2` = Claude instant (9k)
        * `chinchilla` = ChatGPT (4k)

    `poe_api_token` = token used to login to Poe. To obtain:
        * Login to [poe.com](https://poe.com) in browser
        * Open devtools on [quora.com](https://quora.com) (same browser)
        * Go to Application > Cookies
        * Value of the `m-b` cookie is your token!
    """
    poe_api_token: str = os.environ.get("POE_API_TOKEN")
    bot_name: str = "a2_100k"
    prompt: str = "@claude.r3.txt"

    def analyze(self, text):
        client = PoeApi(self.poe_api_token or os.environ.get("POE_API_TOKEN"))
        bot = self.bot_name or "a2_100k"
        if self.prompt.startswith("@"):
            file_path = os.path.join(os.path.dirname(
                __file__), f"prompts/{self.prompt[1:]}")
            prompt = open(file_path, "r").read()
        elif self.prompt.startswith("#"):
            file_path = self.prompt[1:]
            prompt = open(file_path, "r").read()
        else:
            prompt = self.prompt

        prompt = prompt.replace("{transcript}", text)
        prompt += "\n\n"

        response = ""
        console.log(
            f"[grey46]Sending message with {len(prompt.split())} words, {len(prompt)} chars to poe@{bot}...")

        try:
            for chunk in client.send_message(bot, prompt, timeout=20):
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

        # r1 code
        # parsed = '[' + response.split("[").pop().split("]")[0] + ']'
        # items = json.loads(parsed)
        # og_length = len(items)

        print(response)
        if "{" not in response and "}" not in response:
            return []
        # parsed = response.split("{").pop().split("}").pop()
        parsed = re.match(r".*?({.*}).*", response, re.DOTALL).group(1)
        data = json.loads(parsed)
        items = data["clips"]
        og_length = len(items)

        def seconds(x):
            return parse_timestamp_date(x)[1] * 60 + parse_timestamp_date(x)[2]

        def check_time(x):
            return x >= 10 and x <= 75

        items = [item for item in items if check_time(seconds(
            item["end"]) - seconds(item["start"]))]

        # if len(items) == 0:
        #     reason = data["reason"]
        #     raise ValueError(
        #         "No segments were found that were longer than 10 seconds.\nModel reason: " + reason)

        if og_length != len(items):
            console.log(
                f"[grey46]Filtered out {og_length - len(items)} segments that were too short or too long.")

        return [AnalysisChunk(**item) for item in items]

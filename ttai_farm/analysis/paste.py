from . import AnalysisProvider, AnalysisChunk
from ttai_farm.console import status, console
from rich.syntax import Syntax
import json


class PasteAnalysisProvider(AnalysisProvider):
    """
    Literally asks the user to paste in the analysed text in the terminal.
    """

    def print_screen(self, json_input_lines):
        console.clear()
        console.print(
            "[grey46]Please paste the analysis JSON for the video below.\nType 'CLS' and press enter to clear all input.\nType 'EOF' and press enter to save and continue.")
        if len(json_input_lines) > 0:
            console.print(Syntax("\n".join(json_input_lines),
                                 "json", theme="ansi_dark",  word_wrap=True))
        else:
            console.print()

    def analyze(self, text):
        console.input(
            "[medium_purple3]Press enter to enter the paste analysis editor...")
        # with console.screen():
        #     console.show_cursor()
        #     console.print(
        #         "[grey46]Please paste the analysis JSON for the video below.\nType 'CLS' and press enter to clear all input.\nType 'EOF' and press enter to save and continue.\n")
        #     json_input_lines = []
        #     while True:
        #         line = input()
        #         if line.strip().lower() == "eof":
        #             break
        #         if line.strip().lower() == "cls":
        #             json_input_lines = []
        #             console.clear()
        #             console.print(
        #                 "[grey46]Please paste the analysis JSON for the video below.\nType 'CLS' and press enter to clear all input.\nType 'EOF' and press enter to save and continue.\n")
        #             continue
        #         json_input_lines.append(line)
        #     json_input = "\n".join(json_input_lines)

        #     try:
        #         data = json.loads(json_input)
        #     except json.JSONDecodeError as e:
        #         raise ValueError(f"Invalid JSON file: {e}") from e

        #     return [AnalysisChunk(**chunk) for chunk in data]
        with console.screen(style='grey46'):
            console.show_cursor()
            json_input_lines = []
            self.print_screen(json_input_lines)
            while True:
                line = console.input()
                if line.strip().lower() == "eof":
                    break
                if line.strip().lower() == "cls":
                    json_input_lines = []
                    self.print_screen(json_input_lines)
                    continue
                json_input_lines.append(line)
                self.print_screen(json_input_lines)

            json_input = "\n".join(json_input_lines)

            try:
                data = json.loads(json_input)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON file: {e}") from e

            return [AnalysisChunk(**chunk) for chunk in data]

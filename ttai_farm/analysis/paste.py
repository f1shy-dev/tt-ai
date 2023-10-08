from . import AnalysisProvider, AnalysisChunk
import json
from ttai_farm.console import status, console
from ttai_farm.editor import Editor


class PasteAnalysisProvider(AnalysisProvider):
    """
    Literally asks the user to paste in the analysed text in the terminal.
    """

    def analyze(self, text):
        with console.screen():
            console.show_cursor()
            console.print(
                "[grey46]Please paste the analysis JSON for the video below.\nType 'CLS' and press enter to clear all input.\nType 'EOF' and press enter to save and continue.\n")
            json_input_lines = []
            while True:
                line = input()
                if line.strip().lower() == "eof":
                    break
                if line.strip().lower() == "cls":
                    json_input_lines = []
                    console.clear()
                    console.print(
                        "[grey46]Please paste the analysis JSON for the video below.\nType 'CLS' and press enter to clear all input.\nType 'EOF' and press enter to save and continue.\n")
                    continue
                json_input_lines.append(line)
            json_input = "\n".join(json_input_lines)

            try:
                data = json.loads(json_input)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON file: {e}") from e

            return [AnalysisChunk(**chunk) for chunk in data]

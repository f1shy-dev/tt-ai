from .farm.farm import Farm
from .analysis import PasteAnalysisProvider
from os import path
from .console import console


def main():
    farm = Farm(
        workspace_dir="workspace",
        analysis_provider=PasteAnalysisProvider(),
        torch_device="cpu",
        whisper_into_memory=True,
        whisper_model="tiny",
    )
    info = farm.get_video_info("https://www.youtube.com/watch?v=9bZkp7q19f0")
    farm.download_video(info)
    farm.transcribe_video(info, language=None)
    farm.analyze_video(info)


if __name__ == "__main__":
    main()

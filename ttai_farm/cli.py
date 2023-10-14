import argparse
from .farm.farm import Farm
from .analysis import PasteAnalysisProvider, OpenAIAnalysisProvider
from os import path
from .console import console
import whisper


def main():
    parser = argparse.ArgumentParser(
        description="Automatically generate videos using AI.")
    parser.add_argument("--workspace", type=path.abspath, default="workspace", metavar="PATH",
                        help="The directory to store workspace files.")

    parser.add_argument("--analysis-provider", type=str, default="paste",
                        choices=["paste", "openai"], help="The analysis provider to use.")

    parser.add_argument("--whisper-model", type=str,
                        default="small.en", help="The whisper model to use.", choices=whisper.available_models())

    parser.add_argument("--whisper-into-memory", action="store_true", default=False,
                        help="Whether to load the whisper model into memory.")

    parser.add_argument("--torch-device", type=str, choices=["cpu", "cuda", "mps"],
                        default="cpu", help="The torch device to use.")

    parser.add_argument("--skip-if-exists", type=str, metavar="analysis,dl,clip,transcribe", default="analysis,dl,clip,transcribe",
                        help="Comma-separated list of steps to skip if the results are already cached. Valid values: analysis, dl, clip, transcribe")

    parser.add_argument("--max-chars-per-sub-chunk", type=int, default=18, metavar="N",
                        help="The maximum number of characters per sub-chunk.")

    parser.add_argument("videos", nargs="+",
                        help="The URLs of the videos to process.")
    args = parser.parse_args()

    analysis_providers = [PasteAnalysisProvider, OpenAIAnalysisProvider]
    analysis_provider = analysis_providers[[
        "paste", "openai"].index(args.analysis_provider)]()

    farm = Farm(
        workspace_dir=args.workspace,
        analysis_provider=analysis_provider,
        whisper_model=args.whisper_model,
        whisper_into_memory=args.whisper_into_memory,
        torch_device=args.torch_device,
        skip_analysis_if_cached=("analysis" in args.skip_if_exists),
        skip_dl_video_if_cached=("dl" in args.skip_if_exists),
        skip_clip_if_cached=("clip" in args.skip_if_exists),
        skip_transcription_if_cached=("transcribe" in args.skip_if_exists),
        max_chars_per_sub_chunk=args.max_chars_per_sub_chunk,
    )

    for video_url in args.videos:
        info = farm.get_video_info(video_url)
        farm.download_video(info)
        farm.transcribe_video(info, language=None)
        farm.analyze_video(info)
        farm.clip_video(info)

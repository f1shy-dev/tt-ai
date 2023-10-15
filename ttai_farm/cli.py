import argparse
from .farm.farm import Farm
from .analysis import PasteAnalysisProvider, OpenAIAnalysisProvider, PoeAnalysisProvider
from os import path
from .console import console
import whisper


def main():
    parser = argparse.ArgumentParser(
        description="Automatically clip and subtitle videos using AI.")
    parser.add_argument("--workspace", type=path.abspath, default="workspace", metavar="PATH",
                        help="The directory to store workspace files.")

    parser.add_argument("--analysis-provider", type=str, default="paste",
                        choices=["paste", "openai", 'poe'], help="The analysis provider to use.")

    parser.add_argument("--openai-api-key", type=str, default=None, metavar="sk-***",
                        help="The OpenAI API key to use when using 'openai' for analysis. If not specified, the OPENAI_API_KEY environment variable will be used.")

    parser.add_argument("--poe-token", type=str, default=None, metavar="***",
                        help="The Poe token to use when using 'poe' for analysis. If not specified, the POE_TOKEN environment variable will be used. Token is the 'm-b' cookie @ https://quora.com/")

    parser.add_argument("--analysis-model", type=str,
                        help="The analysis model ID/name to use if using 'openai' or 'poe' for analysis.")

    parser.add_argument("--whisper-model", type=str,
                        default="small.en", help="The whisper model to use.", choices=whisper.available_models())

    parser.add_argument("--whisper-into-memory", action="store_true", default=False,
                        help="Whether to load the whisper model into memory.")

    parser.add_argument("--whisper-device", type=str, choices=["cpu", "cuda", "mps"],
                        default="cpu", help="The torch device to use for running the whisper transcription model.")

    parser.add_argument("--skip-if-exists", type=str, metavar="analysis,dl,clip,transcribe", default="analysis,dl,clip,transcribe",
                        help="Comma-separated list of steps to skip if the results are already cached. Valid values: analysis, dl, clip, transcribe")

    parser.add_argument("--max-chars-per-sub-chunk", type=int, default=18, metavar="N",
                        help="The maximum number of characters per sub-chunk.")

    parser.add_argument("--spotify-user", type=str, default=None, metavar="USERNAME",
                        help="The Spotify username to use when downloading Spotify videos.")

    parser.add_argument("--spotify-password", type=str, default=None, metavar="PASSWORD",
                        help="The Spotify password to use when downloading Spotify videos.")

    parser.add_argument("videos", nargs="+",
                        help="The URLs of the videos to process.")
    args = parser.parse_args()

    analysis_provider = None
    if args.analysis_provider == "paste":
        analysis_provider = PasteAnalysisProvider()
    if args.analysis_provider == "openai":
        analysis_provider = OpenAIAnalysisProvider(model=args.analysis_model,
                                                   openai_api_key=args.openai_api_key)
    if args.analysis_provider == "poe":
        analysis_provider = PoeAnalysisProvider(
            poe_api_token=args.poe_token, bot_name=args.analysis_model)

    farm = Farm(
        workspace_dir=args.workspace,
        analysis_provider=analysis_provider,
        whisper_model=args.whisper_model,
        whisper_into_memory=args.whisper_into_memory,
        torch_device=args.whisper_device,
        skip_analysis_if_cached=("analysis" in args.skip_if_exists),
        skip_dl_video_if_cached=("dl" in args.skip_if_exists),
        skip_clip_if_cached=("clip" in args.skip_if_exists),
        skip_transcription_if_cached=("transcribe" in args.skip_if_exists),
        max_chars_per_sub_chunk=args.max_chars_per_sub_chunk,
        spotify_credentials=(args.spotify_user, args.spotify_password)
    )

    for video_url in args.videos:
        info = farm.get_video_info(video_url)
        farm.download_video(info)
        farm.transcribe_video(info, language=None)
        farm.analyze_video(info)
        farm.clip_video(info)

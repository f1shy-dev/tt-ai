import os
from ..analysis import AnalysisProvider
from dataclasses import dataclass, field
import torch
from .download_video import download_video, download_video_info, VideoInfo
from .download_spotify import download_spotify, download_spotify_info
from .transcribe import transcribe_video
import warnings
import json
from ttai_farm.console import status, console
from .clipper import clip_video


def detect_device():
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


@dataclass
class Farm:
    workspace_dir: os.PathLike
    analysis_provider: AnalysisProvider
    whisper_model: str = "small.en"
    whisper_into_memory: bool = False
    whisper_cpp_path: str | None = None
    whisper_cpp_threads: int = 8
    whisper_cpp_args: list[str] = field(default_factory=list)
    torch_device: str = detect_device()

    skip_analysis_if_cached: bool = True
    skip_dl_video_if_cached: bool = True
    skip_clip_if_cached: bool = True
    skip_transcription_if_cached: bool = True
    max_chars_per_sub_chunk: int = 18
    spotify_credentials: tuple[str, str] | None = None

    def __post_init__(self):
        self.workspace_dir = os.path.abspath(self.workspace_dir)
        # make sure workspace dir exists
        os.makedirs(self.workspace_dir, exist_ok=True)
        # make workspace/cache and workspace/clips
        os.makedirs(os.path.join(self.workspace_dir, "cache"), exist_ok=True)
        os.makedirs(os.path.join(self.workspace_dir, "clips"), exist_ok=True)

    def debug(self):
        print("Workspace dir:", self.workspace_dir)
        print("Analysis provider:", self.analysis_provider)
        print("Torch device:", self.torch_device)
        print("Whisper model:", self.whisper_model)

        print("\nSkip analysis if cached:", self.skip_analysis_if_cached)
        print("Skip DL video if cached:", self.skip_dl_video_if_cached)
        print("Skip transcription if cached:",
              self.skip_transcription_if_cached)

    def get_video_info(self, url):
        if 'spotify' in url:
            return download_spotify_info(self.workspace_dir, self.skip_dl_video_if_cached, url, self.spotify_credentials[0], self.spotify_credentials[1])
        return download_video_info(self.workspace_dir, self.skip_dl_video_if_cached, url)

    def download_video(self, info: VideoInfo):
        if info.extractor == 'spotify-show':
            return download_spotify(self.workspace_dir, self.skip_dl_video_if_cached, info)
        return download_video(self.workspace_dir, self.skip_dl_video_if_cached, info)

    def transcribe_video(self, info: VideoInfo, *, language: str | None = "en"):
        if self.torch_device == "cpu":
            warnings.filterwarnings(
                "ignore", message="FP16 is not supported on CPU; using FP32 instead")

        return transcribe_video(
            self.workspace_dir,
            self.skip_transcription_if_cached,
            info,
            self.whisper_model,
            self.torch_device,
            self.max_chars_per_sub_chunk,
            language,
            self.whisper_into_memory,
            self.whisper_cpp_path,
            self.whisper_cpp_threads,
            self.whisper_cpp_args
        )

    def analyze_video(self, info: VideoInfo):
        video_folder = os.path.join(
            self.workspace_dir, 'cache', info.folder_name())
        analysis_path = os.path.join(video_folder, "analysis.json")

        if self.skip_analysis_if_cached and os.path.exists(analysis_path):
            try:
                afile = open(analysis_path, "r", encoding="utf-8")
                analysis = json.load(afile)
                afile.close()
                if analysis is None or len(analysis) == 0:
                    console.log(
                        "Cached analysis is empty or invalid, re-analyzing...", style="red")
                else:
                    console.log(
                        f"Found cached analysis with {len(analysis)} clips")
                    return
            except Exception as e:
                console.log(
                    "Failed to load cached analysis, re-analyzing...", style="red")

        file = open(os.path.join(
            video_folder, "transcript.sen_chunked.compact.srt"), "r", encoding="utf-8")
        text_content = file.read()
        console.log(
            f"[grey46]Sending {len(text_content)} chars of transcript to analysis provider...")
        analysis = self.analysis_provider.analyze(text_content)
        if analysis is None or len(analysis) == 0:
            console.print(analysis)
            raise Exception("Analysis provider returned empty analysis")

        console.log(
            f"[white]Saving analysis with {len(analysis)} clips to cache...")
        with open(analysis_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(list(map(lambda x: x.__dict__, analysis)), indent=4))

    def clip_video(self, info: VideoInfo):
        clip_video(self.workspace_dir, self.skip_clip_if_cached, info)

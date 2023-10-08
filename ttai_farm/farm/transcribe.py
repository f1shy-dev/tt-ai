from tqdm import TqdmExperimentalWarning
import warnings
import whisper
from ttai_farm.utils import write_compact_srt, write_srt, write_word_chunked_srts
from .download_video import VideoInfo
import os
from dataclasses import dataclass
import sys
from tqdm.rich import tqdm
from ttai_farm.console import status, console
import whisper.transcribe
transcribe_module = sys.modules['whisper.transcribe']
transcribe_module.tqdm.tqdm = tqdm
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)

file_names = [
    "transcript.srt",
    "transcript.compact.srt",
    "transcript.txt",
    "transcript.chunked.compact.srt",
    "transcript.chunked.srt",
]


def transcribe_video(workspace_dir: str, skip_transcription_if_cached: bool, video: VideoInfo, whisper_model: str, torch_device: str, chars_per_chunk: int = 18, language: str | None = None, whisper_into_memory: bool = False):
    video_folder = os.path.join(workspace_dir, 'cache', video.folder_name())
    audio_path = os.path.join(video_folder, f"{video.video_id}.wav")
    all_exist = all(list(map(lambda x: os.path.exists(
        os.path.join(video_folder, x)), file_names)))

    if not skip_transcription_if_cached or not all_exist:
        console.log("[grey46]Removing cached/incomplete transcriptions...")
        for file_name in file_names:
            if os.path.exists(os.path.join(video_folder, file_name)):
                os.remove(os.path.join(video_folder, file_name))

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if all_exist:
        return

    console.log(
        f"[grey46]Loading whisper model {whisper_model} on device {torch_device}")
    model = whisper.load_model(
        whisper_model, device=torch_device, in_memory=whisper_into_memory)

    console.log("[white]Transcribing audio...")
    result = model.transcribe(
        audio_path, language=language, word_timestamps=True, verbose=False)

    console.log("[grey46]Saving transcribed transcript...")

    with open(os.path.join(video_folder, "transcript.srt"), "w", encoding="utf-8") as srt:
        write_srt(result["segments"], file=srt)

    with open(os.path.join(video_folder, "transcript.compact.srt"), "w", encoding="utf-8") as csrt:
        write_compact_srt(result["segments"], file=csrt)

    with open(os.path.join(video_folder, "transcript.txt"), "w", encoding="utf-8") as txt:
        txt.write(result["text"])

    ch_csrt_file = open(os.path.join(
        video_folder, "transcript.chunked.compact.srt"), "w", encoding="utf-8")
    ch_srts_file = open(os.path.join(
        video_folder, "transcript.chunked.srt"), "w", encoding="utf-8")
    write_word_chunked_srts(result["segments"], srt_file=ch_srts_file,
                            csrt_file=ch_csrt_file, chars_per_chunk=chars_per_chunk)

    console.log(
        f"Saved transcribed transcript - {len(result['text'].split())} words")

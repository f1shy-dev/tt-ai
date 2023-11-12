from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TotalFileSizeColumn, DownloadColumn, TransferSpeedColumn, TimeElapsedColumn, RenderableColumn
import torch
from tqdm import TqdmExperimentalWarning
import warnings
import whisper
from ttai_farm.utils import write_compact_srt, write_srt, write_chunked_srts, parse_timestamp_date
from .download_video import VideoInfo
import os
import sys
from tqdm.rich import tqdm
from ttai_farm.console import console
import json
import whisper.transcribe
import subprocess
transcribe_module = sys.modules['whisper.transcribe']
transcribe_module.tqdm.tqdm = tqdm
warnings.filterwarnings("ignore", category=TqdmExperimentalWarning)
file_names = [
    "transcript.srt",
    "transcript.map",
    "transcript.compact.srt",
    "transcript.txt",
    "transcript.chunked.compact.srt",
    "transcript.chunked.srt",
    "transcript.sen_chunked.compact.srt",
    "transcript.sen_chunked.srt",
]


def transcribe_video(
        workspace_dir: str,
        skip_transcription_if_cached: bool,
        video: VideoInfo,
        whisper_model: str,
        torch_device: str,
        chars_per_chunk: int = 18,
        language: str | None = None,
        whisper_into_memory: bool = False,
        whisper_cpp_path: str | None = None,
        whisper_cpp_threads: int = 8,
        whisper_cpp_args: list[str] = []):
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

    if whisper_cpp_path is not None:

        command = [
            whisper_cpp_path,
            '-m', whisper_model,
            '-f', audio_path,
            '-osrt',
            '-t', str(whisper_cpp_threads),
            '--max-len', '1',
            '-sow',
            *whisper_cpp_args
        ]
        print_comm = command.copy()
        print_comm[4] = "/path/to/audio.wav"
        console.log(
            f"[grey46]$ {' '.join(print_comm)}")

        with Progress(
            SpinnerColumn(),
            TextColumn("{task.description}"),
            TimeElapsedColumn(),
            "[progress.elapsed]elapsed",
            transient=True,
        ) as progress:
            task = progress.add_task(
                "[white]Transcribing audio with whisper.cpp...", total=1)
            output = subprocess.run(command, capture_output=True)
            if output.returncode != 0:
                raise Exception(
                    f"whisper.cpp failed with return code {output.returncode}\n{output.stderr.decode('utf-8')}")
            progress.update(task, advance=1)
        console.log("[grey46]Loading whisper.cpp output...")
        out_srt_path = os.path.join(
            video_folder, f'{video.video_id}.wav.srt')
        with open(out_srt_path, "r", encoding="utf-8") as srt_file:
            srt_data = srt_file.read()

        def seconds(x): return (x[0] * 3600) + (x[1] * 60) + x[2]
        fmt_srt_data = srt_data.split("\n\n")
        fmt_srt_data = [x.strip() for x in fmt_srt_data]
        fmt_srt_data = list(filter(lambda x: x != "", fmt_srt_data))
        fmt_srt_data = list(
            map(lambda x: list(filter(lambda y: y != "", x.split("\n"))), fmt_srt_data))
        fmt_srt_data = list(
            map(lambda x: [x[0], x[1], "\n".join(x[2:])], fmt_srt_data))
        fmt_srt_data = list(map(lambda x: [
            x[0],
            seconds(parse_timestamp_date(x[1].split(" --> ")[0])),
            seconds(parse_timestamp_date(x[1].split(" --> ")[1])),
            x[2]
        ], fmt_srt_data))

        result = {}
        result["text"] = "".join([x[3] for x in fmt_srt_data])
        result["segments"] = []
        for chunk in fmt_srt_data:
            result["segments"].append({
                "start": chunk[1],
                "end": chunk[2],
                "text": chunk[3],
                "words": [{"word": chunk[3], "start": chunk[1], "end": chunk[2]}]
            })

    else:
        console.log(
            f"[grey46]Loading whisper model {whisper_model} on device {torch_device}")
        model = whisper.load_model(
            whisper_model, device=torch.device(torch_device), in_memory=whisper_into_memory)

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

    sch_csrt_file = open(os.path.join(
        video_folder, "transcript.sen_chunked.compact.srt"), "w", encoding="utf-8")
    sch_srts_file = open(os.path.join(
        video_folder, "transcript.sen_chunked.srt"), "w", encoding="utf-8")

    sch_srts_file = open(os.path.join(
        video_folder, "transcript.map"), "w", encoding="utf-8")

    print(json.dumps(result), file=sch_srts_file)

    write_chunked_srts(result["segments"], srt_file=ch_srts_file,
                       csrt_file=ch_csrt_file, chars_per_chunk=chars_per_chunk, sentence_csrt_file=sch_csrt_file, sentence_srt_file=sch_srts_file)

    console.log(
        f"Saved transcribed transcript - {len(result['text'].split())} words")

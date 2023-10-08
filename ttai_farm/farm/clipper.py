import warnings
from .download_video import VideoInfo
import sys
import os
from dataclasses import dataclass
from ttai_farm.console import status, console
import json
from ttai_farm.analysis import AnalysisChunk
from ttai_farm.utils import parse_timestamp_date
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import subprocess


def clip_video(workspace_dir: str, skip_clip_if_cached: bool, video_info: VideoInfo):
    video_folder = os.path.join(
        workspace_dir, 'cache', video_info.folder_name())

    video_path = os.path.join(video_folder, f"{video_info.video_id}.mp4")
    srt_path = os.path.join(video_folder, "transcript.srt")
    analysis_path = os.path.join(video_folder, "analysis.json")

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if not os.path.exists(srt_path):
        raise FileNotFoundError(f"SRT file not found: {srt_path}")

    if not os.path.exists(analysis_path):
        raise FileNotFoundError(f"Analysis file not found: {analysis_path}")

    if os.path.exists(os.path.join(video_folder, "clips")) and not skip_clip_if_cached:
        console.log("[grey46]Removing cached clips...")
        for file_name in os.listdir(os.path.join(video_folder, "clips")):
            os.remove(os.path.join(video_folder, "clips", file_name))

    if os.path.exists(os.path.join(video_folder, "clips")) and len(os.listdir(os.path.join(video_folder, "clips"))) > 0:
        console.log(
            f"Found {len(os.listdir(os.path.join(video_folder, 'clips')))} cached clips for video '{video_info.extractor}-{video_info.video_id}'")
        if len(os.listdir(os.path.join(video_folder, "clips"))) == len(json.load(open(analysis_path, "r", encoding="utf-8"))):
            return

    try:
        with open(analysis_path, "r", encoding="utf-8") as afile:
            analysis = json.load(afile)
            if analysis is None or len(analysis) == 0:
                raise Exception("Analysis file is empty or invalid")

            analysis = [AnalysisChunk(**x) for x in analysis]

    except Exception as e:
        raise Exception("Failed to load analysis file") from e

    os.makedirs(os.path.join(video_folder, "clips"), exist_ok=True)
    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        main_bar = progress.add_task(
            f"Clipping video '{video_info.extractor}-{video_info.video_id}'...", total=len(analysis))

        for i, chunk in enumerate(analysis):
            clip_path = os.path.join(
                video_folder, "clips", f"{i:03d}-{chunk.start}-{chunk.end}.mp4")

            if os.path.exists(clip_path):
                continue

            command = f"ffmpeg -y -i \"{video_path}\" -ss {chunk.start} -to {chunk.end} -c copy \"{clip_path}\""
            output = subprocess.run(command, shell=True, capture_output=True)
            assert output.returncode == 0, f"Failed to clip video: {output.stderr.decode('utf-8')}"
            progress.update(main_bar, advance=1)

    console.log(
        f"[green]Successfully made {len(analysis)} clips for video '{video_info.extractor}-{video_info.video_id}'")

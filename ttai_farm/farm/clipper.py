import warnings
from .download_video import VideoInfo
import sys
import os
from dataclasses import dataclass
from ttai_farm.console import status, console
import json
from ttai_farm.analysis import AnalysisChunk
from ttai_farm.utils import parse_timestamp_date, format_timestamp
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import subprocess


def clip_video(workspace_dir: str, skip_clip_if_cached: bool, video_info: VideoInfo):
    video_folder = os.path.join(
        workspace_dir, 'cache', video_info.folder_name())

    video_path = os.path.join(video_folder, f"{video_info.video_id}.mp4")
    srt_path = os.path.join(video_folder, "transcript.chunked.srt")
    with open(srt_path, "r", encoding="utf-8") as srt_file:
        srt_data = srt_file.read()
    analysis_path = os.path.join(video_folder, "analysis.json")

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if not os.path.exists(srt_path):
        raise FileNotFoundError(f"SRT file not found: {srt_path}")

    if not os.path.exists(analysis_path):
        raise FileNotFoundError(f"Analysis file not found: {analysis_path}")

    paths = [[video_folder, "clips"], [video_folder, "crop-clips"], [video_folder, "sub-clips"],
             [workspace_dir, "clips", video_info.folder_name()]]
    hasPrinted = False
    for path in paths:
        if not os.path.exists(os.path.join(*path)):
            os.makedirs(os.path.join(*path), exist_ok=True)
        elif not skip_clip_if_cached:
            if not hasPrinted:
                hasPrinted = True
                console.log("[grey46]Removing cached clips...")
            for file_name in os.listdir(os.path.join(*path)):
                os.remove(os.path.join(*path, file_name))

    try:
        with open(analysis_path, "r", encoding="utf-8") as afile:
            analysis = json.load(afile)
            if analysis is None or len(analysis) == 0:
                # raise Exception("Analysis file is empty or invalid")
                analysis = []

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
                video_folder, "clips", f"{i:03d}.mp4")
            crop_path = os.path.join(
                video_folder, "crop-clips", f"{i:03d}.mp4")

            if os.path.exists(clip_path):
                continue
            # command = f"ffmpeg -y -i \"{video_path}\" -ss {chunk.start} -to {chunk.end} -c copy \"{clip_path}\" -vf \"crop=ih*(9/16):ih\""
            command = [
                "ffmpeg", "-y",
                "-ss", chunk.start,
                "-to", chunk.end,
                "-i", video_path,
                # "-crf", "18",
                "-c:a", "copy",
                "-c:v", "copy",
                clip_path,
            ]
            output = subprocess.run(command,  capture_output=True)
            assert output.returncode == 0, f"Failed to clip video: {output.stderr.decode('utf-8')}"

            crop_command = [
                "ffmpeg", "-y", "-i", clip_path,
                "-vf", "crop=ih*(9/16):ih",
                "-c:a", "copy",
                # "crf", "18",
                crop_path,
            ]
            crop_output = subprocess.run(crop_command,  capture_output=True)
            assert output.returncode == 0, f"Failed to crop video: {crop_output.stderr.decode('utf-8')}"
            progress.update(main_bar, advance=1)
    console.log(
        f"[grey46]Cropped {len(analysis)} clips for video '{video_info.extractor}-{video_info.video_id}'")

    clip_folder = os.path.join(
        video_folder, "sub-clips")
    os.makedirs(clip_folder, exist_ok=True)

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        main_bar = progress.add_task(
            f"Adding subtitiles to clips for video '{video_info.extractor}-{video_info.video_id}'...", total=len(analysis))

        fmt_srt_data = srt_data.split("\n\n")
        # print(fmt_srt_data[:5])
        fmt_srt_data = [x.strip() for x in fmt_srt_data]
        # print(fmt_srt_data[:5])
        fmt_srt_data = list(filter(lambda x: x != "", fmt_srt_data))
        # print(fmt_srt_data[:5])
        fmt_srt_data = list(
            map(lambda x: list(filter(lambda y: y != "", x.split("\n"))), fmt_srt_data))
        # print(fmt_srt_data[:5])
        fmt_srt_data = list(
            map(lambda x: [x[0], x[1], "\n".join(x[2:])], fmt_srt_data))
        # print(fmt_srt_data[:5])
        fmt_srt_data = list(map(lambda x: [
            x,
            parse_timestamp_date(fmt_srt_data[x][1].split(" --> ")[0]),
            parse_timestamp_date(fmt_srt_data[x][1].split(" --> ")[1]),
            fmt_srt_data[x][2]
        ], range(len(fmt_srt_data))))
        # print(fmt_srt_data[:5])

        if os.path.exists(os.path.join(video_folder, "clipped-srts")):
            for file in os.listdir(os.path.join(video_folder, "clipped-srts")):
                os.remove(os.path.join(video_folder, "clipped-srts", file))
        srtclip_folder = os.path.join(video_folder, "clipped-srts")
        os.makedirs(srtclip_folder, exist_ok=True)

        for i, chunk in enumerate(analysis):
            og_clip_path = os.path.join(
                video_folder, "crop-clips", f"{i:03d}.mp4")

            sub_clip_path = os.path.join(
                # clip_folder, f"{i:03d}-sub.mp4")
                video_folder, "sub-clips", f"{i:03d}.mp4")
            if os.path.exists(sub_clip_path):
                continue

            def seconds(x): return (x[0] * 3600) + (x[1] * 60) + x[2]
            start_ts = seconds(parse_timestamp_date(chunk.start))
            end_ts = seconds(parse_timestamp_date(chunk.end))

            start_chunk = [x for x in fmt_srt_data if seconds(x[1])
                           <= start_ts and seconds(x[2]) >= start_ts]
            # print("SC", start_chunk, start_ts)

            end_chunk = [x for x in fmt_srt_data if seconds(x[1])
                         <= end_ts and seconds(x[2]) >= end_ts]
            # print("EC", end_chunk, end_ts)

            if len(start_chunk) == 0 or len(end_chunk) == 0:
                # console.log(
                #     f"[yellow]Could not find segment for clip #{i}, skipping...")
                analysis[i] = None
                continue
            start_chunk = list(start_chunk).pop()
            # print("SC2", start_chunk)

            end_chunk = list(end_chunk).pop()
            # print("EC2", end_chunk)

            sub_srt_data = fmt_srt_data[int(
                start_chunk[0]):int(end_chunk[0])+1]

            sub_srt_path = os.path.join(
                srtclip_folder, f"{i:03d}-{chunk.start.replace(':', '_')}-{chunk.end.replace(':', '_')}.srt")

            first_chunk = sub_srt_data[0]
            num_offset = int(first_chunk[0])
            ts_offset = first_chunk[1]
            ts_offset_ms = ts_offset[0] * 3600 + \
                ts_offset[1] * 60 + ts_offset[2]

            def fmt_ts(x): return format_timestamp(
                (x[0] * 3600 + x[1] * 60 + x[2]) - ts_offset_ms, always_include_hours=True)

            with open(sub_srt_path, "w", encoding="utf-8") as sub_srt_file:
                sub_srt_file.write("\n\n".join(list(map(lambda x: "\n".join(
                    [str(int(x[0]) - num_offset + 1), f"{fmt_ts(x[1])} --> {fmt_ts(x[2])}", x[3]]), sub_srt_data))))

            sub_style = "Alignment=6,Fontname=Dela Gothic One,BackColour=&H80000000,Spacing=0.2,Outline=0,Shadow=0.75,PrimaryColour=&H00FFFFFF,Bold=1,MarginV=170,Fontsize=16"
            # command = f"ffmpeg -y -i \"{og_clip_path}\" -vf 'subtitles=\"{srt_path}\":force_style=\"{sub_style}\"' \"{sub_clip_path}\""
            # console.log(
            #     f"[grey46]Using subtitles from {sub_srt_path}")
            command = [
                "ffmpeg",
                "-y",
                "-i",
                og_clip_path,
                "-vf",
                # :force_style='{sub_style}'
                f"subtitles='{sub_srt_path}':force_style='{sub_style}':fontsdir='fonts'",
                "-c:a",
                "copy",
                # "crf", "18",
                sub_clip_path
            ]
            output = subprocess.run(command,  capture_output=True)
            assert output.returncode == 0, f"Failed to add subtitles to clip: {output.stderr.decode('utf-8')}"
            progress.update(main_bar, advance=1)

    console.log(
        f"[grey46]Subtitled {len(list(filter(lambda x: x is not None, analysis)))} clips for video '{video_info.extractor}-{video_info.video_id}'")

    if None in analysis:
        console.log(
            f"[yellow]{len(list(filter(lambda x: x is None, analysis)))} clips were skipped due to missing segments...")

    final_clips_folder = os.path.join(
        workspace_dir, "clips", video_info.folder_name())

    os.makedirs(final_clips_folder, exist_ok=True)
    # watermarking clips step
    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        main_bar = progress.add_task(
            f"Watermarking clips for video '{video_info.extractor}-{video_info.video_id}'...", total=len(analysis))

        for i, chunk in enumerate(analysis):
            sub_clip_path = os.path.join(
                video_folder, "sub-clips", f"{i:03d}.mp4")
            watermarked_clip_path = os.path.join(
                final_clips_folder, f"{i:03d}.mp4")
            if os.path.exists(watermarked_clip_path):
                continue
            if not os.path.exists(sub_clip_path):
                continue

            # command = f"ffmpeg -y -i \"{sub_clip_path}\" -i \"{WATERMARK_PATH}\" -filter_complex \"[1]scale=100:100[wm];[0][wm]overlay=10:10\" \"{watermarked_clip_path}\""
            command = [
                "ffmpeg",
                "-y",
                "-i",
                sub_clip_path,
                "-i",
                "watermarks/km-watermark.png",
                "-filter_complex",
                # center watermark, make it 512x512 (image is 1024x1024)
                "[1]scale=304:304[wm];[0][wm]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2+200",

                "-c:a",
                "copy",
                # "crf", "18",
                watermarked_clip_path
            ]
            output = subprocess.run(command,  capture_output=True)
            assert output.returncode == 0, f"Failed to watermark clip: {output.stderr.decode('utf-8')}"
            progress.update(main_bar, advance=1)
    console.log(
        f"[green]Successfully made {len(analysis)} clips for video '{video_info.extractor}-{video_info.video_id}'")

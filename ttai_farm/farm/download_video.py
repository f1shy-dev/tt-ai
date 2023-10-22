import yt_dlp
import json
import os
import subprocess
from dataclasses import dataclass
from ttai_farm.console import status, console


@dataclass
class VideoInfo:
    extractor: str
    video_id: str
    video_url: str

    def folder_name(self):
        return f"{self.extractor}-{self.video_id}"


def download_video_info(workspace_dir: str, skip_dl_video_if_cached: bool, url: str):
    with status(f"Downloading video info for {url}..."):
        with yt_dlp.YoutubeDL({
            'quiet': True,
            'no_warnings': True,
        }) as ydl:
            info = ydl.extract_info(url, download=False)
            v_info = VideoInfo(
                extractor=info['extractor'], video_id=info['id'], video_url=info['webpage_url'])

            v_folder = os.path.join(
                workspace_dir, 'cache', v_info.folder_name())
            os.makedirs(v_folder, exist_ok=True)
            info_path = os.path.join(v_folder, 'info.json')
            exists = os.path.exists(info_path)
            print(json.dumps(ydl.sanitize_info(info)),
                  file=open(info_path, 'w'))
            console.log(
                f"{'Fetched' if exists else 'Saved'} info for video '{v_info.extractor}-{v_info.video_id}'")
            return v_info


def download_video(workspace_dir: str, skip_dl_video_if_cached: bool, video_info: VideoInfo):
    with status(f"Downloading video '{video_info.extractor}-{video_info.video_id}'") as s:
        video_path = os.path.join(
            workspace_dir, 'cache', video_info.folder_name(), f"{video_info.video_id}.mp4")
        audio_path = os.path.join(
            workspace_dir, 'cache', video_info.folder_name(), f"{video_info.video_id}.wav")
        info_path = os.path.join(workspace_dir, 'cache',
                                 video_info.folder_name(), 'info.json')

        if not skip_dl_video_if_cached:
            if os.path.exists(video_path):
                os.remove(video_path)
            if os.path.exists(audio_path):
                os.remove(audio_path)

        # colab detect
        RunningInCOLAB = 'google.colab' in str(get_ipython()) if hasattr(
            __builtins__, '__IPYTHON__') else False

        if not os.path.exists(video_path):
            with yt_dlp.YoutubeDL({
                'format': 'bestvideo+bestaudio',
                'merge_output_format': 'mp4',
                'outtmpl': video_path,
                'quiet': RunningInCOLAB,
                'no_warnings': True,
                'noprogress': RunningInCOLAB
            }) as ydl:
                error_code = ydl.download_with_info_file(info_path)
                if error_code != 0:
                    raise Exception("Failed to download video")
                console.log(
                    f"Downloaded video '{video_info.extractor}-{video_info.video_id}' as mp4@best")

        if not os.path.exists(audio_path):
            s.update(
                f"Extracting audio from video '{video_info.extractor}-{video_info.video_id}' with ffmpeg")
            output = subprocess.run(["ffmpeg", "-y", "-i", video_path, "-vn", "-acodec",
                                    "pcm_s16le", "-ac", "1", "-ar", "16k", audio_path], capture_output=True)
            if output.returncode != 0:
                raise Exception("Failed to extract audio from video")
            console.log(
                f"Extracted audio from video '{video_info.extractor}-{video_info.video_id}' as wav@16khz")

import yt_dlp
import json
import os
import subprocess
from dataclasses import dataclass
from ttai_farm.console import status, console
from .download_video import VideoInfo
from librespot.core import Session
from ttai_farm.console import console
from librespot.metadata import EpisodeId
from .threaded_downloader import threaded_downloader
from rich.filesize import decimal as dec


def download_spotify_info(workspace_dir: str, skip_dl_video_if_cached: bool, url: str, username: str, password: str):
    with status(f"Downloading video info for {url}..."):
        if username is None or password is None:
            raise Exception(
                "Spotify username and password are required to download Spotify videos")
        session = Session.Builder() \
            .user_pass(username, password) \
            .create()

        # console.log("got spotify session", session)
        # access_token = session.tokens().get("playlist-read")
        # console.log("got access token", access_token)
        ep = EpisodeId.from_base62(url.split("/")[-1])

        # console.log("got episode id", ep)
        meta = session.api().get_metadata_4_episode(ep)
        # console.log("got episode metadata", meta.video)
        # console.print(meta.video, type(meta.video))

        hex_id = meta.video[0].file_id.hex()
        # console.log("hexid", hex_id)

        response = session.api()\
            .send("GET", f"/manifests/v7/json/sources/{hex_id}/options/supports_drm", None, None)

        v_info = VideoInfo(
            extractor='spotify-show', video_id=url.split("/")[-1], video_url=url)

        v_folder = os.path.join(
            workspace_dir, 'cache', v_info.folder_name())
        os.makedirs(v_folder, exist_ok=True)
        info_path = os.path.join(v_folder, 'info.json')
        exists = os.path.exists(info_path)
        print(json.dumps({
            'drm_manifest': json.loads(response.content),
            'hex_id': hex_id,
        }),
            file=open(info_path, 'w'))
        console.log(
            f"{'Fetched' if exists else 'Saved'} info for video '{v_info.extractor}-{v_info.video_id}'")
        return v_info


def template(string, **kwargs):
    for key, value in kwargs.items():
        string = string.replace("{{" + key + "}}", value)
    return string


def download_spotify(workspace_dir: str, skip_dl_video_if_cached: bool, video_info: VideoInfo):
    with status(f"Downloading video '{video_info.extractor}-{video_info.video_id}'") as s:
        v_folder = os.path.join(
            workspace_dir, 'cache', video_info.folder_name())

        video_path = os.path.join(v_folder, f"{video_info.video_id}.video.ts")
        audio_path = os.path.join(v_folder, f"{video_info.video_id}.audio.ts")
        wav_audio_path = os.path.join(v_folder, f"{video_info.video_id}.wav")
        combined_path = os.path.join(v_folder, f"{video_info.video_id}.ts")
        video_segment_folder = os.path.join(v_folder, "seg_video")
        audio_segment_folder = os.path.join(v_folder, "seg_audio")
        info_path = os.path.join(v_folder, 'info.json')

        if not skip_dl_video_if_cached:
            for file in [video_path, audio_path, combined_path, wav_audio_path]:
                if os.path.exists(file):
                    os.remove(file)
            for folder in [video_segment_folder, audio_segment_folder]:
                if os.path.exists(folder):
                    for file_name in os.listdir(folder):
                        os.remove(os.path.join(folder, file_name))
            console.log("[grey46]Removed cached video/audio downloads...")

        # colab detect
        RunningInCOLAB = 'google.colab' in str(get_ipython()) if hasattr(
            __builtins__, '__IPYTHON__') else False

        info_data = json.load(open(info_path, "r", encoding="utf-8"))
        drm_manifest = info_data['drm_manifest']
        profiles = drm_manifest['contents'][0]['profiles']

        segment_length = drm_manifest['contents'][0]['segment_length']
        seg_count = int(round(drm_manifest['end_time_millis'] / 1000) /
                        segment_length)
        base_url = drm_manifest['base_urls'][0]

    if not os.path.exists(video_path):
        best_video_stream = max(list(filter(
            lambda x: x['mime_type'] == 'video/mp2t', profiles)), key=lambda x: x.get('video_bitrate', 0))
        video_segments_urls = list(map(lambda x: base_url + template(
            drm_manifest['segment_template'],
            profile_id=str(best_video_stream['id']),
            segment_timestamp=str(
                x * segment_length),
            file_type=best_video_stream['file_type']
        ), range(seg_count)))
        if not os.path.exists(video_segment_folder):
            os.makedirs(video_segment_folder, exist_ok=True)
        threaded_downloader(video_segments_urls, video_segment_folder, 16)
        console.log(
            f"Downloaded {len(video_segments_urls)} video segments")
        with status(f"Concatenating {len(video_segments_urls)} video segments with ffmpeg"):

            with open(os.path.join(video_segment_folder, "ffmpeg-video-packlist.txt"), "w", encoding="utf-8") as f:
                for i in range(len(video_segments_urls)):
                    file_path = os.path.join(
                        video_segment_folder, f'{i * segment_length}.ts')
                    print(f"file '{file_path}'", file=f)

            command = [
                "ffmpeg",
                "-f", "concat",
                "-safe", "0",
                "-i", os.path.join(video_segment_folder,
                                   "ffmpeg-video-packlist.txt"),
                "-c", "copy",
                video_path,
            ]

            output = subprocess.run(command, capture_output=True)
            assert output.returncode == 0, f"[red]Failed to merge video segments: {output.stderr.decode('utf-8')}"
            console.log(
                f"[grey46]Merged {len(video_segments_urls)} video segments into one {dec(os.path.getsize(video_path))} file")

    if not os.path.exists(audio_path):
        best_audio_stream = max(list(filter(
            lambda x: x['mime_type'] == 'audio/mp2t', profiles)), key=lambda x: x.get('audio_bitrate', 0))
        audio_segments_urls = list(map(lambda x: base_url + template(
            drm_manifest['segment_template'],
            profile_id=str(best_audio_stream['id']),
            segment_timestamp=str(
                x * segment_length),
            file_type=best_audio_stream['file_type']
        ), range(seg_count)))
        if not os.path.exists(audio_segment_folder):
            os.makedirs(audio_segment_folder, exist_ok=True)
        threaded_downloader(audio_segments_urls, audio_segment_folder, 16)
        console.log(
            f"Downloaded {len(audio_segments_urls)} audio segments")

        with status(f"Concatenating {len(audio_segments_urls)} audio segments with ffmpeg"):
            with open(os.path.join(audio_segment_folder, "ffmpeg-audio-packlist.txt"), "w", encoding="utf-8") as f:
                for i in range(len(audio_segments_urls)):
                    file_path = os.path.join(
                        audio_segment_folder, f'{i * segment_length}.ts')
                    print(f"file '{file_path}'", file=f)

            command = [
                "ffmpeg",
                "-f", "concat",
                "-safe", "0",
                "-i", os.path.join(audio_segment_folder,
                                   "ffmpeg-audio-packlist.txt"),
                "-c", "copy",
                audio_path,
            ]

            output = subprocess.run(command, capture_output=True)
            assert output.returncode == 0, f"[red]Failed to merge audio segments: {output.stderr.decode('utf-8')}"
            console.log(
                f"[grey46]Merged {len(audio_segments_urls)} audio segments into one {dec(os.path.getsize(audio_path))} file")

    if not os.path.exists(wav_audio_path):
        with status(
                f"Converting audio '{video_info.extractor}-{video_info.video_id}' to wav@16khz with ffmpeg"):
            output = subprocess.run(["ffmpeg", "-y", "-i", audio_path, "-vn", "-acodec",
                                    "pcm_s16le", "-ac", "1", "-ar", "16k", wav_audio_path], capture_output=True)
            assert output.returncode == 0, f"[red]Failed to convert video from audio: {output.stderr.decode('utf-8')}"

            console.log(
                f"Converted audio from video '{video_info.extractor}-{video_info.video_id}' as wav@16khz")

    if not os.path.exists(combined_path):
        with status(
                f"Combining video and audio into one file with ffmpeg"):
            command = [
                "ffmpeg",
                "-i", video_path,
                "-i", audio_path,
                "-c", "copy",
                combined_path,
            ]

            output = subprocess.run(command, capture_output=True)
            assert output.returncode == 0, f"[red]Failed to merge video and audio: {output.stderr.decode('utf-8')}"
            console.log(
                f"Combined video and audio into one {dec(os.path.getsize(combined_path))} file")

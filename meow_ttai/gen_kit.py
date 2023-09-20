import os
import subprocess
import yt_dlp
import whisper
import ffmpeg
from .utils import write_srt, write_compact_srt

#####################
#     Variables     #

DEVICE = os.environ.get("WHISPER_DEVICE", "cuda") # or "cpu" or "mps" for mac
MODEL = os.environ.get("WHISPER_MODEL", "small.en") # or "medium.en" or "large.en"

#####################

def main():
    # Ensure that the necessary directories exist
    os.makedirs("./workspace", exist_ok=True)

    # Ask for a YouTube URL
    # url = input("meow <3! enter your youtewb url: ")
    url = os.environ.get("WHISPER_URL", input("meow <3! enter your youtewb url: "))
    # url = "https://www.youtube.com/watch?v=xFWakbQAk5Q"

    print("Downloading video info...")
    with yt_dlp.YoutubeDL({
        'quiet': True,
    }) as ydl:
        info = ydl.extract_info(url, download=False)
        video_id = info['id']

        # make workspace/<video_id>/(gen_temp, gen_final)
        os.makedirs(f"./workspace/{video_id}/gen_temp", exist_ok=True)
        os.makedirs(f"./workspace/{video_id}/gen_final", exist_ok=True)


    audio_path = f"./workspace/{video_id}/gen_temp/audio.wav"
    video_path = f"./workspace/{video_id}/gen_temp/video.mp4"
    ydl_opts = {
        'format': 'mp4/bestvideo+bestaudio',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'outtmpl': video_path,
        'quiet': True,
    }

# check if video is already downloaded as mp4+audio
    if os.path.exists(video_path) and os.path.exists(audio_path):
        print("Video already downloaded as mp4+audio.")
    else:
        print("Downloading video as mp4...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download([url])


        # extract mp3 from mp4

        print("Extracting audio from video...")
        # ffmpeg.input(video_path).output(audio_path, acodec="pcm_s16le", ac=1, ar="16k").run(quiet=True, overwrite_output=True)
        #run quietly but print errors, overwrite files
        output = subprocess.run(["ffmpeg", "-y", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16k", audio_path], capture_output=True)
        assert output.returncode == 0


    # https://www.youtube.com/watch?v=xFWakbQAk5Q
    print(f"Loading whisper model {MODEL} on device {DEVICE}...")
    model = whisper.load_model(MODEL, device=DEVICE)

    print("Transcribing audio...")
    result = model.transcribe(audio_path, language="en")

    print("Saving subtitles as txt/srt/csrt...")

    # save result["segments"] to srt file
    # save result["text"] to txt file

    with open(f"./workspace/{video_id}/gen_final/subtitles.srt", "w", encoding="utf-8") as srt:
        write_srt(result["segments"], file=srt)

    with open(f"./workspace/{video_id}/gen_final/subtitles.csrt", "w", encoding="utf-8") as csrt:
        write_compact_srt(result["segments"], file=csrt)

    with open(f"./workspace/{video_id}/gen_final/subtitles.txt", "w", encoding="utf-8") as txt:
        txt.write(result["text"])

if __name__ == "__main__":
    main()
# from IPython.display import display, Markdown
import openai
import os
import subprocess
import yt_dlp
import whisper
import ffmpeg
from .utils import write_srt, write_compact_srt
openai.api_key = os.environ.get("OPENAI_API_KEY")

#####################
#     Variables     #

DEVICE = os.environ.get("WHISPER_DEVICE", "cuda") # or "cpu" or "mps" for mac
MODEL = os.environ.get("WHISPER_MODEL", "small.en") # or "medium.en" or "large.en"

#####################

def download_and_transcribe(url=None):
    # Ensure that the necessary directories exist
    os.makedirs("./workspace", exist_ok=True)

    # Ask for a YouTube URL
    # url = input("meow <3! enter your youtewb url: ")
    url = url or input("meow <3! enter your youtewb url: ")
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
    
    return video_id


def analyse_with_chatgpt(video_id):
    system_prompt = """You are an analyser, which looks at the transcripts of podcasts and selects a few (max three) high quality 10-30second (must be AT LEAST 10 seconds, dont pick out like 15 short segments, only a few high quality ones) segments which would engage the most largest audience and most amount of viewers in a video clip on social media - audience would be age of between 13 and 24, and dont forget to consider things such as the main hooks in the transcript, and stuff like controversial opinions or interesting facts which could attract attention

You are to return a JSON array of objects, where in the object: "start" and "end" are the start/end points, "summary" is a one sentence (max 30word) summary of the clip section, and "reason" is a reason from you about why you picked this clip (max 15 words)

example:
[{
  "start":"0:00:28.300",
  "end": "0:00:45.620",
  "summary": "Freedom won't happen for the rest of the world, the divide will remain.",
  "reason": "Super controversial opinion - would engage audience/comments"
}]"""
    file = open(f"./workspace/{video_id}/gen_final/subtitles.csrt", "r", encoding="utf-8")
    transcript = file.read()
    print("Analyzing transcript with ChatGPT...")
    response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo-16k",
              messages=[{"role": "system", "content": system_prompt},
                        {"role": "user", "content": file.read()}
              ])

    usage = response["usage"]
    prompt = usage['prompt_tokens']
    comp = usage['completion_tokens']
    print(f"Used {prompt} prompt + {comp} completion ({usage['total_tokens']} total ~ ${(prompt/1000*0.0015) + (comp/1000*0.002)}) tokens.")
    print(response["choices"][0]["message"]["content"])

    with open(f"./workspace/{video_id}/gen_final/analysis.json", "w", encoding="utf-8") as json:
        json.write(response["choices"][0]["message"]["content"])

# if __name__ == "__main__":
#     video_id = download_and_transcribe()
#     analyse_with_chatgpt(video_id)
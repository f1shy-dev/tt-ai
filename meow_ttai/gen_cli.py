import os

from .gen_kit import download_and_transcribe, seperate_into_clips, analyse_with_chatgpt, analyse_with_paste

os.environ.setdefault("WHISPER_DEVICE", "cpu")
os.environ.setdefault("WHISPER_MODEL", "small.en")
print("meow <3! you're using the bestest content farm ^w^")

if __name__ == "__main__":
    # video_id = download_and_transcribe("https://www.youtube.com/watch?v=xFWakbQAk5Q")
    # video_id = download_and_transcribe()
    video_id = download_and_transcribe()
    analyse_with_paste(video_id)
    seperate_into_clips(video_id)

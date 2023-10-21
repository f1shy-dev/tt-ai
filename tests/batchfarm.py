import os
from ttai_farm.analysis import PoeAnalysisProvider
from ttai_farm import Farm
from ttai_farm.console import console
from dotenv import load_dotenv
load_dotenv()

farm = Farm(
    workspace_dir="workspace",
    analysis_provider=PoeAnalysisProvider(
        poe_api_token=os.getenv("POE_API_TOKEN")),
    whisper_model="base",
    whisper_into_memory=True,
    torch_device="cpu",
    spotify_credentials=(os.getenv("SPOTIFY_USER"),
                         os.getenv("SPOTIFY_PASSWORD")),
)

videos = [
    'spotify:show:66edV3LAbUXa26HG1ZQaKB'
]

console.clear()
for video_url in videos:
    console.print(
        f"[medium_purple3](BatchFarm) Processing video [bold]'{video_url}'")
    info = farm.get_video_info(video_url)
    farm.download_video(info)
    farm.transcribe_video(info, language=None)
    farm.analyze_video(info)
    farm.clip_video(info)

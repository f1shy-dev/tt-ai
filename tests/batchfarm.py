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
    # 'https://open.spotify.com/episode/3pdAvrBlzzZWbkriWjZmSd?si=ByW5Q0yqTLGaXPfnH6EloA'
    'https://open.spotify.com/episode/6OwITXMGgY0mVCGdKRJrYr',
    'https://open.spotify.com/episode/6fppkhPnw5PCspRVGhZhOG',
    'https://open.spotify.com/episode/62tozdFpzt1iSmia1KlCfm',
    'https://open.spotify.com/episode/07TNGl4VKA4UfM4wFehiGD',
    'https://open.spotify.com/episode/5EFrNB3hEU3yjFcuPhBCeF',
    'https://open.spotify.com/episode/3DQfcTY4viyXsIXQ89NXvg',
    'https://open.spotify.com/episode/41RxLAMSdaAd97OAFEpG3H',
    'https://open.spotify.com/episode/7elrOcatC8aOTKARyZT1EF'
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

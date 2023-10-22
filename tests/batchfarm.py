import os
from ttai_farm.analysis import PoeAnalysisProvider
from ttai_farm import Farm
from ttai_farm.console import console
from dotenv import load_dotenv
load_dotenv()

farm = Farm(
    workspace_dir="workspace",
    analysis_provider=PoeAnalysisProvider(
        poe_api_token=os.getenv("POE_API_TOKEN"), prompt="@claude.r3.txt"),
    # ,, bot_name="a2_2"
    whisper_model="/Users/mobilekraft/Downloads/whisper.cpp/models/ggml-base.en.bin",
    whisper_into_memory=True,
    torch_device="mps",
    spotify_credentials=(os.getenv("SPOTIFY_USER"),
                         os.getenv("SPOTIFY_PASSWORD")),
    whisper_cpp_path="/Users/mobilekraft/Downloads/whisper.cpp/main",
    skip_clip_if_cached=False,
    whisper_cpp_threads=8,
)


# on ted playlist page devtools:
# [...document.querySelectorAll(`#maincontent > div > div > div > div > div > div > div > a`)].map(x => x.href.split("?")[0])

videos = [
    # 'https://open.spotify.com/episode/3pdAvrBlzzZWbkriWjZmSd?si=ByW5Q0yqTLGaXPfnH6EloA'
    # 'https://open.spotify.com/episode/6OwITXMGgY0mVCGdKRJrYr',
    # 'https://open.spotify.com/episode/6fppkhPnw5PCspRVGhZhOG',
    # 'https://open.spotify.com/episode/62tozdFpzt1iSmia1KlCfm',
    # 'https://open.spotify.com/episode/07TNGl4VKA4UfM4wFehiGD',
    # 'https://open.spotify.com/episode/5EFrNB3hEU3yjFcuPhBCeF',
    # 'https://open.spotify.com/episode/3DQfcTY4viyXsIXQ89NXvg',
    # 'https://open.spotify.com/episode/41RxLAMSdaAd97OAFEpG3H',
    # 'https://open.spotify.com/episode/7elrOcatC8aOTKARyZT1EF'
    # 'https://www.youtube.com/watch?v=PYaixyrzDOk',
    # 'https://www.youtube.com/watch?v=2E6cg8c0M38',
    # 'https://www.youtube.com/watch?v=rUESS_KGjj4',
    # 'https://www.youtube.com/watch?v=P3i19APsYNs',
    # 'https://www.youtube.com/watch?v=8beoStypxrM',
    # 'https://www.youtube.com/watch?v=dUUwFE7cGXc'
    # "https://www.ted.com/talks/greg_brockman_the_inside_story_of_chatgpt_s_astonishing_potential",
    "https://www.ted.com/talks/gary_marcus_the_urgent_risks_of_runaway_ai_and_what_to_do_about_them",
    "https://www.ted.com/talks/imran_chaudhri_the_disappearing_computer_and_a_world_where_you_can_take_ai_everywhere",
    "https://www.ted.com/talks/yejin_choi_why_ai_is_incredibly_smart_and_shockingly_stupid",
    "https://www.ted.com/talks/alexandr_wang_war_ai_and_the_new_global_arms_race",
    "https://www.ted.com/talks/eliezer_yudkowsky_will_superintelligent_ai_end_the_world",
    "https://www.ted.com/talks/tom_graham_the_incredible_creativity_of_deepfakes_and_the_worrying_future_of_ai",
    "https://www.ted.com/talks/frances_s_chance_are_insect_brains_the_secret_to_great_ai",
    "https://www.ted.com/talks/andrew_ng_how_ai_could_empower_any_business",
    "https://www.ted.com/talks/sofia_crespo_ai_generated_creatures_that_stretch_the_boundaries_of_imagination",
    "https://www.ted.com/talks/maurice_conti_the_incredible_inventions_of_intuitive_ai"
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

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
    # "https://www.ted.com/talks/gary_marcus_the_urgent_risks_of_runaway_ai_and_what_to_do_about_them",
    # "https://www.ted.com/talks/imran_chaudhri_the_disappearing_computer_and_a_world_where_you_can_take_ai_everywhere",
    # "https://www.ted.com/talks/yejin_choi_why_ai_is_incredibly_smart_and_shockingly_stupid",
    # "https://www.ted.com/talks/alexandr_wang_war_ai_and_the_new_global_arms_race",
    # "https://www.ted.com/talks/eliezer_yudkowsky_will_superintelligent_ai_end_the_world",
    # "https://www.ted.com/talks/tom_graham_the_incredible_creativity_of_deepfakes_and_the_worrying_future_of_ai",
    # "https://www.ted.com/talks/frances_s_chance_are_insect_brains_the_secret_to_great_ai",
    # "https://www.ted.com/talks/andrew_ng_how_ai_could_empower_any_business",
    # "https://www.ted.com/talks/sofia_crespo_ai_generated_creatures_that_stretch_the_boundaries_of_imagination",
    # "https://www.ted.com/talks/maurice_conti_the_incredible_inventions_of_intuitive_ai"

    'https://www.youtube.com/watch?v=N8Nf56srwcA' # Elon Musk on Buying Twitter and Turning It Into X
    'https://www.youtube.com/watch?v=5m5ybZD_z6A' # Joe Tries to Shoot an Arrow Into the CyberTruck
    'https://www.youtube.com/watch?v=7wxqo44zsT8' # The Director's of "Talk to Me" Discuss How it Was Made
    'https://www.youtube.com/watch?v=HVt9fue4mnY' # Danny Phillipou's Crazy Story of Participating in Experimental Drug Trials
    'https://www.youtube.com/watch?v=FZHa3oGkB6o' # Tranq: The Latest Development in the Fentanyl Epidemic
    'https://www.youtube.com/watch?v=C-j_8B22MnY' # Why Some People Can Sleep Only 2 Hours a Night
    'https://www.youtube.com/watch?v=1RK1V3ATAkg' # Graham Hancock on Archaeological Mysteries in the Amazon
    'https://www.youtube.com/watch?v=XH-um009UMU' # Dan Henderson on Training with Sean Strickland
    'https://www.youtube.com/watch?v=mYuuIUvi3g4' # Dan Henderson's Crazy Punching Power and Fighting After Knee Surgery
    'https://www.youtube.com/watch?v=XOnH0WMk22U' # Reacting to Makhachev's Head Kick KO of Volkanovski
    'https://www.youtube.com/watch?v=qO_a0lriy-w' # Eddie Bravo's Theory on Abe Lincoln and the CIA's Influence on 60's Music
    'https://www.youtube.com/watch?v=KSIfUfJ_UbQ' # The End of the USADA Era
    'https://www.youtube.com/watch?v=4wjK71VS8T4' # The Possibility of AI Being Used in Propaganda
    'https://www.youtube.com/watch?v=7jgEkK2tWFA' # Writer Coleman Hughes Explains What Started the Israel-Hamas Conflict
    'https://www.youtube.com/watch?v=kyjOAD3FQm4' # Reggie Watts Speculates on UFO's and Shares Story of His Own Encounter
    'https://www.youtube.com/watch?v=0eZKYLIrNmQ' # The Prospect of Having an AI President
    'https://www.youtube.com/watch?v=BVl-apcetUQ' # Evidence of Early Christian Psychedelic Rituals in Ancient Rome
    'https://www.youtube.com/watch?v=MJy8GeO2oo8' # Freaking Out Over the Israel and Hamas Conflict
    'https://www.youtube.com/watch?v=frCnYp9Wwrg' # Jimmy Carr Doesn't Think America is Collapsing Like the Roman Empire
    'https://www.youtube.com/watch?v=GXH0u_Z_gME' # What Innovations of the Past Tell Us About the Future
    'https://www.youtube.com/watch?v=MTJZpO3bTpg' # OpenAI CEO on Artificial Intelligence Changing Society
    'https://www.youtube.com/watch?v=IiHfY5eqGbQ' # Bernard Hopkins on How Prison Prepared Him for Boxing
    'https://www.youtube.com/watch?v=Mp-dMDn9Afw' # Dispute Over the Worth of Trump's Mar-a-lago
    'https://www.youtube.com/watch?v=lqsUH2-AgA8' # Canada's New Regulations for Podcasts
    'https://www.youtube.com/watch?v=WYT3QnbsFRA' # Pollution and the Uptick in Wildfires
    'https://www.youtube.com/watch?v=MOVSufTxsJk' # Is the Crowd Work Trend Causing More Heckling?
    'https://www.youtube.com/watch?v=RIHMp6r6104' # Sean Strickland's Dominant Performance Against Israel Adesanya
    'https://www.youtube.com/watch?v=Iu5muKibWDc' # Thoughts on Dillon Danis vs. Logan Paul
    'https://www.youtube.com/watch?v=pDxA1UvRD0Y' # Is Social Media Affecting the Success Rate of Marriages?
    'https://www.youtube.com/watch?v=30TFjJj0xpY' # 7 Eye Surgeries Later - Steve Strope's Crazy Story of Having His Retina Fall Off
    'https://www.youtube.com/watch?v=uER-ko2sL5o' # Russia, Putin, and Ideological Subversion
    'https://www.youtube.com/watch?v=MUmMcDKF_HM' # David Goggins Spotted Grizzly Bear Tracks While Smokejumping
    'https://www.youtube.com/watch?v=-c8yxiXpgeU' # How Casinos Are Able to Predict Human Behavior
    'https://www.youtube.com/watch?v=5Tg2yaC4R80' # Francis Ngannou on Leaving the UFC, Signing Tyson Fury Fight, and Training with Mike Tyson
    'https://www.youtube.com/watch?v=OR7vtVnU5SE' # Mexico's Alien Skeletons Examined by Doctors
    'https://www.youtube.com/watch?v=eXSOeRdw_3U' # Trae the Truth on Getting Shot and Having the Bullet Stuck in His Arm
    'https://www.youtube.com/watch?v=9gC2y1m_bWo' # Journalist Alex Berenson on the Real Cost of Pharmaceutical Incentives
    'https://www.youtube.com/watch?v=xFWakbQAk5Q' # What Happen if All Drugs Were Legalized?
    'https://www.youtube.com/watch?v=u-eDY9YCrJg' # Kurt Angle Candidly Speaks About Regretting Past Drug Use
    'https://www.youtube.com/watch?v=po6cG-y_RMY' # How Kurt Angle Won an Olympic Golden Medal with a Broken Neck
    'https://www.youtube.com/watch?v=QErqFqnhUDE' # Ultimate Flushing Challenge - JRE Toons
    'https://www.youtube.com/watch?v=8SapgxHBxDs' # Looking Into the South Pole Direct Energy Weapon Conspiracy
    'https://www.youtube.com/watch?v=3JpWEwfo4Dw' # Woman Who Accepted Marlon Brando's Oscar Faked Native American Heritage
    'https://www.youtube.com/watch?v=Hl9rwhFni8c' # Pro Pool Player Jeremy Jones Tells His Craziest Gambling Stories
    'https://www.youtube.com/watch?v=r0J3EUxcgCM' # What's Going on with Alien Abductions?
    'https://www.youtube.com/watch?v=-tUMqudtrHU' # Matt Rife Went Ghost Hunting in the Conjuring House
    'https://www.youtube.com/watch?v=26WYd3gQkgM' # Reacting to Sean Strickland Beating Israel Adesanya
    'https://www.youtube.com/watch?v=ijhn1QMkilw' # Sam Tripoli's Theory About the Next Election Cycle
    'https://www.youtube.com/watch?v=W2PaaWekBSA' # Discussing the Newest Revelation in the JFK Assassination
    'https://www.youtube.com/watch?v=-vMNbuxFvrg' # Tulsi Gabbard on the Response to the Maui Wildfires
    'https://www.youtube.com/watch?v=DbDCnjrC0OE' # Tulsi Gabbard Analyzes the Trump Indictments
    'https://www.youtube.com/watch?v=9gtUAA5PcGQ' # Brain Implants, Space Balloons, and the Technology of the Future
    'https://www.youtube.com/watch?v=h3ZjtgicHs4' # Luis J. Gomez's 3 Day Long Acid Trip
    'https://www.youtube.com/watch?v=KaWihejcGcM' # The Disgusting Parts of History
    'https://www.youtube.com/watch?v=JWFZDnanEbI' # Shane Gillis Tells His Dublin Bar Fight Story
    'https://www.youtube.com/watch?v=4btqj2Ghk04' # Bill Maher on the Trump Indictments and the 2024 Election
    'https://www.youtube.com/watch?v=pcWeT-eI8hY' # Bill Maher on Obesity Being Treated as a Disease
    'https://www.youtube.com/watch?v=lPRTYOJeIxE' # UFO Investigator's on the David Grusch Hearings
    'https://www.youtube.com/watch?v=hH75fQ3SVO8' # Oliver Anthony on the Unexpected Success and Backlash from "Rich Men North of Richmond"
    'https://www.youtube.com/watch?v=DZnFVxXv2II' # How the Sackler Family Made Billions From OxyContin
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

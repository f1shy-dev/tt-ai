from threading import Thread
from queue import Queue
from ttai_farm.v4.write_ass import write_ass
import whisperx
import gc
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import os
import yt_dlp
import subprocess
from rich.console import Console
import json
console = Console()


def status(x, **kwargs):
    return console.status(x, spinner='dots2', **kwargs)


#fmt: off
videos = [
    ['https://www.youtube.com/shorts/pEN42WHePzU', "Random Not So Fun Facts 👀"],
    ['https://www.youtube.com/shorts/Dq8gljHeeXA', "Random Facts You Never Knew 👀"],
    ['https://www.youtube.com/shorts/i3f4fF-wyN0', "Random Facts You Didn't Know👀"],
    ['https://www.youtube.com/shorts/1kK7mJa_R6Q', "Random Facts That Will SHOCK You 👀"],
    ['https://www.youtube.com/shorts/RBHsIEKhOW4', "Random Facts To SCARE You 👀"],
    ['https://www.youtube.com/shorts/USfRLvBFC08', "Random Facts To SHOCK You 👀"],
    ['https://www.youtube.com/shorts/UwsN3kZCUZ4', "Random Facts To SURPRISE You 👀"],
    ['https://www.youtube.com/shorts/o4f0WKXoHLs', "Random Facts To SHOCK You 👀"],
    ['https://www.youtube.com/shorts/Fk837soi1Vo', "Random Facts To RETHINK Your Life 👀"],
    ['https://www.youtube.com/shorts/2sBMjqEYyrg', "Random Facts To HORRIFY You 👀"],
    ['https://www.youtube.com/shorts/EFW-BTYC45M', "Random Facts To TERRIFY You 👀"],
    ['https://www.youtube.com/shorts/iJ5lI2E1Ex8', "Random Facts To BLOW Your Mind 👀"],
    ['https://www.youtube.com/shorts/9tK0sy8lRSo', "Facts That Could Potentially SAVE Your Life 👀"],
    ['https://www.youtube.com/shorts/hhfjXBgsxIA', "Shower Thoughts That Will Make You Think Twice 👀"],
    ['https://www.youtube.com/shorts/Bh7P0jUwKH8', "Facts That Can Save Your Life 👀"],
    ['https://www.youtube.com/shorts/OAogPGfly6E', "Shower Thoughts That May Scare You 👀"],
    ['https://www.youtube.com/shorts/FyIoZnfUit0', "Tips That Can Save Your Life 👀"],
    ['https://www.youtube.com/shorts/I-QUUaGhmbI', "Shower Thoughts That Will Terrify You 👀"],
    ['https://www.youtube.com/shorts/d9qQF31wPXk', "Random Facts That Can Save Your Life👀"],
    ['https://www.youtube.com/shorts/1ww7yjp0Fzw', "Facts You Never Could Have Guessed Were True 👀"],
    ['https://www.youtube.com/shorts/UmKpmP0Hhu0', "Facts That Will Save Your Life 👀"],
    ['https://www.youtube.com/shorts/wb7hHjfT3OY', "Bizarre Facts That Will Shock You 👀"],
    ['https://www.youtube.com/shorts/RnLeEjF_8U4', "Random Facts That Could Save Your Life 👀"],
    ['https://www.youtube.com/shorts/EKsnkZNPRiU', "Bizarre Facts You Didn't Know 👀"],
    ['https://www.youtube.com/shorts/XbdvjrbjrGE', "Facts That Can Save Your Life 👀"],
    ['https://www.youtube.com/shorts/0voNBg8r9xc', "Random Curiosities That Sound Fake 👀"],
    ['https://www.youtube.com/shorts/I1IgrkfG94Y', "Bizarre Facts You Didn't Know 👀"],
    ['https://www.youtube.com/shorts/2KZkEfGdfvE', "Random Facts To Save Your Life 👀"],
    ['https://www.youtube.com/shorts/MHOXtGbVgp4', "Terrifying Curiosities That May Scare You 👀"],
    ['https://www.youtube.com/shorts/oht1xoavyCs', "Random Curiosities About Love 👀"],
    ['https://www.youtube.com/shorts/WW5HJT_xV3w', "Random Facts That Will Scare You 👀"],
    ['https://www.youtube.com/shorts/9ZqRVY23pfs', "Random Curiosities That You Didn't Know 👀"],
    ['https://www.youtube.com/shorts/wC0NIVWWcZo', "Random Curiosities That Can Save Your Life👀"],
    ['https://www.youtube.com/shorts/PwFmPrRbUTc', "Random Curiosities That Will Scare You 👀"],
    ['https://www.youtube.com/shorts/gNek15jyAHU', "Random Curiosities That Might Scare You 👀"],
    ['https://www.youtube.com/shorts/rLR9GjNW2Do', "Shower Thoughts To Shock You 👀"],
    ['https://www.youtube.com/shorts/-NxLmfuaZtc', "Random Facts That Can Save Your Life 👀"],
    ['https://www.youtube.com/shorts/iMsff76n7Ag', "Random Facts That Are Going to Shock You 36 👀"],
    ['https://www.youtube.com/shorts/d5gs6laeNZQ', "Random Curiosities That Will Scare You 👀 #funfact"],
    ['https://www.youtube.com/shorts/hPewmVzM2S8', "Random Facts To Shock You 35 👀"],
    ['https://www.youtube.com/shorts/8YpoDdzh_b8', "Random Facts To Shock You 34 👀"],
    ['https://www.youtube.com/shorts/_4YpJDjRkLQ', "Random Facts That Could Save Your Life 👀"],
    ['https://www.youtube.com/shorts/Szqx4XwiLAA', "Random Facts That Will Shock You 33 👀"],
    ['https://www.youtube.com/shorts/KDJJpS7X5bc', "Random Facts To Shock You 32 👀"],
    ['https://www.youtube.com/shorts/mbkSQuxRnA0', "Random Facts That Will Shock You 31 👀"],
    ['https://www.youtube.com/shorts/JqHEGMtokYI', "Facts That Can SAVE Your Life 👀"],
    ['https://www.youtube.com/shorts/NGS-xmrFuxw', "Random Facts That Surprised Me 30 👀"],
    ['https://www.youtube.com/shorts/Nr4BGgcDhwA', "Random Facts To Shock You 29 👀"],
    ['https://www.youtube.com/shorts/lPMHZHzA7jg', "Random Facts That Could Save Your Life 👀"],
    ['https://www.youtube.com/shorts/sHb5_GBVj_0', "Random Facts To Shock You 28 👀"],
    ['https://www.youtube.com/shorts/TNJzlBKXGNM', "Random Facts To Shock You 27👀"],
    ['https://www.youtube.com/shorts/or9kIoErZIE', "Random Facts To Shock You 26 👀"],
    ['https://www.youtube.com/shorts/0EybXGojTF0', "Random Facts To Shock You 25 👀"],
    ['https://www.youtube.com/shorts/x0-3CRO_Qjc', "Random Facts To Shock You 24 👀"],
    ['https://www.youtube.com/shorts/A-S_XTvK3Xs', "Random Facts To Shock You 23 👀"],
    ['https://www.youtube.com/shorts/7FDzAwl2xT8', "Random Facts To Surprise You 22 👀"],
    ['https://www.youtube.com/shorts/A6BzPESSWjE', "Random Facts To Shock You 21 👀"],
    ['https://www.youtube.com/shorts/vhM5RlvDPms', "Random Facts To Surprise You 20 👀"],
    ['https://www.youtube.com/shorts/KOvZOQr6EYY', "Random Facts To Shock You 19 👀"],
    ['https://www.youtube.com/shorts/S_qWKGzbO5E', "Random Facts You Didn't Know 18 👀"],
    ['https://www.youtube.com/shorts/jgxMWMZadFs', "Random Facts You Didn't Know 17 👀"],
    ['https://www.youtube.com/shorts/OAG59ElFk0o', "Facts That Will EXPOSE You 👀"],
    ['https://www.youtube.com/shorts/DC1b18BD6_w', "Random Facts You Didn't Know 16"],
    ['https://www.youtube.com/shorts/JnoNDxseaeE', "Random Facts You Don't Know 15"],
    ['https://www.youtube.com/shorts/0Mz2fqwCb-8', "Random Facts You Didn't Know 14"],
    ['https://www.youtube.com/shorts/J9yGsD4FZq4', "Random Facts You Didn't Know 13"],
    ['https://www.youtube.com/shorts/tFD-O7-dh5U', "Random Facts You Didn't Know 12"],
    ['https://www.youtube.com/shorts/qUy_d2qQ1Ds', "Put A Finger Down: Weird Edition"],
    ['https://www.youtube.com/shorts/ZQZtm2wg-rk', "Random Facts You Didn't Know 11"],
    ['https://www.youtube.com/shorts/kkxahfat3nU', "Put A Finger Down: Attractive Edition"],
    ['https://www.youtube.com/shorts/k9WRNM962zk', "Random Facts You Didn't Know pt.10"],
    ['https://www.youtube.com/shorts/dA2qXi_9rsk', "Random Facts You Didn't Know 9"],
    ['https://www.youtube.com/shorts/5jKSwOVi5g8', "Fun Facts You Didn't Know pt.8"],
    ['https://www.youtube.com/shorts/h7hovfjljKM', "I Didn't Know The Fourth #funfact"],
    ['https://www.youtube.com/shorts/kg8kzOYWxyk', "You Didn't Know The Last #funfact"],
    ['https://www.youtube.com/shorts/PlSVcKuJXY4', "I Didn't Know The Fourth Fact"],
    ['https://www.youtube.com/shorts/qCGsTVfv4Us', "The Last One Is The Most Shocking!"],
    ['https://www.youtube.com/shorts/HKp49z5xdNk', "Nobody Knew The Last One!"],
    ['https://www.youtube.com/shorts/oPrjzH4nRNg', "Signs a boy is losing feelings for you #facts"],
    ['https://www.youtube.com/shorts/UjujJk5wJQE', "How to make a boy have a crush on you #facts"],
    ['https://www.youtube.com/shorts/Bhx5kA8S2tc', "Random facts about boys part 4 #facts"],
    ['https://www.youtube.com/shorts/fOhVBfKcMvI', "Exposing the boys again #facts"],
    ['https://www.youtube.com/shorts/fxyIgYc-kiE', "Things That Boys Do When They Have A Crush"],
    ['https://www.youtube.com/shorts/uC51cdl6yW8', "Things girls wish boys knew #facts"],
    ['https://www.youtube.com/shorts/XDOpkQa2gVE', "Exposing the girls again #facts"],
    ['https://www.youtube.com/shorts/PV70oFXgatE', "Random facts about boys #facts"],
    ['https://www.youtube.com/shorts/Jo0wEaXspDo', "You have a strong friendship #facts"],
    ['https://www.youtube.com/shorts/vHR3R3-0xdw', "Are you attractive? #facts"],
    ['https://www.youtube.com/shorts/qJHEYN3_ECI', "Random facts about girls pt 2 #facts"],
    ['https://www.youtube.com/shorts/qY12TxlIgjQ', "How to know if a boy is flirting with you #facts"],
    ['https://www.youtube.com/shorts/GkMugH66LVk', "Signs she's losing interest #facts"],
    ['https://www.youtube.com/shorts/82d9vH_XJZg', "Signs He's losing interest #facts"],
    ['https://www.youtube.com/shorts/AbYpPAAHr6Y', "Exposing girls for you boys #facts"],
    ['https://www.youtube.com/shorts/mer1XChr8Qs', "Exposing boys for you girls  #facts"],
    ['https://www.youtube.com/shorts/gvCVnuYi-Qg', "What girls wish boys knew #facts"],
    ['https://www.youtube.com/shorts/JHm2QqqwGuQ', "What boys wish girls knew #facts"],
    ['https://www.youtube.com/shorts/1WzEiUpB6eE', "how to make a girl fall in love #facts"],
    ['https://www.youtube.com/shorts/Oq0htRhaw4w', "What girls love but won't admit"],
    ['https://www.youtube.com/shorts/8YbE_CXa6gI', "What boys love but won't admit"],
    ['https://www.youtube.com/shorts/luRZCrXtbe8', "Signs she likes you"],
    ['https://www.youtube.com/shorts/Fwsg_HQ3brY', "Signs he likes you  #facts"],
    ['https://www.youtube.com/shorts/Pi62KS9PgLw', "Random facts about girls part 3"],
    ['https://www.youtube.com/shorts/9gN_8DHeGoI', "Random facts about hugs"],
    ['https://www.youtube.com/shorts/jpH428Yxv5U', "Random facts about boys"],
    ['https://www.youtube.com/shorts/gwDx0Ue16eY', "How to make a boy obsessed"],
    ['https://www.youtube.com/shorts/89datd0x7nc', "Facts about crushes #facts"],
    ['https://www.youtube.com/shorts/5yH0XBggc5E', "Facts about love"],
    ['https://www.youtube.com/shorts/OaMP7eB14dI', "He likes you?"],
    ['https://www.youtube.com/shorts/ACTqJee8S4A', "Random facts about girls"],
    ['https://www.youtube.com/shorts/JEVY_BAGV1s', "Girls facts"],
    ['https://www.youtube.com/shorts/Y8O9-dRk0bM', "She likes you?"],
    ['https://www.youtube.com/shorts/gJa7SATcmwQ', "Random facts about girls"],
    ['https://www.youtube.com/shorts/N-zU50cv8Ls', "Random Facts You Didn't Know... #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/oGtH_LKVu_Y', "5 Disturbing Facts You Need to Know... #shorts #facts"],
    ['https://www.youtube.com/shorts/UAdDYvRMdhY', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/K1urYwoLqbs', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/xZ_W_RyGCYs', "Interesting Facts To Cure Boredom... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/g0lT-FmKoFo', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/lClpMQIN5mU', "Crazy Facts You Didn't know... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/ToUh07k99Xw', "Random Facts... #shorts #randomfacts #facts"],
    ['https://www.youtube.com/shorts/N9Et5Ul2Vsc', "Crazy Facts You Didn't Know! #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/FYQ7R9cltMw', "Crazy Shower Thoughts... #shorts #showerthoughts"],
    ['https://www.youtube.com/shorts/76BU8jmHxjQ', "Facts That Will Save Your Life😱 #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/Syw6JYzhTJc', "The Hole Never Ends... #shorts"],
    ['https://www.youtube.com/shorts/MOfTG566Bgs', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/uaB2lX9nsZM', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/qaC9e3Q7B9E', "Random Facts You Didn't Know... #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/AL97LW5L0Fo', "Facts That Will Save Your Life... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/57iViiJbZY8', "Insane Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/TaC_Esvm2Dg', "Random Facts... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/EUcl2_dfMIM', "Mind-Blowing Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/cSul-prpQLA', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/YpQFGLrSWB8', "Random Facts You Need To know... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/tam0dqBdNI0', "Random Curiosities That Hit Hard... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/620760MQ6YI', "Shocking Facts You Didn't Know! #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/pb42sqqGqyE', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/yOqbGlFz3wk', "Shower Thoughts That Will Blow Your Mind! #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/kEY0jTVox0A', "Random Facts You Didn't Know... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/DGjeFyx4Dqg', "Shower Thoughts Your Mum Told Me... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/2fcRb1603lA', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/61qqSTHfMQU', "Shower Thoughts That Will Blow Your Mind... #shorts #thoughts #showerthoughts"],
    ['https://www.youtube.com/shorts/YiFYcZDiK5Y', "Cute Facts To Make Your Day... #shorts"],
    ['https://www.youtube.com/shorts/ADNBd_zNYe8', "Random Thoughts You Didn't Know... #shorts #facts #thoughts"],
    ['https://www.youtube.com/shorts/c_FUP9zzoaQ', "Insane Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/9ECPEzxY0U4', "Random Facts You Didn't Know... #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/IViikNDu9aY', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/p4Ln4JX0Kfk', "Random Curiosities... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/irG_Gle5AuM', "Random Facts #shorts #factshorts #interestingfacts"],
    ['https://www.youtube.com/shorts/eQrYLDogUIE', "Mind Blowing Shower Thoughts... #shorts #facts #showerthoughts"],
    ['https://www.youtube.com/shorts/O6BC4YGlmwU', "Mind-Blowing Shower Thoughts... #shorts #facts #showerthoughts"],
    ['https://www.youtube.com/shorts/a7kB-oUEsHg', "Disney Thoughts That Will Blow Your Mind... #shorts #disney  #showerthoughts"],
    ['https://www.youtube.com/shorts/2LeSYXREe2w', "Random Facts You Didn't know... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/9uIr6arA2mM', "Facts That Will Save Your Life... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/qc-bR1aZH5A', "Random Curiosities You Didn't Know... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/AdBfPHyuhwM', "Facts That Will Save Your Life...😱 #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/J8tqAMecxqs', "Random Facts to Creep You Out... #shorts #facts #scary"],
    ['https://www.youtube.com/shorts/nQnjNv3FKog', "Random Curiosities... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/QJj93WA34mw', "Facts That Will Give You Chills..."],
    ['https://www.youtube.com/shorts/tedUegx-FVA', "Mind-Blowing Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/kn7tjg1h-3M', "Random Curiosities... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/NP7DD2wEp18', "Facts That Will Save Your Life😱 #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/o0xg5CpUElU', "Random Facts You Didn't know..."],
    ['https://www.youtube.com/shorts/DlpdTryvpv0', "Random facts #short #interestingfacts #factshorts"],
    ['https://www.youtube.com/shorts/TQtKuSmG8Yk', "Stupid Things You Just Realised... #shorts #facts #entertainment"],
    ['https://www.youtube.com/shorts/7pesWSGl8sE', "Facts That Will Scare You... #scary #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/l_drDVA62vs', "Animal Facts That Will Make Your Day! #shorts #facts #animals"],
    ['https://www.youtube.com/shorts/Rvc927Sy118', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/oJsRQ9RvlQY', "Random Facts You Didn't Know.. #shorts #randomfacts #factshorts"],
    ['https://www.youtube.com/shorts/UJFSFyktOjg', "Weird Animal Facts That Will Blow Your Mind... #shorts #animals #facts"],
    ['https://www.youtube.com/shorts/pmw8InYWzFw', "Random Facts You Didn't Know.. #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/KbOLEbovPO8', "Positive Facts! #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/tod75haW70E', "Random Facts To Creep You Out... #scary #facts #scary"],
    ['https://www.youtube.com/shorts/nIssyh_50-Q', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/sHOv2Y6Gx8g', "Crazy Laws You Never Knew! 😱 #shorts #factshorts #facts"],
    ['https://www.youtube.com/shorts/L9nyGXAOwUA', "Random Facts You Didn't Know.. #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/54kBIe_Bq6M', "Random Facts You Didn't Know.. #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/CnTj1zQmbj0', "Random Thoughts #shorts #randomfacts #facts"],
    ['https://www.youtube.com/shorts/PLcDZSqi18U', "Random Facts You Didn't Know.. #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/NJyXFculix8', "Facts You Didn't Know... #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/lKdSPJrYZ1U', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts"],
    ['https://www.youtube.com/shorts/JinZLcCCpdQ', "Random Facts You Didn't Know.. #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/Cn4Oj134tsM', "TikTok Shower Thoughts #shorts #randomfacts #facts"],
    ['https://www.youtube.com/shorts/meEDLiJtCp4', "Scary Mind-Blowing Facts  #facts #shorts #scaryfacts"],
    ['https://www.youtube.com/shorts/219Y5KBgDaM', "Mind-Blowing Facts🤯 #shorts #facts"],
    ['https://www.youtube.com/shorts/BQmMJyvDBgk', "Stupid Things You Just Realised..."],
    ['https://www.youtube.com/shorts/Cxq0OAiNP4Y', "Facts That Will Make You Less Stupid #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/QeuwvmQTbZY', "Facts You Didn't know... #shorts #facts"],
    ['https://www.youtube.com/shorts/uBe2FH1IU5A', "Random Facts #shorts #facts"],
    ['https://www.youtube.com/shorts/6ft94FGHOM8', "Facts That Could Save Your Life #shorts #factshorts #facts"],
    ['https://www.youtube.com/shorts/4CVWIfzfmCA', "Random Curiosities #shorts #randomfacts"],
    ['https://www.youtube.com/shorts/1fEXqv7FkrU', "Facts That Will Save Your Life😱 #shorts #facts"],
    ['https://www.youtube.com/shorts/Qp7WlFexVLY', "Facts To Find Your Soulmate #shorts #love #facts"],
    ['https://www.youtube.com/shorts/dd-sbz7VM0A', "Interesting Facts You Didn’t Know… #shorts #facts"],
    ['https://www.youtube.com/shorts/CtISySXGfec', "This Video Will Save Your Life #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/DCN-eYc-qpk', "This Video Will Save Your Life #shorts #factshorts #facts"],
    ['https://www.youtube.com/shorts/nlVQWTs71AI', "Random Thoughts #shorts #thoughts #interestingfacts"],
    ['https://www.youtube.com/shorts/VBe0yA2RLBk', "Scary facts That  Will Blow Your Mind! #facts #shorts #scaryfacts"],
    ['https://www.youtube.com/shorts/z_oFC8Am2LY', "Random Facts You Didn’t Know… #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/1TU_F0fMe-4', "Shower Thoughts to Cure Boredom (pt.1)  #shorts #interestingfacts #thoughts"],
    ['https://www.youtube.com/shorts/FL7KVNBs1Oo', "Facts You Didn’t Know… #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/m-YMVjJI8X8', "Facts That Leave You Speechless #shorts #interestingfacts #facts"],
    ['https://www.youtube.com/shorts/oSbxZ61pqYw', "This Video Can Save Your Life!😳 #shorts #facts #factshorts"],
    ['https://www.youtube.com/shorts/dvamNxd7h9A', "Interesting Facts You've Never Heard… #shorts #facts #interestingfacts"],
    ['https://www.youtube.com/shorts/8p4yrrTsqjY', "Interesting Facts #shorts #facts"],

]
#fmt: on

DATA_DIR = "./yshorts/data"
AUDIO_DIR = "./yshorts/audio"
TEMP_DIR = "./yshorts/temp"
DEVICE = "cpu"
BATCH_SIZE = 16  # reduce if low on GPU mem
# change to "int8" if low on GPU mem (may reduce accuracy)
COMPUTE_TYPE = "float16"
MODEL_NAME = 'tiny'
console.log(f"loading whisperx {MODEL_NAME} model...")
model = whisperx.load_model(MODEL_NAME, DEVICE, compute_type=COMPUTE_TYPE)
model_a, metadata = whisperx.load_align_model(
    language_code='en', device=DEVICE)


def download_audio_one(url, ydl):
    if not os.path.exists(f"{AUDIO_DIR}/{url.split('/')[-1]}.wav"):
        ydl.download([url])
        ffmpeg_cmd = f"ffmpeg -i {TEMP_DIR}/{url.split('/')[-1]}.webm -ac 1 -ar 16000 {AUDIO_DIR}/{url.split('/')[-1]}.wav"
        output = subprocess.run(
            ffmpeg_cmd.split(" "), capture_output=True)
        assert output.returncode == 0, f"ffmpeg failed: {output.stderr}"
        os.remove(f"{TEMP_DIR}/{url.split('/')[-1]}.webm")
        console.log(f"[medium_purple3]downloaded {url}")
    else:
        console.log(f"[green]exists: {url}")


def download_threaded(urls, ydl, adv, n_threads=8):
    q = Queue()

    def worker():
        while True:
            url = q.get()
            try:
                download_audio_one(url, ydl)
                adv()
            finally:
                q.task_done()

    for i in range(n_threads):
        t = Thread(target=worker)
        t.daemon = True
        t.start()

    for url in urls:
        q.put(url[0])

    q.join()


def main():
    # download with yt-dlp
    # convert to wav 16khz mono
    # transcribe with whisperx
    # save to ./shorts/data/<video_id>.json
    # save to ./shorts/audio/<video_id>.wav
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(AUDIO_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestaudio',
        'outtmpl': f"{TEMP_DIR}/%(id)s.%(ext)s",
        'quiet': True,
        'no_warnings': True,
        'noprogress': True,
    })

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("Downloading videos", total=len(videos))

        # for url, title in videos:
        #     if not os.path.exists(f"{AUDIO_DIR}/{url.split('/')[-1]}.wav"):
        #         ydl.download([url])
        #         ffmpeg_cmd = f"ffmpeg -i {TEMP_DIR}/{url.split('/')[-1]}.webm -ac 1 -ar 16000 {AUDIO_DIR}/{url.split('/')[-1]}.wav"
        #         output = subprocess.run(
        #             ffmpeg_cmd.split(" "), capture_output=True)
        #         assert output.returncode == 0, f"ffmpeg failed: {output.stderr}"
        #         os.remove(f"{TEMP_DIR}/{url.split('/')[-1]}.webm")
        #     progress.advance(task)
        def adv():
            progress.advance(task)
        download_threaded(videos, ydl, adv)

        task = progress.add_task("Transcribing videos", total=len(videos))
        for url, title in videos:
            if not os.path.exists(f"{DATA_DIR}/{url.split('/')[-1]}.json"):
                audio = whisperx.load_audio(
                    f"{AUDIO_DIR}/{url.split('/')[-1]}.wav")
                result = model.transcribe(
                    audio, batch_size=BATCH_SIZE, language='en')
                # print(result["segments"])  # before alignment
                result = whisperx.align(
                    result["segments"], model_a, metadata, audio, DEVICE, return_char_alignments=False)
                segs = result['segments']
                ass_content = write_ass(segs)
                print(f"\n\n\n# {title} #\n{ass_content}")
                data = {
                    'transcribe': result,
                    'ass': ass_content,
                    'url': url,
                    'title': title,
                }

                with open(f'{DATA_DIR}/{url.split("/")[-1]}.json', 'w') as f:
                    f.write(json.dumps(data))
            progress.advance(task)


if __name__ == "__main__":
    main()

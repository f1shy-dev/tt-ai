from threading import Thread
from ttai_farm.v4.write_ass import write_adv_substation_alpha
from queue import Queue
import whisperx
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import os
import yt_dlp
import subprocess
import json
from rich.console import Console
console = Console()


def status(x, **kwargs):
    return console.status(x, spinner='dots2', **kwargs)


#fmt: off
videos = [
    ['https://www.youtube.com/shorts/YKplhwnlS-0', "Random Fun Facts 👀", "13K views"],
['https://www.youtube.com/shorts/RUDHPCab0uw', "Random Interesting Facts 👀", "85K views"],
['https://www.youtube.com/shorts/sNMSXARzub8', "Random Shocking Facts 👀", "186K views"],
['https://www.youtube.com/shorts/pEN42WHePzU', "Random Not So Fun Facts 👀", "383K views"],
['https://www.youtube.com/shorts/Dq8gljHeeXA', "Random Facts You Never Knew 👀", "250K views"],
['https://www.youtube.com/shorts/i3f4fF-wyN0', "Random Facts You Didn't Know👀", "256K views"],
['https://www.youtube.com/shorts/1kK7mJa_R6Q', "Random Facts That Will SHOCK You 👀", "175K views"],
['https://www.youtube.com/shorts/RBHsIEKhOW4', "Random Facts To SCARE You 👀", "123K views"],
['https://www.youtube.com/shorts/USfRLvBFC08', "Random Facts To SHOCK You 👀", "284K views"],
['https://www.youtube.com/shorts/UwsN3kZCUZ4', "Random Facts To SURPRISE You 👀", "1M views"],
['https://www.youtube.com/shorts/o4f0WKXoHLs', "Random Facts To SHOCK You 👀", "654K views"],
['https://www.youtube.com/shorts/Fk837soi1Vo', "Random Facts To RETHINK Your Life 👀", "206K views"],
['https://www.youtube.com/shorts/2sBMjqEYyrg', "Random Facts To HORRIFY You 👀", "647K views"],
['https://www.youtube.com/shorts/EFW-BTYC45M', "Random Facts To TERRIFY You 👀", "742K views"],
['https://www.youtube.com/shorts/iJ5lI2E1Ex8', "Random Facts To BLOW Your Mind 👀", "242K views"],
['https://www.youtube.com/shorts/9tK0sy8lRSo', "Facts That Could Potentially SAVE Your Life 👀", "443K views"],
['https://www.youtube.com/shorts/hhfjXBgsxIA', "Shower Thoughts That Will Make You Think Twice 👀", "877K views"],
['https://www.youtube.com/shorts/Bh7P0jUwKH8', "Facts That Can Save Your Life 👀", "333K views"],
['https://www.youtube.com/shorts/OAogPGfly6E', "Shower Thoughts That May Scare You 👀", "718K views"],
['https://www.youtube.com/shorts/FyIoZnfUit0', "Tips That Can Save Your Life 👀", "520K views"],
['https://www.youtube.com/shorts/I-QUUaGhmbI', "Shower Thoughts That Will Terrify You 👀", "406K views"],
['https://www.youtube.com/shorts/d9qQF31wPXk', "Random Facts That Can Save Your Life👀", "121K views"],
['https://www.youtube.com/shorts/1ww7yjp0Fzw', "Facts You Never Could Have Guessed Were True 👀", "306K views"],
['https://www.youtube.com/shorts/UmKpmP0Hhu0', "Facts That Will Save Your Life 👀", "700K views"],
['https://www.youtube.com/shorts/wb7hHjfT3OY', "Bizarre Facts That Will Shock You 👀", "648K views"],
['https://www.youtube.com/shorts/RnLeEjF_8U4', "Random Facts That Could Save Your Life 👀", "3.4M views"],
['https://www.youtube.com/shorts/EKsnkZNPRiU', "Bizarre Facts You Didn't Know 👀", "431K views"],
['https://www.youtube.com/shorts/XbdvjrbjrGE', "Facts That Can Save Your Life 👀", "1.5M views"],
['https://www.youtube.com/shorts/0voNBg8r9xc', "Random Curiosities That Sound Fake 👀", "564K views"],
['https://www.youtube.com/shorts/I1IgrkfG94Y', "Bizarre Facts You Didn't Know 👀", "829K views"],
['https://www.youtube.com/shorts/2KZkEfGdfvE', "Random Facts To Save Your Life 👀", "2.1M views"],
['https://www.youtube.com/shorts/MHOXtGbVgp4', "Terrifying Curiosities That May Scare You 👀", "1.2M views"],
['https://www.youtube.com/shorts/oht1xoavyCs', "Random Curiosities About Love 👀", "235K views"],
['https://www.youtube.com/shorts/WW5HJT_xV3w', "Random Facts That Will Scare You 👀", "2.6M views"],
['https://www.youtube.com/shorts/9ZqRVY23pfs', "Random Curiosities That You Didn't Know 👀", "1M views"],
['https://www.youtube.com/shorts/wC0NIVWWcZo', "Random Curiosities That Can Save Your Life👀", "1.5M views"],
['https://www.youtube.com/shorts/PwFmPrRbUTc', "Random Curiosities That Will Scare You 👀", "705K views"],
['https://www.youtube.com/shorts/gNek15jyAHU', "Random Curiosities That Might Scare You 👀", "2.7M views"],
['https://www.youtube.com/shorts/rLR9GjNW2Do', "Shower Thoughts To Shock You 👀", "1.1M views"],
['https://www.youtube.com/shorts/-NxLmfuaZtc', "Random Facts That Can Save Your Life 👀", "8.1M views"],
['https://www.youtube.com/shorts/iMsff76n7Ag', "Random Facts That Are Going to Shock You 36 👀", "1M views"],
['https://www.youtube.com/shorts/d5gs6laeNZQ', "Random Curiosities That Will Scare You 👀 #funfact", "1.1M views"],
['https://www.youtube.com/shorts/hPewmVzM2S8', "Random Facts To Shock You 35 👀", "584K views"],
['https://www.youtube.com/shorts/8YpoDdzh_b8', "Random Facts To Shock You 34 👀", "2.3M views"],
['https://www.youtube.com/shorts/_4YpJDjRkLQ', "Random Facts That Could Save Your Life 👀", "2.6M views"],
['https://www.youtube.com/shorts/Szqx4XwiLAA', "Random Facts That Will Shock You 33 👀", "980K views"],
['https://www.youtube.com/shorts/KDJJpS7X5bc', "Random Facts To Shock You 32 👀", "697K views"],
['https://www.youtube.com/shorts/mbkSQuxRnA0', "Random Facts That Will Shock You 31 👀", "953K views"],
['https://www.youtube.com/shorts/JqHEGMtokYI', "Facts That Can SAVE Your Life 👀", "3.1M views"],
['https://www.youtube.com/shorts/NGS-xmrFuxw', "Random Facts That Surprised Me 30 👀", "3.6M views"],
['https://www.youtube.com/shorts/Nr4BGgcDhwA', "Random Facts To Shock You 29 👀", "793K views"],
['https://www.youtube.com/shorts/lPMHZHzA7jg', "Random Facts That Could Save Your Life 👀", "4.1M views"],
['https://www.youtube.com/shorts/sHb5_GBVj_0', "Random Facts To Shock You 28 👀", "5.6M views"],
['https://www.youtube.com/shorts/TNJzlBKXGNM', "Random Facts To Shock You 27👀", "2M views"],
['https://www.youtube.com/shorts/or9kIoErZIE', "Random Facts To Shock You 26 👀", "582K views"],
['https://www.youtube.com/shorts/0EybXGojTF0', "Random Facts To Shock You 25 👀", "1.2M views"],
['https://www.youtube.com/shorts/x0-3CRO_Qjc', "Random Facts To Shock You 24 👀", "635K views"],
['https://www.youtube.com/shorts/A-S_XTvK3Xs', "Random Facts To Shock You 23 👀", "410K views"],
['https://www.youtube.com/shorts/7FDzAwl2xT8', "Random Facts To Surprise You 22 👀", "1.9M views"],
['https://www.youtube.com/shorts/A6BzPESSWjE', "Random Facts To Shock You 21 👀", "817K views"],
['https://www.youtube.com/shorts/vhM5RlvDPms', "Random Facts To Surprise You 20 👀", "2.1M views"],
['https://www.youtube.com/shorts/KOvZOQr6EYY', "Random Facts To Shock You 19 👀", "4.6M views"],
['https://www.youtube.com/shorts/S_qWKGzbO5E', "Random Facts You Didn't Know 18 👀", "830K views"],
['https://www.youtube.com/shorts/jgxMWMZadFs', "Random Facts You Didn't Know 17 👀", "217K views"],
['https://www.youtube.com/shorts/OAG59ElFk0o', "Facts That Will EXPOSE You 👀", "451K views"],
['https://www.youtube.com/shorts/DC1b18BD6_w', "Random Facts You Didn't Know 16", "409K views"],
['https://www.youtube.com/shorts/JnoNDxseaeE', "Random Facts You Don't Know 15", "1.3M views"],
['https://www.youtube.com/shorts/0Mz2fqwCb-8', "Random Facts You Didn't Know 14", "6.4M views"],
['https://www.youtube.com/shorts/J9yGsD4FZq4', "Random Facts You Didn't Know 13", "2.6M views"],
['https://www.youtube.com/shorts/tFD-O7-dh5U', "Random Facts You Didn't Know 12", "243K views"],
['https://www.youtube.com/shorts/qUy_d2qQ1Ds', "Put A Finger Down: Weird Edition", "296K views"],
['https://www.youtube.com/shorts/ZQZtm2wg-rk', "Random Facts You Didn't Know 11", "1.7M views"],
['https://www.youtube.com/shorts/kkxahfat3nU', "Put A Finger Down: Attractive Edition", "796K views"],
['https://www.youtube.com/shorts/k9WRNM962zk', "Random Facts You Didn't Know pt.10", "175K views"],
['https://www.youtube.com/shorts/dA2qXi_9rsk', "Random Facts You Didn't Know 9", "1.1M views"],
['https://www.youtube.com/shorts/5jKSwOVi5g8', "Fun Facts You Didn't Know pt.8", "4M views"],
['https://www.youtube.com/shorts/h7hovfjljKM', "I Didn't Know The Fourth #funfact", "350K views"],
['https://www.youtube.com/shorts/kg8kzOYWxyk', "You Didn't Know The Last #funfact", "320K views"],
['https://www.youtube.com/shorts/PlSVcKuJXY4', "I Didn't Know The Fourth Fact", "2.1M views"],
['https://www.youtube.com/shorts/qCGsTVfv4Us', "The Last One Is The Most Shocking!", "9.4M views"],
['https://www.youtube.com/shorts/HKp49z5xdNk', "Nobody Knew The Last One!", "2.1M views"],


['https://www.youtube.com/shorts/o-sQ03fxlTI', "What boys wish girls knew #facts", "13K views"],
['https://www.youtube.com/shorts/EbjgwyXrytc', "Are these true girls #facts", "81K views"],
['https://www.youtube.com/shorts/DbrNeabXO8o', "Random facts about crushes #facts", "49K views"],
['https://www.youtube.com/shorts/oPrjzH4nRNg', "Signs a boy is losing feelings for you #facts", "48K views"],
['https://www.youtube.com/shorts/UjujJk5wJQE', "How to make a boy have a crush on you #facts", "22K views"],
['https://www.youtube.com/shorts/Bhx5kA8S2tc', "Random facts about boys part 4 #facts", "114K views"],
['https://www.youtube.com/shorts/fOhVBfKcMvI', "Exposing the boys again #facts", "144K views"],
['https://www.youtube.com/shorts/fxyIgYc-kiE', "Things That Boys Do When They Have A Crush", "54K views"],
['https://www.youtube.com/shorts/uC51cdl6yW8', "Things girls wish boys knew #facts", "82K views"],
['https://www.youtube.com/shorts/XDOpkQa2gVE', "Exposing the girls again #facts", "138K views"],
['https://www.youtube.com/shorts/PV70oFXgatE', "Random facts about boys #facts", "107K views"],
['https://www.youtube.com/shorts/Jo0wEaXspDo', "You have a strong friendship #facts", "41K views"],
['https://www.youtube.com/shorts/vHR3R3-0xdw', "Are you attractive? #facts", "40K views"],
['https://www.youtube.com/shorts/qJHEYN3_ECI', "Random facts about girls pt 2 #facts", "148K views"],
['https://www.youtube.com/shorts/qY12TxlIgjQ', "How to know if a boy is flirting with you #facts", "121K views"],
['https://www.youtube.com/shorts/GkMugH66LVk', "Signs she's losing interest #facts", "67K views"],
['https://www.youtube.com/shorts/82d9vH_XJZg', "Signs He's losing interest #facts", "99K views"],
['https://www.youtube.com/shorts/AbYpPAAHr6Y', "Exposing girls for you boys #facts", "292K views"],
['https://www.youtube.com/shorts/mer1XChr8Qs', "Exposing boys for you girls  #facts", "137K views"],
['https://www.youtube.com/shorts/gvCVnuYi-Qg', "What girls wish boys knew #facts", "215K views"],
['https://www.youtube.com/shorts/JHm2QqqwGuQ', "What boys wish girls knew #facts", "156K views"],
['https://www.youtube.com/shorts/1WzEiUpB6eE', "how to make a girl fall in love #facts", "143K views"],
['https://www.youtube.com/shorts/Oq0htRhaw4w', "What girls love but won't admit", "533K views"],
['https://www.youtube.com/shorts/8YbE_CXa6gI', "What boys love but won't admit", "103K views"],
['https://www.youtube.com/shorts/luRZCrXtbe8', "Signs she likes you", "156K views"],
['https://www.youtube.com/shorts/Fwsg_HQ3brY', "Signs he likes you  #facts", "219K views"],
['https://www.youtube.com/shorts/Pi62KS9PgLw', "Random facts about girls part 3", "126K views"],
['https://www.youtube.com/shorts/9gN_8DHeGoI', "Random facts about hugs", "42K views"],
['https://www.youtube.com/shorts/jpH428Yxv5U', "Random facts about boys", "325K views"],
['https://www.youtube.com/shorts/gwDx0Ue16eY', "How to make a boy obsessed", "120K views"],
['https://www.youtube.com/shorts/89datd0x7nc', "Facts about crushes #facts", "229K views"],
['https://www.youtube.com/shorts/5yH0XBggc5E', "Facts about love", "133K views"],
['https://www.youtube.com/shorts/OaMP7eB14dI', "He likes you?", "538K views"],
['https://www.youtube.com/shorts/ACTqJee8S4A', "Random facts about girls", "86K views"],
['https://www.youtube.com/shorts/JEVY_BAGV1s', "Girls facts", "121K views"],
['https://www.youtube.com/shorts/Y8O9-dRk0bM', "She likes you?", "88K views"],
['https://www.youtube.com/shorts/gJa7SATcmwQ', "Random facts about girls", "3.9M views"],


    ['https://www.youtube.com/shorts/556vN8UQPeo', "🤯Shower thoughts that will blow your mind #16🤯 #showerthoughts #randomfacts #shorts", "4.8K views"],
['https://www.youtube.com/shorts/lmvmSj2ioJM', "🤯Shower thoughts that will blow your mind #15🤯 #showerthoughts #randomfacts #shorts", "17K views"],
['https://www.youtube.com/shorts/gkZHvvxZNyM', "🤯Shocking facts that sound fake but are 100% true #3🤯#shockingfacts  #randomfacts #shorts", "17K views"],
['https://www.youtube.com/shorts/AM4gs6U1Hqw', "🤯Shocking facts that sound fake but are 100% true #2🤯#shockingfacts  #randomfacts #shorts", "31K views"],
['https://www.youtube.com/shorts/k0skB4VCHe0', "😍Wholesome and incredible animal facts😍 #facts #randomfacts #shorts", "18K views"],
['https://www.youtube.com/shorts/X3lIlHM2wQ0', "Unbelievable Facts🤯 #facts #shorts #randomfacts", "16K views"],
['https://www.youtube.com/shorts/0b2G1IZAJ7U', "🤯Mind bending shower thoughts #15🤯 #showerthoughts #randomfacts #shorts", "47K views"],
['https://www.youtube.com/shorts/86iv6UDIUWg', "🤯Shower thoughts that will blow your mind #14🤯 #showerthoughts #randomfacts #shorts", "43K views"],
['https://www.youtube.com/shorts/eSd0_EVK-0w', "🤯Shower thoughts that will blow your mind #13🤯 #showerthoughts #randomfacts #shorts", "67K views"],
['https://www.youtube.com/shorts/_fwf54F7h30', "🤯Shower thoughts that will blow your mind #12🤯 #showerthoughts #randomfacts #shorts", "110K views"],
['https://www.youtube.com/shorts/cMYSfDHZJ5g', "😳Things you wouldn't admit on a first date😳 #fingerdown #shorts #truth", "50K views"],
['https://www.youtube.com/shorts/A5Qv0pymfwk', "🤯Are you smarter than average?🤯 #test #fingerdown #shorts", "36K views"],
['https://www.youtube.com/shorts/ikn3zr9Woas', "🤯Shower thoughts that will blow your mind #11🤯 #showerthoughts #randomfacts #shorts", "464K views"],
['https://www.youtube.com/shorts/F07FNvwkpZA', "🤯Shower thoughts that will blow your mind #10🤯 #showerthoughts #randomfacts #shorts", "115K views"],
['https://www.youtube.com/shorts/Az37LvnKWtk', "😳Things you would never admit #2😳 #putafingerdown #fingerdown #shorts", "126K views"],
['https://www.youtube.com/shorts/5sbZCI3EFu8', "🤯Shower thoughts that will blow your mind #9🤯 #showerthoughts #randomfacts #shorts", "105K views"],
['https://www.youtube.com/shorts/3W1PQc4hKs8', "🤯Shower thoughts that will blow your mind #8🤯 #showerthoughts #randomfacts #shorts", "549K views"],
['https://www.youtube.com/shorts/tebQd-nRDio', "🤯Shower thoughts that will blow your mind #7🤯 #showerthoughts #randomfacts #shorts", "693K views"],
['https://www.youtube.com/shorts/ZkPmJc9MiEQ', "🤯Comment how many fingers you put down🤯 #putafingerdown #fingerdown #shorts", "94K views"],
['https://www.youtube.com/shorts/1XLTp_CUz9I', "🤯Shower thoughts that will BLOW your mind #7🤯 #showerthoughts #randomfacts #shorts", "52K views"],
['https://www.youtube.com/shorts/bXe639pb2Gg', "🤯Shower thoughts that will BLOW your mind #6🤯 #showerthoughts #randomfacts #shorts", "57K views"],
['https://www.youtube.com/shorts/vRIXaYDB-cg', "🤯Shower thoughts that will blow your mind #5🤯 #showerthoughts #randomfacts #shorts", "110K views"],
['https://www.youtube.com/shorts/LBvzm3KBanQ', "🤯Shower thoughts that will blow your mind #5🤯 #showerthoughts #randomfacts #shorts", "111K views"],
['https://www.youtube.com/shorts/POsU9rkOgOM', "🤯Shower thoughts that will blow your mind #4🤯 #showerthoughts #randomfacts #shorts", "1.4M views"],
['https://www.youtube.com/shorts/sgWsQtX3HY0', "🤯SHOCKING facts that sound fake but are 100% true #3🤯#shockingfacts #randomfacts #shorts", "25K views"],
['https://www.youtube.com/shorts/cj202n5u_Dw', "🤯SHOCKING facts that sound fake but are 100% true #2🤯#shockingfacts #randomfacts #shorts", "172K views"],
['https://www.youtube.com/shorts/DJd733ElJLs', "🚨LIFE SAVING Facts #2... #facts #shorts #survivalfacts", "1.7M views"],
['https://www.youtube.com/shorts/jn9uT0VEzP4', "🔪Try and solve this murder mystery #riddle #mystery #shorts", "45K views"],
['https://www.youtube.com/shorts/fVyZ-xX3LNI', "😳MOST embarrassing moments!!😳 #awkwardmoments #awkwardfeeling #embarrassingmoments", "28K views"],
['https://www.youtube.com/shorts/egKlzocxbjI', "🤯Incredible true facts🤯#interestingfacts #randomfacts #shorts", "51K views"],
['https://www.youtube.com/shorts/FnztBNEzPwU', "🤯Shower thoughts that will blow your mind #4🤯 #showerthoughts #randomfacts #shorts", "86K views"],
['https://www.youtube.com/shorts/m0XpceljuY4', "🤯Shower thoughts that will blow your mind #3🤯 #showerthoughts #randomfacts #shorts", "2.1M views"],
['https://www.youtube.com/shorts/7Z5YecOhLhc', "🤯Shower thoughts that will blow your mind #2🤯 #showerthoughts #randomfacts #shorts", "33K views"],
['https://www.youtube.com/shorts/jmUpz0Dbwpc', "🤯Shocking facts that sound fake but are 100% true🤯#shockingfacts  #randomfacts #shorts", "251K views"],
['https://www.youtube.com/shorts/48KBBap38PM', "🤯 Shower thoughts that will blow your mind 🤯 #showerthoughts #randomfacts #shorts", "3.9M views"],
['https://www.youtube.com/shorts/r-W0dwk4riQ', "😳 Embarassing celebrity facts you didn’t know😳 #celebrityfacts #celebritysecrets #celebritytrivia", "68K views"],
['https://www.youtube.com/shorts/Iw8XaL3pTwU', "🤯Random facts I bet you didn’t know🤯 #facts #randomfacts #shorts", "13K views"],
['https://www.youtube.com/shorts/jy4JWxfno3M', "Facts You've Never Heard Before 🤯 #facts #shorts #randomfacts", "101K views"],
['https://www.youtube.com/shorts/tVxhW_zucYE', "Life Saving Facts... #facts #shorts #randomfacts", "284K views"],

['https://www.youtube.com/shorts/J3Au-FSJ3zw', "Random facts 🤯 #shorts #randomfacts", "1.9K views"],
['https://www.youtube.com/shorts/nGJ9LkHXavI', "Interesting facts 🤯 #shorts #randomfacts", "7.6K views"],
['https://www.youtube.com/shorts/QvRHcLOoMnA', "Shower thoughts 🤯 #shorts #randomfacts #showerthoughts", "4.5K views"],
['https://www.youtube.com/shorts/POeWwbBXBgc', "Random facts 🤯 #shorts #randomfacts", "4.8K views"],
['https://www.youtube.com/shorts/_PdhytpWZIs', "Crazy shower thoughts 🤯 #shorts #randomfacts #showerthoughts", "8.7K views"],
['https://www.youtube.com/shorts/8WTcRFqccVk', "Random curiosities 🤯 #shorts #randomfacts", "4.9K views"],
['https://www.youtube.com/shorts/kocfU0XEyqA', "Interesting facts 🤯 #shorts #interestingfacts", "5K views"],
['https://www.youtube.com/shorts/8CvlrAq1vSk', "Amazing facts 🤯 #shorts #randomfacts", "372 views"],
['https://www.youtube.com/shorts/mqJaG7iywj8', "Shower Thoughts! 🤯 #randomfacts #shorts", "2.3K views"],
['https://www.youtube.com/shorts/PFVwNDoLSp4', "Strange facts about WW2 #ww2 #shorts #randomfacts", "1.6K views"],
['https://www.youtube.com/shorts/21OugkMH5Jg', "Unraveling Autumn: Mind-Bending Fall Facts #funfact #shorts #fall", "1.8K views"],

['https://www.youtube.com/shorts/pqAMwwJq6Sg', "facts that could save your life #ramdomfacts #interestingfacts #facts #fyp #shorts", "2.5K views"],
['https://www.youtube.com/shorts/Zcf9BhYNoeQ', "#shorts #humor #funny #funnycomedy #funnyshorts #viral #jokes", "13K views"],
['https://www.youtube.com/shorts/4KefNXlpp1Y', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo", "7.1K views"],
['https://www.youtube.com/shorts/96245bRJe90', "Random Thoughts #shorts #fypシ #randomfacts #facts", "12K views"],
['https://www.youtube.com/shorts/5sxunPGS1Yg', "Put a finger down SMART Edition #viralvideo #shorts #fypシ #trendingshorts", "4.4K views"],
['https://www.youtube.com/shorts/ApZ8Buc7nV0', "Random Facts 🤯 #shorts #facts #ramdomfacts", "5.9K views"],
['https://www.youtube.com/shorts/Y7TFgTHQx_A', "Put a finger down Lazy Edition #viralvideo #shorts #fypシ #shortsviral #funshorts", "27K views"],
['https://www.youtube.com/shorts/Fip46zfbc4E', "Put a finger down Funny Edition #funnyshorts #shorts #funny #funnycomedy #fypシ", "27K views"],
['https://www.youtube.com/shorts/tLLXp8IWgU0', "random curiosities #shorts #randomfacts #facts #fyp", "6K views"],
['https://www.youtube.com/shorts/kc12XL0eN5I', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo #funfacts #dailyfacts", "6.8K views"],
['https://www.youtube.com/shorts/nJr-q_2RxlE', "random facts that could save your life #ramdomfacts #interestingfacts #facts #fyp #shorts", "14K views"],
['https://www.youtube.com/shorts/89deH2VUqrs', "Put a finger down bad Edition  #viralvideo #shorts #fypシ", "3.8K views"],
['https://www.youtube.com/shorts/2Th9a_0uxiM', "Put a finger down Depressed Edition #viralvideo #shorts #fypシ", "7.7K views"],
['https://www.youtube.com/shorts/J1lDz2nprBE', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo #funfacts #dailyfacts", "4.3K views"],
['https://www.youtube.com/shorts/-mJuxm6GcT0', "Put a finger down Rich Edition #viralvideo #shorts #fypシ", "23K views"],
['https://www.youtube.com/shorts/K1JFsKUzm9k', "random facts that could save your life #ramdomfacts #interestingfacts #facts #fyp #shorts", "3.5M views"],
['https://www.youtube.com/shorts/iH22zT_CnQg', "Put a finger down introvert Edition #viralvideo #shorts #fypシ #shortsviral", "8.2K views"],
['https://www.youtube.com/shorts/uWCtvskYSCA', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo #funfacts #dailyfacts", "4K views"],
['https://www.youtube.com/shorts/NtxK_e6NIgQ', "Put a finger down Extravert Edition #viralvideo #shorts #fypシ #shortsviral", "13K views"],
['https://www.youtube.com/shorts/gh90nwcXdkk', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo #funfacts #dailyfacts", "12K views"],
['https://www.youtube.com/shorts/m4pnqPerxIw', "facts that could save your life #ramdomfacts #interestingfacts #facts #fyp #shorts", "36K views"],
['https://www.youtube.com/shorts/AiVws51NS3g', "Put a finger down Attractive  Edition #viralvideo #shorts #fypシ", "13K views"],
['https://www.youtube.com/shorts/7Zza29fXdJs', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo", "10K views"],
['https://www.youtube.com/shorts/zVtwa93PaYc', "random facts #shorts #ramdomfacts #facts #fyp #viralvideo", "36K views"],
['https://www.youtube.com/shorts/iqlKunTua0k', "Put a finger down  Anxiety Edition #shorts #viralvideo #fypシ", "10K views"],
['https://www.youtube.com/shorts/lhmW77f--ss', "random facts you didn't know #shorts #ramdomfacts #interestingfacts #facts #fyp", "3.3K views"],
['https://www.youtube.com/shorts/qGAhcWEx6Ck', "random facts #shorts #ramdomfacts #interestingfacts #facts #fyp", "3.4K views"],
['https://www.youtube.com/shorts/sdM2t56E-BI', "facts that could save your life #ramdomfacts #interestingfacts #facts #fyp #shorts", "19K views"],
['https://www.youtube.com/shorts/LLmlmjJfdRo', "random facts #shorts #ramdomfacts #facts #fyp", "14K views"],

['https://www.youtube.com/shorts/0TYaRi-_VVc', "Shower Thoughts That Will BLOW Your MIND... #shorts #life #satisfying", "26K views"],
['https://www.youtube.com/shorts/Rc6Dfm8QbA0', "Facts You Didn't Know... #shorts #facts #satisfying", "52K views"],
['https://www.youtube.com/shorts/u1K8xOdOfKk', "North Korea Facts That Will Blow Your Mind... #shorts #facts #korea", "72K views"],
['https://www.youtube.com/shorts/UePacRkyJVU', "Facts That Will DISTURB You... #shorts #facts #scary", "54K views"],
['https://www.youtube.com/shorts/F9YU0vtnskU', "Facts That Will Make Your Question Everything #shorts #facts #satisfying", "42K views"],
['https://www.youtube.com/shorts/CR8AGG33kHI', "Facts That Could SAVE Your LIFE... #shorts #facts #satisfying", "275K views"],
['https://www.youtube.com/shorts/9UTLaUaZkD4', "Mind Destroying Shower Thoughts... #shorts #satisfying #facts", "86K views"],
['https://www.youtube.com/shorts/BaGEQgv_YPo', "Movie Facts You Didn't Know... #shorts #facts #movie", "48K views"],
['https://www.youtube.com/shorts/6a5we6wmInA', "Wholesome Facts That WILL Make You Smile #shorts #facts #happy", "79K views"],
['https://www.youtube.com/shorts/2oXUh2Rn9jk', "Animal Facts That Will Blow Your Mind... #shorts #facts #animals", "98K views"],
['https://www.youtube.com/shorts/LJnajUUUwNM', "Useless Facts You Didn't Know #shorts #facts #satisfying", "84K views"],
['https://www.youtube.com/shorts/tGPaq0k6tu0', "Mind Blowing Shower Thoughts... #shorts #facts #satisfying", "197K views"],
['https://www.youtube.com/shorts/bWdQt9-U7qU', "Shocking Facts That Will Blow Your Mind #shorts #facts #satisfying", "58K views"],
['https://www.youtube.com/shorts/_5VgSE32JmQ', "Cat Facts That Will Blow Your Mind #shorts #cat #facts", "130K views"],
['https://www.youtube.com/shorts/FIGdPyx5OXg', "Disturbing Facts That WILL Ruin Your Day #shorts #facts #satisfying", "92K views"],
['https://www.youtube.com/shorts/QLp3B5u2vE8', "Facts That WILL Save Your Life #shorts #facts #satisfying", "96K views"],
['https://www.youtube.com/shorts/YGb8wEx2oXI', "Shower Thoughts That Will Blow Your Mind #shorts #facts #satisfying", "186K views"],
['https://www.youtube.com/shorts/EaDfurkO2FQ', "Animal Facts That Will Blow Your Mind #shorts #facts #animals", "95K views"],
['https://www.youtube.com/shorts/v6YAMNiT8k8', "Wholesome Facts That Will Make Your Day #shorts #facts #happy", "85K views"],
['https://www.youtube.com/shorts/YkLJ-sRPpg8', "Random Facts That Will Blow Your Mind #shorts #facts #interestingfacts", "158K views"],
['https://www.youtube.com/shorts/KPSVQRvg5UQ', "Cat Facts That Will Blow Your Mind #shorts #cat #facts", "544K views"],
['https://www.youtube.com/shorts/3Yl0z9XzljI', "Disturbing Facts That Will Ruin Your Day #shorts #facts #scary", "212K views"],
['https://www.youtube.com/shorts/An40lnO_LzM', "Facts That Could Save Your Life #shorts #facts #life", "150K views"],
['https://www.youtube.com/shorts/9A-nVKZokxM', "Dog Facts That Will Blow Your Mind... #shorts #facts #dog", "141K views"],
['https://www.youtube.com/shorts/pquvBB2bEeY', "North Korea Facts That Will Blow your Mind... #shorts #facts #scary", "1.7M views"],
['https://www.youtube.com/shorts/35zKhhve560', "Shower Thoughts That Will Blow Your Mind... #shorts #thoughts #facts", "550K views"],
['https://www.youtube.com/shorts/AR7Sl4qz8-M', "Animal Facts You Didn't Know... #shorts #facts #animals", "196K views"],
['https://www.youtube.com/shorts/U1rr0oft57Q', "Wholesome Facts That Will Make Your Day Better... #shorts #happy #facts", "277K views"],
['https://www.youtube.com/shorts/EWn08tDP3YA', "Disturbing Facts That Will Ruin Your Day... #shorts #facts #scary", "472K views"],
['https://www.youtube.com/shorts/46n7zG1xM4A', "Facts That Could Save Your Life... #shorts #life #facts", "183K views"],
['https://www.youtube.com/shorts/mgztfgwAshY', "Shower Thoughts That Will Blow Your Mind... #shorts #facts #life", "595K views"],
['https://www.youtube.com/shorts/tAEz3-0T55w', "Animal Facts That Will Blow Your Mind... #shorts #animals #facts", "697K views"],
['https://www.youtube.com/shorts/n3mn_G1i__0', "Facts That Will Make Your Day Better... #shorts #happy #facts", "1.3M views"],
['https://www.youtube.com/shorts/WVl5VHqO3YY', "Scary Facts That Will Disturb You.. #shorts #scary #facts", "346K views"],
['https://www.youtube.com/shorts/XgW0sqz50lQ', "Facts That Could Save Your Life... #shorts #facts #life", "8.7M views"],
['https://www.youtube.com/shorts/SnsGEg3fF6k', "Shower Thoughts That Will Blow Your Mind... #shorts #life #facts", "1.2M views"],
['https://www.youtube.com/shorts/-4RtvNr1HsA', "Animal Facts That Will Blow Your Mind... #shorts #animals #facts", "4.3M views"],
['https://www.youtube.com/shorts/Dgn0I9DOXOc', "Wholesome Facts That Will Make Your Day... #shorts #happy #facts", "217K views"],
['https://www.youtube.com/shorts/AFpbWERbnVU', "Scary Facts That Will Blow Your Mind... #shorts #scary #facts", "436K views"],
['https://www.youtube.com/shorts/xgy0QIqApRM', "Life Saving Facts... #shorts #life #facts", "734K views"],
['https://www.youtube.com/shorts/r8zRl5w4b1U', "Shower Thoughts That Will Blow Your Mind... #shorts #life #facts", "1.3M views"],
['https://www.youtube.com/shorts/rZAY1i4vRws', "Animal Facts You Didn't Know... #shorts #animals #facts", "1.3M views"],
['https://www.youtube.com/shorts/7bmNdXW9w_w', "Wholesome Facts That Will Make Your Day Better... #shorts #happy #facts", "510K views"],
['https://www.youtube.com/shorts/amfGbqBLTag', "Scary Facts That Will Blow Your Mind... #shorts #scary #facts", "1.2M views"],
['https://www.youtube.com/shorts/BO8-HaLlCNU', "Life Saving Facts... #shorts #life #facts", "1M views"],
['https://www.youtube.com/shorts/qhl_3amw7LM', "Shower Thoughts That Will Blow Your Mind... #shorts #life #facts", "985K views"],
['https://www.youtube.com/shorts/l8m4fWCKWu4', "Wholesome Facts That Will Blow Your Mind... #shorts #happy #facts", "9M views"],
['https://www.youtube.com/shorts/o8kVcYiIHSs', "Animal Facts You Didn't Know... #shorts #animals #facts", "577K views"],
['https://www.youtube.com/shorts/c3C2sLf6Xf8', "Scary Facts That Will Keep You Up At Night... #shorts #scary #facts", "1.2M views"],
['https://www.youtube.com/shorts/zswNQ3BIXuM', "Facts That Could Save Your Life... #shorts #life #facts", "1.7M views"],
['https://www.youtube.com/shorts/YEnHKuEeRjY', "Shower Thoughts That Will Blow Your Mind... #shorts #thoughts #facts", "3.2M views"],
['https://www.youtube.com/shorts/qGmT48tpdDI', "Wholesome Facts That Will Make Your Day... #shorts #happy #facts", "1.3M views"],
['https://www.youtube.com/shorts/a9uiG_Q-umM', "Scary Facts That Will Disturb You... #shorts #scary #facts", "3.3M views"],
['https://www.youtube.com/shorts/cQFBxrvA0YA', "Facts That Could Save Your Life... #shorts #life #facts", "4M views"],
['https://www.youtube.com/shorts/BYo3HVW6ftQ', "Shower Thoughts That Will Blow Your Mind... #shorts #life #facts", "8.2M views"],
['https://www.youtube.com/shorts/FYdz9IgIvu0', "Wholesome Facts That Will Make Your Day Better... #shorts #happy #facts", "8.2M views"],
['https://www.youtube.com/shorts/u03wMWuUkiA', "Scary Facts That Will Disturb You.. #shorts #scary #facts", "852K views"],
['https://www.youtube.com/shorts/Ygq-2-nOU4w', "Life Saving Facts... #shorts #life #facts", "8.3M views"],
['https://www.youtube.com/shorts/Z8yasPdKXbc', "Shower Thoughts That Will Blow Your Mind... #shorts #facts #life", "2.8M views"],
['https://www.youtube.com/shorts/qdFzqylJrlE', "Animal Facts That Will Disturb You... #shorts #animals #facts", "4M views"],
['https://www.youtube.com/shorts/DFkwtHBNY_w', "Scary Facts That Will Disturb You... #shorts #scary #facts", "868K views"],
['https://www.youtube.com/shorts/hiklVrKQevg', "Life Saving Facts... #shorts #life #facts", "5M views"],
['https://www.youtube.com/shorts/92GsEiIqHGI', "Shower Thoughts That Will Blow Your Mind...  #shorts #interesting #thoughts", "774K views"],
['https://www.youtube.com/shorts/h4rAQQRSwz8', "Animal Facts That Will Blow Your Mind... #shorts #animals #facts", "457K views"],
['https://www.youtube.com/shorts/6WH4hVCIKwU', "Scary Facts That Will Terrify You... #shorts #scary #facts", "2.5M views"],
['https://www.youtube.com/shorts/pOm7kM5rI8k', "Facts That Could Save Your Life... #shorts #facts #life", "6.7M views"],
['https://www.youtube.com/shorts/3A_TGhedXJo', "Random Facts That You Didn't Know... #shorts #random #facts", "312K views"],
['https://www.youtube.com/shorts/QNBE76Rmfd0', "Animal Facts That Will Blow Your Mind... #shorts #animals #facts", "1.6M views"],
['https://www.youtube.com/shorts/9VtRD0ytCrs', "Scary Facts That Will Disturb You... #shorts #scary #facts", "1.9M views"],
['https://www.youtube.com/shorts/k4nZdLFYGVs', "Shower Thoughts That Will Blow Your Mind... #shorts #thoughts #facts", "3.2M views"],
['https://www.youtube.com/shorts/VNIenfiL3Po', "Random Facts You Didn't Know...#shorts #random #facts", "455K views"],
['https://www.youtube.com/shorts/mHPNTY44fR0', "Animal Facts That You Didn't Know... #shorts #animals #facts #viral #tiktok", "298K views"],
['https://www.youtube.com/shorts/MS88xlvx4LA', "Scary Facts That Will Blow Your Mind... #scary #facts #interesting", "11M views"],
['https://www.youtube.com/shorts/uvTSPeaMZmQ', "Shower Thoughts That Will Blow Your Mind #shorts #interesting #facts", "19M views"],
['https://www.youtube.com/shorts/epeq0v8lm8o', "Random Facts You Didn't Know. #shorts #random #facts", "752K views"],
['https://www.youtube.com/shorts/OXzjbNB1miA', "Life Saving Facts... #shorts #life #facts", "1.2M views"],
['https://www.youtube.com/shorts/ygAE1tP6a6o', "Animal Facts That You Didn't Know!! #shorts #animals #facts", "852K views"],
['https://www.youtube.com/shorts/Lhp8oZMazdY', "Scary Facts That Will Blow Your Mind... #shorts #scary #facts", "2.6M views"],
['https://www.youtube.com/shorts/KIobAeuZpuE', "Weird History Facts That Are Unbelievable... #shorts #history #facts", "193K views"],
['https://www.youtube.com/shorts/jH3Mrc74bIQ', "Shower Thoughts That Will Blow Your Mind... #shorts #facts #viral", "8.6M views"],
['https://www.youtube.com/shorts/K4ObgWMZLq4', "Random Facts You Didn't Know... #shorts #facts #random", "336K views"],
['https://www.youtube.com/shorts/qgTcdJX_xKo', "These Facts Could SAVE Your Life... #shorts #interesting #facts", "230K views"],
['https://www.youtube.com/shorts/98ehJk4TkdQ', "Cat Facts That Will Blow Your Mind. #shorts #cat #facts", "162K views"],
['https://www.youtube.com/shorts/-kyXYhdfl7E', "Scary Facts That Will Shock You. #shorts #scary #facts", "160K views"],
['https://www.youtube.com/shorts/FqM9On5MvoA', "Weird Human Body Facts #shorts #body #facts", "151K views"],
['https://www.youtube.com/shorts/rpxaLAGJttA', "Random Facts You Didn't Know. #shorts #random #facts", "139K views"],
['https://www.youtube.com/shorts/RJiTZhIar3o', "Shower Thoughts That Will Blow Your Mind. #shorts #thoughts #interesting", "462K views"],
['https://www.youtube.com/shorts/EecXCtMGddg', "Space Facts That Will Blow Your Mind. #shorts #space #facts", "65K views"],
['https://www.youtube.com/shorts/Ej0mabUpEiE', "Weird History Facts You Didn't Know. #shorts #history #facts", "95K views"],
['https://www.youtube.com/shorts/FLjjourKDmc', "Scary Facts You Didn't Know... #shorts #scary #facts", "80K views"],
['https://www.youtube.com/shorts/qnwaHboFxJ8', "Dog Facts You'll Only Learn Here... #shorts #dog  #facts", "67K views"],
['https://www.youtube.com/shorts/AgTrBNDQTuA', "Facts About The Human Body... #shorts #facts #interesting", "4.3M views"],
['https://www.youtube.com/shorts/djDLI0rIQJM', "Shower Thoughts... #shorts #showerthoughts #interesting", "98K views"],
['https://www.youtube.com/shorts/Ht1MS8KJUV0', "Ocean Facts That Will Blow Your Mind. #shorts #ocean #facts", "101K views"],
['https://www.youtube.com/shorts/T8esbRW9uhU', "Weird History Facts That Are Unbelievable. #shorts #history #facts", "72K views"],
['https://www.youtube.com/shorts/MizIHA7so2I', "Morbid Facts You Will Only Learn Here. #shorts #facts #interesting", "69K views"],
['https://www.youtube.com/shorts/oRxeYau9QuQ', "North Korea Facts They Dont You To Know. #shorts #northkorea #facts", "67K views"],
['https://www.youtube.com/shorts/8jKH9vvdQa4', "Space Facts That Will Blow Your Mind. #shorts #space #facts", "42K views"],
['https://www.youtube.com/shorts/_YvOuW3VFv0', "Cute Animal Facts That Will Make You Smile. #shorts #facts #cuteanimals", "39K views"],
['https://www.youtube.com/shorts/eihwF-LD0iw', "Random Facts You Didn't Know.", "88K views"],
['https://www.youtube.com/shorts/JV4tOjccuEk', "How Tall Was The Tallest Man In the World??", "51K views"],
['https://www.youtube.com/shorts/XbaySAQt_e0', "Animal Facts That Will Blow Your Mind.", "27K views"],
['https://www.youtube.com/shorts/OQO7t7ruaEY', "Unknown Facts About US Presidents That'll Amaze You.", "28K views"],
['https://www.youtube.com/shorts/Qa_CkoKoff4', "Did You Know These??", "29K views"],
['https://www.youtube.com/shorts/mVBrE3dP_7o', "Historys Weirdest Leaders...", "30K views"],
['https://www.youtube.com/shorts/9giQ-t9l5kU', "Random Facts You Wont Know.", "27K views"],
['https://www.youtube.com/shorts/w0Yx21goBo0', "Weird and Unbelievable History Facts.", "22K views"],
['https://www.youtube.com/shorts/MFCOMGLRSkI', "These Cute Animal Facts Will Make You Smile!!", "21K views"],
['https://www.youtube.com/shorts/RV3wrnTg5pc', "Random Facts You Don't Need To Know!! -shorts-", "19K views"],
['https://www.youtube.com/shorts/_Ft12KJJS-w', "These Facts Could Save Your Life!!", "12K views"],
['https://www.youtube.com/shorts/QLI23uSBu0I', "Food Facts That will Blow Your Mind!!", "14K views"],
['https://www.youtube.com/shorts/4S91Sjk_YuY', "Terrifying Facts That Will Scare You!!", "26K views"],
['https://www.youtube.com/shorts/oipTrblPnrQ', "History Facts That Will Amaze You!!", "11K views"],
['https://www.youtube.com/shorts/RHWWfvd6b4M', "Ocean Facts That Will Blow Your Mind!!", "13K views"],
['https://www.youtube.com/shorts/eLdfTK6YksM', "Random Facts You Didn't Know!!", "18K views"],
['https://www.youtube.com/shorts/s1zZhJ51qEo', "Jaw-Dropping Dog Facts You Won't Believe!", "10K views"],
['https://www.youtube.com/shorts/R1rB9mzpiLc', "Interesting Space Facts That Will Blow Your Mind!!", "13K views"],
['https://www.youtube.com/shorts/HlwRvdw_O5E', "Unbelievable Cat Facts!!  -Shorts-", "13K views"],
['https://www.youtube.com/shorts/OduDDNmVvpo', "Do You Walk This Much?!   -Shorts-", "18K views"],


['https://www.youtube.com/shorts/BBF3S2714kk', "Random facts that could save your life.#facts #randomfacts #curiosity", "12K views"],
['https://www.youtube.com/shorts/x7KDSN-pWqc', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "6.8K views"],
['https://www.youtube.com/shorts/tau9PUHsU-Q', "Facts that could save your life someday.#facts #randomfacts #curiosity", "9.6K views"],
['https://www.youtube.com/shorts/Q0282KSe8Ns', "Curious facts that could save your life.#facts #randomfacts #facts", "8.9K views"],
['https://www.youtube.com/shorts/tWiMIw8TxD0', "Curious facts that might scare you.#facts #randomfacts #curiosity", "12K views"],
['https://www.youtube.com/shorts/sRBdBPEb5UA', "curiosities that may scare you and I bet you don't know these facts.#facts #randomfacts #curiosity", "3.6K views"],
['https://www.youtube.com/shorts/wOuCDMHKZWs', "Curious facts that may scare you.#facts #randomfacts #curiosity", "2.2K views"],
['https://www.youtube.com/shorts/GIJcWvW3OEs', "Curious facts that may scare you.#facts #randomfacts #curiosity", "11K views"],
['https://www.youtube.com/shorts/lvIMEh-ZvSY', "Random and curious facts I bet you don't know.#facts #randomfacts #curiosity", "8.9K views"],
['https://www.youtube.com/shorts/-taM3ka9qus', "Crazy random facts I bet you don't know.#facts #randomfacts #curiosity", "12K views"],
['https://www.youtube.com/shorts/a3cYRylDaDM', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "4.5K views"],
['https://www.youtube.com/shorts/12yp8_Pj9K4', "Curious facts I bet you don't know.#facts #randomfacts #curiosity", "5.9K views"],
['https://www.youtube.com/shorts/OaeYi2s_-Ho', "Did you know these facts I bet you don't know.#facts #randomfacts #curiosity", "15K views"],
['https://www.youtube.com/shorts/XkpLjaUddKY', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "3.7K views"],
['https://www.youtube.com/shorts/YIZnEtH0GUQ', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "9.4K views"],
['https://www.youtube.com/shorts/Eyx_tcJPaDE', "Photos that relieve anxiety.#vibes #anxiety #anxietyrelief", "3.6K views"],
['https://www.youtube.com/shorts/0s3jwusBOdA', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "10K views"],
['https://www.youtube.com/shorts/bONswlZnR7A', "Random curiosities I bet you don't know.#facts #randomfacts #curiosity #short", "11K views"],
['https://www.youtube.com/shorts/ifEVgi_w178', "Random facts I bet you don't know.#facts #curiosity #curiosity", "21K views"],
['https://www.youtube.com/shorts/hDlZv-T_zLo', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "5.2K views"],
['https://www.youtube.com/shorts/wLilguyLTv4', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "11K views"],
['https://www.youtube.com/shorts/WC9OsLSYh_I', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "25K views"],
['https://www.youtube.com/shorts/HYdDY-RF3ss', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "20K views"],
['https://www.youtube.com/shorts/QW0--MoKmsM', "Random facts that will blow your mind🤯.#facts #randomfacts #curiosity", "11K views"],
['https://www.youtube.com/shorts/hDu-7zSBScE', "Random facts you don't know.#facts #randomfacts #curiosity", "27K views"],
['https://www.youtube.com/shorts/jgQ_oh47y2Y', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "14K views"],
['https://www.youtube.com/shorts/WAy6RmPUgX0', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "14K views"],
['https://www.youtube.com/shorts/jkIaQ3TOnJc', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "37K views"],
['https://www.youtube.com/shorts/6pYzIo4LMFQ', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "12K views"],
['https://www.youtube.com/shorts/5IrH5UX6-WQ', "I dare you  to pass this test!! #test #concentration #psychologytest #psychology", "5.8K views"],
['https://www.youtube.com/shorts/lx0MRNv24m0', "Random facts that will blow your mind🤯#facts #randomfacts #curiosity", "199K views"],
['https://www.youtube.com/shorts/pDCwoPFhVfg', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "11K views"],
['https://www.youtube.com/shorts/fHH3zCAwoh0', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "15K views"],
['https://www.youtube.com/shorts/yzvWkmVKeaU', "Comment how many you got right.#test #quiz #real or cake", "19K views"],
['https://www.youtube.com/shorts/rzjz4wsGwO4', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "187K views"],
['https://www.youtube.com/shorts/FbKRtfYP6zU', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "8.6K views"],
['https://www.youtube.com/shorts/frumPihyfnw', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "13K views"],
['https://www.youtube.com/shorts/p7g4lvh2K6M', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "10K views"],
['https://www.youtube.com/shorts/4vGk7SpKc5o', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "13K views"],
['https://www.youtube.com/shorts/STYvyWSO9hQ', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "5.5K views"],
['https://www.youtube.com/shorts/xGr4EbBWLFU', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "22K views"],
['https://www.youtube.com/shorts/klgaSxYADFw', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "70K views"],
['https://www.youtube.com/shorts/EhW5xbEI2zg', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "27K views"],
['https://www.youtube.com/shorts/Xhan951-eOo', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "89K views"],
['https://www.youtube.com/shorts/Z16o9XyqMH4', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "4.9K views"],
['https://www.youtube.com/shorts/uWWNumwx6K8', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "12K views"],
['https://www.youtube.com/shorts/44D_aS-gMKg', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "246K views"],
['https://www.youtube.com/shorts/Hoe4BppEq3Q', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "655K views"],
['https://www.youtube.com/shorts/xgB5ZUYoBdc', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "34K views"],
['https://www.youtube.com/shorts/GvPteP095Cg', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "30K views"],
['https://www.youtube.com/shorts/5y_p93SpgZc', "Random facts I bet you don't know.#facts  #randomfacts #curiosity", "7.3K views"],
['https://www.youtube.com/shorts/z1A-GRxy-nA', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "4.8K views"],
['https://www.youtube.com/shorts/vK02yWlHCYU', "Random facts I bet you don't know.#facts #randomfacts #curiosity", "8.7K views"],
['https://www.youtube.com/shorts/uaC0j6cF1VQ', "Random facts I bet you don't know. #facts #randomfacts #curiosity", "108K views"],
['https://www.youtube.com/shorts/WcBhOMfR4nY', "Random facts I bet you don't know. #facts #randomfacts #curiosity", "19K views"],
['https://www.youtube.com/shorts/BdeUq_fQSaw', "Random facts I bet you don't know. #facts #randomfacts #curiosity", "6.5K views"],
['https://www.youtube.com/shorts/Mwl3vhWG9CM', "Random facts I bet you don't know about 👀. #randomfacts #curiosity #facts", "6.3K views"],
['https://www.youtube.com/shorts/Hi6q2q2m70Y', "Random facts I bet you don't know 👀. #randomfacts #curiosity #facts", "1.5K views"],
['https://www.youtube.com/shorts/ZodONlJh4oM', "Random facts you should know about 👀.#randomfacts #curiosity #facts", "766 views"],
['https://www.youtube.com/shorts/b4pCjiiA05c', "Random facts I bet you don't know.👀 #facts #curiosity #randomfacts", "887 views"],
['https://www.youtube.com/shorts/789GedpF4LA', "Random facts I bet you don't know 👀. #facts #curiosity #randomfacts", "7.7K views"],
['https://www.youtube.com/shorts/-2d2hXbwJKQ', "Random facts I bet you don't know 👀.#facts #curiosity #randomfacts", "6.9K views"],
['https://www.youtube.com/shorts/DTPH2pAOklE', "Random facts I bet you don't know👀 #facts #curiosity #randomfacts", "6.5K views"],
['https://www.youtube.com/shorts/rgOzL3rEyPk', "Random facts I bet you don't know👀. #facts #curiosity #randomfacts", "2.9K views"],
['https://www.youtube.com/shorts/1UDnwnc-Uug', "Do you know about these I bet you don't know.#randomfacts", "871 views"],
['https://www.youtube.com/shorts/DGJW0yjJ2TI', "Random facts I bet you don't know.#randomfacts", "174K views"],
['https://www.youtube.com/shorts/oj6FF2ApB7Y', "Did you know about these facts I bet you don't know.#randomfacts", "677 views"],
['https://www.youtube.com/shorts/tgz6_j9ntyo', "Did you know about these facts I bet you don't know #randomfacts", "5K views"],
['https://www.youtube.com/shorts/1W1bhFTvgWc', "Did you know about these ? #facts #randomfacts #curiosity #learning #didyouknowfacts", "1.1K views"],


['https://www.youtube.com/shorts/N-zU50cv8Ls', "Random Facts You Didn't Know... #shorts #facts #interestingfacts", "228K views"],
['https://www.youtube.com/shorts/oGtH_LKVu_Y', "5 Disturbing Facts You Need to Know... #shorts #facts", "255K views"],
['https://www.youtube.com/shorts/UAdDYvRMdhY', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts", "624K views"],
['https://www.youtube.com/shorts/K1urYwoLqbs', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "440K views"],
['https://www.youtube.com/shorts/xZ_W_RyGCYs', "Interesting Facts To Cure Boredom... #shorts #facts #factshorts", "195K views"],
['https://www.youtube.com/shorts/g0lT-FmKoFo', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "1.2M views"],
['https://www.youtube.com/shorts/lClpMQIN5mU', "Crazy Facts You Didn't know... #shorts #facts #factshorts", "555K views"],
['https://www.youtube.com/shorts/ToUh07k99Xw', "Random Facts... #shorts #randomfacts #facts", "879K views"],
['https://www.youtube.com/shorts/N9Et5Ul2Vsc', "Crazy Facts You Didn't Know! #shorts #facts #interestingfacts", "429K views"],
['https://www.youtube.com/shorts/FYQ7R9cltMw', "Crazy Shower Thoughts... #shorts #showerthoughts", "1.9M views"],
['https://www.youtube.com/shorts/76BU8jmHxjQ', "Facts That Will Save Your Life😱 #shorts #facts #factshorts", "486K views"],
['https://www.youtube.com/shorts/Syw6JYzhTJc', "The Hole Never Ends... #shorts", "411K views"],
['https://www.youtube.com/shorts/MOfTG566Bgs', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "585K views"],
['https://www.youtube.com/shorts/uaB2lX9nsZM', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "1.5M views"],
['https://www.youtube.com/shorts/qaC9e3Q7B9E', "Random Facts You Didn't Know... #shorts #facts #interestingfacts", "348K views"],
['https://www.youtube.com/shorts/AL97LW5L0Fo', "Facts That Will Save Your Life... #shorts #facts #factshorts", "1.3M views"],
['https://www.youtube.com/shorts/57iViiJbZY8', "Insane Shower Thoughts... #shorts #showerthoughts #thoughts", "1.5M views"],
['https://www.youtube.com/shorts/TaC_Esvm2Dg', "Random Facts... #shorts #facts #factshorts", "432K views"],
['https://www.youtube.com/shorts/EUcl2_dfMIM', "Mind-Blowing Shower Thoughts... #shorts #showerthoughts #thoughts", "1.8M views"],
['https://www.youtube.com/shorts/cSul-prpQLA', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts", "467K views"],
['https://www.youtube.com/shorts/YpQFGLrSWB8', "Random Facts You Need To know... #shorts #facts #factshorts", "523K views"],
['https://www.youtube.com/shorts/tam0dqBdNI0', "Random Curiosities That Hit Hard... #shorts #showerthoughts #thoughts", "794K views"],
['https://www.youtube.com/shorts/620760MQ6YI', "Shocking Facts You Didn't Know! #shorts #randomfacts", "1.7M views"],
['https://www.youtube.com/shorts/pb42sqqGqyE', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "1M views"],
['https://www.youtube.com/shorts/yOqbGlFz3wk', "Shower Thoughts That Will Blow Your Mind! #shorts #showerthoughts #thoughts", "1.4M views"],
['https://www.youtube.com/shorts/kEY0jTVox0A', "Random Facts You Didn't Know... #shorts #facts #factshorts", "596K views"],
['https://www.youtube.com/shorts/DGjeFyx4Dqg', "Shower Thoughts Your Mum Told Me... #shorts #showerthoughts #thoughts", "572K views"],
['https://www.youtube.com/shorts/2fcRb1603lA', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts", "1M views"],
['https://www.youtube.com/shorts/61qqSTHfMQU', "Shower Thoughts That Will Blow Your Mind... #shorts #thoughts #showerthoughts", "1M views"],
['https://www.youtube.com/shorts/YiFYcZDiK5Y', "Cute Facts To Make Your Day... #shorts", "2M views"],
['https://www.youtube.com/shorts/ADNBd_zNYe8', "Random Thoughts You Didn't Know... #shorts #facts #thoughts", "1.2M views"],
['https://www.youtube.com/shorts/c_FUP9zzoaQ', "Insane Shower Thoughts... #shorts #showerthoughts #thoughts", "3M views"],
['https://www.youtube.com/shorts/9ECPEzxY0U4', "Random Facts You Didn't Know... #shorts #facts #interestingfacts", "1.5M views"],
['https://www.youtube.com/shorts/IViikNDu9aY', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts", "5.5M views"],
['https://www.youtube.com/shorts/p4Ln4JX0Kfk', "Random Curiosities... #shorts #showerthoughts #thoughts", "2.8M views"],
['https://www.youtube.com/shorts/irG_Gle5AuM', "Random Facts #shorts #factshorts #interestingfacts", "990K views"],
['https://www.youtube.com/shorts/eQrYLDogUIE', "Mind Blowing Shower Thoughts... #shorts #facts #showerthoughts", "2.1M views"],
['https://www.youtube.com/shorts/O6BC4YGlmwU', "Mind-Blowing Shower Thoughts... #shorts #facts #showerthoughts", "2.6M views"],
['https://www.youtube.com/shorts/a7kB-oUEsHg', "Disney Thoughts That Will Blow Your Mind... #shorts #disney  #showerthoughts", "2.9M views"],
['https://www.youtube.com/shorts/2LeSYXREe2w', "Random Facts You Didn't know... #shorts #facts #factshorts", "1.1M views"],
['https://www.youtube.com/shorts/9uIr6arA2mM', "Facts That Will Save Your Life... #shorts #facts #factshorts", "6.3M views"],
['https://www.youtube.com/shorts/qc-bR1aZH5A', "Random Curiosities You Didn't Know... #shorts #showerthoughts #thoughts", "1.8M views"],
['https://www.youtube.com/shorts/AdBfPHyuhwM', "Facts That Will Save Your Life...😱 #shorts #facts #factshorts", "2.7M views"],
['https://www.youtube.com/shorts/J8tqAMecxqs', "Random Facts to Creep You Out... #shorts #facts #scary", "593K views"],
['https://www.youtube.com/shorts/nQnjNv3FKog', "Random Curiosities... #shorts #showerthoughts #thoughts", "998K views"],
['https://www.youtube.com/shorts/QJj93WA34mw', "Facts That Will Give You Chills...", "1M views"],
['https://www.youtube.com/shorts/tedUegx-FVA', "Mind-Blowing Shower Thoughts... #shorts #showerthoughts #thoughts", "5.4M views"],
['https://www.youtube.com/shorts/kn7tjg1h-3M', "Random Curiosities... #shorts #showerthoughts #thoughts", "2M views"],
['https://www.youtube.com/shorts/NP7DD2wEp18', "Facts That Will Save Your Life😱 #shorts #facts #factshorts", "2.8M views"],
['https://www.youtube.com/shorts/o0xg5CpUElU', "Random Facts You Didn't know...", "713K views"],
['https://www.youtube.com/shorts/DlpdTryvpv0', "Random facts #short #interestingfacts #factshorts", "1.3M views"],
['https://www.youtube.com/shorts/TQtKuSmG8Yk', "Stupid Things You Just Realised... #shorts #facts #entertainment", "5.5M views"],
['https://www.youtube.com/shorts/7pesWSGl8sE', "Facts That Will Scare You... #scary #facts #interestingfacts", "1M views"],
['https://www.youtube.com/shorts/l_drDVA62vs', "Animal Facts That Will Make Your Day! #shorts #facts #animals", "546K views"],
['https://www.youtube.com/shorts/Rvc927Sy118', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "11M views"],
['https://www.youtube.com/shorts/oJsRQ9RvlQY', "Random Facts You Didn't Know.. #shorts #randomfacts #factshorts", "606K views"],
['https://www.youtube.com/shorts/UJFSFyktOjg', "Weird Animal Facts That Will Blow Your Mind... #shorts #animals #facts", "494K views"],
['https://www.youtube.com/shorts/pmw8InYWzFw', "Random Facts You Didn't Know.. #shorts #randomfacts", "254K views"],
['https://www.youtube.com/shorts/KbOLEbovPO8', "Positive Facts! #shorts #facts #factshorts", "519K views"],
['https://www.youtube.com/shorts/tod75haW70E', "Random Facts To Creep You Out... #scary #facts #scary", "621K views"],
['https://www.youtube.com/shorts/nIssyh_50-Q', "Facts That Will Save Your Life😱 #shorts #facts #interestingfacts", "3.2M views"],
['https://www.youtube.com/shorts/sHOv2Y6Gx8g', "Crazy Laws You Never Knew! 😱 #shorts #factshorts #facts", "1M views"],
['https://www.youtube.com/shorts/L9nyGXAOwUA', "Random Facts You Didn't Know.. #shorts #randomfacts", "437K views"],
['https://www.youtube.com/shorts/54kBIe_Bq6M', "Random Facts You Didn't Know.. #shorts #randomfacts", "3.5M views"],
['https://www.youtube.com/shorts/CnTj1zQmbj0', "Random Thoughts #shorts #randomfacts #facts", "1.5M views"],
['https://www.youtube.com/shorts/PLcDZSqi18U', "Random Facts You Didn't Know.. #shorts #randomfacts", "3.8M views"],
['https://www.youtube.com/shorts/NJyXFculix8', "Facts You Didn't Know... #shorts #facts #factshorts", "233K views"],
['https://www.youtube.com/shorts/lKdSPJrYZ1U', "Crazy Shower Thoughts... #shorts #showerthoughts #thoughts", "9.1M views"],
['https://www.youtube.com/shorts/JinZLcCCpdQ', "Random Facts You Didn't Know.. #shorts #randomfacts", "1.7M views"],
['https://www.youtube.com/shorts/Cn4Oj134tsM', "TikTok Shower Thoughts #shorts #randomfacts #facts", "1.1M views"],
['https://www.youtube.com/shorts/meEDLiJtCp4', "Scary Mind-Blowing Facts  #facts #shorts #scaryfacts", "765K views"],
['https://www.youtube.com/shorts/219Y5KBgDaM', "Mind-Blowing Facts🤯 #shorts #facts", "671K views"],
['https://www.youtube.com/shorts/BQmMJyvDBgk', "Stupid Things You Just Realised...", "13M views"],
['https://www.youtube.com/shorts/Cxq0OAiNP4Y', "Facts That Will Make You Less Stupid #shorts #facts #factshorts", "374K views"],
['https://www.youtube.com/shorts/QeuwvmQTbZY', "Facts You Didn't know... #shorts #facts", "302K views"],
['https://www.youtube.com/shorts/uBe2FH1IU5A', "Random Facts #shorts #facts", "2M views"],
['https://www.youtube.com/shorts/6ft94FGHOM8', "Facts That Could Save Your Life #shorts #factshorts #facts", "1.4M views"],
['https://www.youtube.com/shorts/4CVWIfzfmCA', "Random Curiosities #shorts #randomfacts", "305K views"],
['https://www.youtube.com/shorts/1fEXqv7FkrU', "Facts That Will Save Your Life😱 #shorts #facts", "32M views"],
['https://www.youtube.com/shorts/Qp7WlFexVLY', "Facts To Find Your Soulmate #shorts #love #facts", "185K views"],
['https://www.youtube.com/shorts/dd-sbz7VM0A', "Interesting Facts You Didn’t Know… #shorts #facts", "103K views"],
['https://www.youtube.com/shorts/CtISySXGfec', "This Video Will Save Your Life #shorts #facts #interestingfacts", "465K views"],
['https://www.youtube.com/shorts/DCN-eYc-qpk', "This Video Will Save Your Life #shorts #factshorts #facts", "24M views"],
['https://www.youtube.com/shorts/nlVQWTs71AI', "Random Thoughts #shorts #thoughts #interestingfacts", "199K views"],
['https://www.youtube.com/shorts/VBe0yA2RLBk', "Scary facts That  Will Blow Your Mind! #facts #shorts #scaryfacts", "406K views"],
['https://www.youtube.com/shorts/z_oFC8Am2LY', "Random Facts You Didn’t Know… #shorts #facts #interestingfacts", "96K views"],
['https://www.youtube.com/shorts/1TU_F0fMe-4', "Shower Thoughts to Cure Boredom (pt.1)  #shorts #interestingfacts #thoughts", "117K views"],
['https://www.youtube.com/shorts/FL7KVNBs1Oo', "Facts You Didn’t Know… #shorts #facts #factshorts", "204K views"],
['https://www.youtube.com/shorts/m-YMVjJI8X8', "Facts That Leave You Speechless #shorts #interestingfacts #facts", "57K views"],
['https://www.youtube.com/shorts/oSbxZ61pqYw', "This Video Can Save Your Life!😳 #shorts #facts #factshorts", "70K views"],
['https://www.youtube.com/shorts/dvamNxd7h9A', "Interesting Facts You've Never Heard… #shorts #facts #interestingfacts", "197K views"],
['https://www.youtube.com/shorts/8p4yrrTsqjY', "Interesting Facts #shorts #facts", "304K views"],
]
#fmt: on


def convert_views_to_int(views_str):
    views_str = views_str.replace(',', '')
    views_str = views_str.split('views')[0].strip()
    multiplier = 1
    if 'K' in views_str:
        multiplier = 1000
        views_str = views_str.replace('K', '')
    elif 'M' in views_str:
        multiplier = 1000000
        views_str = views_str.replace('M', '')
    return int(float(views_str) * multiplier)


DATA_DIR = "./workspace/yshorts/data"
AUDIO_DIR = "./workspace/yshorts/audio"
TEMP_DIR = "./workspace/yshorts/temp"
DEVICE = "cuda"
BATCH_SIZE = 16  # reduce if low on GPU mem
# change to "int8" if low on GPU mem (may reduce accuracy)
COMPUTE_TYPE = "float16"
MODEL_NAME = 'base'
TOP_NUMBER = 200


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

        # for url, title, views in videos:
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
        for url, title, views in videos:
            if not os.path.exists(f"{DATA_DIR}/{url.split('/')[-1]}.json"):
                audio = whisperx.load_audio(
                    f"{AUDIO_DIR}/{url.split('/')[-1]}.wav")
                result = model.transcribe(
                    audio, batch_size=BATCH_SIZE, language='en')
                # print(result["segments"])  # before alignment
                result = whisperx.align(
                    result["segments"], model_a, metadata, audio, DEVICE, return_char_alignments=False)
                segs = result['segments']
                ass_content = write_adv_substation_alpha(segs)
                joined = '\n'.join([seg['text'] for seg in result['segments']])
                print(f"\n\n\n# {title} #\n{joined}")
                data = {
                    'transcribe': result,
                    'ass': ass_content,
                    'url': url,
                    'title': title,
                    'views': views
                }

                with open(f'{DATA_DIR}/{url.split("/")[-1]}.json', 'w') as f:
                    f.write(json.dumps(data))
            progress.advance(task)


if __name__ == "__main__":
    og_len = len(videos)
    videos.sort(key=lambda x: convert_views_to_int(x[2]), reverse=True)
    videos = videos[:TOP_NUMBER]
    # for url, title, views in videos:
    #     console.print(
    #         f'[medium_purple3]{url.split("/").pop()} - {views} - {title}')
    # console.log('og len', og_len)
    main()

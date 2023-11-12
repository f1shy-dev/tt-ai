import datetime
import ffmpeg
import whisperx
from ttai_farm.v4.write_ass import write_adv_substation_alpha
from ttai_farm.v4.tts import text_to_speach
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
from rich.prompt import Confirm
import os
import subprocess
from rich.console import Console
import json
import random
from poe_api_wrapper import PoeApi

def genScript():
    client = PoeApi('ze72NYTMJwGeu4_hdNqP2A==')
    console = Console()
    bot = "a2"
    prompt = '''
    {
    "video1": {
    "title": "Put a finger down - <theme> edition!",
    "sentence1": "Put a finger down if you put more than 5 fingers down, you are <relate to theme>",
    "sentence2": "Put a finger down <relatable fact>",
    "sentence3": "Put a finger down <relatable, interesting hook fact>",
    "sentence4": "Put a finger down <relatable fact>",
    "sentence5": "Put a finger down <relatable fact>",
    "sentence6": "Put a finger down <relatable fact>",
    "sentence7": "Put a finger down <relatable, interesting hook fact>",
    "sentence8": "Put a finger down <relatable fact>",
    "sentence9": "Put a finger down <relatable fact>",
    "sentence10": "Put a finger down <relatable fact>",
    "sentence11": "Put a finger down <relatable fact>",
    "sentence12": "Put a finger down <relatable fact>"
    }
    }

    Generate 10+ "Put a finger down" style TikTok videos in the above relatable JSON format. All facts should be surprising yet relatable tidbits starting with "Put a finger down...". Even the hook sentences should start this way. The facts should subtly hint for viewers to like/subscribe. Make sure to include "put a finger down" instructions and end with clear prompts to engage. Use conversational language as if speaking directly to the viewer. Mention the "share" button and "second person" casually. Overall create a relatable, engaging style similar to provided examples that draws in viewers. Get creative with titles, themes and relatable facts!
    '''

    # for chunk in client.send_message(bot, prompt):
    #     pass
    # response = chunk["text"]
    response = '''
    Here are 12 "Put a finger down" style video concepts in the requested format:

    {
    "video1": {
    "title": "Put a finger down if you're constantly scrolling...",
    "sentence1": "Put a finger down if you've spent more on apps than you planned to this month!",
    "sentence2": "Put a finger down if you've ever fallen asleep with your phone in your hand",
    "sentence3": "Put a finger down if you recognize every notification sound",
    "sentence4": "Put a finger down if you've almost run out of battery before the day is done",
    "sentence5": "Put a finger down if social media is the first thing you check in the morning",
    "sentence6": "Put a finger down if you've had to limit your screen time",
    "sentence7": "Put a finger down if you've ever missed your stop because you were too busy scrolling",
    "sentence8": "Put a finger down if you feel naked without your phone",
    "sentence9": "Put a finger down if you end up spending way longer online than you meant to",
    "sentence10": "Put a finger down if you're watching this video on your phone right now!",
    "sentence11": "So if you related, make sure to like and subscribe for more relatable content! Tap that share button too if you think a friend would enjoy",
    "sentence12": "Don't forget to comment below and let me know how many fingers you put down - I'll reply to some of you!"
    },
    "video2": {
    "title": "Put a finger down if you're acaffeinated...",
    "sentence1": "Put a finger down if you can't function before your first cup of coffee",
    "sentence2": "Put a finger down if the coffee pot is your first stop in the morning",
    "sentence3": "Put a finger down if you've ever accidentally drank decaf thinking it was regular",
    "sentence4": "Put a finger down if coffee breath is a permanent state for you",
    "sentence5": "Put a finger down if you measure your day in cups rather than hours",
    "sentence6": "Put a finger down if you have more mugs than anyone could reasonably use",
    "sentence7": "Put a finger down if coffee fixes any problem - can't sleep? coffee. Stressed? Coffee. Bored? Coffee.",
    "sentence8": "Put a finger down if you've ever drank cold brew straight like a shot",
    "sentence9": "Put a finger down if coffee shops are your third home",
    "sentence10": "Put a finger down if you're already looking forward to your next cup",
    "sentence11": "If you relate, give this vid a like for the coffee lovers out there! Let me know below how many fingers you put down",
    "sentence12": "Make sure to subscribe so you don't miss my next video - I'm thinking of doing a 'coffee hacks' one..."
    },
    "video3": {
    "title": "Put a finger down if you're a clean freak...",
    "sentence1": "Put a finger down if you stress clean when you're anxious",
    "sentence2": "Put a finger down if dusting is a daily habit for you",
    "sentence3": "Put a finger down if you hover over anyone who tracks dirt in",
    "sentence4": "Put a finger down if you have more cleaning products than you know what to do with",
    "sentence5": "Put a finger down if you can't relax in a messy space",
    "sentence6": "Put a finger down if messes physically bother you",
    "sentence7": "Put a finger down if you find cleaning therapeutic",
    "sentence8": "Put a finger down if you've ever reorganized someone else's cabinets",
    "sentence9": "Put a finger down if you organize cleaning by room or task",
    "sentence10": "Put a finger down if you prefer cleaning to most other hobbies",
    "sentence11": "If you're a fellow neat freak, hit like and subscribe so we can motivate each other to keep things spick and span!",
    "sentence12": "And share this with any other clean friends you have - I'm sure they'll relate too!"
    }
    }
    '''
    response = response[response.find("{"):]
    response = response[:response.rfind("}")+1]
    # print(response)
    # separate the json 
    data = json.loads(response)
    print(data)
    directory = 'workspace/temp/tempscripts/'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")
    for video in data:
        print(f"Processing {video}")
        video_data = data[video]
        print(video_data["title"])
        filename = f"workspace/temp/tempscripts/{video:04}.json"
        with open(filename, 'w') as f:
            json.dump(video_data, f, indent=4)
        print(f"Saved {video} data to {filename}")

def makeBG():
    directory = "workspace/bg-mirror"
    files = os.listdir(directory)
    bg_vids = []
    combined_length = 0
    while combined_length < 60:
        file = random.choice(files)
        print(file)
        bg_vids.append(file)
        print(bg_vids)
        file_length = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", f"{directory}/{file}"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        combined_length += float(file_length.stdout)
        print(combined_length)
    # create a filelist.txt with the bg_vids
    with open("workspace/filelist.txt", "w") as f:
        for file in bg_vids:
            print(f"file '{file}'\n")
            f.write(f"file 'bg-mirror/{file}'\n")
    # Use ffmpeg to combine the videos in bg_vids
    subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "/media/OS/Users/Mohid/tt-ai/workspace/filelist.txt", "-c", "copy", "workspace/temp/background.mp4"])
    # os.remove("workspace/temp/filelist.txt")

def makeTTS():
    directory = "workspace/temp/tempscripts"
    files = os.listdir(directory)
    for file in files:
        with open(f"{directory}/{file}") as f:
            data = json.load(f)
        print(data)
        # generate the tts
        tts = text_to_speach(data["title"])
        tts += text_to_speach(data["sentence1"])
        tts += text_to_speach(data["sentence2"])
        tts += text_to_speach(data["sentence3"])
        tts += text_to_speach(data["sentence4"])
        tts += text_to_speach(data["sentence5"])
        tts += text_to_speach(data["sentence6"])
        tts += text_to_speach(data["sentence7"])
        tts += text_to_speach(data["sentence8"])
        tts += text_to_speach(data["sentence9"])
        tts += text_to_speach(data["sentence10"])
        tts += text_to_speach(data["sentence11"])
        tts += text_to_speach(data["sentence12"])
        # save the tts to a file
        with open(f"workspace/temp/tts/{file[:-5]}.mp3", "wb") as f:
            f.write(tts)
        # save the tts to a file
        with open(f"workspace/temp/tts/{file[:-5]}.txt", "w") as f:
            f.write(tts)
makeTTS()
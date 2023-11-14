import datetime
import ffmpeg
import whisperx
# from ttai_farm.v4.write_ass import write_adv_substation_alpha
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
from rich.prompt import Confirm
import os
import subprocess
from rich.console import Console
import json
import random
from poe_api_wrapper import PoeApi
import requests
from requests.exceptions import JSONDecodeError
from rich.progress import track
from mutagen.mp3 import MP3

def genScript():
    # Parameters
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
    directory = 'workspace/v5/temp/tempscripts/'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")
    for video in data:
        print(f"Processing {video}")
        video_data = data[video]
        print(video_data["title"])
        filename = f"workspace/v5/temp/tempscripts/{video:04}.json"
        with open(filename, 'w') as f:
            json.dump(video_data, f, indent=4)
        print(f"Saved {video} data to {filename}")

def makeBG():
    # Parameters
    directory = "workspace/v5/bg"
    files = os.listdir(directory)
    bg_vids = []
    combined_length = 0

    while combined_length < 60:
        file = random.choice(files)
        print(file)
        bg_vids.append(file)
        print(bg_vids)
        file_length = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", f"{directory}/{file}"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        print(file_length.stdout)
        combined_length += float(file_length.stdout)
        print(combined_length)
    # create a filelist.txt with the bg_vids
    with open("workspace/v5/temp/filelist.txt", "w") as f:
        for file in bg_vids:
            print(f"file '../bg/{file}'\n")
            f.write(f"file '../bg/{file}'\n")
    # Use ffmpeg to combine the videos in bg_vids
    subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "workspace/v5/temp/filelist.txt", "-c", "copy", "workspace/v5/output/background.mp4"])
    # os.remove("workspace/temp/filelist.txt")

def text_to_speech(text):
    body = {"voice": "Brian", "text": text, "service": "StreamElements"}
    response = requests.post(
        "https://lazypy.ro/tts/request_tts.php", data=body)
    print(response.status_code)
    voice_data = requests.get(response.json()["audio_url"])
    with open("workspace/v5/temp/voicedata.mp3", "wb") as f:
        f.write(voice_data.content)

def transcribeTTS():
    # Parameters
    device = "cuda"
    audio_file = "workspace/v5/temp/voicedata.mp3"
    batch_size = 16 # reduce if low on GPU mem
    compute_type = "float16" # change to "int8" if low on GPU mem (may reduce accuracy)
    align_model = "WAV2VEC2_ASR_BASE_960H"
    model_a, metadata = whisperx.load_align_model(language_code='en', device=device, model_name=align_model)

    if not audio_file:
        raise ValueError("No audio file found. Please run text_to_speech() first.")
    
    # Transcribe
    model = whisperx.load_model("large-v2", device, compute_type=compute_type)

    # Do something cool
    audio = whisperx.load_audio(audio_file)
    result = model.transcribe(audio, batch_size=batch_size)
    
    # Alignmentation
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

    print(result["segments"]) # Print.

    # Store the thing in the other thing
    # store the result in the json file with nice formatting
    with open("workspace/v5/temp/voicedata.json", "w") as f:
        json.dump(result["segments"], f, indent=4)
    # omg finallyyy its done

def burnSubs():
    # 1. Load the json file
    # 2. split the sentences into 20 character chunks (or less) and add them to a list
    # 3. Burn the subs to the video using the format: (font_size=18,color='00FFFF',underline=False,Fontname='Dela Gothic One',BackColor='&H80000000', Spacing='0.2', Outline='0', Shadow='0.75', Fontsize='18', Alignment='5',MarginL='10',MarginR='10',MarginV='10')
    # 4. Save the video to output
    # 1
    with open("workspace/v5/temp/voicedata.json", "r") as f:
        voicedata = json.load(f)
    # 2. split the sentences into 20 character chunks (or less) and add them to a list
    chunks = []
    for segment in voicedata:
        for word in segment["words"]:
            while len(word) > 20:
                chunks.append(word[:20])
                word = word[20:]
            chunks.append(word)
    print(chunks)
            


burnSubs()

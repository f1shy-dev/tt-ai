import datetime
import ffmpeg
# import whisperx
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
    subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "workspace/v5/temp/filelist.txt", "-c", "copy", "workspace/v5/temp/background.mp4"])
    # os.remove("workspace/temp/filelist.txt")

def text_to_speech(text, file_path="workspace/v5/temp/voicedata.mp3"):
    body = {"voice": "Brian", "text": text, "service": "StreamElements"}
    response = requests.post(
        "https://lazypy.ro/tts/request_tts.php", data=body)
    print(response.status_code)
    voice_data = requests.get(response.json()["audio_url"])
    with open(file_path, "wb") as f:
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
    jsondata = json.dumps(result["segments"], indent=4)
    with open("workspace/v5/temp/voicedata.json", "w") as f:
        f.write(jsondata)
    # yay its done

def chunkSubs():
    # Parameters
    chunk_length = 20
    # WHYS THE JSON BROKEN NOW
    with open("workspace/v5/temp/voicedata.json", "r") as f:
        jsondata = json.load(f)
        for sentence in jsondata:
            for word in sentence["words"]:
                index = sentence["words"].index(word) # wth is this code
                if 'start' not in word:
                    if index == 0:
                        word["start"] = sentence["start"]
                        print(f'Number detected - start time assigned to sentence start time', {word["word"]})
                    else:
                        word["start"] = sentence["words"][index-1]["end"]
                        print(f'Number detected - start time assigned to previous word end time', {word["word"]})
                    if index == len(sentence["words"])-1:
                        # if a number is the last word in a sentence, we need to run the text to speech function on just that word, then assign the end time to the start time + length of the output from the text to speech function
                        text_to_speech(word["word"], "workspace/v5/temp/temp-number.mp3")
                        length = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", "workspace/v5/temp/temp-number.mp3"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
                        length = float(length.stdout)
                        word["end"] = sentence["start"] + length
                        print(f'Number detected - end time assigned using magic.', word["word"])
                    else:
                        word["end"] = sentence["words"][index+1]["start"] # 3d arrays omgggg
                        print(f'Number detected - end time assigned to next word start time', word["word"])
        print('JSON data is good.')
    with open("workspace/v5/temp/voicedata.json", "w") as f:
        json.dump(jsondata, f, indent=4)

    # FINALLY WE CAN DO THE THING
    with open("workspace/v5/temp/voicedata.json", "r") as f:
        voicedata = json.load(f)
    chunks = []
    script = ""
    for sentence in voicedata:
        sentencetemp = ""
        for word in sentence["words"]:
            sentencetemp += word["word"] + " "
        script += sentencetemp
    print(script)
    chunk = ""
    for word in script.split():
        if len(chunk) + len(word) <= chunk_length:
            chunk += word + " "
        else:
            chunks.append(chunk)
            chunk = ""
            chunk += word + " "
    chunks.append(chunk)

    chunks_json = {}
    for chunk in chunks:
        chunks_json[chunk] = {}
        chunks_json[chunk]["words"] = []
        for word in chunk.split():
            chunks_json[chunk]["words"].append(word)

    chunks = json.dumps(chunks_json, indent=2)
    chunks_json = json.loads(chunks)

    # NOW WE NEED TO ADD THE TIMINGS AHHHHH
    # BUN THIS STUPID CODE
    with open("workspace/v5/temp/voicedata.json", "r") as f:
        print(type(chunks_json))
        for chunk in chunks_json:
            chunk_json = chunks_json[chunk]
            print(type(chunk_json))
            for word in chunk_json["words"]:
                index = chunk_json["words"].index(word)
                voicedata_list = json.load(f)
                voicedata = voicedata_list[0]
                for sentence in voicedata_list:
                    for sentenceword in sentence["words"]:
                        if sentenceword["word"] == chunk_json["words"][index]:
                            wordStart = sentenceword["start"]
                            wordEnd = sentenceword["end"]
                            print(wordStart)
                            print(wordEnd)
                            chunk_json["words"][index] = {'start': wordStart, 'end': wordEnd, 'word': word}
        chunk_json = chunks_json[chunk]
        chunk_json["start"] = chunk_json["words"][0]["start"]
        chunk_json["end"] = chunk_json["words"][-1]["end"]
        print(chunk_json["start"])
        print(chunk_json["end"])
                    
    print('JSON data is all good.')
    with open("workspace/v5/temp/chunks.json", "w") as f:
        json.dump(chunks_json, f, indent=4)
    print('JSON data saved.')

# Function to format time in HH:MM:SS.mmm format
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:06.3f}"

def generate_subtitle_file():
    json_file_path = 'workspace/v5/temp/chunks.json'
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    
    output_file = 'workspace/v5/temp/subtitles.ass'

    with open(output_file, 'w', encoding='utf-8') as subtitle_file:
        # Write subtitle file header
        subtitle_file.write('[Script Info]\n')
        subtitle_file.write('ScriptType: v4.00+\n\n')

        subtitle_file.write('[Events]\n')
        subtitle_file.write('Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')

        # Iterate through each text block in the JSON data
        for text_block, data in json_data.items():
            start_time = data['start']
            end_time = data['end']

            # Iterate through each word in the text block
            for word_data in data['words']:
                word_start = word_data['start']
                word_end = word_data['end']
                word_text = word_data['word']

                word_start_time = start_time + word_start
                word_end_time = start_time + word_end
                word_start_time = format_time(word_start_time)
                word_end_time = format_time(word_end_time)


                # Write word-level entry to subtitle file
                subtitle_file.write(
                    'Dialogue: 0,{},{},Default,,0,0,0,,{}\n'.format(
                        word_start_time, word_end_time, word_text
                    )
                )

    print(f'Subtitle file "{output_file}" has been generated successfully.')

def burn_subtitles():
    input_video_path = 'workspace/v5/temp/background.mp4'
    subtitle_file_path = 'workspace/v5/temp/subtitles.ass'
    output_video_path = 'workspace/v5/temp/background_subbed.mp4'
    cmd = [
        'ffmpeg', '-y',
        '-hwaccel', 'cuda',
        '-i', input_video_path,
        '-vf', f'ass={subtitle_file_path}',
        '-an',
        output_video_path
    ]
    

    subprocess.run(cmd)

    # cmd = 

def combine_audio_video():
    audio_path = 'workspace/v5/temp/voicedata.mp3'
    video_path = 'workspace/v5/temp/background_subbed.mp4' # yo
    output_path = 'workspace/v5/output/output.mp4'

    # ffmpeg command to combine audio and video
    command = [
        'ffmpeg', '-y',
        '-i', video_path,
        '-i', audio_path,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-shortest',  # Ensure that the output is at least as long as the input audio
        output_path
    ]

    # Run the subprocess command
    subprocess.run(command
                   )
# generate_subtitle_file()
burn_subtitles()
combine_audio_video()
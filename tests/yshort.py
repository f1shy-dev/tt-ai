import ffmpeg
import whisperx
from ttai_farm.v4.write_ass import write_adv_substation_alpha
from ttai_farm.v4.tts import text_to_speach
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
from rich.prompt import Confirm
import os
import subprocess
import openai
from rich.console import Console
import json
import random
console = Console()
openai.api_key = os.environ.get(
    "OPENAI_API_KEY")
console.log(f"[grey46]Loaded OpenAI API Key: {openai.api_key[:8]}")


BG_CLIP = './bg-sand.mp4'
DEVICE = "cuda"
BATCH_SIZE = 16  # reduce if low on GPU mem
COMPUTE_TYPE = "float16" # float16 if using gpu
MODEL_NAME = 'base'
FT_MODEL = "ft:gpt-3.5-turbo-0613:personal::8HNFjrTY"
ALIGN_MODEL = "WAV2VEC2_ASR_BASE_960H" # jonatasgrosman/wav2vec2-large-xlsr-53-english
MAX_WORDS_PER_SEG = 5
BACKGROUND_DIR = './workspace/bg-vids'

console.log("[grey46]Done loading imports...")

# open file for writing packlist
with console.status("Collating background videos...") as s:
    with open('workspace/temp/ffmpeg-packlist-bg.txt', 'w') as packlist_file:
        videos = os.listdir(BACKGROUND_DIR)
        random.shuffle(videos)
        duration = 0
        for idx, video in enumerate(videos):
            s.update(f"Collating background videos... (processing #{idx}/{len(videos)} - at {duration}s duration)")
            if video.startswith('random-'):
                vid_duration = float(ffmpeg.probe(os.path.join(BACKGROUND_DIR, video))['format']['duration'])
                print(vid_duration, os.path.join(BACKGROUND_DIR, video))
                duration += vid_duration
                start_time = random.uniform(0, duration - 10)
                output_cmd = ['ffmpeg', '-y', '-ss', f'{start_time}', '-i', f"'{os.path.join(BACKGROUND_DIR, video)}'", '-t', '10', '-c', 'copy', f"'workspace/temp/bg-{idx}.mp4'"]
                
                ffresult = subprocess.run(output_cmd, capture_output=True)
                assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"

            elif video.startswith('whole-'):
                vid_duration = float(ffmpeg.probe(os.path.join(BACKGROUND_DIR, video))['format']['duration'])
                vid_duration = min(vid_duration, 10)
                duration += vid_duration
                output_cmd = ['ffmpeg','-y', '-i', f'{os.path.join(BACKGROUND_DIR, video)}', '-t', f'{duration}', '-c', 'copy', f'workspace/temp/bg-{idx}.mp4']
                ffresult = subprocess.run(output_cmd, capture_output=True)
                assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
            packlist_file.write(f"file bg-{idx}.mp4\n")
            if duration >= 70:
                break
        packlist_file.close()
    s.update("Merging background videos...")
    merge_cmd = ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'workspace/temp/ffmpeg-packlist-bg.txt', '-an', '-vf', 'crop=ih*(9/16):ih', '-t', '70', 'workspace/temp/bg-merge.mp4']
    ffresult = subprocess.run(merge_cmd, capture_output=True)
    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"


prompt = """you are generating a script for a social media short/reel about facts.
the topic for the facts is just "random/interesting facts".
make sure to include:
    * hooks to social media features like "like and follow for more facts" or "comment your favorite fact below", or "follow since you'll never see me again".
    * end the video with a form of hook like "and so" then start the video with "here are ..." since the video loops, so it will seem like it's a never ending list of facts to increase watch time
    * in total, around 10 facts+hooks - minimum 2 hooks
    * the title of the video - with emojis, ellipses, question marks, exclamation marks, hashtags, etc

format in JSON like so:
{
    "title": "<title>",
    "content": [
        {"text": "<fact>", "type": "fact"},
        {"text": "<fact>", "type": "fact"},
        {"text": "<hook>", "type": "hook"},
        //... and so on
    ]
}"""
console.log(f"[grey46]Generating script w/ model {FT_MODEL}...")

def gpt_loop(tries = 0):
    response = openai.ChatCompletion.create(
        model=FT_MODEL,
        messages=[{"role": "system", "content": prompt}],
        temperature=0.68,
        max_tokens=512,
        frequency_penalty=0.32,
        presence_penalty=0.12,
    )
    usage_tk = response["usage"]
    prompt_tk = int(usage_tk['prompt_tokens'])
    comp_tk = int(usage_tk['completion_tokens'])
    console.log(
        f"Used {prompt_tk} prompt + {comp_tk} completion ({usage_tk['total_tokens']} total ~ ${(prompt_tk/1000*0.012) + (comp_tk/1000*0.016)}) tokens.")
    content = response["choices"][0]["message"]["content"]

    try:
        data = json.loads(content)
        print(data, file=open('workspace/temp/data.json', 'w'))
        return data
    except Exception as e:
        if tries > 3:
            raise ValueError('Content generated is not valid json')
        else:
            console.log(f'[red]Content generated is not valid json, trying again ({tries}/3)...')
            gpt_loop(tries + 1)

data = gpt_loop()
joined = ''
for idx, line in enumerate(data['content']):
    if line['text'].strip() == '':
        continue
    color = 'red' if line['type'] == 'hook' else 'medium_purple3'
    joined += f'[{color}]{line["text"]}[/{color}]\n'

console.print(joined)
assert Confirm.ask('Is this script good?')


console.log(
    f"[grey46]Loading models whisperx:{MODEL_NAME}, align:{ALIGN_MODEL}")
model = whisperx.load_model(
    MODEL_NAME, DEVICE, compute_type=COMPUTE_TYPE, language='en', threads=16)
model_a, metadata = whisperx.load_align_model(
    language_code='en', device=DEVICE, model_name=ALIGN_MODEL)

os.makedirs('workspace/temp', exist_ok=True)

console.log('[grey46]Converting text to speech...')
text_to_speach(joined, f'workspace/temp/tts.mp3')

console.log("[grey46]Loading audio to tensor...")
audio = whisperx.load_audio(
    'workspace/temp/tts.mp3')

console.log("Transcribing audio...")
result = model.transcribe(
    audio, batch_size=BATCH_SIZE, language='en')


console.log("Aligning audio...")
result = whisperx.align(
    result["segments"], model_a, metadata, audio, DEVICE)
formatted_segs = result['segments']
words = []
comp_segs = []

print(json.dumps(formatted_segs), file=open('workspace/temp/formatted_segs.json', 'w'))
for segm in formatted_segs:
    words += [
        {
            "word": w['word'],
            "start": float(w['start']) if 'start' in w else None,
            "end": float(w['end']) if 'end' in w else None,
            "score": float(w['score']) if 'score' in w else None,
        } for w in segm['words']
    ]
has_split = False
for idx, word in enumerate(words):
    if idx % MAX_WORDS_PER_SEG == 0:
        has_split = False
    if not has_split:
        if 'start' in word and word['start'] is not None:
            comp_segs.append({
                "text": "",
                "start": word['start'],
                "end": word['end'],
                "words": []
            })
            has_split = True
    comp_segs[-1]['text'] += word['word'] + " "
    comp_segs[-1]['words'].append(word)
    comp_segs[-1]['end'] = word['end'] if word['end'] is not None else comp_segs[-1]['end']

console.log("[grey46]Generating subtitle file...")
ass_content = write_adv_substation_alpha(
    comp_segs, 
    Fontname='Dela Gothic One',
    BackColor='&H80000000', Spacing='0.2', Outline='0', Shadow='0.75', Fontsize='12',
    Alignment='5',
    MarginL='10',
    MarginR='10',
    MarginV='10')

with open('./workspace/temp/subs.ass', 'w') as f:
    f.write(ass_content)

with console.status("Merging background video and audio + cropping...") as s:
    ffresult = subprocess.run(['ffmpeg', '-i', './workspace/temp/bg-merge.mp4', '-i', './workspace/temp/tts.mp3', '-y', '-vf', 'crop=ih*(9/16):ih',
                            '-c:a', 'aac', '-map', '0:v:0', '-map', '1:a:0', '-shortest', './workspace/temp/bg_with_tts_audio.mp4'], capture_output=True)
    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"

    s.update("Burning subs onto video...")
    ffresult = subprocess.run(['ffmpeg', '-i', './workspace/temp/bg_with_tts_audio.mp4',
                            '-vf', "ass=./workspace/temp/subs.ass:fontsdir='fonts'",
                            '-y', '-c:a', 'copy', './workspace/temp/final.mp4'], capture_output=True)
    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"

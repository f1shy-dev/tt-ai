import datetime
import ffmpeg
import whisperx
from ttai_farm.v4.write_ass import write_adv_substation_alpha
from ttai_farm.v4.tts import text_to_speach
import os
import subprocess
from openai import OpenAI
from rich.console import Console
from rich.prompt import Confirm
import json
import random
import torch
console = Console()
client = OpenAI()

#fmt: off
BG_CLIP = './bg-sand.mp4'
DEVICE = "cuda"
BATCH_SIZE = 1  # reduce if low on GPU mem
COMPUTE_TYPE = "float16"  # float16 if using gpu
MODEL_NAME = 'medium' # jonatasgrosman/wav2vec2-large-xlsr-53-english
FT_MODEL = "ft:gpt-3.5-turbo-1106:personal:farm-chan:8IVnpqJi" # gpt-3.5-turbo-1106
ALIGN_MODEL = "WAV2VEC2_ASR_BASE_960H"
MAX_WORDS_PER_SEG = 2
BACKGROUND_DIR = './workspace/bg-vids'
OUT_DIR = './workspace/clips/yshort'
TEMP_DIR = './workspace/temp'
SAVE_ANALYSIS_DIR = './workspace/temp/saves'
WATERMARK_IMG = "watermarks/f-plug-wm.png"
PROMPT = "@facts.r9.txt"
#fmt: on

[os.makedirs(x, exist_ok=True) for x in [TEMP_DIR, SAVE_ANALYSIS_DIR, OUT_DIR]]

if not torch.cuda.is_available():
    BATCH_SIZE = 1
    COMPUTE_TYPE = 'int8'
    DEVICE = 'cpu'

console.log("[grey46]Done initalising...")

common_topics = [
    ["random facts", ["random/interesting facts/curiosities"]],
    ['love/relationships', ['signs she likes you',
                            'signs he likes you', 'signs they hate you']],
    ['girls/boys', ['things girls dont want you to know', 'things boys dont want you to know',
                    'things girls should know about boys', 'the girls want you to know that']],
    ['save your life', ['save your life']],
]


def script_loop():
    console.print("")
    for idx, tpk in enumerate(common_topics):
        console.print(f"[light_steel_blue](#{idx}) {tpk[0]}")
    console.print(f"[light_steel_blue](#666) load last analysis from file")
    console.print(f"[light_steel_blue](#999) custom topic")

    topic_idx = int(console.input("[medium_purple3]Enter topic: "))
    topic = ''
    if topic_idx == 999:
        topic = console.input("[medium_purple3]Enter topic title: ")
    elif topic_idx != 666:
        topic = random.choice(common_topics[topic_idx][1])
    console.log(f"[grey46]Generating script w/ model {FT_MODEL}...")

    def gpt_loop(tries=0):
        response = client.chat.completions.create(
            model=FT_MODEL,
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7,
            max_tokens=512,
            frequency_penalty=0.07,
            presence_penalty=0.07,
            response_format={"type": "json_object"}
        )
        prompt_tk = int(response.usage.prompt_tokens)
        comp_tk = int(response.usage.completion_tokens)
        console.log(
            f"Used {prompt_tk} prompt + {comp_tk} completion ({response.usage.total_tokens} total ~ ${(prompt_tk/1000*0.003) + (comp_tk/1000*0.006)}) tokens.")
        content = response.choices[0].message.content

        try:
            data = json.loads(content)
            print(content, file=open(
                f'{SAVE_ANALYSIS_DIR}/analysis-{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json', 'w'))
            return data
        except Exception as e:
            if tries > 3:
                raise ValueError('Content generated is not valid json')
            else:
                console.log(
                    f'[red]Content generated is not valid json, trying again ({tries}/3)...')
                return gpt_loop(tries + 1)

    if PROMPT.startswith("@"):
        file_path = os.path.join(os.path.dirname(
            __file__), f"../ttai_farm/analysis/prompts/{PROMPT[1:]}")
        prompt = open(file_path, "r").read()
    elif PROMPT.startswith("#"):
        file_path = PROMPT[1:]
        prompt = open(file_path, "r").read()
    else:
        prompt = PROMPT

    prompt = prompt.replace('{_{0}_}', topic)

    if topic_idx == 666:
        if os.system("command -v fzf >/dev/null 2>&1") == 0:
            file_path = os.popen(
                f"find {SAVE_ANALYSIS_DIR} -type f | fzf").read().strip()
        else:
            file_path = input("Enter file name: ")
        data = json.load(open(file_path, 'r'))
    else:
        data = gpt_loop()
    joined = ''
    for idx, line in enumerate(data['content']):
        if line['text'].strip() == '':
            continue
        color = 'red' if line['type'] == 'hook' else 'medium_purple3'
        joined += f'[{color}]{line["text"]}[/{color}]\n'

    console.print(joined)
    if not Confirm.ask('Is this script good?'):
        return script_loop()

    return data


data = script_loop()

with console.status("Collating background videos...") as s:
    packlist = []
    videos = os.listdir(BACKGROUND_DIR)
    random.shuffle(videos)
    rand_count = len([v for v in videos if v.startswith('random-')])
    whole_count = len([v for v in videos if v.startswith('whole-')])
    duration = 0

    for idx, video in enumerate(videos):
        s.update(
            f"Collating background videos... (processing #{idx}/{len(videos)} - at {duration}s duration)")
        if video.startswith('random-'):
            vid_duration = float(ffmpeg.probe(os.path.join(
                BACKGROUND_DIR, video))['format']['duration'])
            # print(vid_duration, os.path.join(BACKGROUND_DIR, video))
            back_dur = 20 if vid_duration > 100 else 7

            start_time = 3 if vid_duration < 100 else random.uniform(
                0, vid_duration - back_dur)
            duration += back_dur
            output_cmd = ['ffmpeg', '-y', '-ss', f'{start_time}', '-i', f'{os.path.join(BACKGROUND_DIR, video)}', '-t', f'{back_dur}',
                          '-vf', 'crop=ih*(9/16):ih', '-c:v', 'libx264', '-crf', '18', '-b:v', '8000k', '-r', '30', '-preset', 'medium',
                          f'workspace/temp/bg-{idx}.mp4']

            ffresult = subprocess.run(output_cmd, capture_output=True)
            assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}\n\n$> {' '.join(output_cmd)}"

        elif video.startswith('whole-'):
            vid_duration = float(ffmpeg.probe(os.path.join(
                BACKGROUND_DIR, video))['format']['duration'])
            vid_duration = min(vid_duration, 10)
            duration += vid_duration
            output_cmd = [
                'ffmpeg', '-y', '-i', f'{os.path.join(BACKGROUND_DIR, video)}', '-t', f'{duration}',
                '-vf', 'crop=ih*(9/16):ih', '-c:v', 'libx264', '-crf', '18', '-b:v', '8000k', '-r', '30', '-preset', 'medium',
                f'workspace/temp/bg-{idx}.mp4']
            ffresult = subprocess.run(output_cmd, capture_output=True)
            assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}\n\n$> {' '.join(output_cmd)}"
        packlist.append(f"file bg-{idx}.mp4")
        if duration >= 70:
            break

    s.update("Merging background videos...")
    with open('workspace/temp/ffmpeg-packlist-bg.txt', 'w') as packlist_file:
        packlist_file.write('\n'.join(packlist))

    merge_cmd = ['ffmpeg', '-y', '-f', 'concat', '-i', 'workspace/temp/ffmpeg-packlist-bg.txt',
                 '-an', '-c:v', 'copy', '-t', '70', 'workspace/temp/bg-merge.mp4']
    ffresult = subprocess.run(merge_cmd, capture_output=True)
    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}\n\n$> {' '.join(merge_cmd)}"
    console.log("Generated background video...")

console.log(
    f"[grey46]Loading models whisperx:{MODEL_NAME}, align:{ALIGN_MODEL}")
model = whisperx.load_model(
    MODEL_NAME, DEVICE, compute_type=COMPUTE_TYPE, language='en', threads=16)
model_a, metadata = whisperx.load_align_model(
    language_code='en', device=DEVICE, model_name=ALIGN_MODEL)

os.makedirs('workspace/temp', exist_ok=True)

console.log('[grey46]Converting text to speech...')
joined_tts = '\n'.join([line['text']
                       for line in data['content'] if line['text'].strip() != ''])
text_to_speach(joined_tts, f'workspace/temp/tts.mp3')

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

print(json.dumps(formatted_segs), file=open(
    'workspace/temp/formatted_segs.json', 'w'))
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
    font_size=18,
    color='00FFFF',
    underline=False,
    Fontname='Dela Gothic One',
    BackColor='&H80000000', Spacing='0.2', Outline='0', Shadow='0.75', Fontsize='18',
    Alignment='5',
    # MarginL='10',
    # MarginR='10',
    MarginV='170')

with open('./workspace/temp/subs.ass', 'w') as f:
    f.write(ass_content)

with console.status("Merging background video and audio + cropping...") as s:
    os.makedirs(OUT_DIR, exist_ok=True)
    ffresult = subprocess.run(['ffmpeg', '-i', './workspace/temp/bg-merge.mp4', '-i', './workspace/temp/tts.mp3', '-y', '-vf', 'crop=ih*(9/16):ih',
                               '-c:a', 'aac', '-map', '0:v:0', '-map', '1:a:0', '-shortest', './workspace/temp/bg_with_tts_audio.mp4'], capture_output=True)
    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
    console.log("Merged bg video and audio...")
    s.update("Burning subs onto video...")

    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    final_output = f"{OUT_DIR}/short_{current_time}.mp4"

    ffresult = subprocess.run(['ffmpeg', '-i', './workspace/temp/bg_with_tts_audio.mp4',
                               '-vf', "ass=./workspace/temp/subs.ass:fontsdir='fonts'",
                               '-y', '-c:a', 'copy', './workspace/temp/subbed.mp4'], capture_output=True)

    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
    console.log("Subtitled video...")

    s.update("Watermarking video...")
    ffresult = subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        './workspace/temp/subbed.mp4',
        "-i",
        WATERMARK_IMG,
        "-filter_complex",
        # center watermark, make it 512x512 (image is 1024x1024)
        "[1]format=rgba,colorchannelmixer=aa=0.6[logo];[logo][0]scale2ref=oh*mdar:ih*0.1[logo][video];[video][logo]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2+525",

        "-c:a",
        "copy",
        # "crf", "18",
        final_output
    ], capture_output=True)
    assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
    console.log("Watermarked video...Done!")

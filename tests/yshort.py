import whisperx
import torch
from ttai_farm.v4.write_ass import write_adv_substation_alpha
from ttai_farm.v4.tts import text_to_speach
# import whisperx
import gc
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
from rich.prompt import Confirm
import os
import yt_dlp
import subprocess
import openai
from rich.console import Console
import json
console = Console()

BG_CLIP = './bg-sand.mp4'

console.log("importing done")
openai.api_key = 'sk-' or os.environ.get(
    "OPENAI_API_KEY")

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

# response = openai.ChatCompletion.create(
#     model="ft:gpt-3.5-turbo-0613:personal::8HNFjrTY",
#     messages=[{"role": "system", "content": prompt}],
#     temperature=0.68,
#     max_tokens=512,
#     frequency_penalty=0.32,
#     presence_penalty=0.12,
# )

# content = response.choices[0].message.content
content = """
{
    "title": "Random Facts You Didn't Know 10 👀",
    "content": [
        {
            "text": "If you're stranded in the desert, eating a snake will give you enough hydration to walk for an extra three days.",
            "type": "fact"
        },
        {
            "text": "Random facts.",
            "type": "fact"
        },
        {
            "text": "More than 3,000 new species are discovered each year.",
            "type": "fact"
        },
        {
            "text": "Curly fries were invented in Greece, not America.",
            "type": "fact"
        },
        {
            "text": "You're more likely to get a virus from visiting religious sites than adult sites.",
            "type": "fact"
        },
        {
            "text": "The Bible is the most stolen book in the world.",
            "type": "fact"
        },
        {
            "text": "A lot of people died while trying to climb Mount Everest, and now their bodies are just used as landmarks.",
            "type": "fact"
        },
        {
            "text": "Before matches were invented, people would use a tiny hammer to ignite a small piece of wood with chemicals on it.",
            "type": "fact"
        },
        {
            "text": "Most lipstick contains fish scales.",
            "type": "fact"
        },
        {
            "text": "Sharks kill fewer people per year than vending machines do.",
            "type": "fact"
        },
        {
            "text": "'I love you' was first said by Yoko Ono in a letter to John Lennon that read, 'When you sleep, you look like a beautiful monkey.'",
            "type": "fact"
        },
        {
            "text": "Like and follow for more interesting facts.",
            "type": "hook"
        }
    ]
}
"""

try:
    data = json.loads(content)
    print(data, file=open('workspace/temp/data.json', 'w'))
except Exception as e:
    console.log(content)
    raise ValueError('content generated is not valid json')

joined = '\n'.join(
    [f"{c['text']}" for c in data['content'] if c['text'].strip() != ''])
console.print(joined)
assert Confirm.ask('is this ok?')

DEVICE = "cpu"
BATCH_SIZE = 1  # reduce if low on GPU mem
# change to "int8" if low on GPU mem (may reduce accuracy)
COMPUTE_TYPE = "int8"
MODEL_NAME = 'base'

console.log(
    f"loading models whisperx:{MODEL_NAME}, align:wav2vec2-large-xlsr-53-english")
model = whisperx.load_model(
    MODEL_NAME, DEVICE, compute_type=COMPUTE_TYPE, language='en', threads=16)
model_a, metadata = whisperx.load_align_model(
    language_code='en', device=DEVICE)

# , model_name='jonatasgrosman/wav2vec2-large-xlsr-53-english'
aligned_segs = []
os.makedirs('workspace/temp', exist_ok=True)
# for idx, line in enumerate(data['content']):
#     if line['text'].strip() == '':
#         continue

#     console.log(f"generating tts for {len(line['text'].split(' '))} words...")
#     # text_to_speach(line['text'], f'workspace/temp/lc-{idx}.mp3')

#     # get length of audio with ffprobe
#     ffout = subprocess.run(['ffprobe', '-i', f'workspace/temp/lc-{idx}.mp3',
#                             '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")], capture_output=True)
#     duration = float(ffout.stdout)
#     console.log(f"duration: {duration}")

#     # console.log("loading audio...")
#     audio = whisperx.load_audio(
#         f'workspace/temp/lc-{idx}.mp3')
#     # console.log("aligning...")
#     result = whisperx.align(
#         [{
#             "text": line['text'],
#             "start": 0,
#             "end": duration
#         }], model_a, metadata, audio, DEVICE, return_char_alignments=False, print_progress=False)
#     segs = result['segments']
#     console.log(f'loaded+aligned into {len(segs[0]["words"])} words')

#     aligned_segs.append({
#         "text": line['text'],
#         "start": 0,
#         "end": duration,
#         'aligned': segs,
#         'filename': f'lc-{idx}.mp3'
#     })
#     print()

# SILENCE_DURATION = 0

text_to_speach(joined, f'workspace/temp/tts.mp3')
console.log("loading audio...")
audio = whisperx.load_audio(
    'workspace/temp/tts.mp3')
console.log("transcribing...")
result = model.transcribe(
    audio, batch_size=BATCH_SIZE, language='en', print_progress=True)
# print(result["segments"])  # before alignment

# gc.collect()
# torch.cuda.empty_cache()


console.log("aligning...")
result = whisperx.align(
    result["segments"], model_a, metadata, audio, DEVICE)
formatted_segs = result['segments']
# console.log("creating silence.mp3...")
# # ensure overwrite
# ffresult = subprocess.run(['ffmpeg', '-f', 'lavfi', '-i',
#                            'anullsrc=channel_layout=stereo:sample_rate=44100',  '-y',
#                            '-t', str(SILENCE_DURATION), '-q:a', '1', 'workspace/temp/silence.mp3'], capture_output=True)
# assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
#####################
# print(json.dumps(aligned_segs), file=open('workspace/temp/al_segs.json', 'w'))
# formatted_segs = []
# ffmpeg_packlist = open('workspace/temp/ffmpeg_packlist.txt', 'w')
# for idx, seg in enumerate(aligned_segs):
#     offset = SILENCE_DURATION + formatted_segs[-1]['words'][-1]['end'] if len(
#         formatted_segs) > 0 else 0
#     assert len(seg['aligned']) == 1
#     formatted_segs.append({
#         "text": seg['aligned'][0]['text'],
#         "start": float(seg['aligned'][0]['start']) + offset,
#         "end": float(seg['aligned'][0]['end']) + offset,
#         "words": [{
#             "word": w['word'],
#             "start": float(w['start']) + offset if 'start' in w else None,
#             "end": float(w['end']) + offset if 'end' in w else None,
#             "score": float(w['score']) if 'score' in w else None,
#         } for w in seg['aligned'][0]['words']]
#     })
#     ffmpeg_packlist.write(
#         # f"file '{seg['filename']}'\nfile 'silence.mp3'\n")
#         f"file '{seg['filename']}'\n")
#####################
# ffmpeg_packlist.close()
# print(json.dumps(formatted_segs), file=open('workspace/temp/segs.json', 'w'))
MAX_WORDS_PER_SEG = 5
words = []
comp_segs = []
# for segm in formatted_segs:
#     words += [
#         {
#             "word": w['word'],
#             "start": float(w['start']) if 'start' in w else None,
#             "end": float(w['end']) if 'end' in w else None,
#             "seg_start": float(segm['start']) if 'start' in segm else None,
#             "seg_end": float(segm['end']) if 'end' in segm else None,
#             "score": float(w['score']) if 'score' in w else None,
#         } for w in segm['words']
#     ]
# # for idx, word in enumerate(words):
# #     if idx % MAX_WORDS_PER_SEG == 0:
# #         comp_segs.append({
# #             "text": "",
# #             "start": word['start'] else word['seg_start'] else None,
# #             "end": word['end'] else word['seg_end'] else None,
# #             "words": [],
# #         })
# #     comp_segs[-1]['text'] += word['word'] + ' '
# #     comp_segs[-1]['words'].append(word)
# #     comp_segs[-1]['end'] = word['end'] if word['end'] is not None else comp_segs[-1]['end']

# print(json.dumps(comp_segs), file=open('workspace/temp/comp_segs.json', 'w'))
# sub_style = "Alignment=6,Fontname=Dela Gothic One,BackColour=&H80000000,Spacing=0.2,Outline=0,Shadow=0.75,PrimaryColour=&H00FFFFFF,Bold=1,MarginV=170,Fontsize=16"

ass_content = write_adv_substation_alpha(formatted_segs, Fontname='Dela Gothic One',
                                         BackColor='&H80000000', Spacing='0.2', Outline='0', Shadow='0.75', MarginV='170', Fontsize='16')

# console.log("mergging audio")
# ffresult = subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i',
#                            'workspace/temp/ffmpeg_packlist.txt', '-y', '-c', 'copy', 'workspace/temp/tts.mp3'], capture_output=True)
# assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
# console.log("loading audio...")
# audio = whisperx.load_audio(
#     'workspace/temp/tts.mp3')
# console.log("transcribing...")
# result = model.transcribe(
#     audio, batch_size=BATCH_SIZE, language='en', print_progress=True)
# # print(result["segments"])  # before alignment
# console.log("aligning...")
# result = whisperx.align(
#     result["segments"], model_a, metadata, audio, DEVICE, return_char_alignments=False, print_progress=True)
# segs = result['segments']


with open('./workspace/temp/subs.ass', 'w') as f:
    f.write(ass_content)


# delete audio from sand.mp4
# subprocess.run(['ffmpeg', '-i', './temp/sand.mp4', '-ss', '00:00:00',
#                '-t', '00:05:00', '-c:v', 'copy', '-an', './temp/sand_no_audio.mp4'])

# add audio from tts.mp3
console.log("merging audio + tts")
ffresult = subprocess.run(['ffmpeg', '-i', './workspace/temp/sand_no_audio.mp4', '-i', './workspace/temp/tts.mp3', '-y', '-vf', 'crop=ih*(9/16):ih',
                           '-c:a', 'aac', '-map', '0:v:0', '-map', '1:a:0', '-shortest', './workspace/temp/sand_with_tts_audio.mp4'], capture_output=True)
assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"
console.log("merge subs ")
ffresult = subprocess.run(['ffmpeg', '-i', './workspace/temp/sand_with_tts_audio.mp4',
                           '-vf', "ass=./workspace/temp/subs.ass:fontsdir='/Users/vrishank/Documents/tt-farm-v2/fonts'",
                           '-y', '-c:a', 'copy', './workspace/temp/combine.mp4'])
assert ffresult.returncode == 0, f"ffmpeg failed: {ffresult.stderr}"

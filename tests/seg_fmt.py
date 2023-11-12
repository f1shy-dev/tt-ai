from ttai_farm.v4.write_ass import write_adv_substation_alpha
from rich.console import Console
import json
console = Console()

with open(
        'workspace/temp/formatted_segs.json', 'r') as file_h:
    formatted_segs = json.loads(file_h.read())

words = []
comp_segs = []
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
    if idx % 3 == 0:
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

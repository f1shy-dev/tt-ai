<<<<<<< HEAD
import re
import tiktoken
import random
import textwrap
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import os
from rich.console import Console
import json
console = Console()
DATA_DIR = "./yshorts/data"
OUT_FILE = "./yshorts/combine.jsonl"
out_file = open(OUT_FILE, 'w')
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")


def replace_unicode_escapes(match):
    print(match)
    return chr(int(match.group(1), 16))


files = os.listdir(DATA_DIR)
total_tokens = 0
total_wrote = 0
with Progress(
    SpinnerColumn(),
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    TextColumn("[bold yellow]{task.fields[status]}", justify="right"),
    MofNCompleteColumn(),
    console=console,
    transient=True,
) as progress:
    task = progress.add_task(
        "Processing",
        total=len(files),
        filename="",
        status="starting",
    )
    random.shuffle(files)
    for i, filename in enumerate(files):
        if total_wrote > 100 - 1:
            break
        progress.update(task, filename=filename, status="processing")
        with open(os.path.join(DATA_DIR, filename)) as f:
            data = json.load(f)

            transcript = data['transcribe']['segments']
            text = '\n'.join([seg['text'] for seg in transcript])
            ttitle = data['title'].lower()
            probably_random_incl = [
                'random',
                'didn\'t know',
                'didn\'t realize',
                'never could have guessed',
                'interesting facts',
                'blow your mind'
            ]
            if 'finger down' in ttitle:
                console.log(f'[red]skipping {filename} (finger down)')
                continue
            elif any([p in ttitle for p in probably_random_incl]):
                ttitle = 'random/interesting facts'
            else:
                splitters = ['that could', 'that can', 'that will', 'that would', 'that should',
                             'that might', 'that must', 'that shall', 'that ought', 'that may', 'about', 'this video can', 'this video will', 'potentially']
                for splitter in splitters:
                    if splitter in ttitle:
                        ttitle = ttitle.split(splitter)
                        ttitle = ttitle.pop()
                        break
                replace = ['👀', '😱', '...', '?', "!", '😳', '(pt.1)', '🤯']
                for r in replace:
                    ttitle = ttitle.replace(r, '')
                ttitle = ttitle.replace('-', ' ')
                ttitle = ttitle.split("#").pop(0).strip()

            facts_prompt = """you are generating a script for a social media short/reel about facts.
the topic for the facts is just "{0}".
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
            facts_prompt = textwrap.dedent(facts_prompt)
            sentences = [s['text'].strip() for s in transcript]
            hook_words = ['subscribe', 'share', 'follow', 'comment']

            # def enc(ij): return re.sub(
            #     r'\\u([0-9a-fA-F]{4})', replace_unicode_escapes, ij).encode('utf-8', 'replace').decode()
            def enc(ij):
                # if '\\u' in ij:
                # print(ij)
                # return ij.encode('utf-8', 'replace').decode()
                return ij

            content = [{"text": enc(s), "type": "hook" if any(
                [hw in s for hw in hook_words]) else "fact"} for s in sentences]
            content = [c for c in content if c['text'] != '']
            if len(content) < 10:
                console.log(f'[red]skipping {filename} (<10 facts)')
                continue

            if len(content) > 18:
                console.log(f'[red]skipping {filename} (>18 facts)')
                continue

            sys_content_str = facts_prompt.replace('{0}', ttitle)
            ass_content_str = json.dumps({
                "title": enc(data['title']),
                # replace \u<> with
                "content": content
            }, ensure_ascii=False)
            out_str = json.dumps({
                'messages': [
                    {
                        'role': 'system',
                        'content': sys_content_str
                    },
                    {
                        'role': 'assistant',
                        'content': ass_content_str
                    }
                ]
            }, ensure_ascii=False) + '\n'
            # out_str = (out_str)
            tokens = encoding.encode(sys_content_str) + \
                encoding.encode(ass_content_str)
            if len(tokens) > 4096:
                console.log(f'[red]skipping {filename} (too long)')
                continue
            console.log(
                f'[green]{filename} - {len(content)} facts - {len(tokens)} tokens - {ttitle}')

            out_file.write(out_str)
            # print(out_str, file=out_file)
            total_tokens += len(tokens)
            total_wrote += 1
            progress.advance(task)


out_file.close()
console.log(
    f'[medium_purple3]wrote {total_wrote} - token size: {total_tokens}')
=======
import re
import tiktoken
import random
import textwrap
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import os
from rich.console import Console
import json
console = Console()
DATA_DIR = "./workspace/yshorts/data"
OUT_FILE = "./workspace/yshorts/combine.jsonl"
out_file = open(OUT_FILE, 'w')
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")


def replace_unicode_escapes(match):
    print(match)
    return chr(int(match.group(1), 16))


files = os.listdir(DATA_DIR)
total_tokens = 0
total_wrote = 0
skipped_too_long = 0
skipped_too_short = 0
skipped_other = 0
topics = {}

with Progress(
    SpinnerColumn(),
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    TextColumn("[bold yellow]{task.fields[status]}", justify="right"),
    MofNCompleteColumn(),
    console=console,
    transient=True,
) as progress:
    task = progress.add_task(
        "Processing",
        total=len(files),
        filename="",
        status="starting",
    )
    random.shuffle(files)
    for i, filename in enumerate(files):
        # if total_wrote > 100 - 1:
        #     break
        if total_tokens >= 140_000:
            break
        progress.update(task, filename=filename, status="processing")
        with open(os.path.join(DATA_DIR, filename)) as f:
            data = json.load(f)

            transcript = data['transcribe']['segments']
            text = '\n'.join([seg['text'] for seg in transcript])
            ttitle = data['title'].lower()
            probably_random_incl = [
                'random',
                'didn\'t know',
                'didn\'t realize',
                'never could have guessed',
                'interesting facts',
                'blow your mind'
            ]
            if 'finger down' in ttitle:
                console.log(f'[red]skipping {filename} (finger down)')
                continue
            elif any([p in ttitle for p in probably_random_incl]):
                ttitle = 'random/interesting facts/curiosities'
            else:
                splitters = ['that could', 'that can', 'that will', 'that would', 'that should',
                             'that might', 'that must', 'that shall', 'that ought', 'that may', 'about', 'this video can', 'this video will', 'potentially']
                for splitter in splitters:
                    if splitter in ttitle:
                        ttitle = ttitle.split(splitter)
                        ttitle = ttitle.pop()
                        break
                replace = ['👀', '😱', '...', '?', "!", '😳', '(pt.1)', '🤯']
                for r in replace:
                    ttitle = ttitle.replace(r, '')
                ttitle = ttitle.replace('-', ' ')
                ttitle = ttitle.split("#").pop(0).strip()

            facts_prompt = """you are generating a script for a social media short/reel about facts.
the topic for the facts is just "{0}".
make sure to include:
    * hooks to social media features like "like and follow for more facts" or "comment your favorite fact below"
    * end the video with either:
        * a hook like "and so" then start the video with "here are ..." since the video loops, so it will seem like it's a never ending list of facts to increase watch time
        * something like "follow since you'll never see me again" and a cliffhangery fact/statement
    * in total, around 10 facts+hooks - minimum 2 hooks
    * the title of the video - with emojis, ellipses, question marks, exclamation marks, hashtags, etc
    * facts that would be seen as 'outrageous'/'disturbing' - grabbing the audience's attention - something bizzare or really random if needed, depending on the topic

format in JSON like so:
{
    "title": "<title>",
    "content": [
        {"text": "<fact>", "type": "fact"},
        {"text": "<fact>", "type": "fact"},
        {"text": "<hook>", "type": "hook"},
        {"text": "<fact>", "type": "fact"},
        {"text": "<hook>", "type": "hook"},
        //... and so on
    ]
}"""
            facts_prompt = textwrap.dedent(facts_prompt)
            sentences = [s['text'].strip() for s in transcript]
            hook_words = ['subscribe', 'share', 'follow', 'comment']

            # def enc(ij): return re.sub(
            #     r'\\u([0-9a-fA-F]{4})', replace_unicode_escapes, ij).encode('utf-8', 'replace').decode()
            def enc(text, checkHash=False):
                # if '\\u' in ij:
                # print(ij)
                # return ij.encode('utf-8', 'replace').decode()
                if checkHash and '#' in text:
                    return ''
                return text

            content = [{"text": enc(s, True), "type": "hook" if any(
                [hw in s for hw in hook_words]) else "fact"} for s in sentences]
            prelen = len(content)
            content = [c for c in content if c['text'] != '']
            postlen = len(content)
            if prelen != postlen:
                console.log(
                    f'[red]skipping {filename} (removed {prelen - postlen} empty sentences)')
                skipped_other += 1
                continue
            if len(content) < 10:
                console.log(f'[red]skipping {filename} (<10 facts)')
                skipped_too_short += 1
                continue

            if len(content) > 18:
                console.log(f'[red]skipping {filename} (>18 facts)')
                skipped_too_long += 1
                continue

            ttitle_cpy = ttitle
            if 'shower thoughts' in ttitle_cpy:
                ttitle_cpy = 'shower thoughts'

            if 'girls' in ttitle_cpy:
                ttitle_cpy = 'girls'

            if 'boy' in ttitle_cpy:
                ttitle_cpy = 'boy(s)'
            topics[ttitle_cpy] = topics.get(ttitle_cpy, 0) + 1
            sys_content_str = facts_prompt.replace('{0}', ttitle)
            ass_content_str = json.dumps({
                "title": enc(data['title']),
                # replace \u<> with
                "content": content
            }, ensure_ascii=False)
            out_str = json.dumps({
                'messages': [
                    {
                        'role': 'system',
                        'content': sys_content_str
                    },
                    {
                        'role': 'assistant',
                        'content': ass_content_str
                    }
                ]
            }, ensure_ascii=False) + '\n'
            # out_str = (out_str)
            tokens = encoding.encode(sys_content_str) + \
                encoding.encode(ass_content_str)
            if len(tokens) > 4096:
                console.log(f'[red]skipping {filename} (too long)')
                continue
            console.log(
                f'[green]{filename} - {len(content)} facts - {len(tokens)} tokens - {ttitle}')

            out_file.write(out_str)
            # print(out_str, file=out_file)
            total_tokens += len(tokens)
            total_wrote += 1
            progress.advance(task)


out_file.close()
console.log(
    f'[medium_purple3]wrote {total_wrote} - token size: {total_tokens}')
# ski
console.log(
    f'[red]skipped {skipped_too_long} videos for >18 facts')

console.log(
    f'[red]skipped {skipped_too_short} videos for <10 facts')

console.log(
    f'[red]skipped {skipped_other} videos "other"')

console.print()

console.log(
    f'[medium_purple3 bold]topic distribution')

for topic, count in topics.items():
    console.log(
        f'[medium_purple3]  * {topic} - {count}')
>>>>>>> 9158c539ea44c648cdd581c047eda4ed6543f517

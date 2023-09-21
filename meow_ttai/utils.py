import os
from typing import Iterator, TextIO


def str2bool(string):
    string = string.lower()
    str2val = {"true": True, "false": False}

    if string in str2val:
        return str2val[string]
    else:
        raise ValueError(
            f"Expected one of {set(str2val.keys())}, got {string}")


def format_timestamp(seconds: float, always_include_hours: bool = False):
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    hours_marker = f"{hours}:" if always_include_hours or hours > 0 else ""
    return f"{hours_marker}{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


def write_srt(transcript: Iterator[dict], file: TextIO):
    for i, segment in enumerate(transcript, start=1):
        print(
            f"{i}\n"
            f"{format_timestamp(segment['start'], always_include_hours=True)} --> "
            f"{format_timestamp(segment['end'], always_include_hours=True)}\n"
            f"{segment['text'].strip().replace('-->', '->')}\n",
            file=file,
            flush=True,
        )


def write_compact_srt(transcript: Iterator[dict], file: TextIO):
    for i, segment in enumerate(transcript, start=1):
        print(
            f"[{format_timestamp(segment['start'], always_include_hours=True)} --> "
            f"{format_timestamp(segment['end'], always_include_hours=True)}] "
            f"{segment['text'].strip().replace('-->', '->')}",
            file=file,
            flush=True,
        )

def write_word_chunked_srts(transcript: Iterator[dict], srt_file: TextIO, csrt_file: TextIO, chars_per_chunk: int = 48):
    words = []
    for i, segment in enumerate(transcript, start=1):
        words = words + segment['words']

    # split words into chunks of x chars
    chunks = []
    chunk = []
    for word in words:
        if len(
            ''.join([word['word'] for word in chunk]).strip().replace('-->', '->')
        ) + len(word['word']) > chars_per_chunk:
            chunks.append(chunk)
            chunk = []
        chunk.append(word)
    chunks.append(chunk)

    # write chunks to srt

        # for i in range(0, len(words), words_per_chunk):
    #     chunk = words[i:min(i + words_per_chunk, len(words))]
    #     print(
    #         f"{i}\n"
    #         f"{format_timestamp(chunk[0]['start'], always_include_hours=True)} --> "
    #         f"{format_timestamp(chunk[-1]['end'], always_include_hours=True)}\n"
    #         f"{''.join([word['word'] for word in chunk]).strip().replace('-->', '->')}\n",
    #         file=srt_file,
    #         flush=True,
    #     )
    #     print(
    #         f"[{format_timestamp(chunk[0]['start'], always_include_hours=True)} --> "
    #         f"{format_timestamp(chunk[-1]['end'], always_include_hours=True)}] "
    #         f"{''.join([word['word'] for word in chunk]).strip().replace('-->', '->')}",
    #         file=csrt_file,
    #         flush=True,
    #     )
    #     if i + words_per_chunk >= len(words):
    #         break

    # rewrite to use chars_per_chunk instead of words_per_chunk

    for chunk in chunks:
        print(
            f"{i}\n"
            f"{format_timestamp(chunk[0]['start'], always_include_hours=True)} --> "
            f"{format_timestamp(chunk[-1]['end'], always_include_hours=True)}\n"
            f"{''.join([word['word'] for word in chunk]).strip().replace('-->', '->')}\n",
            file=srt_file,
            flush=True,
        )
        print(
            f"[{format_timestamp(chunk[0]['start'], always_include_hours=True)} --> "
            f"{format_timestamp(chunk[-1]['end'], always_include_hours=True)}] "
            f"{''.join([word['word'] for word in chunk]).strip().replace('-->', '->')}",
            file=csrt_file,
            flush=True,
        )

        

        

def filename(path):
    return os.path.splitext(os.path.basename(path))[0]

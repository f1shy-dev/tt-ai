from typing import Callable, TextIO, Iterator, Tuple
import pandas as pd
import numpy as np


def write_adv_substation_alpha(transcript: Iterator[dict],
                               #   file: TextIO,
                               resolution: str = "word",
                               color: str = None, underline=True,
                               prefmt: str = None, suffmt: str = None,
                               font: str = None, font_size: int = 12,
                               strip=True, **kwargs):
    """
    Credit: https://github.com/jianfch/stable-ts/blob/ff79549bd01f764427879f07ecd626c46a9a430a/stable_whisper/text_output.py
        Generate Advanced SubStation Alpha (ass) file from results to
    display both phrase-level & word-level timestamp simultaneously by:
     -using segment-level timestamps display phrases as usual
     -using word-level timestamps change formats (e.g. color/underline) of the word in the displayed segment
    Note: ass file is used in the same way as srt, vtt, etc.
    Parameters
    ----------
    transcript: dict
        results from modified model
    file: TextIO
        file object to write to
    resolution: str
        "word" or "char", timestamp resolution to highlight.
    color: str
        color code for a word at its corresponding timestamp
        <bbggrr> reverse order hexadecimal RGB value (e.g. FF0000 is full intensity blue. Default: 00FF00)
    underline: bool
        whether to underline a word at its corresponding timestamp
    prefmt: str
        used to specify format for word-level timestamps (must be use with 'suffmt' and overrides 'color'&'underline')
        appears as such in the .ass file:
            Hi, {<prefmt>}how{<suffmt>} are you?
        reference [Appendix A: Style override codes] in http://www.tcax.org/docs/ass-specs.htm
    suffmt: str
        used to specify format for word-level timestamps (must be use with 'prefmt' and overrides 'color'&'underline')
        appears as such in the .ass file:
            Hi, {<prefmt>}how{<suffmt>} are you?
        reference [Appendix A: Style override codes] in http://www.tcax.org/docs/ass-specs.htm
    font: str
        word font (default: Arial)
    font_size: int
        word font size (default: 48)
    kwargs:
        used for format styles:
        'Name', 'Fontname', 'Fontsize', 'PrimaryColour', 'SecondaryColour', 'OutlineColour', 'BackColour', 'Bold',
        'Italic', 'Underline', 'StrikeOut', 'ScaleX', 'ScaleY', 'Spacing', 'Angle', 'BorderStyle', 'Outline',
        'Shadow', 'Alignment', 'MarginL', 'MarginR', 'MarginV', 'Encoding'

    """

    fmt_style_dict = {'Name': 'Default', 'Fontname': 'Dela Gothic One', 'Fontsize': '12', 'PrimaryColour': '&Hffffff',
                      'SecondaryColour': '&Hffffff', 'OutlineColour': '&H0', 'BackColour': '&H0', 'Bold': '0',
                      'Italic': '0', 'Underline': '0', 'StrikeOut': '0', 'ScaleX': '100', 'ScaleY': '100',
                      'Spacing': '0', 'Angle': '0', 'BorderStyle': '1', 'Outline': '1', 'Shadow': '0',
                      'Alignment': '5', 'MarginL': '10', 'MarginR': '10', 'MarginV': '10', 'Encoding': '0'}

    for k, v in filter(lambda x: 'colour' in x[0].lower() and not str(x[1]).startswith('&H'), kwargs.items()):
        kwargs[k] = f'&H{kwargs[k]}'

    fmt_style_dict.update((k, v)
                          for k, v in kwargs.items() if k in fmt_style_dict)

    if font:
        fmt_style_dict.update(Fontname=font)
    if font_size:
        fmt_style_dict.update(Fontsize=font_size)

    fmts = f'Format: {", ".join(map(str, fmt_style_dict.keys()))}'

    styles = f'Style: {",".join(map(str, fmt_style_dict.values()))}'

    ass_str = f'[Script Info]\nScriptType: v4.00+\nPlayResX: 384\nPlayResY: 288\nScaledBorderAndShadow: yes\n\n' \
        f'[V4+ Styles]\n{fmts}\n{styles}\n\n' \
        f'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n\n'

    if prefmt or suffmt:
        if suffmt:
            assert prefmt, 'prefmt must be used along with suffmt'
        else:
            suffmt = r'\r'
    else:
        if not color:
            color = 'HFF00'
        underline_code = r'\u1' if underline else ''

        prefmt = r'{\1c&' + f'{color.upper()}&{underline_code}' + '}'
        suffmt = r'{\r}'

    def secs_to_hhmmss(secs: Tuple[float, int]):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return f'{hh:0>1.0f}:{mm:0>2.0f}:{ss:0>2.2f}'

    def dialogue(chars: str, start: float, end: float, idx_0: int, idx_1: int) -> str:
        if idx_0 == -1:
            text = chars
        else:
            text = f'{chars[:idx_0]}{prefmt}{chars[idx_0:idx_1]}{suffmt}{chars[idx_1:]}'
        return f"Dialogue: 0,{secs_to_hhmmss(start)},{secs_to_hhmmss(end)}," \
               f"Default,,0,0,0,,{text.strip() if strip else text}"

    if resolution == "word":
        resolution_key = "words"
    elif resolution == "char":
        resolution_key = "chars"
    else:
        raise ValueError(
            ".ass resolution should be 'word' or 'char', not ", resolution)

    ass_arr = []

    for segment in transcript:
        # if "12" in segment['text']:
        # import pdb; pdb.set_trace()
        if resolution_key in segment:
            res_segs = pd.DataFrame(segment[resolution_key])
            prev = segment['start']
            if "speaker" in segment:
                speaker_str = f"[{segment['speaker']}]: "
            else:
                speaker_str = ""

            last_idx_map = {}

            def find_idx(str, ch):
                yield [i for i, c in enumerate(str) if c == ch]

            for cdx, crow in res_segs.iterrows():
                if not np.isnan(crow['start']):
                    if resolution == "char":
                        idx_0 = cdx
                        idx_1 = cdx + 1
                    elif resolution == "word":
                        idxs = list(find_idx(segment['text'], crow['word']))
                        if crow['word'] in last_idx_map:
                            offset = last_idx_map[crow['word']]
                        else:
                            offset = 0
                        print("*dl", crow['word'], offset, idxs)
                        idx_0 = idxs[0 + offset]
                        idx_1 = idxs[0 + offset] + len(crow['word'])
                        last_idx_map[crow['word']] = offset + 1
                    # fill gap
                    if crow['start'] > prev:
                        filler_ts = {
                            "chars": speaker_str + segment['text'],
                            "start": prev,
                            "end": crow['start'],
                            "idx_0": -1,
                            "idx_1": -1
                        }

                        ass_arr.append(filler_ts)
                    # highlight current word
                    f_word_ts = {
                        "chars": speaker_str + segment['text'],
                        "start": crow['start'],
                        "end": crow['end'],
                        "idx_0": idx_0 + len(speaker_str),
                        "idx_1": idx_1 + len(speaker_str)
                    }
                    ass_arr.append(f_word_ts)
                    prev = crow['end']

    ass_str += '\n'.join(map(lambda x: dialogue(**x), ass_arr))

    # file.write(ass_str)
    return ass_str

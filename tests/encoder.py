import tiktoken


def parse_timestamp_date(timestamp):
    hours, minutes, seconds = timestamp.split(":")
    return int(hours), int(minutes), float(seconds)

# encoder that converts a number to a 3 character base36 code,
# 000-999 are converted to 000-999
# 1000-46655 are converted to 00a-99z


def encode_base36(number):
    return f"{number:03x}"

# # Example usage:
# number = 12345
# code = encode_base36(number)
# print(f"Number: {number}, Code: {code}")


# [0:00:00.620 --> 0:00:29.500] Welcome back.
# [0:00:29.500 --> 0:00:31.500] Here we go again.
# take the start and end time of the clip
# encode it into like 000>Welcome back.
# and then write the srt to a file and the mapping to another file

SRT_FILE = "./workspace/cache/youtube-RcYjXbSJBN8/transcript.chunked.srt"

with open(SRT_FILE, 'r') as f:
    srt_data = f.read()


fmt_srt_data = srt_data.split("\n\n")
fmt_srt_data = list(filter(lambda x: x != "", fmt_srt_data))
fmt_srt_data = list(
    map(lambda x: list(filter(lambda y: y != "", x.split("\n"))), fmt_srt_data))

fmt_srt_data = list(
    map(lambda x: [x[0], x[1], "\n".join(x[2:])], fmt_srt_data))
print(fmt_srt_data[56:59])

fmt_srt_data = list(map(lambda x: [
    x[0],
    parse_timestamp_date(x[1].split(" --> ")[0]),
    parse_timestamp_date(x[1].split(" --> ")[1]),
    x[2]
], fmt_srt_data))


with open("./encoded.hexline.srt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(fmt_srt_data):
        f.write(f"{encode_base36(i)}>{chunk[3]}\n")

# with open("./encoded.hexline.map", "w", encoding="utf-8") as f:
#     for i, chunk in enumerate(fmt_srt_data):
#         f.write(f"{encode_base36(i)}>{chunk[1]}>{chunk[2]}\n")
hexmap = {}
for i, chunk in enumerate(fmt_srt_data):
    hexmap[encode_base36(i)] = chunk[1:3]
print(hexmap, file=open("./encoded.hexline.map", "w", encoding="utf-8"))

with open("./encoded.hexline.srt", "r", encoding="utf-8") as f:
    srt_data = f.read()
tokens = tiktoken.encoding_for_model("gpt-3.5-turbo-16k").encode(srt_data)
print(len(tokens))

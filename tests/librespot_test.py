from librespot.core import Session
from ttai_farm.console import console
from librespot.metadata import EpisodeId
import json
session = Session.Builder() \
    .user_pass("31aalxj5za4eysf2ikfizinbzvpy", "waffle123X,") \
    .create()

console.log("got spotify session", session)
access_token = session.tokens().get("playlist-read")
console.log("got access token", access_token)
ep = EpisodeId.from_base62(
    "6OwITXMGgY0mVCGdKRJrYr")

console.log("got episode id", ep)
meta = session.api().get_metadata_4_episode(ep)
console.log("got episode metadata", meta.video)
console.print(meta.video, type(meta.video))

# fileid as hex
#        got episode metadata [file_id: ".G\315\327\3014XV\257\313\373\352\257X\216\367" ]
hex_id = meta.video[0].file_id.hex()
console.log("hexid", hex_id)


response = session.api()\
    .send("GET", f"/manifests/v7/json/sources/{hex_id}/options/supports_drm", None, None)
# .send("GET", "/storage-resolve/files/china/interactive/{}".format(meta.video[0].file_id.hex()), None, None)

api_response = json.loads(response.content)
# api_response = json.loads("""{"contents":[{"segment_length":4,"start_time_millis":0,"end_time_millis":9999760,"offline_profiles":[],"profiles":[{"id":14,"audio_bitrate":96000,"audio_codec":"mp4a.40.2","mime_type":"audio/mp4","file_type":"mp4","max_bitrate":100762},{"id":13,"video_bitrate":81588,"video_codec":"avc1.4d400d","video_resolution":180,"video_width":320,"video_height":180,"mime_type":"video/mp4","file_type":"mp4","max_bitrate":287880},{"id":12,"video_bitrate":115718,"video_codec":"avc1.4d4015","video_resolution":240,"video_width":426,"video_height":240,"mime_type":"video/mp4","file_type":"mp4","max_bitrate":503774},{"id":11,"video_bitrate":178047,"video_codec":"avc1.4d401e","video_resolution":320,"video_width":568,"video_height":320,"mime_type":"video/mp4","file_type":"mp4","max_bitrate":734698},{"id":10,"video_bitrate":354834,"video_codec":"avc1.4d401f","video_resolution":480,"video_width":854,"video_height":480,"mime_type":"video/mp4","file_type":"mp4","max_bitrate":1312284},{"id":9,"video_bitrate":808688,"video_codec":"avc1.4d4028","video_resolution":720,"video_width":1280,"video_height":720,"mime_type":"video/mp4","file_type":"mp4","max_bitrate":2252392},{"id":8,"video_bitrate":2504749,"video_codec":"avc1.4d402a","video_resolution":1080,"video_width":1920,"video_height":1080,"mime_type":"video/mp4","file_type":"mp4","max_bitrate":4691728},{"id":7,"audio_bitrate":96000,"audio_codec":"mp4a.40.2","mime_type":"audio/mp2t","file_type":"ts","max_bitrate":149272},{"id":5,"video_bitrate":110381,"video_codec":"avc1.4d400d","video_resolution":180,"video_width":320,"video_height":180,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":319976},{"id":4,"video_bitrate":144044,"video_codec":"avc1.4d4015","video_resolution":240,"video_width":426,"video_height":240,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":539184},{"id":3,"video_bitrate":207347,"video_codec":"avc1.4d401e","video_resolution":320,"video_width":568,"video_height":320,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":775312},{"id":2,"video_bitrate":389954,"video_codec":"avc1.4d401f","video_resolution":480,"video_width":854,"video_height":480,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":1369392},{"id":1,"video_bitrate":853244,"video_codec":"avc1.4d4028","video_resolution":720,"video_width":1280,"video_height":720,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":2330072},{"id":0,"video_bitrate":2586268,"video_codec":"avc1.4d402a","video_resolution":1080,"video_width":1920,"video_height":1080,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":4823704},{"id":19,"audio_bitrate":96000,"audio_codec":"opus","mime_type":"audio/webm","file_type":"webm","max_bitrate":114468},{"id":18,"video_bitrate":235817,"video_codec":"vp9","video_resolution":320,"video_width":568,"video_height":320,"mime_type":"video/webm","file_type":"webm","max_bitrate":996600},{"id":17,"video_bitrate":482101,"video_codec":"vp9","video_resolution":480,"video_width":854,"video_height":480,"mime_type":"video/webm","file_type":"webm","max_bitrate":2262008},{"id":16,"video_bitrate":874547,"video_codec":"vp9","video_resolution":720,"video_width":1280,"video_height":720,"mime_type":"video/webm","file_type":"webm","max_bitrate":2943702},{"id":15,"video_bitrate":2290612,"video_codec":"vp9","video_resolution":1080,"video_width":1920,"video_height":1080,"mime_type":"video/webm","file_type":"webm","max_bitrate":5334962}],"background_profiles":[{"id":6,"video_bitrate":46578,"video_codec":"avc1.4d400d","video_resolution":4,"video_width":8,"video_height":4,"mime_type":"video/mp2t","file_type":"ts","max_bitrate":47376}],"encryption_infos":[]}],"spritemaps":[{"id":0,"height":540,"width":960,"number":1}],"start_time_millis":0,"end_time_millis":9999760,"initialization_template":"v1/origins/b1acc6dba4d449dcf7a71659d3fabea2/sources/2e47cdd7c1345856afcbfbeaaf588ef7/encodings/29bdf360689e11ee90decd4f04944c78/profiles/{{profile_id}}/inits/{{file_type}}?token=DK7NZnK2xyiwLBiB%2FMh8hBzFCv6V39lqYuzE5%2BaBoLQ%3D&token_ak=st%3D1697386006%7Eexp%3D1697990806%7Eacl%3D*%2Fencodings%2F29bdf360689e11ee90decd4f04944c78%2F*%7Ehmac%3D0a369dae82b96932fdc6e67d19e1890987f2814b6a0f5c851a8c0e98f03b84a5","segment_template":"v1/origins/b1acc6dba4d449dcf7a71659d3fabea2/sources/2e47cdd7c1345856afcbfbeaaf588ef7/encodings/29bdf360689e11ee90decd4f04944c78/profiles/{{profile_id}}/{{segment_timestamp}}.{{file_type}}?token=DK7NZnK2xyiwLBiB%2FMh8hBzFCv6V39lqYuzE5%2BaBoLQ%3D&token_ak=st%3D1697386006%7Eexp%3D1697990806%7Eacl%3D*%2Fencodings%2F29bdf360689e11ee90decd4f04944c78%2F*%7Ehmac%3D0a369dae82b96932fdc6e67d19e1890987f2814b6a0f5c851a8c0e98f03b84a5","subtitle_template":"v1/origins/b1acc6dba4d449dcf7a71659d3fabea2/sources/2e47cdd7c1345856afcbfbeaaf588ef7/{{language_code}}.webvtt?token=DK7NZnK2xyiwLBiB%2FMh8hBzFCv6V39lqYuzE5%2BaBoLQ%3D&token_ak=st%3D1697386006%7Eexp%3D1697990806%7Eacl%3D*%2Fencodings%2F29bdf360689e11ee90decd4f04944c78%2F*%7Ehmac%3D0a369dae82b96932fdc6e67d19e1890987f2814b6a0f5c851a8c0e98f03b84a5","spritemap_template":"v1/origins/b1acc6dba4d449dcf7a71659d3fabea2/sources/2e47cdd7c1345856afcbfbeaaf588ef7/encodings/29bdf360689e11ee90decd4f04944c78/profiles/{{spritemap_id}}.jpg","base_urls":["https://video-akpcw-cdn-spotify-com.akamaized.net/segments/","https://video-fa.scdn.co/segments/"],"spritemap_base_urls":["https://spritemaps.scdn.co/spritemaps/"],"subtitle_base_urls":["https://subtitles.spotifycdn.com/subtitles/"],"subtitle_language_codes":["en-US"]}""")


def template(string, **kwargs):
    # replace {{key}} with value
    for key, value in kwargs.items():
        string = string.replace("{{" + key + "}}", value)
    return string


profiles = api_response['contents'][0]['profiles']

best_audio_stream = max(list(filter(
    lambda x: x['mime_type'] == 'audio/mp2t', profiles)), key=lambda x: x.get('audio_bitrate', 0))
best_video_stream = max(list(filter(
    lambda x: x['mime_type'] == 'video/mp2t', profiles)), key=lambda x: x.get('video_bitrate', 0))

console.log("Best Audio Stream:", best_audio_stream)
console.log("Best Video Stream:", best_video_stream)

subtitle_language_codes = api_response['subtitle_language_codes']
subtitle_base_url = api_response['subtitle_base_urls'][0] + \
    api_response['subtitle_template']

subtitle_urls = {}
for language_code in subtitle_language_codes:
    subtitle_urls[language_code] = template(
        subtitle_base_url, language_code=language_code)

segment_length = api_response['contents'][0]['segment_length']

seg_count = int(round(api_response['end_time_millis'] / 1000) /
                segment_length)

base_url = api_response['base_urls'][0]
video_segments_urls = list(map(lambda x: base_url + template(
    api_response['segment_template'],
    profile_id=str(best_video_stream['id']),
    segment_timestamp=str(
        x * segment_length),
    file_type=best_video_stream['file_type']
), range(seg_count)))
# base_url + template(api_response['initialization_template'], profile_id=str(
#     best_video_stream['id']), file_type=best_video_stream['file_type']),


audio_segments_urls = list(map(lambda x: base_url + template(
    api_response['segment_template'],
    profile_id=str(best_audio_stream['id']),
    segment_timestamp=str(
        x * segment_length),
    file_type=best_audio_stream['file_type']
), range(seg_count)))
# [
#     base_url + template(api_response['initialization_template'], profile_id=str(
#         best_audio_stream['id']), file_type=best_audio_stream['file_type']),

#     *
# ]
print(len(video_segments_urls), len(audio_segments_urls))


print("\n".join(video_segments_urls), file=open("video_segments_urls.txt", "w"))
print("\n".join(audio_segments_urls), file=open("audio_segments_urls.txt", "w"))

# write ffmpeg packlist like "file 'dl/0.webm'"

with open("ffmpeg-packlist-video.txt", "w") as f:
    # print(f"file 'testing-dl/init.webm'", file=f)
    for i in range(len(video_segments_urls)):
        print(f"file 'testing-dl/{i * 4}.ts'", file=f)

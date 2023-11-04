from pydub import AudioSegment
from pydub.silence import split_on_silence


def split_mp3_by_silence(mp3_path, min_silence_length=2000, silence_thresh=-40):
    # Load the MP3 file
    audio = AudioSegment.from_file(mp3_path)
    print(f"Loaded {len(audio)} bytes of audio")

    # Split the audio based on silence
    audio_segments = split_on_silence(
        audio, min_silence_len=min_silence_length, silence_thresh=silence_thresh)

    # Convert segment durations to start and end timestamps
    segments = []
    for segment in audio_segments:
        start_time = len(audio) - len(segment)
        end_time = len(audio) - len(segment) + len(segment)
        # Convert milliseconds to seconds
        segments.append((start_time / 1000, end_time / 1000))

    return segments


if __name__ == "__main__":
    # Replace with your MP3 file path
    mp3_path = "honey.opus"
    # Minimum silence length in milliseconds (2 seconds)
    min_silence_length = 100
    silence_thresh = -2  # Adjust this value as needed

    segments = split_mp3_by_silence(
        mp3_path, min_silence_length, silence_thresh)
    print(segments)
    for i, (start, end) in enumerate(segments):
        print(
            f"Segment {i+1}: Start time: {start:.2f} seconds, End time: {end:.2f} seconds")

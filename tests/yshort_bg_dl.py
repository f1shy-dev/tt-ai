from threading import Thread
from queue import Queue
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, MofNCompleteColumn
import os
import yt_dlp
from rich.console import Console
console = Console()


def status(x, **kwargs):
    return console.status(x, spinner='dots2', **kwargs)

# [...document.querySelectorAll(`ytd-rich-item-renderer`)].map(x => [x.querySelector('ytd-thumbnail a').href, x.querySelector('#video-title').textContent, x.querySelector('#time-status #text').textContent.trim()]).filter(x => {
#     console.log(x[2].split(":").map(Number))
#     let [hrs, mins, secs]  = x[2].split(":").map(Number)
#     if (secs == null) {
#         secs = mins
#         mins = hrs
#     }
#     return mins <= 4
# }) .map(x => `'${x[0]}', # ${x[1]} - ${x[2]}`).join("\n")

#fmt: off
videos = [
    'https://www.youtube.com/watch?v=ZzMbU5aOaxI', # Painting Squishy Ghost and Pumpkin #halloween #pumpkin #ghost #painting #sosatisfying  #crafting - 3:12
    'https://www.youtube.com/watch?v=hIRsb2D6bS4', # How to Carve a Pumpkin | ASMR #sosatisfying #halloween #satisfying #jackolantern #pumpkin - 4:04
    'https://www.youtube.com/watch?v=Vm4x9RBg0QU', # Satisfying Slime ASMR Compilation #sosatisfying #asmr #slimeasmr - 3:04
    'https://www.youtube.com/watch?v=VxeQ5p0AMJ8', # Bare Feet Squish Foam Filled Crocs | Satisfying Compilation #feet #crocs  #slime #shavingcream - 4:22
    'https://www.youtube.com/watch?v=A15jorL2xg0', # Food or Soap? Relaxing Soap Cutting Compilation | So Satisfying #nomusic #asmr #soapcutting - 4:23
    'https://www.youtube.com/watch?v=XTD29NyYCMw', # Best of Orbeez Compilation | So Satisfying #orbeez #asmr #satisfying - 4:28
    'https://www.youtube.com/watch?v=C-HKoJ29Iro', # Back to School ASMR Compilation | So Satisfying - 2:41
    'https://www.youtube.com/watch?v=dkxlfHriEuo', # ASMR Floral Foam Satisfying compilation (no music) | So Satisfying - 4:23
    'https://www.youtube.com/watch?v=K9UThVPe7wA', # ASMR Paint Roller compilation | So Satisfying - 4:05
    'https://www.youtube.com/watch?v=QxOCxADoNE8', # the most relaxing ASMR videos (no music) #asmr #satisfyingasmr #sosatisfying - 4:23
    'https://www.youtube.com/watch?v=VmjjvNCXq4k', # ASMR baking chip cookies | most satisfying #sosatisfying #satisfyingasmr #asmr #baking - 3:48
    'https://www.youtube.com/watch?v=R2B3ly49brs', # so satisfying ASMR compilation (no music) | RELAXING #satisfyingasmr #sosatisfying #satisfyingvideos - 3:31
    'https://www.youtube.com/watch?v=bc8Q9LsX0fU', # Crackling Marshmallow Fire Pit Roast ASMR #satisfyingasmr #marshmallow #satisfyingfoods - 3:15
    'https://www.youtube.com/watch?v=KzBcUNjZnY4', # super satisfying asmr food compilation - 4:20
    'https://www.youtube.com/watch?v=gfDgHOclvNI', # the most satisfying video you will ever watch - 4:17
    'https://www.youtube.com/watch?v=DIj9poLKcxU', # Do these videos put you to sleep? | So Satisfying asmr compilation - 4:24
    'https://www.youtube.com/watch?v=ZCnCXMbKgCs', # Honeycomb squeeze & more So Satisfying ASMR - 4:04
    'https://www.youtube.com/watch?v=9fRtlQseL74', # ultra satisfying asmr | paint squeezing - 4:17
    'https://www.youtube.com/watch?v=e2ZrQEYmbd4', # relaxing asmr compilation (no music) crunchy sounds - 4:15
    'https://www.youtube.com/watch?v=s6Sm_45dDiM', # super satisfying nonstop asmr & drawing - 4:08
    'https://www.youtube.com/watch?v=ak-vyVMeDfs', # slicing, squeezing, plucking | the most satisfying ASMR (no music) - 4:00
    'https://www.youtube.com/watch?v=hqxpxrOQPjo', # Satisfying hair pull & asmr no music - 3:59
    'https://www.youtube.com/watch?v=BajhMngtbas', # Super satisfying video (ASMR no MUSIC) - 3:58
    'https://www.youtube.com/watch?v=-dmGcGp44DI', # So Satisfying ASMR Video Compilation (Relaxing) (No Music) - 4:01
    'https://www.youtube.com/watch?v=xhtE9Zem4C4', # So Satisfying ASMR compilation video (No Music) RELAXING & CALMING - 3:40
    'https://www.youtube.com/watch?v=gySiMUTvtXg', # Super Satisfying Cheese Carve (asmr compilation) - 3:36
    'https://www.youtube.com/watch?v=q-J-XdDY-VM', # Best of So Satisfying (ASMR no music) - 3:52
    'https://www.youtube.com/watch?v=culjlCR4cGw', # Less-Mess Magic Sand - Satisfying Compilation - 1:05
    'https://www.youtube.com/watch?v=mbD48wqhyYo', # Super Satisfying video compilation (squeeze ASMR) - 3:59
    'https://www.youtube.com/watch?v=Ekp168IW_D8', # Super Satisfying Video Compilation (No Music) - 4:01
    'https://www.youtube.com/watch?v=ezb4EiJ9Upw', # So Satisfying ASMR video compilation (No Music) RELAXING - 4:04
    'https://www.youtube.com/watch?v=9ST_GPd4ecM', # Super Satisfying Video Compilation (no music) - 4:14
    'https://www.youtube.com/watch?v=eg6z2Lek2og', # Super Satisfying ASMR compilation RELAXING (No music) - 4:18
    'https://www.youtube.com/watch?v=mFQ7OjvQzzk', # Super Relaxing Satisfying Video (ASMR no music) - 4:22
    'https://www.youtube.com/watch?v=apjaPZU-48A', # Best Satisfying Compilation RELAXING - 4:19
    'https://www.youtube.com/watch?v=XQ8sGllzCIs', # DO you find these videos satisfying? ASMR satisfying video compilation - 4:15
    'https://www.youtube.com/watch?v=NtJ-PXsahKI', # So Satisfying ASMR video compilation (No Music) - 4:42
    'https://www.youtube.com/watch?v=DxFb7hysWvQ', # Satisfying Crush and Scrape ASMR - 4:57
    'https://www.youtube.com/watch?v=Pip8nIW9S4Q', # Satisfying ASMR compilation (SUPER RELAXING) - 4:51
    'https://www.youtube.com/watch?v=2YI1cGtHI_w', # BEST OF SO SATISFYING SNAPCHAT (RELAXING) - 2:37
    'https://www.youtube.com/watch?v=8mbCYNtzK-k', # So Satisfying ASMR video compilation (No Music) RELAXING FLORAL FOAM SQUEEZE - 2:37
    'https://www.youtube.com/watch?v=SKzcYHpj7-A', # Satisfying ASMR Hot tool compilation (RELAXING) - 2:38
]
#fmt: on

OUT_DIR = "./workspace/bg-vids"


def download_video_one(url, ydl):
    if not os.path.exists(f"{OUT_DIR}/{url.split('/')[-1]}.mp4"):
        ydl.download([url])
        console.log(f"[medium_purple3]downloaded {url}")
    else:
        console.log(f"[green]exists: {url}")


def download_threaded(urls, ydl, adv, n_threads=8):
    q = Queue()

    def worker():
        while True:
            url = q.get()
            try:
                download_video_one(url, ydl)
                adv()
            finally:
                q.task_done()

    for i in range(n_threads):
        t = Thread(target=worker)
        t.daemon = True
        t.start()

    for url in urls:
        q.put(url)

    q.join()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestaudio',
        'outtmpl': f"{OUT_DIR}/random-%(id)s.%(ext)s",
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        'noprogress': True,
    })

    with Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("Downloading videos", total=len(videos))

        # for url, title in videos:
        #     if not os.path.exists(f"{AUDIO_DIR}/{url.split('/')[-1]}.wav"):
        #         ydl.download([url])
        #         ffmpeg_cmd = f"ffmpeg -i {TEMP_DIR}/{url.split('/')[-1]}.webm -ac 1 -ar 16000 {AUDIO_DIR}/{url.split('/')[-1]}.wav"
        #         output = subprocess.run(
        #             ffmpeg_cmd.split(" "), capture_output=True)
        #         assert output.returncode == 0, f"ffmpeg failed: {output.stderr}"
        #         os.remove(f"{TEMP_DIR}/{url.split('/')[-1]}.webm")
        #     progress.advance(task)
        def adv():
            progress.advance(task)
        download_threaded(videos, ydl, adv)


if __name__ == "__main__":
    main()

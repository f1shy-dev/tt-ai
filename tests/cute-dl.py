import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen
from rich.filesize import decimal
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
    TransferSpeedColumn,
    RenderableColumn,
    MofNCompleteColumn,
    ProgressColumn,
    SpinnerColumn,
    Task
)
from datetime import timedelta
from rich.text import Text


# done_event = Event()


# def handle_sigint(signum, frame):
#     done_event.set()


# signal.signal(signal.SIGINT, handle_sigint)

dlcompletedsize = 0
dltotalsize = 0


class RunningDLSpeed(ProgressColumn):

    def render(self, task: "Task") -> Text:
        elapsed = task.finished_time if task.finished else task.elapsed
        if elapsed is None:
            return Text("?/s", style="progress.data.speed")

        global dlcompletedsize
        speed_bytes = dlcompletedsize / elapsed
        formatted = decimal(speed_bytes)
        return Text(f"{formatted}/s", style="progress.data.speed")


progress = Progress(
    SpinnerColumn(style="blue"),
    TextColumn("[blue]Downloading..."),
    BarColumn(style="medium_purple3", finished_style="bar.complete"),
    "[progress.download]{task.completed}/{task.total} files ({task.fields[dldmsg]}) downloaded",
    # "•",
    # "[progress.percentage]{task.fields[dlcompleted]}/{task.fields[dltotal]}",
    # "[progress.percentage]{task.fields[dldmsg]:.2f}%",
    # "[progress.filesize]",

    # "•",
    # DownloadColumn(),
    # "•",
    "•",
    RunningDLSpeed(),
    # TransferSpeedColumn(),
    "•",
    TimeElapsedColumn(),
    "[progress.elapsed]elapsed",

)


def copy_url(task_id: TaskID, url: str, path: str) -> None:
    """Copy data from a url to a local file."""
    # progress.console.log(f"Requesting {url}")
    response = urlopen(url)
    # This will break if the response doesn't contain content length
    size = int(response.info()["Content-length"])
    # print(size)
    global dltotalsize
    global dlcompletedsize

    dltotalsize += size
    # progress.update(task_id, dldmsg=(dlcompletedsize/dltotalsize)*100)
    progress.update(
        task_id, dldmsg=f"{decimal(dlcompletedsize)}")
    written = 0
    with open(path, "wb") as dest_file:
        for data in iter(partial(response.read, 32768), b""):
            dest_file.write(data)
            written += len(data)
            dlcompletedsize += len(data)
            if written >= size:
                progress.update(task_id, advance=1)
            else:
                progress.update(task_id, dlcompleted=dlcompletedsize)
            # if done_event.is_set():
            #     return
    # progress.console.log(f"Downloaded {path}")


def download(urls: Iterable[str], dest_dir: str):
    """Download multiple files to the given directory."""

    with progress:

        with ThreadPoolExecutor(max_workers=16) as pool:
            dl_task = progress.add_task(
                "download", dltotal=len(urls), dldmsg="0B", total=len(urls), completed=0)
            for url in urls:
                filename = url.split("/")[-1].split("?")[0]
                dest_path = os.path.join(dest_dir, filename)
                if os.path.exists(dest_path):
                    # progress.console.log(
                    #     f"{filename} already exists, skipping")
                    progress.update(dl_task, advance=1)
                    # size = os.path.getsize(dest_path)
                    # # progress.add_task(
                    # #     "download", filename=filename, completed=size, total=size)
                    continue
                # progress.console.log(f"Downloading {url}")
                pool.submit(copy_url, dl_task, url, dest_path)


if __name__ == "__main__":
    # Try with https://releases.ubuntu.com/20.04/ubuntu-20.04.3-desktop-amd64.iso
    file = open("video_segments_urls.txt", "r")
    urls = [x.strip() for x in file.readlines()]
    # print(urls)
    download(urls, "./testing-dl")
    print("Done")

import os.path
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen
from rich.filesize import decimal
from rich.progress import (
    BarColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
    ProgressColumn,
    SpinnerColumn,
    Task
)
from datetime import timedelta
from rich.text import Text


def threaded_downloader(urls: Iterable[str], dest_dir: str, thread_count: int = 16):
    dlcompletedsize = 0
    dltotalsize = 0

    class RunningDLSpeed(ProgressColumn):
        def render(self, task: "Task") -> Text:
            elapsed = task.finished_time if task.finished else task.elapsed
            if elapsed is None:
                return Text("?/s", style="progress.data.speed")
            nonlocal dlcompletedsize
            speed_bytes = dlcompletedsize / elapsed
            formatted = decimal(speed_bytes)
            return Text(f"{formatted}/s", style="progress.data.speed")

    progress = Progress(
        SpinnerColumn(style="blue"),
        TextColumn("[blue]Downloading..."),
        BarColumn(style="medium_purple3", finished_style="bar.complete"),
        "[progress.download]{task.completed}/{task.total} files ({task.fields[dldmsg]}) downloaded",
        "•",
        RunningDLSpeed(),
        "•",
        TimeElapsedColumn(),
        "[progress.elapsed]elapsed",
        transient=True,
    )

    def copy_url(task_id: TaskID, url: str, path: str, retry_ctr=0) -> None:
        try:
            response = urlopen(url, timeout=5)
            size = int(response.info()["Content-length"])
            nonlocal dltotalsize
            nonlocal dlcompletedsize
            dltotalsize += size
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
        except Exception as e:
            if retry_ctr >= 3:
                raise e
            progress.log(f"Error downloading {url}: {e}, retrying...")
            return copy_url(task_id, url, path, retry_ctr + 1)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with progress:
        with ThreadPoolExecutor(max_workers=thread_count) as pool:
            dl_task = progress.add_task(
                "download", dltotal=len(urls), dldmsg="0B", total=len(urls), completed=0)
            for url in urls:
                filename = url.split("/")[-1].split("?")[0]
                dest_path = os.path.join(dest_dir, filename)
                if os.path.exists(dest_path):
                    progress.update(dl_task, advance=1)
                    continue
                pool.submit(copy_url, dl_task, url, dest_path)

import os
import requests
import concurrent.futures
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TotalFileSizeColumn, DownloadColumn, TransferSpeedColumn, TimeElapsedColumn, RenderableColumn

# Function to download a single URL


def download_url(url, download_folder, idx):
    file_path = os.path.join(download_folder, str(idx*4) + "." + "ts")

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        downloaded_bytes = 0
        with open(file_path, "wb") as file:
            for data in response.iter_content(chunk_size=8192):
                file.write(data)
                downloaded_bytes += len(data)
    return downloaded_bytes


if __name__ == "__main__":
    download_folder = "testing-dl"  # Change this to your desired download folder
    num_threads = 16

    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    file = open("video_segments_urls.txt", "r")
    urls = [x.strip() for x in file.readlines()]

    total_size = len(urls)

    console = Console()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        running_size = 0
        with Progress(SpinnerColumn(),
                      TextColumn("{task.description}"),
                      BarColumn(),
                      TotalFileSizeColumn(),
                      #   DownloadColumn(),
                      TransferSpeedColumn(),
                      #   TaskProgressColumn(),
                      TimeElapsedColumn(),
                      transient=True,) as progress:
            task = progress.add_task("[red]Downloading...", total=None)

            for idx, url in enumerate(urls):
                futures.append(executor.submit(
                    download_url, url, download_folder, idx))
            for future in concurrent.futures.as_completed(futures):
                progress.advance(task)
                if future.result() is None:
                    console.log(f"Error downloading {future.result()}")
                    # console.log(f"Downloaded {future.result()}")
                else:
                    old_rs = running_size
                    running_size += future.result()
                    progress.update(task, total=running_size,
                                    completed=old_rs)
            progress.stop()

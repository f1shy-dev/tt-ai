from rich.console import Console
console = Console()


def status(x, **kwargs):
    return console.status(x, spinner='dots2', **kwargs)

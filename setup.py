from setuptools import setup, find_packages

setup(
    version="1.2",
    name="meow",
    packages=find_packages(),
    py_modules=["auto_subtitle"],
    author="Miguel Piedrafita",
    install_requires=[
        'openai-whisper',
        'yt-dlp',
        'ffmpeg'
    ],
    description="Automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['auto_subtitle=auto_subtitle.cli:main'],
    },
    include_package_data=True,
)
from setuptools import setup, find_packages

setup(
    version="1.10",
    name="meow_ttai",
    packages=find_packages(),
    py_modules=["meow_ttai"],
    author="f1shy_dev",
    install_requires=[
        'openai-whisper',
        'yt-dlp',
        'ffmpeg',
        'openai'
    ],
    description="Automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['ttai=meow_ttai.cli:main'],
    },
    include_package_data=True,
)
# SpeechToText

Convert audio files to text files offline.

## Installation

1. Install the requirements via: `pip install -r requirements.txt` into a virtual environment.
2. Download the model `vosk-model-en-us-0.42-gigaspeech` from [the VOSK model page](https://alphacephei.com/vosk/models). Place into the `models/` directory.
3. Place your desired audio file into the `audio/` directory.
4. Create a text file in the `text/` directory.
5. Run via `python offline.py --audio_path=<insert_audio_path_here> --text_path=<insert_text_path_here>`.

## Specifications

Tested on Windows 10 with Python 3.10.11. Installed the following packages in a virtual environment via `pip==23.0.1`:
```
vosk==0.3.45
```

Note that VOSK only takes `.wav` files. If you need to convert from any other filetype, use `ffmpeg` (I used `ffmpeg==2024-08-21-git-9d15fe77e3`). Here is an example command:
```
ffmpeg -i <path_to_audio_file> -acodec pcm_s16le -ac 1 -ar 16000 <path_for_new_audio_file>
```
import sys
import wave
import vosk
import json
import argparse

if __name__ == "__main__":
	# get arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('--audio_path', type=str, default="audio/whatsapp_20240822.wav", help="path to audio data as a .wav file")
	parser.add_argument('--text_path', type=str, default="text/test.txt", help="path to text data as a .txt file")
	args = parser.parse_args()

	# set arguments
	audio_path = args.audio_path
	text_path = args.text_path

	# make sure input is valid
	wf = wave.open(audio_path, "rb")
	if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
	    print("Audio file must be WAV format mono PCM.")
	    sys.exit(1)

	# initialize the model
	model_path = "models/vosk-model-en-us-0.42-gigaspeech"
	model = vosk.Model(model_path)

	# create a recognizer
	rec = vosk.KaldiRecognizer(model, wf.getframerate())
	rec.SetWords(True)
	rec.SetPartialWords(True)

	# getting speech to text and writing
	with open(text_path, "w") as text_file:
		while True:
			# read data and break if there is none left
			data = wf.readframes(4000)
			if len(data) == 0:
				break

			# if model recognises text
			if rec.AcceptWaveform(data):
				# parse the JSON result and get the recognized text
				result = json.loads(rec.Result())
				recognized_text = result['text']

				# write recognized text to the file, separated by newlines
				text_file.write(recognized_text + "\n")
				print(recognized_text)

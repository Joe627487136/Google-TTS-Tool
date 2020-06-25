# Read credential when start
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credential.json"

# User arg handle
import sys
import re
input_text = ''
out_file_prefix= ''
if (len(sys.argv) == 1):
    print('Testing mode...')
    input_text = 'Today is a good day! We are doing testing!'
    out_file_prefix = 'testing'
elif (len(sys.argv) == 2):
    print('File reading mode...')
    with open(sys.argv[1], 'r') as input_file:
        input_text = input_file.read()
        out_file_prefix = os.path.splitext(os.path.basename(sys.argv[1]))[0]
else:
    print('Invalid command given')
    sys.exit(0)

# TTS
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(ssml=input_text)

# Build the voice request, select the language code ("en-US") 
# ****** the NAME
# and the ssml voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code='en-US',
    name='en-US-Wavenet-F',
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    request={
        "input": synthesis_input,
        "voice": voice,
        "audio_config": audio_config
    })

# The response's audio_content is binary.
out_file = './output/' + out_file_prefix + '.mp3'
with open(out_file, 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file: ' + out_file)
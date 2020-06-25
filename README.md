# Google-TTS-Tool
A simple tool to translate text to speech using Google TTS API


### Installation:
1. Please run under python 3.6+ (https://www.python.org/downloads/)

2. Remember to remove old google-cloud core if you have used any before

3. Install client library (Version 2.0): 
```
pip install --upgrade google-cloud-texttospeech
```


### Prepare your own credentials:

1. The given credential.json is not valid (My wallet insist not to bill for your guys not my choice)

2. Therefore you will need to go to https://console.developers.google.com to prepare your own credential

3. Create an API project -> Go to Library -> Search for 'Text To Speech' -> Choose 'Cloud Text-to-Speech API' -> Enable -> Create Credentials

4. Rename your downloaded credential json file to ```credential.json``` and put under the root folder


### How to use:

1. Input folder to put in all your ssml text file

2. Output folder to store all ssml voice file

3. Testing output(will genernate a testing.mp3): 
```
python gtts.py
```

4. Custom tts (will generate your_ssml_text.mp3): 
```
python gtts.py ./input/your_ssml_text.txt
```



### Reference:

https://cloud.google.com/text-to-speech/docs/ssml

https://googleapis.dev/python/texttospeech/latest/index.html

https://github.com/googleapis/python-texttospeech/blob/master/UPGRADING.md#200-migration-guide

https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries

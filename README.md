# Google-TTS-Tool
A simple tool to translate text to speech using Google TTS API


### Installation (Recommand to turn off your VPN):
1. Please run under python 3.6+ (https://www.python.org/downloads/)

2. Remember to remove old google-cloud core if you have used any before

3. Install client library (Version 2.0): 
```
pip install --upgrade google-cloud-texttospeech
```



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

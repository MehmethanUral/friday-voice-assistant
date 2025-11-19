# tts.py (gTTS - hızlı konuşma + terminal çıktısı)
import os
from gtts import gTTS
from playsound import playsound

def speak(text):
    print(f"Friday: {text}")
    try:
        if os.path.exists("output.mp3"):
            os.remove("output.mp3")  # Mevcut dosya varsa sil
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("output.mp3")
        playsound("output.mp3")
    except Exception as e:
        print("Error generating speech:", e)

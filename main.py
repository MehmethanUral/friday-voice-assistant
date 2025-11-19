from commands import handle_command
from tts import speak
import speech_recognition as sr
import pygame

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        try:
            command = recognizer.recognize_google(audio, language="tr-TR")
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand.")
        except sr.RequestError:
            speak("It seems like there is no internet connection.")
    return ""

def stop_music():
    try:
        pygame.mixer.music.stop()
    except:
        pass

if __name__ == "__main__":
    speak("Friday is online. Awaiting your command.")
    while True:
        command = listen_for_command()
        if command:
            response = handle_command(command, stop_music_callback=stop_music)
            if response == "exit":
                break
            if response:
                print(f"Friday said: {response}")
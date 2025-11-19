# commands.py (güncellenmiş - güvenli müzik kontrolü ve çıkış)
import subprocess
import webbrowser
import time
import pygame
from tts import speak
from serper_utils import ask_serper  # type: ignore
from task_manager import add_task, get_tasks, clear_tasks

awaiting_task_input = False  # Görev ekleme modu kontrolü

def play_music(file_path="homepoint.mp3"):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
    except Exception as e:
        speak("Failed to play music.")

def handle_command(command, stop_music_callback=None):
    global awaiting_task_input
    command = command.casefold()

    if awaiting_task_input:
        add_task(command)
        speak("Task added sir.")
        awaiting_task_input = False
        return "Task added sir."

    if "wake up" in command or "wake up friday" in command:
        play_music()
        speak("Welcome home sir.")
        time.sleep(1)
        speak("What would you like to do today?")
        return "Welcome home sir. What would you like to do today?"

    elif any(kw in command for kw in ["satranç modu", "büyük usta", "chess mode"]):
        speak("Entering chess mode sir")
        webbrowser.open("https://www.chess.com/home")
        time.sleep(1)
        webbrowser.open("https://music.youtube.com/")
        time.sleep(1)
        speak("Would you like me to do anything else?")
        return "Entering chess mode sir."

    elif any(kw in command for kw in ["sessiz", "müziği kapat", "müziği durdur", "stop music"]):
        if stop_music_callback:
            stop_music_callback()
        speak("Music has been stopped sir")
        return "Music has been stopped sir."

    elif any(kw in command for kw in ["kapat", "friday kapat", "görüşürüz", "close friday"]):
        speak("As you wish sir. If you need me, just say the word.")
        return "exit"

    elif "google aç" in command:
        speak("Opening Google sir")
        webbrowser.open("https://www.google.com")
        return "Opening Google sir."

    elif "youtube aç" in command:
        speak("Opening YouTube sir")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube sir."

    elif "x aç" in command or "twitter aç" in command:
        speak("Opening X sir")
        webbrowser.open("https://x.com")
        return "Opening X sir."

    elif "instagram aç" in command:
        speak("Opening Instagram sir")
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram sir."

    elif "görev ekle" in command:
        speak("What task should I add sir?")
        awaiting_task_input = True
        return "What task should I add sir?"

    elif "görevlerim" in command or "görevleri oku" in command:
        tasks = get_tasks()
        if tasks:
            speak("Here are your tasks sir.")
            for t in tasks:
                speak(t)
            return "Here are your tasks sir."
        else:
            speak("You have no tasks at the moment.")
            return "You have no tasks at the moment."

    elif "görev dosyasını aç" in command:
        subprocess.Popen(["notepad.exe", "tasks.json"])
        speak("Opening your task list sir.")
        return "Opening your task list sir."

    elif "görevleri sil" in command:
        clear_tasks()
        speak("All tasks have been cleared.")
        return "All tasks have been cleared."

    elif any(kw in command for kw in ["kim", "nedir", "ne zaman", "nerede", "nasıl", "hava", "skor", "haber"]):
        if any(kw in command for kw in ["görev", "dosya"]):
            return None  # Serper'e gönderme
        else:
            response = ask_serper(command)
            speak(response)
            return response

    else:
        speak("I'm not sure how to respond to that.")
        return "I'm not sure how to respond to that."

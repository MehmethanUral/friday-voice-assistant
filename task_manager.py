# task_manager.py
import json
import os

TASKS_FILE = "tasks.json"

# Görev dosyası yoksa oluştur
def init_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

# Görev ekle
def add_task(task):
    init_tasks()
    with open(TASKS_FILE, "r") as f:
        tasks = json.load(f)
    tasks.append(task)
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

# Görevleri oku
def get_tasks():
    init_tasks()
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Görevleri temizle
def clear_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump([], f)
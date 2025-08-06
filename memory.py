import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def add_to_history(user_id, role, message):
    memory = load_memory()
    user_memory = memory.get(str(user_id), {"role": role, "messages": []})
    user_memory["messages"].append(message)
    memory[str(user_id)] = user_memory
    save_memory(memory)
    return user_memory["messages"]

def clear_memory(user_id):
    memory = load_memory()
    if str(user_id) in memory:
        del memory[str(user_id)]
        save_memory(memory)

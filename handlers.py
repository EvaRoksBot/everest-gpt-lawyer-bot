from prompts import PROMPTS
from gpt import ask_gpt
from parser import extract_text_from_file
from telebot import types

def register_handlers(bot):
    @bot.message_handler(commands=list(PROMPTS.keys()))
    def handle_command(message):
        cmd = message.text.strip("/").split()[0]
        prompt = PROMPTS.get(cmd)
        bot.send_message(message.chat.id, "Отправьте текст или документ (PDF/TXT) для анализа.")
        bot.register_next_step_handler(message, lambda msg: process_input(bot, msg, prompt))

    @bot.message_handler(func=lambda m: m.text == "/start")
    def handle_start(message):
        bot.send_message(message.chat.id, "👋 Привет! Я юридический GPT-бот. Используй команды: " +
                         ", ".join("/" + k for k in PROMPTS.keys()))

def process_input(bot, message, prompt):
    input_text = None
    if message.content_type == "document":
        file_info = bot.get_file(message.document.file_id)
        file = bot.download_file(file_info.file_path)
        input_text = extract_text_from_file(file, message.document.mime_type)
    elif message.content_type == "text":
        input_text = message.text

    if input_text:
        answer = ask_gpt(prompt, input_text)
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "❌ Не удалось прочитать текст.")

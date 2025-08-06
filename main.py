import telebot
from config import TELEGRAM_TOKEN
from handlers import register_handlers

bot = telebot.TeleBot(TELEGRAM_TOKEN)
register_handlers(bot)
bot.polling()

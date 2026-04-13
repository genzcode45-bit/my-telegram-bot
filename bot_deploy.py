import telebot, os
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)
# बाकी code same as bot.py
bot.polling()
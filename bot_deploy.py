import telebot
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')
OWNER_ID = 6869861598 
# Owner ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ViewRise Bot Active!")

@bot.message_handler(func=lambda message: True)
def forward(message):
    try:
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.reply_to(message, "Message sent to owner!")
    except Exception as e:
        bot.reply_to(message, "Try again!")

print("Bot starting...")
bot.polling(none_stop=True)

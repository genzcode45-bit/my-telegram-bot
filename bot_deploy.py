import telebot
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')
OWNER_ID = 6869861598  # <- PASTE OWNER TELEGRAM ID HERE

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "✅ ViewRise Bot Active!
Send your message...")

@bot.message_handler(func=lambda message: True)
def forward_to_owner(message):
    try:
        # Forward customer message to owner
        bot.forward_message(OWNER_ID, message.chat.id, message.message_id)
        bot.reply_to(message, "✅ Message sent to owner!")
    except Exception as e:
        bot.reply_to(message, "Please try again.")

print("ViewRise Bot Starting...")
bot.polling(none_stop=True)

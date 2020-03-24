import telebot 

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "sorry. v1.1 it's not finish")

bot.polling()
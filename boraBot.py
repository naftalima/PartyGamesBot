import telebot 

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "hi, o que vc tem interesse em jogar?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "/bora - invite people to play \n /games - list of games")

@bot.message_handler(commands=['bora'])
def send_welcome(message):
	bot.reply_to(message, "o que??")
    
bot.polling()
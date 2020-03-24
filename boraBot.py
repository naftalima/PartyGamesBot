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

imageSelect = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
imageSelect.add('Mickey', 'Minnie')

@bot.message_handler(commands=['bora'])
def send_welcome(message):
	bot.reply_to(message, "jogar o que?")

bot.polling()
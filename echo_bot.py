import telebot

bot = telebot.TeleBot("1110772599:AAHB9ndbH893kZsnp0_pMX3A00LmsiYRb_8")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
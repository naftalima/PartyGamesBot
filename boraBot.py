import telebot
from telebot import types 
import msgs

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, msgs.start)

@bot.message_handler(commands=['help'])
def handle_help(message):
	bot.reply_to(message, msgs.help)

@bot.message_handler(commands=['bora'])
def handle_help(message):
	pass

@bot.message_handler(commands=['jogos'])
def handle_jogos(message):
	bot.reply_to(message, msgs.jogos)

@bot.message_handler(commands=['meusJogos'])
def handle_userJogos(message):
	pass

@bot.message_handler(commands=['editarMeusJogos'])
def handle_editUserJogos(message):
	pass

@bot.message_handler(commands=['SAC'])
def handle_SAC(message):
	pass

bot.polling()
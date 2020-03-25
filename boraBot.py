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
def send_commands(message):
	bot.reply_to(message, msgs.help)

@bot.message_handler(commands=['bora'])
	pass

@bot.message_handler(commands=['jogos'])
def send_games(message):
	bot.reply_to(message, msgs.jogos)

@bot.message_handler(commands=['meusJogos'])
	pass

@bot.message_handler(commands=['editarMeusJogos'])
	pass

@bot.message_handler(commands=['SAC'])
	pass

bot.polling()
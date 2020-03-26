import telebot
from telebot import types
from database import Collections
from dataTypes import UserInfo
import msgs

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
collections = Collections()

@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.send_chat_action(message.chat.id, 'typing')
  bot.send_message(message.chat.id, msgs.start)

  user_id = message.from_user.id
  username = message.from_user.username
  # setup a clean userinfo
  user_info = UserInfo(user_id, username, '', [], [], [])
  collections.create_or_update_user(user_info)
  bot.register_next_step_handler(message, get_steam_name_and_save)

def get_steam_name_and_save(message):
  bot.send_chat_action(message.chat.id, 'typing')
  steam_login = message.text
  if '/cancel' in steam_login:
    bot.reply_to(message, "Ok, depois coletamos seu login na steam :)")
  else:
    collections.update_user_steam_login(message.from_user.id, steam_login)
    bot.reply_to(message, "Suas informações foram salvas!")

@bot.message_handler(commands=['help'])
def handle_help(message):
  bot.send_chat_action(message.chat.id, 'typing')
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
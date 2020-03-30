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
  bot.send_message(message.chat.id, msgs.start_msg)

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
    bot.reply_to(message, msgs.cancel_steam_login_msg)
  else:
    collections.update_user_steam_login(message.from_user.id, steam_login)
    bot.reply_to(message, msgs.success_steam_login_msg)

@bot.message_handler(commands=['help'])
def handle_help(message):
  bot.send_chat_action(message.chat.id, 'typing')
  bot.reply_to(message, msgs.help_msg)

@bot.message_handler(commands=['bora'])
def handle_help(message):
  pass

@bot.message_handler(commands=['jogos'])
def handle_jogos(message):
  bot.reply_to(message, msgs.games_msg)

@bot.message_handler(commands=['meusJogos'])
def handle_userJogos(message):
  pass

@bot.message_handler(commands=['editarMeusJogos'])
def handle_editUserJogos(message):
  bot.send_chat_action(message.chat.id, 'typing')
  user_games = collections.get_user_games(message.from_user.id)
  markup = create_games_markup(user_games)
  bot.send_message(message.chat.id, msgs.add_games_first_msg, reply_markup=markup)
  bot.register_next_step_handler(message, edit_game_list_helper, [], user_games)

def create_games_markup(games_to_exclude):
  markup = types.ReplyKeyboardMarkup(row_width=5)
  markup.add(*[types.KeyboardButton(name) for name in msgs.games_dict.keys() if name not in games_to_exclude])
  return markup

def edit_game_list_helper(message, selected_games, user_games):
  bot.send_chat_action(message.chat.id, 'typing')
  if '/done' in message.text:
    markup = types.ReplyKeyboardRemove(selective=False)
    game_id_list = [msgs.games_dict[game_name].id for game_name in selected_games]
    collections.add_new_game_to_user_list(message.from_user.id, game_id_list)
    bot.send_message(message.chat.id, msgs.add_games_done_msg, reply_markup=markup)
  else:
    game_name = message.text
    if game_name not in msgs.games_dict:
      bot.reply_to(message, msgs.add_games_error_msg)
    elif game_name in (user_games + selected_games):
      bot.reply_to(message, msgs.add_games_duplicate_msg)
    else:
      selected_games.append(game_name)
      new_markup = create_games_markup(user_games+selected_games)
      bot.reply_to(message, msgs.add_games_reply_msg, reply_markup=new_markup)
    bot.register_next_step_handler(message, edit_game_list_helper, selected_games, user_games)

@bot.message_handler(commands=['SAC'])
def handle_SAC(message):
  pass

bot.polling()
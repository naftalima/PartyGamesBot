import telebot
from telebot import types
from database import Collections
from dataTypes import UserInfo, GroupInfo
import games
import msgs

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
bot_id = 1098836049
collections = Collections()

def private_message_filter(message):
  return message.chat.type == "private"

def group_message_filter(message):
  return "group" in message.chat.type

@bot.message_handler(content_types=["new_chat_members"])
def handle_new_chat_member(message):
  members_ids = [member.id for member in message.new_chat_members]
  if bot_id in members_ids:
    group = GroupInfo(message.chat.id, message.chat.title, [])
    collections.create_group(group)
    bot.send_message(message.chat.id, msgs.group_start_msg)

@bot.message_handler(content_types=["left_chat_member"])
def handle_left_chat_member(message):
  if bot_id == message.left_chat_member.id:
    collections.delete_group(message.chat.id)
  else:
    collections.remove_group_member(message.chat.id, message.left_chat_member.id)

@bot.message_handler(commands=['start'], func=private_message_filter)
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

  bot.send_chat_action(message.chat.id, 'typing')
  user_games = games.from_id_to_name_list(collections.get_user_games(message.from_user.id))
  markup = create_games_markup(user_games)
  bot.send_message(message.chat.id, msgs.add_games_intro_msg, reply_markup=markup)
  bot.register_next_step_handler(message, add_game_list_helper, [], user_games)

@bot.message_handler(commands=['join'], func=group_message_filter)
def handle_join(message):
  bot.send_chat_action(message.chat.id, 'typing')
  #Check if bot can talk to user
  try:
    bot.send_message(message.from_user.id, msgs.join_private_msg.format(message.chat.title))
    collections.add_group_member(message.chat.id, message.from_user.id)
    bot.reply_to(message, msgs.join_group_msg)
  except:
    bot.reply_to(message, msgs.join_error_msg)

@bot.message_handler(commands=['leave'], func=group_message_filter)
def handle_leave(message):
  bot.send_chat_action(message.chat.id, 'typing')
  collections.remove_group_member(message.chat.id, message.from_user.id)
  bot.reply_to(message, msgs.leave_reply_msg)

@bot.message_handler(commands=['help'])
def handle_help(message):
  bot.send_chat_action(message.chat.id, 'typing')
  bot.reply_to(message, msgs.help_msg)

@bot.message_handler(commands=['bora'])
def handle_bora(message):
  pass

@bot.message_handler(commands=['jogos'])
def handle_jogos(message):
  bot.reply_to(message, msgs.games_msg)

@bot.message_handler(commands=['meusJogos'], func=private_message_filter)
def handle_meusJogos(message):
  bot.send_chat_action(message.chat.id, 'typing')
  user_games = collections.get_user_games(message.chat.id)
  answer = ''
  if len(user_games) == 0:
    answer = msgs.user_games_list_empty_msg
  else:
    games_string = '\n'.join(
      [msgs.user_games_list_item_msg.format(games.from_id_to_name(game))
        for game in user_games])
    answer = msgs.user_games_list_msg.format(games_string)
  bot.send_message(message.chat.id, answer)

  markup = types.ReplyKeyboardMarkup()
  markup.row(types.KeyboardButton(msgs.yes_msg), types.KeyboardButton(msgs.no_msg))
  bot.send_message(message.chat.id, msgs.user_games_edit_question_msg, reply_markup=markup)
  bot.register_next_step_handler(message, edit_question_helper)

def edit_question_helper(message):
  if message.text == msgs.no_msg:
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, msgs.ok_msg, reply_markup=markup)
  elif message.text == msgs.yes_msg:
    #TODO(luucasv): add remove option here
    add_user_games_helper(message)

def add_user_games_helper(message):
  bot.send_chat_action(message.chat.id, 'typing')
  user_games = games.from_id_to_name_list(collections.get_user_games(message.from_user.id))
  markup = create_games_markup(user_games)
  bot.send_message(message.chat.id, msgs.add_games_first_msg, reply_markup=markup)
  bot.register_next_step_handler(message, add_game_list_helper, [], user_games)

def create_games_markup(games_to_exclude):
  markup = types.ReplyKeyboardMarkup(row_width=5)
  markup.add(*[types.KeyboardButton(name) for name in games.all_game_names() if name not in games_to_exclude])
  return markup

def add_game_list_helper(message, selected_games, user_games):
  bot.send_chat_action(message.chat.id, 'typing')
  if '/done' in message.text:
    markup = types.ReplyKeyboardRemove(selective=False)
    game_id_list = games.from_game_name_to_id_list(selected_games)
    collections.add_new_game_to_user_list(message.from_user.id, game_id_list)
    bot.send_message(message.chat.id, msgs.add_games_done_msg, reply_markup=markup)
  else:
    game_name = message.text
    if not games.game_name_exists(game_name):
      bot.reply_to(message, msgs.add_games_error_msg)
    elif game_name in (user_games + selected_games):
      bot.reply_to(message, msgs.add_games_duplicate_msg)
    else:
      selected_games.append(game_name)
      new_markup = create_games_markup(user_games+selected_games)
      bot.reply_to(message, msgs.add_games_reply_msg, reply_markup=new_markup)
    bot.register_next_step_handler(message, add_game_list_helper, selected_games, user_games)

@bot.message_handler(commands=['SAC'])
def handle_SAC(message):
  pass

bot.polling()

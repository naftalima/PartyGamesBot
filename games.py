import pandas as pd
from dataTypes import GameInfo

df_games = pd.read_csv('data/games.csv')
games_list = [GameInfo(row.Id, row.Name, row.Genre, row.Flag) for row in df_games.itertuples()]

games_name_dict = {}
games_id_dict = {}
for game in games_list:
  games_name_dict[game.name] = game
  games_id_dict[game.id] = game

def from_id_to_name(game_id):
  return games_id_dict[game_id].name

def from_id_to_name_list(game_id_list):
  return [from_id_to_name(game_id) for game_id in game_id_list]

def from_game_name_to_id(game_name):
  return games_name_dict[game_name].id

def from_game_name_to_id_list(game_name_list):
  return [from_game_name_to_id(game_name) for game_name in game_name_list]

def game_name_exists(game_name):
  return game_name in games_name_dict

def all_game_names():
  return list(games_name_dict.keys())
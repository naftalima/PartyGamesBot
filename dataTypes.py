class GroupInfo:
  def __init__(self, id, name, members):
    self.id = id
    self.name = name
    self.members = members
  
  @staticmethod
  def from_dict(json):
    return GroupInfo(json['id'], json['name'], json['members'])

class GameScheduleInfo:
  def __init__(self, id, game_id, time):
    self.id = id
    self.game_id = game_id
    self.time = time
  
  @staticmethod
  def from_dict(json):
    return GameScheduleInfo(json['id'], json['game_id'], json['time'])

class UserInfo:
  def __init__(self, id, username, steam_login, groups, games, scheduled_games):
    self.id = id
    self.username = username
    self.steam_login = steam_login
    self.groups = groups
    self.games = games
    self.scheduled_games = scheduled_games
  
  @staticmethod
  def from_dict(json):
    return UserInfo(json['id'],
      json['username'],
      json['steam_login'], 
      json['groups'],
      json['games'],
      json['scheduled_games'])

class GameInfo:
  def __init__(self, id, name, genre, flag):
    self.id = id
    self.name = name
    self.genre = genre.split('|')
    self.flag = flag

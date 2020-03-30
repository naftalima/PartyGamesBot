import pymongo

class Collections:
  def __init__(self):
    self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    self.db = self.client.boraBotDb
    self.userCollection = self.db.userCollection

  def create_or_update_user(self, user):
    self.userCollection.update_one({'id': user.id}, {'$set': user.__dict__}, upsert=True)

  def update_user_steam_login(self, user_id, steam_login):
    self.userCollection.update_one({'id': user_id}, {'$set': {'steam_login': steam_login}})
  
  def add_new_game_to_user_list(self, user_id, game_id_list):
    self.userCollection.update_one({'id': user_id}, {'$addToSet': {'games': {'$each': game_id_list}}})

  def get_user_games(self, user_id):
    user = self.userCollection.find_one({'id': user_id})
    games = user['games']
    return games if games else []
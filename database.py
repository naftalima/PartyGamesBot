import pymongo
from dataTypes import *

class Collections:
  def __init__(self):
    self.client = pymongo.MongoClient("mongodb://localhost:27017/")
    self.db = self.client.boraBotDb
    self.userCollection = self.db.userCollection
    self.groupCollection = self.db.groupCollection

  # User collection methods
  def create_or_update_user(self, user):
    self.userCollection.update_one({'id': user.id}, {'$set': user.__dict__}, upsert=True)

  def update_user_steam_login(self, user_id, steam_login):
    self.userCollection.update_one({'id': user_id}, {'$set': {'steam_login': steam_login}})
  
  def add_new_game_to_user_list(self, user_id, game_id_list):
    self.userCollection.update_one({'id': user_id}, {'$addToSet': {'games': {'$each': game_id_list}}})

  def add_new_group_to_user_list(self, user_id, group_id):
    self.userCollection.update_one({'id': user_id}, {'$addToSet': {'groups': group_id}})

  def remove_group_from_user_list(self, user_id, group_id):
    self.userCollection.update_one({'id': user_id}, {'$pull': {'groups': group_id}})

  def get_user_games(self, user_id):
    user = UserInfo.from_dict(self.userCollection.find_one({'id': user_id}))
    return user.games if user.games else []

  # Group collection methods
  def create_group(self, group):
    self.groupCollection.insert_one(group.__dict__)

  def delete_group(self, group_id):
    self.groupCollection.remove({'id': group_id})

  def remove_group_member(self, group_id, member_id):
    self.groupCollection.update_one({'id': group_id}, {'$pull': {'members': member_id}})

  def add_group_member(self, group_id, member_id):
    self.groupCollection.update_one({'id': group_id}, {'$addToSet': {'members': member_id}})

  def get_group_members(self, group_id):
    group = GroupInfo.from_dict(self.groupCollection.findOne({'id': group_id}))
    return group.members if group.members else []

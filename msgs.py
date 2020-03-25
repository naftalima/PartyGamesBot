import pandas as pd

class GameInfo:
    def __init__(self,name,description,flag):
        self.name = name
        self.description = description
        self.flag = None

df_games = pd.read_csv('data/games.csv')
gamesList = [GameInfo(row.Name, row.Description, row.Flag) for row in df_games.itertuples()]

names = [j.name for j in gamesList]
names.sort()
jogos = "\n".join(names)

start = (
    'Lorem Ipsum is simply dummy text of the printing'
    'Lorem Ipsum is simply dummy text of the printing'
    'Lorem Ipsum is simply dummy text of the printing'
)

help = (
    '/bora - Lorem Ipsum is simply dummy text of the printing\n'
    '/jogos - Lorem Ipsum is simply dummy text of the printing\n'
    '/meusJogos - Lorem Ipsum is simply dummy text of the printing\n'
    '/editarMeusJogos - Lorem Ipsum is simply dummy text of the printing\n'
    '/SAC - Lorem Ipsum is simply dummy text of the printing'
)

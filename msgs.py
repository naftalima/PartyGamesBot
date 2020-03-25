import pandas as pd

class Game:
    def __init__(self,name,description,flag):
        self.name = name
        self.description = ''
        self.flag = None

df_games = pd.read_csv('data/games.csv')

gamesList = []
for row in df_games.itertuples():
    game = Game(row.Name, row.Description, row.Flag)
    gamesList.append(game)

names = []
for i in gamesList:
    names.append(i.name)

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

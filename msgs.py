import pandas as pd
from dataTypes import GameInfo

df_games = pd.read_csv('data/games.csv')
gamesList = [GameInfo(row.Name, row.Description, row.Flag) for row in df_games.itertuples()]

names = [j.name for j in gamesList]
names.sort()
jogos = "\n".join(names)

start = """
Olá, espero que esteja se cuidando.
Bora cadastrar uns jogos e relaxar um pouco a mente?
Para começar, gostaria de me dizer seu login da steam? (envie /cancel para responder depois)
"""

help = (
    '/bora - Lorem Ipsum is simply dummy text of the printing\n'
    '/jogos - Lorem Ipsum is simply dummy text of the printing\n'
    '/meusJogos - Lorem Ipsum is simply dummy text of the printing\n'
    '/editarMeusJogos - Lorem Ipsum is simply dummy text of the printing\n'
    '/SAC - Lorem Ipsum is simply dummy text of the printing'
)

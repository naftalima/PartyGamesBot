import games
from emoji import emojize

games_msg = "\n".join(sorted(games.all_game_names()))

start_msg = """
Olá, espero que esteja se cuidando.
Bora cadastrar uns jogos e relaxar um pouco a mente?
Para começar, gostaria de me dizer seu login da steam? (envie /cancel para responder depois)
"""

#TODO: improve this message
group_start_msg = """
Olá, eu sou o @boJogarBot
Para receber convites de jogos neste grupo, envie /join
Não esqueça de conversar comigo no privado antes.
"""

yes_msg = "Sim"
no_msg = "Não"
ok_msg = "Ok"

help_msg = """
comandos:
/bora - convide seus amigos para jogar
/jogos - lista de jogos
/meusJogos - lista dos seus jogos
/editarMeusJogos - edite seus jogos
/SAC
"""

cancel_steam_login_msg = """
Ok, depois coletamos seu login na steam :)
"""

success_steam_login_msg = """
Suas informações foram salvas!
"""

add_games_done_msg = "Ótimo, suas mudanças foram salvas. Use /meusJogos para ver sua lista de jogos."

add_games_intro_msg = "Que tal nos dizer quais jogos deseja jogar? Selecione um dos jogos abaixo ou envie /done para finalizar"

add_games_first_msg = "Por favor, escolha um dos jogos abaixo para adicionar a sua lista, envie /done para finalizar sua escolha"

add_games_reply_msg = "Adicionado, deseja adicionar outro? Envie /done para finalizar"

add_games_error_msg = "Jogo invalido, escolha um jogo da lista abaixo"

add_games_duplicate_msg = "O jogo ja foi adicionado, escolha um jogo da lista abaixo"

user_games_list_item_msg = "* {}"

user_games_list_msg = """
Estes são os jogos que você adicionou:

{}
"""

user_games_list_empty_msg = emojize("""
Você não possui jogos em sua lista :confused:
""", use_aliases=True)

user_games_edit_question_msg = """
Você gostaria de editar sua lista de jogos?
"""

join_private_msg = """
Você foi adicionado a um grupo de jogos em "{}"
"""

join_group_msg = """
Feito, envie /leave caso queira reverter esta ação.
"""

join_error_msg = """
Você deve conversar comigo no privado antes.
"""

leave_reply_msg = emojize(":disappointed:", use_aliases=True)

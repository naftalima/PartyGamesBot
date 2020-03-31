import games

games_msg = "\n".join(sorted(games.all_game_names()))

start_msg = """
Olá, eu sou o @boJogarBot.
Vou te ajudar a jogar com os migos.
Vá lavar as mãos I’m telling you, shit is real! Shit is getting real!
"""

add_jogos_msg = """
Bora cadastrar uns jogos e relaxar um pouco a mente?
"""

steam_msg = """
Para começar, gostaria de me dizer seu login da steam? 
(envie /cancel para responder depois)
"""

help_msg = """
comandos:
/bora - convide seus amigos para jogar
/jogos - lista de jogos
/meusJogos - lista dos seus jogos
/SAC
"""

cancel_steam_login_msg = """
Ok, depois coletamos seu login na steam :)
"""

success_steam_login_msg = """
Suas informações foram salvas!
"""

add_games_done_msg = "Ótimo, suas mudanças foram salvas. Use /meusJogos para ver sua lista de jogos."

add_games_intro_msg = """
Bora cadastrar uns jogos e relaxar um pouco a mente?
Selecione um dos jogos abaixo ou envie /done para finalizar"""

add_games_first_msg = "Por favor, escolha um dos jogos abaixo para adicionar a sua lista, envie /done para finalizar sua escolha"

add_games_reply_msg = "Adicionado, deseja adicionar outro? Envie /done para finalizar"

add_games_error_msg = "Jogo invalido, escolha um jogo da lista abaixo"

add_games_duplicate_msg = "O jogo ja foi adicionado, escolha um jogo da lista abaixo"

edit_mygames = """
/addMeusJogos - para adicionar a sua lista de jogos
/removeMeusJogos - para remover de sua lista de jogos 
"""

remove_game = "VOU TE REMOVER"
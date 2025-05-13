from random import randint


lista_npc = []


player = {
    'nome': 'Rafael', 
    'level': 1,
    'exp': 0,
    'exp_max': 50,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,
}

def criar_npc(level):
    

    novo_npc = {
        'nome':f'montro-{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
        'hp_max': 100*level,
        'exp': 7 * level,
    }


    lista_npc.append(novo_npc)


def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        

def exibr_npcs():
    for npc in lista_npc:
        exibir_npc()

def exibir_npc(npc):
     print(f"Nome: {npc['nome']} \\ Level: {npc['level']} \\ Dano: {npc['dano']} \\ HP: {npc['hp']} \\ EXP: {npc['exp']}")


def exibir_player():
     print(f"Nome: {player['nome']} \\ Level: {player['level']} \\ Dano: {player['dano']} \\ HP: {player['hp']} \\ EXP: {player['exp']}\{player['exp_max']}")


def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['hp_max'] += 25
        

def iniciar_batalha (npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        npc['hp'] = npc['hp'] - player['dano']
        atacar_player(npc)
        exibir_inf_batalha(npc)
    if player['hp'] > 0:
        print(f"O {player['nome']} venceu e recebeu {npc['exp']} de XP")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print('O player morreu')
        exibir_npc(npc)
    level_up()

    reset_player()
    reset_npc(npc)


# atacar_player(npc) - player:hp -npc:dano

def atacar_player (npc):
    player['hp'] = player['hp'] - npc['dano']        


def exibir_inf_batalha(npc):
    print(f"Player: {player['hp']}\{player['hp_max']}")
    print(f"NPC: {npc['nome']}\{npc['hp']}\{npc['hp_max']}")
    print("---------------------------\n")

gerar_npcs(5)

npc_selecionado = lista_npc[0]
iniciar_batalha(npc_selecionado)

for i in range(15):
    iniciar_batalha(npc_selecionado)



  














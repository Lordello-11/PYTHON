pessoa = {
    'nome':'programador python',
    'idade': 27,
    'peso': 70.2
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])



# exeplo

player = {
    'nome': 'guilherme',
    'level': 1,
    'hp': 100,
    'exp': 0,
    'dano': 5,

}

npcs = [
    {'nome':'mostro', 'dano':2, 'hp': 50, 'exp':5},
    {'nome':'bruxa', 'dano':5, 'hp': 150, 'exp':15},
]

import os

mansagens = []

nome = input('Nome:')

while True:
    # limpando terminal
    os.system('cls')

    if len(mansagens) > 0:
        for m  in mansagens:
            print(m['nome'], '-', m['texto'])

    print('_________________________')        

    # obtendo texto
    texto = input('mensagem-')
    if texto == 'fim':
        break
    
    # adicionar mensagem na lista
    mansagens.append({
        'nome': nome,
        'texto': texto,
    })
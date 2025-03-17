vendas = [100, 50, 130, 80, 120]
#          0    1   2    3   4 

print(vendas[0])# para pegar o utimo elemento utilize (-1) que pegs da direita para esquerda

total_vendas = sum(vendas)# para somar todos os valores de uma lista
print(total_vendas)

quantidade = len(vendas) # para a quantidade de itens de uma lista
print(quantidade)

valor_max = max(vendas)# para o maior valor
valor_min = min(vendas)# para o menor valor
print(valor_max,valor_min)

posicao = vendas.index(130)# index para pegar o valor da posição do item na lista
print(posicao)
print(vendas[2:])# pode recortar a lista


produtos = ['iphone','ipad', 'airpod']
preco = [4000, 8000, 2000]

# print('iphone' in produtos) para verificar se tem o itwem na lista| in = verifica se o item esta na lista com  true(verdadeiro)ou false(não contem)

# verifica se tem o item
produto_user = input('digite o nome do produto:')
print(produto_user in produtos)

# edita o item
preco[0] = 4500 # editar o valor de um item 
preco [0] = preco[0] * 1.1
print(preco)

# Adicionar na lista
produtos.append('macbook')# append serve par adicionar novo item na lista
preco.append('10000')
print(produtos)
print(preco)

# Remover da lista(romove ou pop)
produtos.remove('macbook')
preco.pop(-1)
print(produtos)
print(preco)

# Inserir um valor
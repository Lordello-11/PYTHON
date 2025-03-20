precos = [ 1500, 1000, 800, 2000]
produtos = ['celular', 'camera', 'fone de ouvido', 'monitor']

dic_preco = {'celular': 1500, 'camera':1000, 'fone de ouvido':800, 'monitor':2000} #Chave:valor,


# pegar um item

precos_celular = dic_preco['celular']
print(precos_celular)

# editar valor
dic_preco['celular'] = 2000
print(dic_preco)

# adicionar

dic_preco['iphone'] = 4500
print(dic_preco)

# remover
dic_preco.pop('iphone')
print(dic_preco)

# tamanho
print(len(dic_preco))
 
# procurar chave
print('televisão' in dic_preco)

# procurar valor
print(1500 in dic_preco.values())

print(dic_preco.keys())
print(dic_preco.values())

# exercicio
dic_produto = {'celular':1500, 'camera':1000, 'fone de ouvido':800, 'monitor':2000}

procura = input('digite o nome do produto:')
procura = procura.lower()

if procura in dic_preco:
    print(f'{procura}: {dic_preco[procura]}')
else:
    print(f'produto {procura} não encontrado, tente novamente')    
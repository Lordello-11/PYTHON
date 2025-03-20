faturamento = 1000
custo = 2800

lucro = faturamento - custo

# if condicao(comparacao):


if lucro >= 0:
    # tudo o que voce quer que aconteça se condição for verdadeira
    print(lucro)
else:
    # tudo o que voce quer que apareça se a condição for falsa
    print(f'PREJUIZO de {lucro}')


# produtos = ['iphone','ipad', 'airpod']
# novo_produto = input('Digite o nome do produto:')
# novo_produto = novo_produto.lower() # tratamento para letra minuscula

# if novo_produto in produtos: # IN verifica de o nome digitado esta na lista de produtos
#     print('produto ja cadastrado')
# else:
#     print('produto cadastrado com sucesso')   
#     produtos.append(novo_produto) 

# print(produtos)


# acima de 15000  -> 500 de bonus
# acima de 10000  -> 150 de bonus
# acima de 5000   -> 50 de bonus
# casso contrario -> 0 de bonus

vendas = int(input('Valor de vendas:'))



if vendas > 15000:
    bonus = 500

#  caso contrario, se  for maior  que 10000
elif vendas > 10000:
    bonus = 150
elif vendas > 5000:
    bonus = 50    
else:
    bonus = 0    

print(bonus)   

# outra forma de fazer
if vendas > 5000:
    if vendas > 10000:
        if vendas > 15000:
            bonus = 500
        else:
            bonus = 150    
    else:
        bonus = 50   
else:
    bonus = 0

print(bonus)    

# acima de 15000  -> 500 de bonus
# acima de 10000  -> 150 de bonus
# acima de 5000   -> 50 de bonus
# casso contrario -> 0 de bonus
# vendas da empresa > 50000

vendas = 17000
vendas_empresa = 40000
meta_empresa = 50000

# and(analiasar mais de uma condição)
# or (analisa se uma ou a outra é verdadeira)

if not vendas_empresa > meta_empresa:
    bonus = 0
if vendas > 15000 and vendas_empresa >= meta_empresa: 
    bonus = 500
elif vendas > 10000 and vendas_empresa >= meta_empresa:
    bonus = 150
elif vendas > 5000 and vendas_empresa >= meta_empresa:
    bonus = 50    
else:
    bonus = 0   


print(bonus)    


# exercicio desafio
# sistema de consulta de preço
precos = [ 1500, 1000, 800, 2000]
produtos = ['celular', 'camera', 'fone de ouvido', 'monitor']

produto_procurado = input('Digite o nome do produto1:')
produto_procurado = produto_procurado.lower()

if produto_procurado in produtos:
    posicao = produtos.index(produto_procurado)
    preco = precos[posicao] 
    print(f'Produto:{produto_procurado}, preço {preco}')
else:
    print('produto não encotardo, tente novamente') 




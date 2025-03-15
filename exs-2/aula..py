
# numeros: inteiros(int) e decimais(float)
# texto:  texto(string),booleanos(verdadeiro ou falso = boolean)

faturamento = int(input('digite o valor do faturamento:'))
custo = int(input('digite o valor do custo:'))
novas_vendas = int(input('digite o valor da nova venda:'))

faturamento = faturamento + novas_vendas
taxa_de_imposto = 0.1 #definir porcentagem em decimal e não fração (10%) -> float
imposto = taxa_de_imposto * faturamento
lucro = faturamento-custo - imposto
mensagem = ('O faturamnto da sua empresa foi de ')

print( 'Faturamnto:' , faturamento)
print('Custo:' , custo )
print('Valor do Imposto:', imposto)
print('lucro:' , lucro)
print(mensagem , faturamento)




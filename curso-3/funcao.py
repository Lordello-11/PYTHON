def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input('valor-1:'))
    valor2 = int(input('valor-2:'))


    reposta = minha_funcao(valor1, valor2)
    print (f'{valor1} + {valor2} = {reposta}')


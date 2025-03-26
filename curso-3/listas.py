lista_numerica = [1, 2 ,3]
                #  0  1  2
print(lista_numerica[0])
print(lista_numerica[1])
print(lista_numerica[2])

# editar lista
lista_numerica = [1, 2 ,3]

lista_numerica[0] = 5

print(lista_numerica[0])
print(lista_numerica[1])
print(lista_numerica[2])

# tipos de lista
numerica = [1,2,3]
strings = ['joão', 'maria', 'bruxa']
decimal = [10.8, 15.2, 33.3]

# Exemplo 1

lista_vazia = []

frase = input('uma frase:')
frase1 = input('outra frase:')

lista_vazia.append(frase)
lista_vazia.append(frase1)

print(lista_vazia)

# Exenplo 2

numero = [10, 9 ,8 ,7 ,6]

print('total:', len(numero))
print('menor valor:', min(numero))
print('maior valor:', max(numero))

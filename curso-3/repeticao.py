for x in range(10):
    print(x)


# exeplo

notas = []
for x in range(5):
    codigo_aluno = input('RM:')
    nota = float(input('Nota:'))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
print(notas)

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM', codigo_aluno, 'tiro a nota:', nota)

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input('RM:')
    nota = float(input('Nota:'))
    resultado = [ codigo_aluno, nota]
    notas.append(resultado)

    # alternativa: contador += 1
    contador = contador + 1

print('quantidade de notas', len(notas
))    
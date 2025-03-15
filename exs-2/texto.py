

faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f'Faturamnto: {faturamento}, Custo: {custo}, Lucro: {lucro}') #formatar com o F no inicio e colocar as variaveis entre chaves
print('Faturamento:' + '1000')# utilizand0 o sinal de (+) para unir dois textos
print('Faturamento:' + str(faturamento) + ',Custo:' + str(custo)+ ',Lucro:'+ str(lucro))# para tranforma o valor da variavel em texto utilizar (str = string)

email = 'EMAIL_falso@gmail.com'
        #1234567891011
print(email.lower()) # utilizando (email.lower) para trocar colocar todo o email em letra minuscula
print(email.find('@'))# -1, se não encontrar o elemento. Se encontrar: a posição

print(email[12])

posicao = email.find('@')
servidor = email[posicao+1:]
print(servidor)

nome_do_email = email[:posicao]
print(nome_do_email)

# tamano de um texto
tamanho = len(email)

print(tamanho)
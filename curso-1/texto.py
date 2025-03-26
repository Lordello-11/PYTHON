

# faturamento = 1000
# custo = 700
# lucro = faturamento - custo

# print(f'Faturamnto: {faturamento}, Custo: {custo}, Lucro: {lucro}') #formatar com o F no inicio e colocar as variaveis entre chaves
# print('Faturamento:' + '1000')# utilizand0 o sinal de (+) para unir dois textos
# print('Faturamento:' + str(faturamento) + ',Custo:' + str(custo)+ ',Lucro:'+ str(lucro))# para tranforma o valor da variavel em texto utilizar (str = string)

# email = 'EMAIL_falso@gmail.com'
#         #1234567891011
# print(email.lower()) # utilizando (email.lower) para trocar colocar todo o email em letra minuscula
# print(email.find('@'))# -1, se não encontrar o elemento. Se encontrar: a posição

# print(email[12])

# posicao = email.find('@')
# servidor = email[posicao+1:]
# print(servidor)

# nome_do_email = email[:posicao]
# print(nome_do_email)

# # tamano de um texto
# tamanho = len(email)# len(tamanho do texto) quantidade de caracteris
# print(tamanho)

# # trocar o texto
# email_troca = email.replace('gmail.com', 'hotmail.com')
# print(email_troca)

# nome = 'rafael martins'
# print(nome.capitalize())# coloca a primeira letra em maiscula
# print(nome.title()) # coloca a primeira letra de cada palavra em maiscula

# #Especiais -> formatação numerico
# margem = lucro / faturamento
# print(f'Faturamnto: R${faturamento:,.2f}\n Custo: {custo}\n Lucro: {lucro}') 
# print(f'Margem:{margem:.1%}')

# exercicio 

nome = 'Rafael Martins Cardoso'
email = 'emailfalso2@gmail.com'

# descubra o servidor do email
num_pro = email.find('@')
nome_serv = email[num_pro:]

print(nome_serv)


# pegar o primeiro nome do usuario
posicao = nome.find(' ')
primeiro_nome = nome[:posicao]
print(primeiro_nome)

#construa uma mensagem:Usuario primeiro_nome cadastro com sucesso  o email
mensagem = f'Usuario {primeiro_nome} cadastrado com sucesso  com o email: {email}'
print(mensagem)

#costrua uma mensagem : Enviamos um email para você( R****@gmail)
primeira_letra = nome[0]
print(f'Enviamos um email para {primeira_letra}*****{nome_serv}')
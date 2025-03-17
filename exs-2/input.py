nome = input('Escreva seu nome:')
email = input('Digite seu e-mail:')


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
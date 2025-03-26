idade = int(input('Informe sua idade:'))

if idade >= 18:
    print('pode entrar')
else:
    print('não pode entrar você é menor de idade')    

salario = int(input('Informe  se salario:'))

if salario <= 3000:
    print('programador junio')
elif salario > 3000 and salario <= 6000:
    print(' programador pleno')
elif salario > 6000 and salario <= 15000:
    print('programador senior')    
else:
    print('gerente de projetos')
lista_precos = [ 1500, 1000, 800, 2000, 3000]

total_imposto = 0 # acumulado

def cal_imposto(preco, aliquota1=0.2, aliquota2=0.15,aliquota3=0.1): # (valor) é a variaavel da função| = 0.2 é o valor padrão

    if preco > 2000:
        imposto = preco * aliquota1    
    elif preco <= 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    print(f'preço:{preco}, imposto:{imposto}')
    return imposto # retorna  a variavel para fora da funçao

for preco in lista_precos:
    imposto = cal_imposto(preco, 0.2, 0.15, 0.1)
    total_imposto = total_imposto +imposto
    
print(total_imposto)


def cal2_imposto(preco, ir=0.275,  csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll , imposto_iss # pode pedir varios resultados

resposta = cal2_imposto(1000)
print(resposta)




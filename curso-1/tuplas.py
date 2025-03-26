def cal2_imposto(preco, ir=0.275,  csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll , imposto_iss # pode pedir varios resultados

resposta = cal2_imposto(1000)
print(resposta)# tupla(275.0, 35.0, 50.0) -> imultavel(não da para )

ir, csll ,iss = resposta
print(ir, csll, iss , sep='\n')

tamanho_tela =( 1920, 1080)


#exercicio desafiador

vendas = {
    'André':[1000,500, 300, 5000, 1500, 80, 3000],
    'Adressa':[1500, 9000, 300, 1500, 1500, 120, 130, 55, 5000, 8500],
    'Alan':[800,100],
    'Ana':[800, 900, 950, 1200, 1600, 130, 50,50,50,50,65,60,70,70,70,200,180],
}

# cada venda o vendedor ganha  R$2 e 1% do valor de venda




# calcular o valor total  de bonus pago  e o  bonus  de cada vendedor

def cal_bonus(lista_vendas):
    qtde = len(lista_vendas)
    bonus1 = qtde*2
    valor_total = sum(lista_vendas_vendedor)
    bonus2 = valor_total * 0.01
    bonus = bonus1 + bonus2
    
    return bonus


bonus_total = 0
for vendedor in vendas:
    lista_vendas_vendedor = vendas[vendedor]
    bonus = cal_bonus(lista_vendas_vendedor)

    print(f'Vendedor {vendedor}, bonus: {bonus} ')
    bonus_total = bonus_total + bonus
print(bonus_total)
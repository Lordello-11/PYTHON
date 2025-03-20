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








vendas = []


while True:

    nova_venda = input('Valor da nova venda:')
    nova_venda = nova_venda.lower()
    
    
    if 'sair' == nova_venda: 
        break

    vendas.append(nova_venda)

print(f'vendas:{vendas}')

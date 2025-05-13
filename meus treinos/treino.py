class MeuGato:
    def __init__(self, nome, comer, sono):
        self.nome = input('novo nome:') # Atributo para o nome do gato
        self.comer = comer  # Atributo para a quantidade de comida que o gato tem
        self.sono = sono  # Atributo para o estado do sono (True ou False)
    
   

    def dormir(self):
        self.sono = True  # Faz o gato dormir, ou seja, muda o estado do sono para True
    
    def comida(self):
        self.comer -= 1  # Diminui 1 unidade de comida do gato
    
    def __str__(self):
        # Método para personalizar a exibição do objeto
        return f'Nome: {self.nome}, Comer: {self.comer}, Sono: {self.sono}, novo nome:{self.nome}'

# Criando instâncias de gato
gato_1 = MeuGato('Sol', 3, True)
gato_2 = MeuGato('Lua', 2, False)




# Exibindo informações dos gatos
print(gato_1)
print(gato_2)



    
















    

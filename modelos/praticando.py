class Carro: #classe
    def __init__(self, modelo, cor, ano): # Métodos
        self.modelo = '' # atributos
        self.cor = '' # atributos
        self.ano = int # atributos 


#instancias
carro1 = Carro ('Toyota' , 'Prata', 2010)

class Restaurante:
    def __init__(self, nome, categoria, ativo, cidade, estado):
        self.nome =''
        self.categoria = ''
        self.ativo = False
        self.cidade = ''
        self.estado = int
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.cidade}'        

restaurante_01 = Restaurante('Chapa', 'Lanches', 'False', 'São Paulo','SP') 

print(restaurante_01.categoria, restaurante_01.cidade)

class Cliente ():
    def __init__(self):
        self.nome = ''
        self.idade = int
        self.cor = ''
        self.genero = ''

cliente_01 = Cliente ('Luan', 26, 'Branco')
        

        






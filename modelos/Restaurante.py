class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # metodo especial
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)


    def __str__(self): #Metodo especial
        return f'{self._nome} | {self._categoria}'
@classmethod    
def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo}')

@property # modificar atributo deve seguir
def ativo(self):
    return 'Alguma coisa' if self._ativo else 'false'

def alternar_estado(self):
     self._ativo = not self.a_ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')    

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()


from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # metodo especial
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
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

def receber_avaliacao(self, cliente, nota):
     avaliacao = Avaliacao(cliente, nota)
     self._avalicao.append(avaliacao)
@property
def media_avaliacoes(self):
     if not self._avaliacao:
          return 0
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) 
    quantidade_de_notas = len(self._avaliacao)
    media = round(soma_das_notas / quantidade_de_notas,1)
    return media
          
          




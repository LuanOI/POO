class Livro:
    def __init__(self, titulo, autor, ano_publicacao): #construtor
        self._disponivel = True
        self._titulo = titulo #atributos
        self._autor = autor 
        self._ano_publicacao = ano_publicacao


    def __str__(self): #Metodo especial
        return f'Título do livro: {self._titulo} | Autor: {self._autor} | Ano da publicação: {self._ano_publicacao} |Livro disponível: {self._disponivel}' 
    
    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(self, ano):
        return f'Livros disponíveis publicados esse ano: {self._titulo | self._ano}'


livro1 = Livro ('Um romance no Jardim', 'Benjamin Button', 2000)#instancia

livro1.emprestar()    


print(livro1)




        


    
    

        




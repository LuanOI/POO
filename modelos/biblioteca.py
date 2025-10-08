from modelos.programa import Livro

livro1 = Livro ('Um romance no Jardim', 'Benjamin Button', 2000)#instancia


livro1.emprestar()

print(f"O livro '{livro1._titulo}' está disponível? {livro1._disponivel}")

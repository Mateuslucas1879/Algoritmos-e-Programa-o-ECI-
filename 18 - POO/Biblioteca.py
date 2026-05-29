class Livro:
    def __init__(self, titulo, autor,disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Livro: {self.titulo}\nAutor: {self.autor}")

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"Livro '{self.titulo}' Disponivel")
        else:
            print(f"Livro '{self.titulo}' Emprestado")



# Criando o livro (ele nasce como True automaticamente)
meu_livro = Livro('Orgulho e Preconceito', 'Jane Austen')
meu_livro.exibir_detalhes()

# Tentativa 1: Livro está livre
meu_livro.emprestar()  # Vai dizer: Sucesso! O livro foi emprestado.

print("-" * 20)

# Tentativa 2: Alguém tenta pegar o MESMO livro de novo
meu_livro.emprestar()  # Vai dizer: Desculpe, o livro já está emprestado...
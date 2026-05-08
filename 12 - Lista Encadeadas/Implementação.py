class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_no_inicio(self, novo_dado):
        novo_no = No(novo_dado)  # 1. Cria a caixa nova
        novo_no.proximo = self.head  # 2. Conecta ela na antiga primeira
        self.head = novo_no  # 3. Atualiza quem é o líder da fila

minha_lista = ListaEncadeada()
minha_lista.inserir_no_inicio(10)
minha_lista.inserir_no_inicio(20)

print(minha_lista.head.valor)
print(minha_lista.head.proximo.valor)


# Estrutura na memória: [20] -> [10] -> None
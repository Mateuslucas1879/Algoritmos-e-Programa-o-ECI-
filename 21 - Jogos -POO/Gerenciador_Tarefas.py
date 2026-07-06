class Node:
    def __init__(self,tarefa):
        self.tarefa = tarefa
        self.next = None

class Lista:
    def __init__(self):
        self.__head = None

    def inserir(self,tarefa):
        no_tarefa = Node(tarefa)
        no_tarefa.next = self.__head
        self.__head = no_tarefa


    def exibir_tarefa(self) -> None:
        atual = self.__head
        while atual is not None:
            print(atual.tarefa)
            atual = atual.next


    def remover_tarefa(self,tarefa_atual) -> bool:
        if self.__head is None:
            return False
        if self.__head.tarefa == tarefa_atual:
            self.__head = self.__head.next
            return True

        atual = self.__head
        while atual.next is not None:
            if atual.next.tarefa == tarefa_atual:
                atual.next = atual.next.next
                return True
            atual = atual.next
        return False


# --- ‘SCRIPT’ DE TESTE AUTOMÁTICO ---
if __name__ == "__main__":
    lista = Lista()

    print("--- 1. Testando Inserção ---")
    lista.inserir("Estudar Java")
    lista.inserir("Praticar Python")
    lista.inserir("Fazer Almoço")

    print("Sua lista atualizada (Deve mostrar: Fazer Almoço -> Praticar Python -> Estudar Java):")
    lista.exibir_tarefa()

    print("\n--- 2. Testando Remoção do Meio ---")
    if lista.remover_tarefa("Praticar Python"):
        print("✓ Removeu 'Praticar Python' com sucesso.")
    else:
        print("Falha ao remover 'Praticar Python'.")
    lista.exibir_tarefa()

    print("\n--- 3. Testando Remoção do Início (Head) ---")
    if lista.remover_tarefa("Fazer Almoço"):
        print("✓ Removeu 'Fazer Almoço' (head) com sucesso.")
    else:
        print("Falha ao remover 'Fazer Almoço'.")
    lista.exibir_tarefa()

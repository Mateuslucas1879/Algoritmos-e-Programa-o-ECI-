class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adiciona um elemento ao final da lista"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def display_forward(self):
        """Exibe a lista do início ao fim"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def display_backward(self):
        """Exibe a lista do fim para o início (navegação reversa)"""
        current = self.head
        if not current: return

        # Primeiro, vai até o último nó
        while current.next:
            current = current.next

        # Agora volta usando o ponteiro 'prev'
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" -> ".join(elements) + " -> None (Início)")



lista = DoublyLinkedList()
lista.append(10)
lista.append(20)
lista.append(30)

print("Caminho Direto:")
lista.display_forward()

print("\nCaminho Reverso (usando ponteiros anteriores):")
lista.display_backward()
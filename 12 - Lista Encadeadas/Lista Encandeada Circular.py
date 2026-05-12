class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Aponta para si mesmo
            return

        temp = self.head
        while temp.next != self.head:  # Busca o último (que aponta para a cabeça)
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head  # Fecha o círculo

    def display(self):
        if not self.head: return

        nodes = []
        curr = self.head
        while True:
            nodes.append(str(curr.data))
            curr = curr.next
            if curr == self.head:  # Se voltou ao início, para
                break
        print(" -> ".join(nodes) + " -> (volta ao início)")


# Teste
cll = CircularLinkedList()
cll.append("A")
cll.append("B")
cll.append("C")
cll.display()
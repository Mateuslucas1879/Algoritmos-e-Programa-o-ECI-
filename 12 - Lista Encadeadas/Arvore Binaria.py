class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, key):
    # Se a árvore estiver vazia, cria o nó
    if root is None:
        return Node(key)

    # Se o valor for menor, vai para a esquerda
    if key < root.val:
        root.left = insert(root.left, key)
    # Se o valor for maior, vai para a direita
    else:
        root.right = insert(root.right, key)

    return root


# Criando a árvore do exemplo anterior
r = Node(8)
insert(r, 3)
insert(r, 10)
insert(r, 1)
insert(r, 6)
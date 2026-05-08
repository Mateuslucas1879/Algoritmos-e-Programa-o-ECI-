"""
List Comprehension é uma forma elegante, concisa e rápida de criar listas em Python. Em vez de escrever várias
linhas de código com um loop for tradicional, você resolve tudo em apenas uma linha.
"""

# Com List Comprehension
quadrado = []
quadrado = [x**2 for x in range(5)]
print(f"Metodo List Comprehension:{quadrado}")
"""
A Estrutura Básica

A sintaxe segue sempre este padrão dentro de colchetes:

    nova_lista = [expressão for item in iterável]

    expressão: O que você quer fazer com o dado (o valor que vai entrar na lista).

    item: A variável que representa cada elemento do grupo.

    iterável: A lista, range ou string original.
"""
## JEITO TRADICIONAL
for x in range(5):
    quadrado.append(x**2)


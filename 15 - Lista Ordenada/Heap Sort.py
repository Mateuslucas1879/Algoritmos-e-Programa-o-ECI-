def heap_sort(lista, n, i):
    maior = i               # Inicializa o maior como a raiz
    esquerda = 2 * i + 1    # Índice do filho da esquerda
    direita = 2 * i + 2     # Índice do filho da direita

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heap_sort(lista, n, maior)


def arvore_binaria(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1,-1):
        heap_sort(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heap_sort(lista, i, 0)

# --- Testando o Algoritmo ---
if __name__ == "__main__":
    dados = [19, 4, 10, 9, 1, 12, 5, 14, 7]
    print("Array original: ", dados)

    arvore_binaria(dados)
    print("Array ordenado: ", dados)
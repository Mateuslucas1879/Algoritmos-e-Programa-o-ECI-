def busca_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(busca_linear(minha_lista, 1))
print(busca_linear(minha_lista, 2))
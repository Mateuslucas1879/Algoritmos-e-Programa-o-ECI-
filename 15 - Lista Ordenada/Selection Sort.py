def selection_sort(lista):
    numero = len(lista)

    for i in range(numero):
        indice_menor = i

        for j in range(i + 1, numero):
            if lista[j] < lista[indice_menor]:
                indice_menor = j

        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]


numeros = [64, 25, 12, 22, 11]
selection_sort(numeros)
print(f"Lista ordenada: {numeros}")
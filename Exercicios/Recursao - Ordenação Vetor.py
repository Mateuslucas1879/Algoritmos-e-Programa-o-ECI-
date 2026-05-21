def encontrar_indice_minimo(vetor, inicio, indice_min):
    if inicio == len(vetor):
        return indice_min

    if vetor[inicio] < vetor[indice_min]:
        indice_min = inicio

    return encontrar_indice_minimo(vetor, inicio+1, indice_min)


def selection_sort(vetor, inicio = 0):
    if inicio >= len(vetor) - 1:
        return vetor

    indice_min = encontrar_indice_minimo(vetor, inicio, inicio)
    vetor[inicio], vetor[indice_min] = vetor[indice_min], vetor[inicio]
    return selection_sort(vetor, inicio+1)


vetor_teste = [6, 3, 0, 5]
print("Vetor original:", vetor_teste)

selection_sort(vetor_teste)
print("Vetor ordenado:", vetor_teste)
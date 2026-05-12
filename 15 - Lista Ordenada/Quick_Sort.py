def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2 ]

    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]

    return quick_sort(esquerda) + meio + quick_sort(direita)


desordenados = [10, 80, 30, 90, 40, 50, 70]
ordenados = quick_sort(desordenados)

print(f"Original: {desordenados}")
print(f"Ordenado: {ordenados}")
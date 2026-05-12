def bubble_sort(lista,n=None):
    if n is None:
        n = len(lista)

    if n == 1:
        return lista

    for i in range(n-1):
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1] = lista[i+1],lista[i]

    return bubble_sort(lista,n-1)


numeros = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numeros)
print(f"Lista ordenada: {numeros}")
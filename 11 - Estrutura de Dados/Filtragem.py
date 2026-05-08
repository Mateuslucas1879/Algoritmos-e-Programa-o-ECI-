def filtro(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return pares

print(filtro([1, 2, 3, 4]))
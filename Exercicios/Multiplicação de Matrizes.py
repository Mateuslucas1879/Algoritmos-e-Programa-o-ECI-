def multiplicaçao_matriz(matriz_a, matriz_b):
    linha_b = len(matriz_b)
    coluna_b = len(matriz_b[0])

    linha_a = len(matriz_a)
    coluna_a = len(matriz_a[0])


    if coluna_a != linha_b:
        return "Erro"

    resultado = [[0 for x in range(coluna_b)] for y in range(linha_b)]

    for i in range(linha_a):
        for j in range(coluna_b):
            for k in range(coluna_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado

m1 = eval(input())
m2 = eval(input())

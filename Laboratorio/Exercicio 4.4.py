def soma_matriz(matriz_a, matriz_b):
    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    linhas_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    if colunas_a != linhas_b:
        return "Erro!"

    resultado = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]

    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado


m1 = eval(input())
m2 = eval(input())
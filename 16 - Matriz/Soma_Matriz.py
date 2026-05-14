def soma_matriz(A,B):
    linha =len(A)
    coluna =len(A[0])

    C = [[0 for _ in range(coluna)] for _ in range(linha)]

    for i in range(linha):
        for j in range(coluna):
            C[i][j] = A[i][j] + B[i][j]
    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(soma_matriz(A, B))
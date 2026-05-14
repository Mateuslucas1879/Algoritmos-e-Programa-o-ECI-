def soma_matriz_dimensoes(A,B):
    if not A or not B:
        return "Erro! Matrizes não podem ser vazias."
    
    if len(A) != len(B):
        return "Erro! Dimensões inválidas (linhas diferentes)."

    linhas = len(A)
    colunas = len(A[0])

    resultado = [[0 for x in range(colunas)] for y in range(linhas)]

    for i in range(linhas):
       for j in range(colunas):
           resultado[i][j] = A[i][j] + B[i][j]

    return resultado

print(f"Teste 2x2: {soma_matriz_dimensoes([[2,1],[3,2]], [[1,2],[1,1]])}")
print(f"Teste 1x1: {soma_matriz_dimensoes([[1]], [[2]])}")
print(f"Teste Erro: {soma_matriz_dimensoes([[1,2]], [[1],[2]])}")
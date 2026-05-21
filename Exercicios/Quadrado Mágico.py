def matriz_Quadrada(matriz):
    if not matriz:
        return True

    num_linhas = len(matriz)
    soma_matriz = sum(matriz[0])

    for linha in matriz:
        if sum(linha) != soma_matriz:
            return False

    for j in range(num_linhas):
        soma_coluna = 0
        for i in range (num_linhas):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma_matriz:
            return False

    soma_diagonal_p = 0
    for i in range(num_linhas):
        soma_diagonal_p += matriz[i][i]
    if soma_diagonal_p != soma_matriz:
        return False

    soma_diagonal_s = 0
    for i in range(num_linhas):
        soma_diagonal_s += matriz[i][num_linhas-1 -i]
    if soma_diagonal_s != soma_matriz:
        return False

entrada = input()
matriz_recebida = eval(entrada)
print(matriz_Quadrada(matriz_recebida))
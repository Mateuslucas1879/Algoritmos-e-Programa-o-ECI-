numero = int(input("Digite o tamanho da matriz: "))

matriz = []

for i in range(numero):
    linha = []
    for j in range(numero):
        valores = int(input(f"Numero de colunas da linha {i} x {j}: "))
        linha.append(valores)
    matriz.append(linha)


def matriz_quadrado(matriz):
    num_linhas = len(matriz)
    soma_refe = sum(matriz[0])

    for linha in matriz:
        if sum(linha) != soma_refe:
            return False

    for j in range(num_linhas):
        soma_coluna = 0
        for i in range (num_linhas):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma_refe:
            return False

    soma_diagonal_p = 0
    for i in range(num_linhas):
        soma_diagonal_p += matriz[i][i]
    if soma_diagonal_p != soma_refe:
        return False


    soma_diagonal_s = 0
    for i in range(num_linhas):
        soma_diagonal_s += matriz[i][num_linhas - 1 - i]
    if soma_diagonal_s != soma_refe:
        return False

    return True


print(matriz)
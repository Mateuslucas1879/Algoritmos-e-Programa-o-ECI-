def soma_matriz(matriz_01,matriz_02):
    if not isinstance(matriz_01[0],list) or not isinstance(matriz_02[0],list):
        return "ERRO!"
    if len(matriz_01) != len(matriz_02):
        return "ERRO!"

    if len(matriz_01[0]) != len(matriz_02[0]):
        return "ERRO!"

    quantidade_linhas = len(matriz_01)
    quantidade_colunas = len(matriz_01[0])

    resultado = [[0 for coluna in range(quantidade_colunas)] for linha in range(quantidade_linhas)]

    if i in range(quantidade_linhas):
        for j in range(quantidade_colunas):
            resultado[i][j] = matriz_01[i][j] + matriz_02[i][j]

    return resultado


l1 =int(input("Numero de Linhas matriz 01: "))
c1= int(input("Numero de colunas matriz 02: "))

m1 = []
for i in range(l1):
    linha = []
    for j in range(c1):
        num = int(input(f"Digite um valor {i} {j}: "))
        linha.append(num)
    m1.append(linha)

l2 = int(input("Numero de linhas matriz 02: "))
c2 = int(input("Numero de colunas matriz 02: "))

m2 = []
for i in range(l2):
    num_linha = []
    for j in range(c2):
        val = int(input(f"Digite um valor {i} {j}: "))
        num_linha.append(val)
    m2.append(num_linha)


print(soma_matriz(m1, m2))
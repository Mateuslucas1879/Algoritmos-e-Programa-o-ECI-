def soma_matriz(matriz_01,matriz_02):
    if len (matriz_01) ==0 or len(matriz_02) == 0:
        return "Erro"

    if len(matriz_01) != len(matriz_02):
        return "Erro"

    for i in range(len(matriz_01)):
        if len(matriz_01[i]) != len(matriz_02[i]):
            return "Erro"

    quantidade_linha = len(matriz_01)
    quantidade_coluna = len(matriz_01[0])

    resultado = [[0 for x in range(quantidade_coluna)] for y in range(quantidade_linha)]

    for i in range(quantidade_linha):
        for j in range(quantidade_coluna):
            resultado[i][j] = matriz_01[i][j] + matriz_02[i][j]
    return resultado


l1 =int(input("Numero de Linhas matriz 01: "))
c1= int(input("Numero de colunas matriz 01: "))
m1 = []

for i in range(l1):
    linha = []
    for j in range(c1):
        num = int(input(f"Digite um valor {i} {j}: "))
        linha.append(num)
    m1.append(linha)

l2 = int(input("Numero de Linhas matriz 02: "))
c2 = int(input("Numero de colunas matriz 02: "))

m2 = []

for i in range(l2):
    num_linha = []
    for j in range(c2):
        val = int(input(f"Digite um valor {i} {j}: "))
        num_linha.append(val)
    m2.append(num_linha)

print(soma_matriz(m1,m2))
l1 =int(input("Numero de Linhas matriz 01: "))
c1= int(input("Numero de colunas matriz 02: "))

m1 = []

for i in range(l1):
    linha = []
    for j in range(c1):
        num = int(input(f"Digite um valor {i} {j}: "))
        linha.append(num)
    m1.append(linha)


l2 =int(input("Numero de linhas matriz 01: "))
c2= int(input("Numero de colunas matriz 02: "))
m2 = []

for i in range(l2):
    num_linha = []
    for j in range(c2):
        num01 = int(input(f"Digite um valor {i} {j}: "))
        num_linha.append(num01)
    m2.append(num_linha)


def soma_matriz(matriz_01,matriz_02):
    if len(matriz_01) != len(m2) or len(matriz_01[0]) != len(matriz_02[0]):
        return "Erro!"

    quantidade_linha = len(matriz_01)
    quantidade_colunas = len(matriz_01[0])

    resultado = [[0 for i in range(quantidade_colunas)] for j in range(quantidade_linha)]

    for i in range(quantidade_linha):
        for j in range(quantidade_colunas):
            resultado[i][j] = matriz_01[i][j] + matriz_02[i][j]
    return resultado

print("\nResultado:")
print(soma_matriz(m1, m2))

"""for i,k in enumerate(matriz_01):
    print(matriz_01[i])

for i,k in enumerate(matriz_02):
    print(matriz_02[i])"""
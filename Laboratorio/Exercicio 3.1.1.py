def gerar_matriz():
    n = input().strip()
    limpo = n[2:-2]
    partir_linhas = limpo.split("],[")
    matriz = []

    for linha in partir_linhas:
        numeros = []
        for valor in linha.split(","):
            numeros.append(int(valor))
        matriz.append(numeros)
    return matriz


def obter_matriz(matriz,remover):
    linha_matriz = []
    for i in matriz[1:]:
        linha = []
        for j in range(len(i)):
            if j != remover:
                linha.append(i[j])
        linha_matriz.append(linha)
    return linha_matriz

def calcular_det(matriz):
    num = len(matriz)
    if num == 1:
        return matriz[0][0]
    elif  num == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    determinante = 0
    for j in range(num):
        sinal = (-1) ** j

        sub = obter_matriz(matriz,j)
        determinante += sinal * matriz[0][j] * calcular_det(sub)

    return determinante


try:
    m = gerar_matriz()
    print(calcular_det(m))

except:
    pass



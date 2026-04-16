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


def det_n1(m): return calcular_det(m)
def det_n2(m): return calcular_det(m)
def det_n3(m): return calcular_det(m)


def gerar_matriz():
    n = int(input("tamanho matriz: "))
    if n > 3: n = 3
    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            valor = int(input(f"Digite valor para [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

m = gerar_matriz()
tamanho = len(m)

if tamanho == 1:
    res = det_n1(m)
elif tamanho == 2:
    res = det_n2(m)
elif tamanho == 3:
    res = det_n3(m)


print(res)


def submatriz(matriz,linha_remover,coluna_remover):
    num =len(matriz)
    resultado = []
    for i in range(num):
        if i == linha_remover:
            continue
        linha_nova = []
        for j in range(num):
            if j == coluna_remover:
                linha_nova.append(matriz[i][j])
            resultado.append(linha_nova)
        return resultado

def calcular_det_1(matriz):
    if isinstance(matriz,list) and isinstance(matriz[0],list):
        return matriz[0][0]
    elif isinstance(matriz,list):
        return matriz[0]
    return matriz

def calcular_det_2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]


def calcular_det_3(matriz):
    resultado = 0
    for j in range(3):
        sinal = (-1) ** j
        elemento = matriz[0][j]
        menor = submatriz(matriz, 0, j)
        cofator = sinal * elemento * calcular_det_2(menor)
        resultado = resultado + cofator
    return resultado


def main():
    num = int(input())
    if num not in [1,2,3]:
        return

    entrada = eval(input())
    if num > 1 and (not isinstance(entrada, list) or not isinstance(entrada[0], list)):
        print("Erro: Para tamanho 2 ou 3, você deve digitar uma matriz válida. Ex: [[1,2],[3,4]]")
        return

    funcao = {
        1: calcular_det_1,
        2: calcular_det_2,
        3: calcular_det_3
    }
    resultado = funcao[num](entrada)
    print(resultado)

if __name__ == "__main__":
    main()
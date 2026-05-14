def det_n1(m):
    return m[0][0]


def det_n2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det_n3(m):
    d_principal = (m[0][0] * m[1][1] * m[2][2]) + (m[0][1] * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])
    d_secundaria = (m[0][2] * m[1][1] * m[2][0]) + (m[0][0] * m[1][2] * m[2][1]) + (m[0][1] * m[1][0] * m[2][2])
    return d_principal - d_secundaria


def obter_submatriz(m, coluna):
    return [linha[:coluna] + linha[coluna + 1:] for linha in m[1:]]


def det_laplace(m):
    n = len(m)

    if n == 3:
        return det_n3(m)

    det = 0
    for j in range(n):
        cofator = m[0][j] * det_laplace(obter_submatriz(m, j))
        if j % 2 == 1:
            det -= cofator
        else:
            det += cofator
    return det


def ler_matriz():
    texto = input().strip()
    for char in "[],":
        texto = texto.replace(char, " ")

    numeros = [int(n) for n in texto.split()]

    total_elementos = len(numeros)
    n = int(total_elementos ** 0.5)

    matriz = []
    for i in range(0, total_elementos, n):
        matriz.append(numeros[i: i + n])

    return matriz


m = ler_matriz()
n = len(m)

if n == 1:
    resultado = det_n1(m)
elif n == 2:
    resultado = det_n2(m)
elif n == 3:
    resultado = det_n3(m)
else:
    resultado = det_laplace(m)

print(resultado)
from unittest import result

import numpy as np

def  multiplicar_matrizes_rec(A,B):
    numeros = len(A)
    if numeros == 1:
        return A * B

    meio = numeros // 2

    a11 = A[:meio, :meio]
    a12 = A[:meio, meio:]
    a21 = A[meio:, :meio]
    a22 = A[meio:, meio:]

    b11 = B[:meio, :meio]
    b12 = B[:meio, meio:]
    b21 = B[meio:, :meio]
    b22 = B[meio:, meio:]

    c11 = multiplicar_matrizes_rec(a11, b11) + multiplicar_matrizes_rec(a12, b21)
    c12 = multiplicar_matrizes_rec(a11, b12) + multiplicar_matrizes_rec(a12, b22)
    c21 = multiplicar_matrizes_rec(a21, b11) + multiplicar_matrizes_rec(a22, b21)
    c22 = multiplicar_matrizes_rec(a21, b12) + multiplicar_matrizes_rec(a22, b22)


    resultado = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return  resultado



matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])

print("Resultado da multiplicação recursiva:")
print(multiplicar_matrizes_rec(matriz_a, matriz_b))


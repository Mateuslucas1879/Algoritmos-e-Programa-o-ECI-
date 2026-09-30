def detA(vetor):
    return vetor[0][0]

def detB(vetor):
    return vetor[0][0] * vetor[1][1] - vetor[0][1] * vetor[1][0]

def detC(vetor):
    diagonal_principal = (
        (vetor[0][0] * vetor[1][1] * vetor[2][2]) +
        (vetor[0][1] * vetor[1][2] * vetor[2][0]) +
        (vetor[0][2] * vetor[1][0] * vetor[2][1])
    )

    diagonal_secundaria = (
        (vetor[0][2] * vetor[1][1] * vetor[2][0]) +
        (vetor[0][0] * vetor[1][2] * vetor[2][1]) +
        (vetor[0][1] * vetor[1][0] * vetor[2][2])
    )

    return diagonal_principal - diagonal_secundaria

def criar_submatriz(m, coluna_remover):
    submatriz = []
    for i in range(1, len(m)):  # Começa na linha 1 para pular a linha 0
        linha = []
        for j in range(len(m)):
            if j != coluna_remover:
                linha.append(m[i][j])
        submatriz.append(linha)
    return submatriz
    

def laplace(m):
    n = len(m)
    if n == 1:
        return detA(m)
    if n == 2:
        return detB(m)
    if n == 3:
        return detC(m)

    det = 0
    for j in range(n):
        coeficiente = m[0][j]
        if coeficiente != 0:
            sinal = (-1) ** j
            sub = criar_submatriz(m, j)
            det += sinal * coeficiente * laplace(sub)

    return det


def matriz():
    texto = input().replace('[', '').replace(']', '')
    numeros = [int(x) for x in texto.split(',') if x.strip()]
    n = int(len(numeros) ** 0.5)
    return [numeros[i * n: (i + 1) * n] for i in range(n)]


m = matriz()
n = len(m)

if n == 1:
    resultado = detA(m)
elif n == 2:
    resultado =detB(m)
elif n == 3:
    resultado = detC(m)
else:
    resultado = laplace(m)
print(resultado)
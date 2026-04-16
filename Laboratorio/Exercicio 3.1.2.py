def det_n1(m):
    return m[0][0]


def det_n2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det_n3(m):
    d1 = m[0][0] * m[1][1] * m[2][2]
    d2 = m[0][1] * m[1][2] * m[2][0]
    d3 = m[0][2] * m[1][0] * m[2][1]


    s1 = m[0][2] * m[1][1] * m[2][0]
    s2 = m[0][0] * m[1][2] * m[2][1]
    s3 = m[0][1] * m[1][0] * m[2][2]

    return (d1 + d2 + d3) - (s1 + s2 + s3)




def ler_matriz():
    entrada = input().strip()
    conteudo = entrada[2:-2]
    linhas_str = conteudo.split("],[")

    matriz = []
    for linha in linhas_str:
        valores = linha.split(",")
        linha_int = []
        for v in valores:
            linha_int.append(int(v))
        matriz.append(linha_int)
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
    resultado = 0  
print(resultado)
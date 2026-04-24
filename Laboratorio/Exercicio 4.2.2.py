def soma_matriz(matriz_01,matriz_02):
    if type(matriz_01) != list or type(matriz_02) != list:
        return "Erro"

    if len(matriz_01)== 0  or type(matriz_01[0]) != list:
        return "Erro"
    if len(matriz_02)== 0 or type(matriz_02[0]) != list:
        return "Erro"

    linha_01 = len(matriz_01)
    linha_02 = len(matriz_02)
    coluna_01 = len(matriz_01[0])
    coluna_02 = len(matriz_02[0])


    if linha_01 != linha_02 or coluna_01!= coluna_02:
        return "Erro"

    resultado = []
    for i in range(linha_01):
        if len(matriz_01[i]) != coluna_01 or len(matriz_02[i]) != coluna_02:
            return "Erro!"

        linha_soma = []
        for j in range(coluna_01):
            soma = matriz_01[i][j] + matriz_02[i][j]
            linha_soma.append(soma)
        resultado.append(linha_soma)

    return resultado


entrada_01 = input().strip()
entrada_02 = input().strip()

m1 = eval(entrada_01)
m2 = eval(entrada_02)
resultado_final = soma_matriz(m1, m2)

if resultado_final == "Erro!":
    print("Erro!")

else:
    print(str(resultado_final).replace(" ", ""))
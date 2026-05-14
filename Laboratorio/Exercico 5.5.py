def selecao_recurso(vetor, indice_inical=0):
    num = len(vetor)

    if indice_inical >= num - 1:
        return vetor

    indice_menor = indice_inical

    for j in range(indice_inical + 1, num):
        if vetor[j] < vetor[indice_menor]:
            indice_menor = j

    vetor[indice_inical], vetor[indice_menor] = vetor[indice_menor], vetor[indice_inical]

    return selecao_recurso(vetor, indice_inical + 1)


entrada = input()
vetor_convertido = eval(entrada)
resultado = selecao_recurso(vetor_convertido)
print(resultado)



def busca_binaria(lista_ordenada, alvo, esquerda,direita):
    if esquerda > direita:
        return -1

    meio = (esquerda + direita)//2
    if lista_ordenada[meio] == alvo:
        return meio

    elif lista_ordenada[meio] < alvo:
        return busca_binaria(lista_ordenada,alvo,meio+1,direita)

    else:
        return busca_binaria(lista_ordenada,alvo,esquerda,meio-1)



entrada_completa = input().strip()
alvo =int(input().strip())

entrada_tratada = entrada_completa.replace('[','').replace(']','').replace(',', ' ')
if not entrada_tratada:
    lista_ordenada = []
else:
    lista_ordenada = [int(x) for x in entrada_tratada.split()]

resultado = busca_binaria(lista_ordenada, alvo, 0, len(lista_ordenada) - 1)
print(resultado)


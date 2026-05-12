def busca_binaria(lista,alvo,esquerda,direita):
    if esquerda > direita:
        return -1

    meio = (esquerda + direita) // 2
    if lista[meio] == alvo:
        return meio

    elif alvo < lista[meio]:
        return busca_binaria(lista,alvo,esquerda, meio -1)

    else:
        return busca_binaria(lista,alvo,esquerda, meio + 1,direita)

minha_lista = [3, 9, 10, 27, 38, 43, 82]
objetivo = 27

resultado = busca_binaria(minha_lista, objetivo, 0, len(minha_lista) - 1)

if resultado != -1:
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado.")
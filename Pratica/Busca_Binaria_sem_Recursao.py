def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

try:
    lista_ordena = input().strip().replace('[','').replace(']','').replace(',', ' ')
    lista = [int(x) for x in lista_ordena.split()] if lista_ordena.strip() else []
    alvo = int(input().strip())
    print(busca_binaria(lista,alvo))
except EOFError:
    pass
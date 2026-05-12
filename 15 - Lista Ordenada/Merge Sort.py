
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    # 1. DIVIDIR: Encontra o meio e divide a lista em duas metades
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])


    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    resultado = []
    i = j = 0
    # Compara os elementos de ambas as listas e adiciona o menor ao resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes (se houver) de cada lado
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

numeros = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(numeros)
print(f"Lista original: {numeros}")
print(f"Lista ordenada: {lista_ordenada}")
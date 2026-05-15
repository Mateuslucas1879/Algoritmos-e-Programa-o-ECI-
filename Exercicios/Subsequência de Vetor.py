entrada01 = input()
entrada02 = input()

lista01 = [item.strip() for item in entrada01.replace('[', '').replace(']', '').split(',')]
lista02 = [item.strip() for item in entrada02.replace('[', '').replace(']', '').split(',')]

def comparar(lista01, lista02):
    i = j = 0
    while i < len(lista01) and j < len(lista02):
        if lista01[i] == lista02[j]:
            i += 1
        j += 1

    return i == len(lista01)


print(comparar(lista01, lista02))
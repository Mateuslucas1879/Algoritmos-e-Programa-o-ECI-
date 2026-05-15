entrada01 = input()
entrada02 = input()

lista01 = [item.strip() for item in entrada01.replace('[','').replace(']','').split(',')]
lista02 = [item.strip() for item in entrada02.replace('[','').replace(']','').split(',')]

def comparar(lista1, lista2):
    limite = min(len(lista1), len(lista2))

    for i in range(limite):
        if lista01[i] == lista02[i]:
            return True

    return False

print(comparar(lista01, lista02))
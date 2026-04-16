entrada01 = input()
entrada02 = input()

lista01 = [item.strip() for item in entrada01.replace('[','').replace(']','').split(',')]
lista02 = [item.strip() for item in entrada02.replace('[','').replace(']','').split(',')]


menor_lista = min(len(lista01),len(lista02))
resultado = False

for i in range(menor_lista):
    if lista01[i] == lista02[i]:
        resultado = True
        break



print(resultado)


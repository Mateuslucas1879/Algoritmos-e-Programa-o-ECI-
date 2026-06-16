import random
def buscar(lista, x,inicio,fim):
    meio = (inicio + fim) // 2

    if x == lista[meio]:
        return meio

    elif x < lista[meio]:
        return buscar(lista, x,inicio,meio-1)

    elif x > lista[meio]:
        return buscar(lista,x,meio + 1,fim)


l = random.sample(range(100),20)
print(l)

l.sort()
print(l)

buscar(l, 84,0,19)

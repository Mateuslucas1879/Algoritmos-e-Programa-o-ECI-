def soma_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

print(soma_elementos([1, 2, 3, 4, 5, 6, 7]))
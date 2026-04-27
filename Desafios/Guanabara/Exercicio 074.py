from random import randint
"""tupla = tuple(randint(1, 10) for i in range(0, 5))
print(tupla)"""
############################################################################################
numeros =()

for c in range(0, 5):
    numero_novo = (randint(1, 10),)
    numeros = numeros + numero_novo


maior = menor = 0
for i,n in enumerate(numeros):
    if i == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n


print(f"Os valores sorteados foram: {numeros}")
print(f"O maior numero: {maior} e o menor numero: {menor}")
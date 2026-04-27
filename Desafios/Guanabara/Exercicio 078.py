lista = list()

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posiçâo {c}: ')))

maior = menor = 0
for c,v in enumerate(lista):
    if c == 0:
        maior = menor = v
    else:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v



print(f"VOCE DIGITOU OS VALORES{lista}")
print(f"O MENOR VALOR FOI: {menor}")
print(f"O MAIOR VALOR FOI: {maior}")
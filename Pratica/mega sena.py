from random import randint
lista = []
jogos = []


numeros = int(input('Quantos numeros deseja gerar: '))
total_jogo = 1

while  total_jogo <= numeros:
    quantidade = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            quantidade += 1
        if quantidade >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogo += 1

for c,v in enumerate(jogos) :
    print(f"Jogo {c+1}: {v}")
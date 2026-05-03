from random import randint


mega_sena = []
numero = int(input("Quantos jogos deseja gerar: "))
total_jogos = 1

while total_jogos <= numero:
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)

    jogo.sort()
    mega_sena.append(jogo[:])
    print(f"Jogo {total_jogos}: {jogo}")
    total_jogos += 1







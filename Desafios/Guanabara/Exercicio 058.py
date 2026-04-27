from random import randint

print('-=-'*20)
print('Vou pensar em um numero entre 0 e 10')
print('-=-'*20)

computador = randint(0, 10)
jogador = int(input("Em que numero eu pensei? "))
tentaivas = 0

while computador != jogador:
    if jogador == computador:
        print("Acertou de primeira")
        break

    else:
        print("Tente mais uma vez")
        jogador = int(input("Em que numero eu pensei? "))
        tentaivas += 1

print(f"O computador pensou no numero: {computador}")
print(f"Acertou com {tentaivas+1} tentativas")
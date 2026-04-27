from time import sleep
from random import randint

tupla = ('pedra', 'papel', 'tesoura')

print('\033[1;34;40m-=-\033[m' * 20)
print("SUAS OPÇÕES"
      "\n [1] PEDRA"
      "\n [2] PAPEL"
      "\n [3] TESOURA")

usuario = int(input("QUAL SUA JOGADA:"))
computador = randint(0,2)


match (usuario-1, computador):
    case (u, c) if u == c:
        print("EMPATE")
    case (0, 2) | (1, 0) | (2, 1):
        print("JOGADOR VENCEU")
    case _:
        print("COMPUTADOR VENCEU")

print(f" O JOGADOR JOGOU: {tupla[usuario-1]}")
print(f" O COMPUTADOR JOGOU: {tupla[computador]}")
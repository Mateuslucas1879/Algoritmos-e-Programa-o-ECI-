from random import randint

print("SUA JOGAS"
      "\n[1] PEDRA "
      "\n[2] PAPEL"
      "\n[3] TESOURA")

usuario = int(input("Qual a sua jogada? "))

computador = randint(1, 3)



if usuario == computador:
    print("EMPATE")


elif usuario == 1 and computador == 2:
    if usuario == computador:
        print("EMPATE")
    print(f"A SUA JOGADA FOI: {usuario} E A DO COMPUTADOR: {computador}")
    print("COMPUTADOR VENCE")

elif usuario == 1 and computador == 3:

    if usuario == computador:
        print("EMPATE")
    print("JOGADOR VENCE")
    print(f"A SUA JOGADA FOI: {usuario} E A DO COMPUTADOR: {computador}")

elif usuario == 2 and computador == 1:

    if usuario == computador:
        print("EMPATE")
    print("JOGADOR VENCE")
    print(f"A SUA JOGADA FOI: {usuario} E A DO COMPUTADOR: {computador}")

elif usuario == 2 and computador == 3:

    if usuario == computador:
        print("EMPATE")
    print("COMPUTADOR VENCE")
    print(f"A SUA JOGADA FOI: {usuario} E A DO COMPUTADOR: {computador}")

elif usuario == 3 and computador == 1:

    if usuario == computador:
        print("EMPATE")
    print("COMPUTADOR  VENCE")
    print(f"A SUA JOGADA FOI: {usuario} E A DO COMPUTADOR: {computador}")

elif usuario == 3 and computador == 2:

    if usuario == computador:
        print("EMPATE")
    print("JOGADOR VENCE")
    print(f"A SUA JOGADA FOI: {usuario} E A DO COMPUTADOR: {computador}")
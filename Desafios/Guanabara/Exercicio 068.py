from random import randint

qtd = 0
while True:
    usuario = int(input("Digite um valor: "))
    computador = randint(0,10)
    soma = computador + usuario
    dedo = str(input("PAR OU IMPAR [P/I}: ")).strip().upper()[0]

    if dedo == "P":
        if soma % 2 == 0:
            print("O Usuario venceu")
            qtd += 1
        else:
            print("O computador venceu")
            break

    if dedo == "I":
        if soma % 2 == 1:
            print("O Usuario venceu")
            qtd += 1
        else:
            print("O computador venceu")
            break

    print("VAMOS JOGAR NOVAMNETE")

print(f"Voce ganhou {qtd} vezes")









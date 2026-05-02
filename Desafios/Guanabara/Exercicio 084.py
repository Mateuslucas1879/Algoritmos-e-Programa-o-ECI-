res = ""

maior = menor = 0
pessoas = []
dados = []

while res != "s":
    pessoas.append(str(input("Digite o nome do pessoa: ")))
    pessoas.append(float(input("Digite o peso do pessoa: ")))


    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
                maior = pessoas[1]

        elif pessoas[1] < menor:
            menor = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()

    res = str(input("Quer continuar[S/N]: ")).strip().upper()[0]
    if res == "N":
        break


print(f"Ao todo voce cadastrou {len(dados)} pessoas")
for i in dados:
    if i[1] == maior:
        print(f"O maior peso foi de {i[0]}.")
for i in dados:
    if i[1] == menor:
        print(f"O menor peso foi de {i[0]}.")
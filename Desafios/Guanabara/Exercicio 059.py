primeiro = int(input("Primeiro numero: "))
segundo = int(input("Segundo numero: "))
opcao = 0

while opcao != 5:
    print("=-" * 20)
    print("[1] SOMAR"
          "\n[2] MULTIPLICAR"
          "\n[3] MAIOR"
          "\n[4] NOVOS NUMEROS"
          "\n[5] SAIR DO PROGRAMA")
    print("=-"*20)
    opcao = int(input("Qual sua opcao: "))
    print("=-"*20)

    if opcao == 1:
        soma = primeiro + segundo
        print(f"O resultado de {primeiro} + {segundo}: {soma}")

    if opcao == 2:
        multiplicar = primeiro * segundo
        print(f"o resultado de {primeiro} * {segundo}: {multiplicar}")

    if opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo

        print(f"O maior numero entre {primeiro} e {segundo}: {maior}")

    if opcao == 4:
        primeiro = int(input("Primeiro novo numero: "))
        segundo = int(input("Segundo noco numero: "))
        print(f"Os novos numeros sao: {primeiro} {segundo}")

    if opcao == 5:
        break
qtd = 0
soma = 0

while True:
    numero = int(input("Digite um numero - [999] para parar: "))
    if numero == 999:
        break

    soma = (numero + soma)
    qtd += 1



print(f"Voce digitou {qtd} e a soma de {soma}")
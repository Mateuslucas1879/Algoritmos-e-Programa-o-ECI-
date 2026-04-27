resp = ""
lista = list()
pares = list()
impares = list()
while resp != "s":
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    if valor % 2 == 1:
        impares.append(valor)
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    while resp not in "SsNn":
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break


if 5 not in lista:
    print("O valor 05 não apareceu na lista.")

print("-="*30)
print(f"VOCE DIGITOU: {len(lista)} ELEMENTOS")
print(f"O valor 5 apareceu {lista.count(5)} vezes")
print(f"Os valores em ordem decrescente foram {sorted(lista,reverse=True)}")
print(f"Os valores pares foram:{pares} ")
print(f"Os valores impares foram {impares} ")

print("-="*30)
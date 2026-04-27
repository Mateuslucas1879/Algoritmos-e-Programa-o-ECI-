resp = ""
lista = []
while resp != "s":
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
    else:
        print("VALOR DUPLICADO! NÃO VOU ADICIONAR")
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break

print("-"*30)
print(f"Lista de numeros digitados: {sorted(lista)}")
print("-"*30)
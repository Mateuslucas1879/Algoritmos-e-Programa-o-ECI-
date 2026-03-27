num = eval(input("Digite um numero: "))
valor = int(input("Digite um valor: "))

menores, maiores = [],[]

for x in num:
    if x <= valor:
        menores.append(x)
    else:
        maiores.append(x)

print ("Menores ou iguais a",valor,":",menores)
print ("Maiores que",valor,":",maiores)

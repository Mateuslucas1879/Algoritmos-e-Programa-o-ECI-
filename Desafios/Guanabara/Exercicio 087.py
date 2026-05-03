matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
impares = []
soma = 0

for i in range(0,3):
    linha = []
    for j in range(0,3):
        num = int(input(f"Digite um valor {i} x {j}: "))
        linha.append(num)

        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)


    matriz[i] = linha

for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]",end="")
    print()

print("=-"*30)

print(f"A soma dos numero pares sao: {sum(pares)}")
print(f"A soma dos numeros impares sao {sum(impares)}")

for i in range(0,3):
    soma += matriz[i][2]
print(f"A soma dos valore da terceira coluna sao: {soma}")
print(f"O maior valor da segunda linha sao: {max(matriz[1])}")


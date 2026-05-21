numero_matriz = int(input(f"Digite o tamaho da matriz: "))
matriz_01 = []
numeros_pares = []

for i in range(numero_matriz):
    linha = []
    for j in range(numero_matriz):
        num = int(input(f"Digite o valor da linha {i} {j}: "))
        linha.append(num)

        #NUMEROS PARES
        if num % 2 == 0:
            numeros_pares.append(num)
    matriz_01.append(linha)


print("\nMatriz completa:")
print(matriz_01)

print(f"\nNúmeros pares encontrados na matriz: {numeros_pares}")
qtd_linhas = 3
qtd_colunas = 2

matriz_01 = []
numeros_pares = []

for i in range(qtd_linhas):
    linha = []
    for j in range(qtd_colunas):
        num = int(input(f"Digite os valores {i+1} x {j+1}: "))
        linha.append(num)

        if num % 2 == 0:
            numeros_pares.append(num)
    matriz_01.append(linha)

print("\nMatriz completa:")
print(matriz_01)

print(f"\nNúmeros pares: {numeros_pares}")
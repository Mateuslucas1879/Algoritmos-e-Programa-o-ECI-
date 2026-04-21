linhas = int(input("Digite qtd de linha: "))
colunas = int(input("Digite qtd de coluna: "))

print("\n--- Matriz A ---")
matriz_a = []
i = 0
while i < linhas:
    linha = []
    j = 0
    while j < colunas:
        num = int(input(f"Digite um valor {i} x {j}: "))
        linha.append(num)
        j += 1
    matriz_a.append(linha)
    i += 1

print("\n--- Matriz B ---")

matriz_b = []
i = 0
while i < linhas:
    linha = []
    j = 0
    while j < colunas:
        num = int(input(f"Digite um valor {i} x {j}: "))
        linha.append(num)
        j += 1
    matriz_b.append(linha)
    i += 1

matriz_c = []
i = 0
while i < linhas:
    linha_doma = []
    j = 0
    while j < colunas:
        soma = matriz_a[i][j] + matriz_b[i][j]
        linha_doma.append(soma)
        j += 1

    matriz_c.append(linha_doma)
    i += 1


print("\nResultado da Soma (Matriz C):")
for linha in matriz_c:
    print(linha)
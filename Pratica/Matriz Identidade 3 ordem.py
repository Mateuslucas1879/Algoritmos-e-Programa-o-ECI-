ordem  = 3
matriz_01 = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_01.append(linha)

print("Matriz Identidade de Ordem 3:")
for linha in matriz_01:
    print(linha)

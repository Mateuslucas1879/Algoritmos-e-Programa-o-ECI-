numero = int(input("Digite o tamanho da matriz (n x n): "))
matriz = []
i = 0
while i < numero:
    num_linha = []
    j = 0
    while j < numero:
        num = int(input(f"Digite um numero {i} x {j}: "))
        num_linha.append(num)
        j += 1

    matriz.append(num_linha)
    i += 1

print("\n --- Matriz --- :")
for linha in matriz:
    print(linha)
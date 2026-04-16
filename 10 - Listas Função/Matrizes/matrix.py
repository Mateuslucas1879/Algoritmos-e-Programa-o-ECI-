num= int(input("Digite o tamanho da matriz:"))

matriz = []
for i in range(num):
    num_linhas = []
    for j in range(num):
        valores = int(input(f"Digite o numero de {i} {j}: "))
        num_linhas.append(valores)

    matriz.append(num_linhas)

print(matriz)

linha = int(input("Digite o numero de linha: "))
coluna = int(input("Digite o numero de coluna: "))

matriz  = []

for i in range(linha):
    nova_linha = []
    for j in range(coluna):
        valor = int(input("Digite um valor: "))
        nova_linha.append(valor)

    matriz.append(nova_linha)

print("_____ Matriz ______")
for l in matriz:
    print(l)
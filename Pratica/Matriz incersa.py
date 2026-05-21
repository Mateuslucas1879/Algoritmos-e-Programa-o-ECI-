# 1. Criando e preenchendo a matriz 2x2 com inputs do usuário
matriz = []

print("--- Preencha a Matriz 2x2 ---")
for i in range(2):
    linha = []
    for j in range(2):
        num = int(input(f"Digite o valor para a Posição [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)

determinante = (matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0])
print("\n-> Matriz Original digitada:")

for linha in matriz:
    print(linha)

if determinante == 0:
    print("\n[Erro] A matriz não possui inversa porque o determinante é zero!")
else:
    matrizInversa = [
        [matriz[1][1] / determinante, -matriz[0][1] / determinante],
        [matriz[1][0] / determinante, -matriz[0][0] / determinante],
    ]

    print("\n=== Matriz Inversa ===")
    for linha in matrizInversa:
        linha_formatada = [f"{elem:.2f}" for elem in linha]
        print(linha_formatada)


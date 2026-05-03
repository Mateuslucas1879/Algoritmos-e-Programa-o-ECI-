matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    linha = []
    for j in range(0,3):
        num = int(input(f"Digite um valor {i} x {j}: "))
        linha.append(num)
    matriz[i] = linha

print("=-"*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print("=-"*30)

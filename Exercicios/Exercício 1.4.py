vetor01 = input()
vetor02 = input()

lista_01 = list(map(int, vetor01.split(',')))
lista_02 = list(map(int,vetor02.split(',')))

produto_interno = 0

for i in range(len(lista_01)):
    produto_interno += lista_01[i] * lista_02[i]

print(f"O produto interno é: {produto_interno}")
qtd_alunos = int(input("Digite a quantidade de alunos para a matriz: "))
qtd_provas = int(input("Digite a quantidade de provas: "))

matriz = []

i = 0
while i < qtd_alunos:
    notas_alunos = []
    j = 0
    while j < qtd_provas:
        nota = float(input(f"Nota do aluno {i} na prova {j}: "))
        notas_alunos.append(nota)
        j += 1
    matriz.append(notas_alunos)
    i = i + 1

print("\n -- MEDIA DOS ALUNOS -- ")
i = 0
while i < qtd_alunos:
    soma = 0
    j = 0
    while j < qtd_provas:
        soma = soma + matriz[i][j]
        j += 1

    media = soma / qtd_alunos
    print(f"Aluno {i} : Media = {media}")
    i = i + 1

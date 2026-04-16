alunos = ["Mateus","Levi","Luz"]
notas = ["A","B","C"]

for nome, notas in zip(alunos,notas):
    print(f"O aluno {nome} -> tirou {notas}")
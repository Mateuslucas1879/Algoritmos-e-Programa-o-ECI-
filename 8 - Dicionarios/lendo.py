estado = dict()
brasil = list()
for c in range(0, 3):
    estado['nome'] = str(input('Sigla: '))
    estado['cidade'] = str(input('Cidade: '))
    estado['estado'] = str(input('Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'{k} - {v}')
    
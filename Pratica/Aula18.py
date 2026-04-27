galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)


for c in galera:
    if c[1] >= 18:
        print(f'{c[0]} tem mais de 18 anos.')
    else:
        print(f'{c[1]} nao tem mais de 18 anos.')

print(galera)
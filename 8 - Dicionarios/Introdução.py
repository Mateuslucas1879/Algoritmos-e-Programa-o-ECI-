pessoas = {'nome': 'Dara','idade':'24','sexo':'F'}
print(pessoas)
print(pessoas['idade'])

print(f"A {pessoas['nome']} tem {pessoas['idade']} anos")
print("=-"*30)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print("=-"*30)
for k,v in pessoas.items():
    print(f"{k} -> {v}")
print("=-"*30)

for k in pessoas.keys():
    print(f"{k}")
print("=-"*30)

for v in pessoas.values():
    print(f"{v}")
print("=-"*30)
del pessoas['sexo']
print(pessoas)

print("=-"*30)

pessoas['peso'] = 45.5
print(pessoas)
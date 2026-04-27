times = ('Flamengo','Palmeiras', 'Atlético-MG','América-MG','Cruzeiro', 'Athletico-PR', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba',
          'Cuiabá', 'Fluminense', 'Fortaleza', 'Goiás', 'Gremio', 'Internacional',
         'Bragantino', 'Santos', 'São Paulo', 'Vasco')

print("A LISTA DE TIMES DO BRASILEIRO")
for c, i in enumerate(times):
    print(f"Posição {c+1} -> {i}")


print(f"OS CINCO PRIMEIROS SAO: {times[:5]}")

for c,v in enumerate(times[:5]):
    print(f"{c+1} {v}")


print(f"OS QUATRO ULTIMOS SAO: {times[-4:]}")
for c,v in enumerate(times[-4:]):
    print(f"{c+1} {v}")

print(f"TIMES EM ORDEM ALFABETICA")
print(sorted(times))


print(f"O GREMIO ESTA NA {times.index('Gremio')} posição")

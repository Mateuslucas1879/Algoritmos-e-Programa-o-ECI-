def func_gerar():
    yield 1
    yield 2
    yield 3
    yield 4

gerador = func_gerar()

print(next(gerador))
print(next(gerador))
print(next(gerador))

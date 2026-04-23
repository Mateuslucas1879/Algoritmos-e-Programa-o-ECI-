def impares(r):
    yield from (n for n in range(r) if n % 2 == 1)


gerador = impares(10)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

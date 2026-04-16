def calcular_serie(n, a, b, c):
    resultado = 0
    for i in range(1, n + 1):
        resultado += (-1)**(c + i) * (1 + a * i) / (3 * b**i)
    return resultado

n, a, b, c = map(int, input().strip().strip("()").split(","))
print(f"{calcular_serie(n, a, b, c):.3f}")
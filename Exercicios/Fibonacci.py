def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

termos = 6
soma = 0

for i in range(termos):
    valor = fibonacci(i)
    soma += valor
    print(valor, end=" ")

print("\nSoma =", soma)
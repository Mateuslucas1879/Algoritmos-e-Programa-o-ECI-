a,b = 1,1
tentativa = 0
limite = 15

print(f"{'Termo':<10} | {'Fibonacci':<10} | {'Proporção (b/a)':<15}")
print("-" * 40)

while tentativa < limite:
    proporcao = b / a
    print(f"{tentativa + 1:<10} | {b:<10} | {proporcao:.10f}")
    a, b = b, a+b
    tentativa += 1

print("-" * 40)
print(f"O valor aproximado de Phi é: 1.6180339887...")

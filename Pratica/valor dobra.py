valor = 0.01
dias = 28

valor_atual = valor
for dia in range(1, dias + 1):
    print(f"Dias {dia} - Valor:{valor_atual}")
    valor_atual *= 2
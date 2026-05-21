def divisao_inteira_recursiva(dividendo, divisor):
    # Caso base: se o dividendo for menor que o divisor, a divisão dá 0
    if dividendo < divisor:
        return 0

    # Passo recursivo: subtrai o divisor e soma 1 ao resultado da próxima chamada
    return 1 + divisao_inteira_recursiva(dividendo - divisor, divisor)


# --- Testando os exemplos do enunciado ---
print(divisao_inteira_recursiva(1, 3))  # Output: 0
print(divisao_inteira_recursiva(10, 3))  # Output: 3
print(divisao_inteira_recursiva(15, 5))  # Output: 5
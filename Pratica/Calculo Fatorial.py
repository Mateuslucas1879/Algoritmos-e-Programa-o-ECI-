def recursao(num:int)->int:
    if num < 0:
        raise ValueError ("Fatorial Negativo")
    if num == 0 or num == 1:
        return 1
    else:
        return num * recursao(num-1)


print(f"\n--- Recursividade: Fatorial ---")
print(f"Fatorial de 5: {recursao(5)}") # 5 * 4 * 3 * 2 * 1 = 120
print(f"Fatorial de 0: {recursao(0)}") # 1
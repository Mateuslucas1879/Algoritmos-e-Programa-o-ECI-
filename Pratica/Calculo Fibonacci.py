def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Numero Negativo")
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\n--- Recursividade: Fibonacci ---")
print(f"Fibonacci: {fibonacci(7)}")

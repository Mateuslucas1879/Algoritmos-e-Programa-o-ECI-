def recursao(n) -> int:
    if n == 0 or n == 1:
        return 1
    return n * recursao(n-1)

try:
    print(f"Fatoração com recursivo: {recursao(5)}")
except RecursionError as e:
    print(f"Erro {e}")
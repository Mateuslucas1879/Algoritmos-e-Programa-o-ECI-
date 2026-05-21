def obter_divisores(n: int )-> set:
    divisores = set()
    limite = int(n/2)
    for i in range(1, limite + 1):
        if n % i == 0:
            divisores.add(i)
            divisores.add(n//i)
        return divisores

def divisores_comuns(numeros: tuple)-> set:
    if not numeros:
        return set()

    resultado = obter_divisores(numeros[0])

    for num in numeros[1:]:
        resultado = resultado & obter_divisores(num)
    return resultado


entrada = (12, 18, 24)
saida = divisores_comuns(entrada)

print(f"Entrada: {entrada}")
print(f"Saída: {saida}")
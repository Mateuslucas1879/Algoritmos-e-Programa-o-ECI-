def qtd_dgitos(n):
    return len(str(abs(n)))

def numero_invertido(n):
    converter = str(n)[::-1]
    return int(converter)


entrada = int(input())

tamanho = qtd_dgitos(entrada)
invertido = numero_invertido(entrada)

resultado = [tamanho, invertido]
print(resultado)
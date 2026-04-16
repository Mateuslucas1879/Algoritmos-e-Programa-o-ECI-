def num(n):
    return len(str(abs(n)))

def reverte(n):
    converte = str(n)[::-1]
    return int(converte)


entrada = int(input())

tamanho = num(entrada)
inverte = reverte(entrada)

resultado = [tamanho, inverte]
print(resultado)
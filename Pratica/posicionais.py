def media_calcular(*numeros):
    if not numeros:
        return 0
    soma = 0
    for numero in numeros:
        soma += numero

    soma = soma/len(numeros)
    return soma

print(f"A media dos numeros usando parametros posicionais foi:")
print(f"{media_calcular(6,4,2,8,10)}")
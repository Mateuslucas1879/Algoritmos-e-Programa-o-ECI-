def obeter_divisores(num):
    num = int(num)
    divisores = set()
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            divisores.add(i)
            divisores.add(num//i)
    return divisores

def calcular_divisores(numeros):
    if not numeros:
        return set()
    intersecao = obeter_divisores(numeros[0])

    for numero in numeros[1:]:
        intersecao = intersecao.intersection(obeter_divisores(numero))

    return intersecao

entrada_usuario = input()
entrada_limpa = entrada_usuario.replace("(", "").replace(")", "").replace(" ", "")

lista_numeros = []
for x in entrada_limpa.split(","):
    if x:
        lista_numeros.append(int(x))

tupla_final = tuple(lista_numeros)

if tupla_final:
    resultado = calcular_divisores(tupla_final)
    print(resultado)
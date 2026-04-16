def calcular_serie(n, a, b, c):
    resultado = 0
    for i in range(1, n + 1):
        resultado += (-1)**(c+i)*(1+a*i)/(3*b**i)
    return resultado

entrada = input()
nova_entrada = ""

for i in entrada:
    if i != "(" and i != ")" and i != " ":
        nova_entrada += i

numeros = []
numero_atual = ""
for i in nova_entrada:
    if i == ",":
        numeros.append(int(numero_atual))
        numero_atual = ""
    else:
        numero_atual += i
numeros.append(int(numero_atual))

n = numeros[0]
a = numeros[1]
b = numeros[2]
c = numeros[3]

print(f"{calcular_serie(n, a, b, c):.3f}")
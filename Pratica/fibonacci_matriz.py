n = 3
matriz = []
a,b = 0,1

i = 0
while i<n:
    linha = []
    j = 0
    while j<n:
        linha.append(a)
        a,b = b,a+b
        j+=1
    matriz.append(linha)
    i+=1

for linha in matriz:
    print(linha)
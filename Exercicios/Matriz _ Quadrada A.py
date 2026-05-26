def deter_matriz_0(matriz):
    if isinstance(matriz, list) and isinstance(matriz[0], list):
        return matriz[0][0]
    elif isinstance(matriz, list):
        return matriz[0]
    return matriz

def deter_matriz_2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def deter_matriz_3(matriz):
    a,b,c = matriz[0]
    d,e,f = matriz[1]
    g,h,i = matriz[2]

    return (a * e * i + b * f * g + c * d* h) - (a*f*h + b*d*i + c*e*g)

def deter_matriz_4(matriz):
    num = len(matriz)
    if num == 1:
        return matriz[0][0]
    if num == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    if num == 3:
        return deter_matriz_3(matriz)

    return sum (
        ((-1) ** j) * matriz[0][j] * deter_matriz_4([[matriz[i][k] for k in range(num) if k != j]
                                                     for i in range(1,num)])
        for j in range(num) if matriz[0][j] != 0
    )


mat = eval(input("Digite o valor da matriz: "))
print(deter_matriz_4(mat))
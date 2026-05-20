def det_matriz_1(mat):
    if isinstance(mat, list) and isinstance(mat[0], list):
        return mat[0][0]
    elif isinstance(mat, list):
        return mat[0]
    return mat

def det_matriz_2(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def det_matriz_3(mat):
    a,b,c = mat[0]
    d,e,f = mat[1]
    g,h,i = mat[2]

    return (a * e * i + b * f * g + c * d * h) - (a * f * h + b * d * i + c * e * g)

def determinante(mat):
    num = len(mat)
    if num == 1:
        return mat[0][0]
    if num == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    if num == 3:
        return det_matriz_3(mat)
    
    # Se um dia testarem n >= 4, o seu motor de Laplace recursivo funciona!
    return sum (
        ((-1) ** j) * mat[0][j] * determinante([[mat[i][k] for k in range(num) if k != j]
                                     for i in range(1, num)])
        for j in range(num) if mat[0][j] != 0
    )

mat = eval(input("Digite o valor da matriz: "))
print(determinante(mat))
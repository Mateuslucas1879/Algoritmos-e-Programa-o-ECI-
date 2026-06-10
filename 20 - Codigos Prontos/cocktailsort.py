def cocktailsort(A):
    trocado = True
    fim = len(A)-1
    ini = 0
    j = 0
    while trocado:
        trocado = False
        if j & 1:
            for i in range(fim,ini,-1):
                if A[ i-1 ] > A[ i ]:
                    aux = A[i]
                    A[ i ] = A[ i -1 ]
                    A[i-1] = aux
                    trocado = True
        else:
            for i in range(ini,fim):
                if A[ i ] > A[ i + 1 ]:
                    aux = A[i]
                    A[ i ] = A[ i + 1 ]
                    A[i+1] = aux
                    trocado = True
        print(A)
        if j & 1: 
            ini += 1
        else:
            fim -= 1
        j +=1

A = [7,6,5,4,3,2,1]
cocktailsort(A)
print(A)
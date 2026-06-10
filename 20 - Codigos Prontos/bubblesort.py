def bubblesort(A):
    trocado = True
    while trocado:
        trocado = False
        for i in range(len( A )-1):
            if A[ i ] > A[ i + 1 ]:
                aux = A[i]
                A[ i ] = A[ i + 1 ]
                A[i+1] = aux
                trocado = True
        #print(A)

A = [5,2,4,6,1,3]
bubblesort(A)
print(A)
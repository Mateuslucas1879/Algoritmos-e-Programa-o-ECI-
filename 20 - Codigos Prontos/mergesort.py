def merge(A,p,q,r):
    m = max(A)+1
    n1 = q - p + 1 
    n2 = r-q
    L = A[p:q+1] + [m]
    R = A[q+1:r+1] + [m]
    #print(L,R)
    i,j = 0,0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    #print(A)
    
def mergesort(A,p,r):
    if p < r:
        q = (p+r)//2
        #print(p,q,r)
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

A = [5,2,4,6,1,3]
mergesort(A,0,len(A)-1)
print(A)
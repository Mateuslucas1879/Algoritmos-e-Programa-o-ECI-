def recursao(A,B,i=0):
 if i >= len(A) or i >= len(B):
   return False

 if A[i] == B[i]:
   return True

 return recursao(A,B,i+1)

vetor_a = eval(input())
vetor_b = eval(input())

resultado = recursao(vetor_a, vetor_b)
print(resultado)
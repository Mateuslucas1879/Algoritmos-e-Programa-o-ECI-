def multiplica_recursivo(a,b):

    return 1 + multiplica_recursivo(a * b, b)


n1 = int(input())
n2 = int(input())

print(multiplica_recursivo(n1,n2))
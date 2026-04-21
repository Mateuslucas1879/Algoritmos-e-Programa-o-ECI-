limite = 100
a,b = 0,1

while a <= limite:
    print(a, end=' ')
    a += 1
    a,b = b,a+b
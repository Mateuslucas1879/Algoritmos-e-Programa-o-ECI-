termo = int(input("Numero: "))
a,b = 0,1

for i in range(termo):
    print(a, end=' ')
    proximo = a + b
    a = b
    b = proximo
numero  = int(input("Digite um numero para fibonacci: "))
lista = []

a,b = 0,1

while a <= numero:
    lista.append(a)
    a,b = b,a+b

print(lista)
total = sum(lista)
print(total)
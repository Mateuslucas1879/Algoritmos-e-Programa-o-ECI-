numero  = int(input("Quantos termos deseja mostrar: "))
a = 0
b = 1
print(f"{a} -> {b}", end='')
contador = 3

while contador <= numero:
    t3 = a + b
    print(f' -> {t3} -> ', end='')
    a = b
    b = t3
    contador += 1

print('FIM')









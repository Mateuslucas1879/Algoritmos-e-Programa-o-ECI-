num = int(input("Valor de numero: "))
list = []

for x in range(2,num+2):
    list += [x]
resto = []

while len(list) > 0:
    primo = list[0]
    resto = resto + [primo]
    list2 = []
    for x in list:
        if x % primo != 0:
            list2 += [x]
    list = list2
print(resto)


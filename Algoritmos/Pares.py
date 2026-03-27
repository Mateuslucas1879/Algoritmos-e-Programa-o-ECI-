list = eval(input("Digite uma lista de valores: "))
resto = []

for x in list:
    if x % 2 == 0:
        resto = resto + [x]
    print(resto)
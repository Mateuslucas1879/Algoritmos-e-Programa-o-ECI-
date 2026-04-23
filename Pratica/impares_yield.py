from time import sleep


def impares():
    valor = 1
    while True:
        yield valor
        valor += 2


for x in impares():
    sleep(1)
    print(x)

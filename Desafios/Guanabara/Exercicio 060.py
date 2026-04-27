fatorial = num0 = int(input('Digite o numero que você deseja encontrar o fatorial: '))
valorfinal = 1
numeros = [fatorial]
while fatorial > 1  :
    valorfinal = valorfinal*fatorial
    fatorial = fatorial - 1
    numeros.append(fatorial)
print (f'{num0}! = {' x '.join(map(str, numeros))} = {valorfinal}')
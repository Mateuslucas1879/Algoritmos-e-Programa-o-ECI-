palimedro = str(input("Digite uma palavra: ")).strip().upper()
palavras = palimedro.split(" ")
junto = ''.join(palavras)

inverter = ''

for letra in range(len(junto)-1,-1,-1):
    inverter += junto[letra]

print(junto[::-1])

if junto == inverter:
    print("Temos um palíndromo!")
else:
    print("Palavra nao e palimedro")
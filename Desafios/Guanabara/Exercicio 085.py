pares = []
impares = []

for c in range(1,8):
    num = int(input(f"Digite {c} numero: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Os valores pares digitados foram {pares}")
print(f"Os valores impares foram {impares}")
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
sexo = str(input("Digite seu sexo (M/F): "))
altura = float(input("Digite sua altura: "))

print(f"Voce precisa arrumar um emprego")

if sexo == "F" and idade < 20:
    print(f"Voce precisa fazer um emprego")


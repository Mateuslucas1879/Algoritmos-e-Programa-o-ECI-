sexo = input("Informe o sexo [F/M]: ").upper()
while not sexo in "FM":
    if sexo not in "F" and sexo not in "M":
        sexo = input("Dados invalidos - Informe o sexo [F/M]: ").upper().strip()

print(f"Sexo {sexo} registrado.")
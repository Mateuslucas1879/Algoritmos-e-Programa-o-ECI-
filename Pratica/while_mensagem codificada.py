msg = input()

decodificada = ""
indice = 0

while indice < len(msg):
    letra = msg[indice]

    if letra == "P":
        decodificada += letra

    indice += 1

print(f"Mensagem decodificada: {decodificada}")
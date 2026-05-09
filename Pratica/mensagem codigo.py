mensagem_codificada = input().strip().upper()
resultado = []
for letra in mensagem_codificada:
    if letra != "P":
        resultado.append(letra)

mensagem_final = "".join(resultado)
print(f"Mensagem decodificada: {mensagem_final}")

# LIST COMPEHENSION
mensagem_decodificada = input()
descodificada = "".join([l for l in mensagem_decodificada if l != "P" ])
print(descodificada)

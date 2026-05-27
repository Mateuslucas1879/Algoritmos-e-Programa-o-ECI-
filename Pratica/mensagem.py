mensagem_codificada = input()
mensagem_decodificada =""
lista = []
i = 0

while i < len(mensagem_codificada):
    if mensagem_codificada == "p" and i + 1 < len(mensagem_codificada):
        mensagem_decodificada += mensagem_codificada[i+1]
        i += 2
    else:
        mensagem_decodificada += mensagem_codificada[i]
        i += 1

print(mensagem_decodificada)


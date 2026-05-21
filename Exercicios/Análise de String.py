frase = str(input("Digite uma frase: "))

caracters = len(frase)
espaco = [letra for letra in frase if letra.isalpha()]
numero = [numero for numero in frase if numero.isnumeric()]
simbolos = [simbolo for simbolo in frase if not simbolo.isalnum()]

string_limpa = ""
for char in frase:
    if char.isalnum() or char == "":
        string_limpa += char
    else:
        string_limpa += " "

palavras = len(string_limpa.split())

print(f"O numero de caracters:{caracters}")
print(f"O numero de letras:{len(espaco)}")
print(f"O numero de numeros:{len(numero)}")
print(f"O numero de simbolos:{len(simbolos)}")
print(f"O numero de palavras:{palavras}")

string = str(input("Digite uma frase: "))


caracters = len(string)
espaco = [letra for letra in string if letra.isalpha()]
numero = [num for num in string if num.isnumeric()]
simbolos = [simbolo for simbolo in string if not simbolo.isalnum()]

string_limpa = ""
for char in string:
    if char.isalnum() or char == "-":
        string_limpa += char
    else:
        string_limpa += " "

palavras = len(string_limpa.split())

print(f"O numero de caracters:{caracters}")
print(f"O numero de letras:{len(espaco)}")
print(f"O numero de numeros:{len(numero)}")
print(f"O numero de simbolos:{len(simbolos)}")
print(f"O numero de palavras:{palavras}")


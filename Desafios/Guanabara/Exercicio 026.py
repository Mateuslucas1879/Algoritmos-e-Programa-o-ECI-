frase = str(input('Digite uma frase: ')).strip().upper()
letras = frase.count('A')
posicao_primeira = frase.find('A')
posicao_ultima = frase.rfind('A')

print(f"A Letra A apareceu: {letras}")
print(f"A primiera letra A apareceu na posicao: {posicao_primeira + 1}")
print(f"A ultima letra A apareceu na posicao: {posicao_ultima + 1}")

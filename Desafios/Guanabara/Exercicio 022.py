nome = str(input('Digite seu nome completo: '))

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_tamaho = len(nome.replace(' ','').strip())

print(f"Seu nome maiusculo: {nome_maiusculo}")
print(f"Seu nome minusculo: {nome_minusculo}")
print(f"Seu nome tem ao todo {nome_tamaho} letras")

primeiro_nome = ""
for i in nome:
    if i == ' ':
        break
    primeiro_nome += i


print(f"Seu primeiro nome: {primeiro_nome}")
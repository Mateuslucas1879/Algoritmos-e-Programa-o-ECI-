def codifica(m,s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    tamanho = len(alfabeto)
    retorno = ""

    for letra in m:
        if letra in alfabeto:
            posicao_atual = alfabeto.find(letra)
            novo_posicao = (posicao_atual + s) % 27
            retorno += alfabeto[novo_posicao]
        return retorno

def decodifica(m,s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    retorno = ""
    for letra in m:
        posicao_atual = alfabeto.find(letra)
        novo_posicao = (posicao_atual - s) % 27
        retorno += alfabeto[novo_posicao]
    return retorno

escolha = input()
x , m , s = eval(escolha)

if x:
    print(codifica(m,s))
else:
    print(decodifica(m,s))
def codifica(m,s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    tamanho = len(alfabeto)
    retorno = ""

    for letra in m:
        if letra in alfabeto:
            posicao_atul = alfabeto.find(letra)
            nova_posicao = (posicao_atul + s)%27
            retorno += alfabeto[nova_posicao]
    return retorno

def descodificar(m,s):
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    retorno = ""
    for letra in m:
        posicao_atul = alfabeto.find(letra)
        nova_posicao = (posicao_atul - s)%27
        retorno += alfabeto[nova_posicao]
    return retorno

escolha = input()
x, m, s = eval(escolha)

if x:
    print(codifica(m,s))
else:
    print(descodificar(m,s))

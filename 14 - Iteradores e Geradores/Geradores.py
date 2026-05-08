"""
Geradores são uma forma concisa de criar iteradores. Eles são funções que usam
a palavra-chave yield para produzir uma sequência de valores sob demanda,
pausando a sua execução e retomando-a do mesmo ponto quando o próximo valor é solicitado.
Isso economiza memória, pois os valores não são gerados e armazenados de uma vez.

"""

def contador_infinito(inicio):
    atual = inicio
    while True:
        yield atual
        atual += 1

gerador = contador_infinito(10)
print(next(gerador))
print(next(gerador)) 
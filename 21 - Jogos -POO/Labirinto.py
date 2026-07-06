class Jogador:
    def __init__(self, linha,coluna):
        self.__linha = linha
        self.__coluna = coluna
    @property
    def linha(self):
        return self.__linha
    @property
    def coluna(self):
        return self.__coluna

    def mover(self,direcao):
        nova_linha = self.__linha
        nova_coluna = self.__coluna

        if direcao == 'w':
            nova_linha -= 1
        elif direcao == 's':
            nova_linha += 1
        elif direcao == 'a':
            nova_coluna -= 1
        elif direcao == 'd':
            nova_coluna += 1
        return nova_linha,nova_coluna

    def confimar_movimento(self,new_linha,new_coluna):
        self.__linha = new_linha
        self.__coluna = new_coluna


class Labirinto:
    def __init__(self):
        self.__mapa = [
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', '#', ' ', 'X', '#'],
            ['#', '#', ' ', '#', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
        ]
        self.__linha_saida = 1
        self.__coluna_saida = 5

    def imprimir_mapa(self,jogador):
        for linha in range(len(self.__mapa)):
            for coluna in range(len(self.__mapa[linha])):
                if linha == jogador.linha and coluna == jogador.coluna:
                    print("P",end='')
                else:
                    print(f"{self.__mapa[linha][coluna]} ", end='')
            print()

    def movimento_valido(self,new_linha,new_coluna):
        if new_linha < 0 or new_linha >= len(self.__mapa) or new_coluna < 0 or new_coluna >= len(self.__mapa[0]):
            return False
        if self.__mapa[new_linha][new_coluna] == '#':
            return False
        return True

    def finish(self,jogador):
        return jogador.linha == self.__linha_saida and jogador.coluna == self.__coluna_saida

if __name__ == "__main__":
    labirinto = Labirinto()
    jogador = Jogador(1, 1)  # Começa na posição livre (1, 1)

    print("--- BEM-VINDO AO JOGO DO LABIRINTO (POO) ---")
    print("Comandos: W (cima), S (baixo), A (esquerda), D (direita)\n")

    while not labirinto.finish(jogador):
        labirinto.imprimir_mapa(jogador)

        comando = input("Para onde ir? ").lower().strip()

        if comando in ['w', 'a', 's', 'd']:
            # 1. Ajustado para chamar o método correto que você criou (.mover)
            prox_l, prox_c = jogador.mover(comando)

            # 2. Pergunta ao labirinto se essa posição é válida
            if labirinto.movimento_valido(prox_l, prox_c):
                # Ajustado o nome do método corrigindo a digitação
                jogador.confirmar_movimento(prox_l, prox_c)
            else:
                print("\n Bloqueado! Você bateu em uma parede ou saiu do mapa.\n")
        else:
            print("\n Comando inválido! Use apenas W, A, S ou D.\n")

    # Tela de vitória
    labirinto.imprimir_mapa(jogador)
    print("\n Parabéns! Você encontrou a saída do labirinto!")
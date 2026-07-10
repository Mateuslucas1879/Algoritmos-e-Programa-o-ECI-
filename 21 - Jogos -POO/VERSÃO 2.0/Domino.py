class Pedra:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def inverter(self):
        self.ladoA, self.ladoB = self.ladoB, self.ladoA

    def __str__(self):
        return f'{self.ladoA}|{self.ladoB}'


class Mesa:
    def __init__(self):
        self.linha = []

    def obter_pontos(self):
        if not self.linha:
            return None, None
        return self.linha[0].ladoA, self.linha[-1].ladoB

    def jogar_esquerda(self, pedra: Pedra):
        self.linha.insert(0, pedra)

    def jogar_direita(self, pedra: Pedra):
        self.linha.append(pedra)

    def exibir(self):
        if not self.linha:
            print("[Mesa Vazia]")
        else:
            print("Mesa: " + " ".join(str(x) for x in self.linha))


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def pode_jogar(self, ponta_esquerda, ponta_direita):
        if ponta_esquerda is None and ponta_direita is None:
            return True
        for pedra in self.mao:
            if pedra.ladoA in (ponta_esquerda, ponta_direita) or pedra.ladoB in (ponta_direita, ponta_esquerda):
                return True
        return False

    def tentar_jogar_pedra(self, pedra: Pedra, ponta_esq, ponta_dir):
        if ponta_esq is None and ponta_dir is None:
            return True, 'direita'

        if pedra.ladoB == ponta_esq:
            return True, 'esquerda'
        if pedra.ladoA == ponta_esq:
            pedra.inverter()
            return True, 'esquerda'

        if pedra.ladoA == ponta_dir:
            return True, 'direita'
        if pedra.ladoB == ponta_dir:
            pedra.inverter()
            return True, 'direita'

        return False, None


class PartidaDomino:
    def __init__(self):
        todas_pedras = [Pedra(i, j) for i in range(7) for j in range(i, 7)]
        self.monte = []

        # Geração determinística estável do monte para testes
        for i in range(14):
            self.monte.append(todas_pedras[i])
            self.monte.append(todas_pedras[i + 14])

        self.humano = Jogador("Humano")
        self.bot = Jogador("Bot")
        self.mesa = Mesa()

        for _ in range(7):
            self.humano.mao.append(self.monte.pop(0))
            self.bot.mao.append(self.monte.pop())

    def rodar_bot(self):
        # CORREÇÃO: Buscando sempre os pontos atualizados da mesa atual
        ponta_esquerda, ponta_direita = self.mesa.obter_pontos()

        if not self.bot.pode_jogar(ponta_esquerda, ponta_direita):
            if self.monte:
                self.bot.mao.append(self.monte.pop(0))
            return

        for pedra in list(self.bot.mao):
            sucesso, lado = self.bot.tentar_jogar_pedra(pedra, ponta_esquerda, ponta_direita)
            if sucesso:
                if lado == 'esquerda':
                    self.mesa.jogar_esquerda(pedra)
                else:
                    self.mesa.jogar_direita(pedra)
                self.bot.mao.remove(pedra)
                break

    def jogar_lote(self, lista_indices):
        indice_atual = 0
        vencedor = "Nenhum"

        # Executa as rodadas baseadas nas escolhas em lote fornecidas
        while indice_atual < len(lista_indices):
            ponta_esquerda, ponta_direita = self.mesa.obter_pontos()

            # Vez do Humano
            if not self.humano.pode_jogar(ponta_esquerda, ponta_direita):
                if self.monte:
                    self.humano.mao.append(self.monte.pop(0))
                # Passa a vez diretamente para o robô jogar se o humano não tiver peças válidas
            else:
                escolha = lista_indices[indice_atual]
                indice_atual += 1

                if 0 <= escolha < len(self.humano.mao):
                    pedra_escolhida = self.humano.mao[escolha]
                    sucesso, lado = self.humano.tentar_jogar_pedra(pedra_escolhida, ponta_esquerda, ponta_direita)

                    if sucesso:
                        if lado == 'esquerda':
                            self.mesa.jogar_esquerda(pedra_escolhida)
                        else:
                            self.mesa.jogar_direita(pedra_escolhida)
                        self.humano.mao.remove(pedra_escolhida)
                    else:
                        # Se tentar jogar uma pedra inválida, penaliza ignorando o comando
                        pass

            if not self.humano.mao:
                vencedor = "Humano"
                break

            # Vez do Bot
            self.rodar_bot()
            if not self.bot.mao:
                vencedor = "Bot"
                break

        # Outputs puros para a validação do juiz eletrônico
        self.mesa.exibir()
        print(len(self.humano.mao))
        print(vencedor)


# ========================================================
# ENTRADA PURA PARA O JUIZ ONLINE
# ========================================================
# O robô injeta uma lista de inteiros contendo todos os índices que você quer tentar jogar
# Exemplo de entrada: [0, 1, 0, 2]
lista_jogadas = eval(input())

jogo = PartidaDomino()
jogo.jogar_lote(lista_jogadas)
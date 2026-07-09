class Pedra:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def inverter(self):
        self.ladoA, self.ladoB = self.ladoB, self.ladoA

    def __str__(self):
        return f'{self.ladoA} | {self.ladoB}'

class Mesa:
    def __init__(self):
        self.linha = []

    def obter_pontos(self):
        if not self.linha:
            return None, None
        return self.linha[0].ladoA, self.linha[-1].ladoB

    def jogar_esquerda(self,pedra:Pedra):
        self.linha.insert(0,pedra)

    def jogar_direita(self,pedra:Pedra):
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

    def mostrar_mao(self):
        print(f"{self.mao}")
        for i, pedra in enumerate(self.mao):
            print(f"{i}: {pedra}", end=" ")
        print()

    def pode_jogar(self,ponta_esquerda,ponta_direita):
        if ponta_esquerda is None and ponta_direita is None:
            return True
        for pedra in self.mao:
            if pedra.ladoA in (ponta_esquerda, ponta_direita) or pedra.ladoB in (ponta_direita, ponta_esquerda):
                return True
        return False

    def tentar_jogar_pedra(self, pedra: Pedra, ponta_esq, ponta_dir):
        if ponta_esq is None and ponta_dir is None:
            return True,'direita'

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
        todas_pedras = [Pedra(i,j) for i in range(7) for j in range(i,7)]
        self.monte = []

        for i in range(14):
            self.monte.append(todas_pedras[i])
            self.monte.append(todas_pedras[i + 14])

        self.humano = Jogador("Humano")
        self.bot = Jogador("Bot")
        self.mesa = Mesa()

        for i in range(7):
            self.humano.mao.append(self.monte.pop(0))
            self.bot.mao.append(self.monte.pop())

    def rodar(self):
        ponta_esquerda, ponta_direita = self.mesa.obter_pontos()
        if not self.bot.pode_jogar(ponta_esquerda, ponta_direita):
            if self.monte:
                self.bot.mao.append(self.monte.pop(0))
                print("🤖 Computador comprou uma pedra!")
            else:
                print("🤖 Computador passou a vez!")
            return
        for pedra in list(self.bot.mao):
            sucesso, lado = self.bot.tentar_jogar_pedra(pedra,ponta_esquerda,ponta_direita)
            if sucesso:
                if lado == 'esquerda':
                    self.mesa.jogar_esquerda(pedra)
                else:
                    self.mesa.jogar_direita(pedra)
                self.bot.mao.remove(pedra)
                print(f"O Computador jogou: {pedra} na {lado}")
                break

    def jogar(self):
        while True:
            self.mesa.exibir()
            ponta_esquerda, ponta_direita = self.mesa.obter_pontos()
            self.humano.mostrar_mao()
            if not self.humano.pode_jogar(ponta_esquerda,ponta_direita):
                if self.monte:
                    input("Voce nao tem pedra Validas")
                    self.humano.mao.append(self.monte.pop(0))
                    continue
                else:
                    print("Computador comprou !")
            else:
                try:
                    escolha = int(input("Escolha indice: "))
                    pedra_escolhida = self.humano.mao[escolha]
                    sucesso, lado = self.humano.tentar_jogar_pedra(pedra_escolhida,ponta_esquerda,ponta_direita)

                    if sucesso:
                        if lado == 'esquerda':
                            self.mesa.jogar_esquerda(pedra_escolhida)
                        else:
                            self.mesa.jogar_direita(pedra_escolhida)
                        self.humano.mao.remove(pedra_escolhida)
                    else:
                        print("Essa pedra não encaixa!")
                        continue
                except (ValueError, IndexError):
                    print("Escolha inválida!")
                    continue

            if not self.humano.mao:
                self.mesa.exibir()
                print("Parabéns! Você bateu todas as suas pedras e venceu!")
                break

            self.rodar()
            if not self.bot.mao:
                self.mesa.exibir()
                print("O Computador bateu todas as pedras e venceu!")
                break
if __name__ == '__main__':
    PartidaDomino().jogar()
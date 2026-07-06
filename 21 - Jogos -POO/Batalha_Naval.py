class Oceano:
    def __init__(self):
        self.__grid = [["~" for i in range(5)] for j in range(5)]
        self.__navios_restantes = 0
        self.__inserir()

    def __inserir(self):
        posicao = [(1,1),(2,3),(4,0)]
        for x, y in posicao:
            self.__grid[x][y] = "*"
        self.__navios_restantes = len(posicao)

    @property
    def navios_restantes(self):
        return self.__navios_restantes

    def receber_tiros(self,x,y):
        """
                TODO: Implemente a lógica do tiro recebido nas coordenadas (x, y).
                - Se a célula contiver "N": muda para "[N]" (navio atingido), decrementa self.__navios_restantes e retorna True.
                - Se a célula contiver "~": muda para "X" (tiro na água) e retorna False.
                - Se já contiver "X" ou "[N]", avise que já atirou ali e retorne False.
                """
        if self.__grid[x][y] == "*":
            self.__grid[x][y] = "[N]"
            self.__navios_restantes -= 1
            return True
        elif self.__grid[x][y] == "~":
            self.__grid[x][y] = "X"
            return False
        else:
            print("Voce ja atirou nessa coodernadas")
            return False

    def exibir_mapa(self):
        print("\n   0  1  2  3  4")
        # TODO: Imprima as linhas da matriz.
        # IMPORTANTE: Se a célula contiver "N" (navio intacto), imprima "~" para o jogador não ver!
        # Mostre apenas "~", "X" e "[N]".
        for i in range(5):
            linha_formada = f"{i} "
            for j in range(5):
                if self.__grid[i][j] == "*":
                    linha_formada += "~ "
                else:
                    linha_formada += f"{self.__grid[i][j]} "
            print(linha_formada)

class Jogador:
    def dar_tiro(self):
        while True:
            try:
                print("--- SUA VEZ DE ATIRAR ---")
                linha = int(input("Escolha a linha (0-4): "))
                coluna = int(input("Escolha a coluna (0-4): "))

                if 0 <= linha < 5 and 0 <= coluna < 5:
                    return linha, coluna
                print("Coodernadas Fora do Oceano")
            except ValueError:
                print("Entrada Invalida")


class PartidaNaval:
    def __init__(self):
        self.__oceano = Oceano()
        self.__jogador = Jogador()
        self.__tiros_disponiveis = 10

    def jogar(self):
        print("--- BEM-VINDO À BATALHA NAVAL (POO) ---")
        print("Existem 3 navios ocultos no oceano. Você tem 10 tentativas para afundá-los.")

        ganhou = False
        while self.__tiros_disponiveis > 0 and not ganhou:
            self.__oceano.exibir_mapa()
            print(f"Munição: {self.__tiros_disponiveis} | Navios Restantes: {self.__oceano.navios_restantes}")

            x,y = self.__jogador.dar_tiro()
            acertou = self.__oceano.receber_tiros(x,y)
            if acertou:
                print("FOGO")
            else:
                print("AGUA")

            # TODO: Verifique se os navios restantes no oceano chegaram a 0 para ativar a vitória
            if self.__oceano.navios_restantes == 0:
                ganhou = True
            self.__tiros_disponiveis -= 1
        self.__oceano.exibir_mapa()
        if ganhou:
            print("VITORIA")
        else:
            print("FIM DE JOGO")


if __name__ == "__main__":
    PartidaNaval().jogar()



class Oceano:
    def __init__(self, tabuleiro):
        # Agora recebemos a matriz vinda do eval(input())
        self.__grid = tabuleiro
        self.__linhas = len(tabuleiro)
        self.__colunas = len(tabuleiro[0])
        self.__navios_restantes = 0
        self.__contar_navios()

    def __contar_navios(self):
        # Varre a matriz recebida para contar quantos navios ("*") existem nela
        for i in range(self.__linhas):
            for j in range(self.__colunas):
                if self.__grid[i][j] == "*":
                    self.__navios_restantes += 1

    @property
    def navios_restantes(self):
        return self.__navios_restantes

    def receber_tiros(self, x, y):
        # Garante que o tiro não quebre os limites da matriz recebida
        if not (0 <= x < self.__linhas and 0 <= y < self.__colunas):
            return False

        if self.__grid[x][y] == "*":
            self.__grid[x][y] = "[N]"
            self.__navios_restantes -= 1
            return True
        elif self.__grid[x][y] == "~":
            self.__grid[x][y] = "X"
            return False
        else:
            return False

    def exibir_mapa(self):
        # Mostra o resultado final ocultando os navios intactos
        for i in range(self.__linhas):
            linha_formada = ""
            for j in range(self.__colunas):
                if self.__grid[i][j] == "*":
                    linha_formada += "~ "
                else:
                    linha_formada += f"{self.__grid[i][j]} "
            print(linha_formada.strip())


class PartidaNaval:
    def __init__(self, tabuleiro):
        self.__oceano = Oceano(tabuleiro)
        self.__tiros_disponiveis = 10

    def jogar_lote(self, lista_tiros):
        ganhou = False

        for tiro in lista_tiros:
            if self.__tiros_disponiveis <= 0 or ganhou:
                break

            x, y = tiro[0], tiro[1]
            self.__oceano.receber_tiros(x, y)

            if self.__oceano.navios_restantes == 0:
                ganhou = True

            self.__tiros_disponiveis -= 1

        self.__oceano.exibir_mapa()
        print(self.__oceano.navios_restantes)
        print(ganhou)


# ========================================================
# ENTRADAS PURAS PARA O JUIZ ONLINE (DUAS MATRIZES/LISTAS)
# ========================================================

# 1ª Entrada: O robô envia a matriz do oceano com os navios posicionados
# Exemplo de entrada: [["~", "~"], ["*", "~"]]
tabuleiro_entrada = eval(input())

# 2ª Entrada: O robô envia a lista de coordenadas dos tiros
# Exemplo de entrada: [[1, 0]]
lista_tiros_entrada = eval(input())

# Inicializa o jogo passando a matriz que foi lida com sucesso
partida = PartidaNaval(tabuleiro_entrada)
partida.jogar_lote(lista_tiros_entrada)
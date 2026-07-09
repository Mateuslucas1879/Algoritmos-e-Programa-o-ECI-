class TabuleiroDamas:
    def __init__(self, num=4):
        self.__num = num
        self.__tabuleiro = [["." for i in range(num)] for j in range(num)]

    def exibir_tabuleiro(self):
        for linha in self.__tabuleiro:
            print(" ".join(linha))
        print("-" * (self.__num * 4))

    def seguro(self,linha,coluna):
        for i in range(linha):
            if self.__tabuleiro[i][coluna] == "D":
                return False

        i, j = linha, coluna
        while i >= 0 and j >= 0:
            if self.__tabuleiro[i][j] == "D":
                return False
            i -= 1
            j -= 1
        i, j = linha, coluna
        while i >= 0 and j < self.__num:
            if self.__tabuleiro[i][j] == "D":
                return False
            i -= 1
            j += 1
        return True

    def resolver(self,linha ):
        if linha == self.__num:
            self.exibir_tabuleiro()
            return True

        for coluna in range(self.__num):
            if self.seguro(linha,coluna):
                self.__tabuleiro[linha][coluna] = "D"


                if self.resolver(linha + 1) :
                    return True
                self.__tabuleiro[linha][coluna] = "."
        return False

    def iniciar(self):
        print(f"--- Buscando solução para {self.__num} Damas ---")
        if not self.resolver(0):
            print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    # Teste mudando para 8 se quiser ver o clássico das 8 rainhas rodar!
    jogo = TabuleiroDamas(8)
    jogo.iniciar()
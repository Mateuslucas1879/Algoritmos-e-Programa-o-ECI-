class PalavraSecreta:
    def __init__(self,palavra):
        self._palavra = palavra.upper()

    def gerar_palavra(self,palpite):
        palpite = palpite.upper()
        feedback = []
        for i in range(len(self._palavra)):
            if palpite[i] == self._palavra[i]:
                feedback.append("[V]")
            elif palpite[i] in self._palavra:
                feedback.append("[A]")
            else:
                feedback.append("[_]")
        return feedback

class Tabuleiro:
    def __init__(self):
        self.__historico = []

    def adicionar_palpite(self,palpite,feedback):
        palpite = palpite.upper()
        linha_visual = ""
        for i in range(len(palpite)):
            linha_visual += f"{palpite[i]}{feedback[i]} "
        self.__historico.append(linha_visual)

    def exibir(self):
        print("\n--- TABULEIRO ---")
        for tentativas in self.__historico:
            print(tentativas)
        print("-----------------\n")

class Jogar:
    def __init__(self):
        self.__palavras_sistema = PalavraSecreta("Darah")
        self.__tabuleiro = Tabuleiro()
        self.__max_tentativas = 7
    def iniciar(self):
        print("--- BEM-VINDO AO JOGO DO TERMO (POO) ---")
        print("Descubra a palavra de 5 letras em até 6 tentativas.")
        print("Dicas: [V] Lugar Certo | [A] Lugar Errado | [_] Não tem a letra\n")

        tentativas = 0
        ganhou = False

        while tentativas < self.__max_tentativas and not ganhou:
            self.__tabuleiro.exibir()
            palpite = input(f"Tentativa {tentativas + 1}/{self.__max_tentativas}: ").strip().upper()

            if len(palpite) != 5:
                print("Palavra Invalida")
                continue

            feedback = self.__palavras_sistema.gerar_palavra(palpite)
            self.__tabuleiro.adicionar_palpite(palpite,feedback)

            if feedback == ["[V]", "[V]", "[V]", "[V]", "[V]"]:
                ganhou = True

            tentativas += 1
        self.__tabuleiro.exibir()
        if ganhou:
            print("Espetacular")
        else:
            print("Fim de Jogo")

if __name__ == "__main__":
    jogo = Jogar()
    jogo.iniciar()


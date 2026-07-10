class JogoForca:
    def __init__(self,palavras):
        self.palavras = palavras.upper()
        self.letras_tentativas = []
        self.erros_cometidos = 0
        self.maximo_erros = 6

    def exibir_palavra(self):
        resultado = ""
        for letra in self.palavras:
            if letra in self.letras_tentativas:
                resultado += letra + " "
            else:
                resultado += "- "
        return resultado.strip()

    def jogo_ganho(self):
        for letra in self.palavras:
            if letra not in self.letras_tentativas:
                return False
        return True

    def jogo_turno(self,chute):
        letra = chute.upper()
        if letra in self.letras_tentativas:
            return
        self.letras_tentativas.append(letra)
        if letra not in self.palavras:
            self.erros_cometidos += 1

    def processar_jogo(self,lista_chutes):
        for chute in lista_chutes:
            if self.erros_cometidos >= self.maximo_erros or self.jogo_ganho():
                break
            self.jogo_turno(chute)

        print(self.exibir_palavra())
        print(self.erros_cometidos)
        print(self.jogo_ganho())

palavras = input()
lista_chutes = eval(input())

jogo = JogoForca(palavras)
jogo.processar_jogo(lista_chutes)
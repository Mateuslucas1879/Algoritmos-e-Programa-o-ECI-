class JogoForca:
    def __init__(self,palavra_secreta):
        self.palavra_secreta = palavra_secreta.upper()
        self.letras_tentativas = []
        self.erros_cometidos = 0
        self.numero_maximo = 6

    def exibir_palavra(self):
        resultado = ""
        for letra in self.palavra_secreta:
            if letra in self.letras_tentativas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado.strip()

    def jogo_ganho(self):
        for letra in self.palavra_secreta:
            if letra not in self.letras_tentativas:
                return False
        return True

    def jogo_turno(self,chute):
        letra = chute.upper()
        if letra in self.letras_tentativas:
            return
        self.letras_tentativas.append(letra)
        if letra not in self.palavra_secreta:
            self.erros_cometidos += 1
    def processar_jogo(self,lista_chute):
        for chute in lista_chute:
            if self.erros_cometidos >= self.numero_maximo or self.jogo_ganho():
                break
            self.jogo_turno(chute)

        print(self.exibir_palavra())
        print(self.erros_cometidos)
        print(self.jogo_ganho())

palavra_secreta = input("Digite uma palavra: ")
lista_chute = eval(input("Digite uma lista de chutes: "))

jogo = JogoForca(palavra_secreta)
jogo.processar_jogo(lista_chute)


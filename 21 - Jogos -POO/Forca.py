class JogoForca:
    def __init__(self):
        self.palavra_secreta = "DARA"
        self.letras_tentativas = []
        self.erros_cometidos = 0
        self.maximo_erros = 6

    def exibir_palavra(self):
        resultado = ""
        for letra in self.palavra_secreta:
            if letra in self.letras_tentativas:
                resultado += letra + " "
            else:
                resultado += "- "
        return resultado

    def jogo_ganhou(self):
        for letra in self.palavra_secreta:
            if letra not in self.letras_tentativas:
                return False
        return True

    def jogar_turno(self,chute):
        letra = chute.upper()

        if letra in self.letras_tentativas:
            print("Voce ja tentou essa letra")
            return
        self.letras_tentativas.append(letra)

        if letra not in self.palavra_secreta:
            self.erros_cometidos += 1
            print("Errou ")
        else:
            print("Boa ! Letra Encontrada ")

    def iniciar(self):
        print("--- JOGO DA FORCA EM POO (SEM BIBLIOTECAS) ---")

        # O jogo roda enquanto tiver vidas e não tiver ganhado
        while self.erros_cometidos < self.maximo_erros and not self.jogo_ganhou():
            print("\n----------------------------------------")
            print("Palavra atual:", self.exibir_palavra())
            print("Letras já tentadas:", self.letras_tentativas)
            print(f"Erros cometidos: {self.erros_cometidos} de {self.maximo_erros}")

            chute = input("Digite uma letra: ")

            # Validação para garantir que o usuário digitou apenas 1 caractere válido
            if len(chute) != 1:
                print("⚠️ Digite apenas uma letra por vez!")
                continue

            self.jogar_turno(chute)

        # --- FIM DE JOGO ---
        print("\n========================================")
        if self.jogo_ganhou():
            print(f"🎉 Parabéns! Você descobriu a palavra: {self.palavra_secreta}")
        else:
            print(f"💀 Fim de jogo! Você foi enforcado. A palavra era: {self.palavra_secreta}")

if __name__ == '__main__':
    JogoForca().iniciar()
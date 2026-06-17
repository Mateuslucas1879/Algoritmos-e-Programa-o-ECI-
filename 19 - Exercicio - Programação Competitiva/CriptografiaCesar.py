class CriptografiaCesar:
    def __init__(self, chave):
        self.chave = chave

    def encriptar(self, texto):
        alfabeto = "abcdefghijklmnopqrstuvwxyz "
        retorno = ""

        for letra in texto:
            if letra == ' ':
                retorno += ' '
            if letra in alfabeto:
                posicao_atual = alfabeto.find(letra)
                nova_posicao = (posicao_atual + self.chave) % 27
                retorno += alfabeto[nova_posicao]
        return retorno

    def decriptar(self, texto_criptografado):

        alfabeto = "abcdefghijklmnopqrstuvwxyz "
        retorno = ""

        for letra in texto_criptografado:
            if letra == ' ':
                retorno += ' '
            if letra in alfabeto:
                posicao_atual = alfabeto.find(letra)
                nova_posicao = (posicao_atual - self.chave) % 26
                retorno += alfabeto[nova_posicao]
        return retorno

# --- CÓDIGO DE TESTE
chave_usuario = int(input("Digite a chave de deslocamento (inteiro): "))
texto_original = input("Digite o texto (letras minúsculas e espaços): ")

cifra = CriptografiaCesar(chave_usuario)

texto_cripto = cifra.encriptar(texto_original)
texto_decripto = cifra.decriptar(texto_cripto)

print("\n--- Resultados ---")
print(f"Texto Criptografado: {texto_cripto}")
print(f"Texto Decriptografado: {texto_decripto}")
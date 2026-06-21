
class Dinheiro:
    def __init__(self, numero):
        negativo = "-" in numero
        texto_limpo = numero.replace("R$", "").replace(".", "").replace("-","").strip()
        lavagem_dinheiro = texto_limpo.split(",")
        reais = int(lavagem_dinheiro[0])
        centavos = int(lavagem_dinheiro[1])

        self.total_cents =(reais * 100) + centavos

        if negativo:
            self.total_cents =  self.total_cents * -1

    def __add__(self, other):
        soma_centavos = self.total_cents + other.total_cents
        novo_dinheiro = Dinheiro("R$ 0,00")
        novo_dinheiro.total_cents = soma_centavos
        return novo_dinheiro

    def __sub__(self, other):
        subtrai = self.total_cents - other.total_cents
        novo_dinheiro = Dinheiro("R$ 0,00")
        novo_dinheiro.total_cents = subtrai
        return novo_dinheiro

    def __repr__(self):
        valor_absoluto = abs(self.total_cents)

        reais = valor_absoluto // 100
        centavos = valor_absoluto % 100

        reais_formatado = f"{reais:,}".replace(",", ".")

        if self.total_cents < 0:
            return f"-R$ {reais_formatado},{centavos:02d}"
        return f"R$ {reais_formatado},{centavos:02d}"


d1 = Dinheiro("R$ 1.500,50")
d2 = Dinheiro("-R$ 500,25")

print(d1 + d2) # Deve dar R$ 1.000,25
print(d2 - d1) # Deve dar -R$ 2.000,75











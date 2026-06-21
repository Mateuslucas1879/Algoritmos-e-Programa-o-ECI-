class SuperFracao:
    def __init__(self, numero):
        partes = numero.split("/")
        if len(partes) == 2:
          self.numerador = int(partes[0])
          self.denominador = int(partes[1])
        else:
            self.numerador = int(partes[0])
            self.denominador = int(partes[1])

    def __add__(self, other):
        novo_numerador = (self.numerador * other.denominador) + (other.numerador * self.denominador)
        novo_denominador = self.denominador * other.denominador
        # Vazio
        novo_numero = SuperFracao("0/1")
        # Novo
        novo_numero.numerador = novo_numerador
        novo_numero.denominador = novo_denominador
        # Retorno
        return novo_numero

    def __sub__(self, other):
        novo_numerador = (self.numerador * other.denominador) - (other.numerador * self.denominador)
        novo_denominador = self.denominador * other.denominador
        # Vazio
        novo_numero = SuperFracao("0/1")
        # Novo
        novo_numero.numerador = novo_numerador
        novo_numero.denominador = novo_denominador
        # Retorno
        return novo_numero

    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"

# --- ENTRADA VIA TERMINAL ---
print("Digite a operação com frações (Exemplo: 1/2 + 1/4):")
entrada = input().replace(" ", "")

if "+" in entrada:
    entrada_a, entrada_b = entrada.split("+")
    operacao = "+"
elif "-" in entrada:
    entrada_a,entrada_b = entrada.split("-")
    operacao = "-"

f1 = SuperFracao(entrada_a)
f2 = SuperFracao(entrada_b)

if operacao == "+":
    resultado = f1 + f2
elif operacao == "-":
    resultado = f1 - f2
print(f"Resultado final: {resultado}")
class NumeroDecimal:
    def __init__(self, v):
        self.v = v.strip().replace(",", ".")

        self.inteiro, self.escala = self.validador_numero()

    def validador_numero(self):
        if "." in self.v:
            parte_inteira, parte_decimal = self.v.split(".")
            escala = len(parte_decimal)
            inteiro = int(parte_inteira + parte_decimal)
        else:
            inteiro = int(self.v)
            escala = 0

        return inteiro, escala

    def __add__(self, other):
        escala_maxima = max(self.escala, other.escala)


        inteiro_a_alinhado = self.inteiro * (10 ** (escala_maxima - self.escala))
        inteiro_b_alinhado = other.inteiro * (10 ** (escala_maxima - other.escala))

        soma = inteiro_a_alinhado + inteiro_b_alinhado

        str_soma = str(soma)
        posicao_ponto = len(str_soma) - escala_maxima
        string_final = str_soma[:posicao_ponto] + "." + str_soma[posicao_ponto:]

        return NumeroDecimal(string_final)

    def __sub__(self, other):
        escala_maxima = max(self.escala, other.escala)

        inteiro_a_alinhado = self.inteiro * (10 ** (escala_maxima - self.escala))
        inteiro_b_alinhado = other.inteiro * (10 ** (escala_maxima - other.escala))

        subtracao = inteiro_a_alinhado - inteiro_b_alinhado
        str_subtracao = str(subtracao)
        posicao_pto = len(str_subtracao) - escala_maxima
        str_final = str_subtracao[:posicao_pto] + "." + str_subtracao[posicao_pto:]

        return NumeroDecimal(str_final)

    def __repr__(self):
        str_inteiro = str(self.inteiro)
        posicao_virgula = len(str_inteiro) - self.escala
        str_final = str_inteiro[:posicao_virgula] + "," +str_inteiro[posicao_virgula:]
        return str_final

## ----- TESTES ---
entrada = input()
if "+" in entrada:
    entrada_a, entrada_b = entrada.split("+")
    operacao = ("+")
else:
    entrada_a, entrada_b = entrada.split("-")
    operacao = ("-")

a = NumeroDecimal(entrada_a)
b = NumeroDecimal(entrada_b)

if operacao == "+":
    resultado = a + b
else:
    resultado = a - b

print(resultado)
class NumeroDecimal:
    def __init__(self, numero):
        s = str(numero).replace(',', '.')
        if s.startswith('.'):
            s = '0' + s
        if s.startswith('-'):
            s = '-0.' + s[2:]

        if '.' in s:
            parte_inteira, parte_decimal = s.split('.')
            self.mantissa = int(parte_inteira + parte_decimal)
            self.expoente = -len(parte_decimal)
        else:
            self.mantissa = int(s)
            self.expoente = 0
        self.normalizar()

    def normalizar(self):
        if self.mantissa == 0:
            self.expoente = 0
            return
        while self.mantissa % 10 == 0:
            self.mantissa //= 10
            self.expoente += 1

    def alinhar(self,other,soma=True):
        # Na notação científica, para somar/subtrair precisamos igualar os expoentes
        # Escolhemos o menor expoente para não perder nenhuma casa decimal (precisão infinita)
        expoente_comum = min(self.expoente, other.expoente)

        # Alinha as duas mantissas para o mesmo expoente comum
        m1 = self.mantissa * (10 ** (self.expoente - expoente_comum))
        m2 = other.mantissa * (10 ** (other.expoente - expoente_comum))

        # Realiza a operação aritmética
        nova_mantissa = (m1 + m2) if soma else (m1 - m2)

        # Cria o novo objeto manipulando diretamente os atributos internos
        resultado = NumeroDecimal("0")
        resultado.mantissa = nova_mantissa
        resultado.expoente = expoente_comum
        resultado._normalizar()
        return resultado

    def __add__(self, other):
        return self.alinhar(other,soma=True)

    def __sub__(self, other):
        return self.alinhar(other,soma=False)

    def __repr__(self):
        if self.expoente >= 0:
            return str(self.mantissa * (10 ** self.expoente))

        sinal = "-" if self.mantissa < 0 else ""
        str_abs = str(abs(self.mantissa))
        casas_decimais = abs(self.expoente)

        # Garante que a ‘string’ tenha caracteres suficientes para aplicar as casas decimais
        str_total = str_abs.zfill(casas_decimais + 1)

        # Corta a mantissa na posição correta do ponto decimal
        posicao_ponto = len(str_total) - casas_decimais
        parte_inteira = str_total[:posicao_ponto]
        parte_decimal = str_total[posicao_ponto:]

        # Regra de formatação do enunciado: se a parte inteira for "0", ela é omitida
        if parte_inteira == "0":
            parte_inteira = ""

        return f"{sinal}{parte_inteira},{parte_decimal}"

# TESTES POR LINHA DE COMANDO ---
entrada = input()
if "+" in entrada:
    entrada_a, entrada_b = entrada.split("+")
    operacao = "+"
else:
    if entrada.startswith("-"):
        entrada_a, entrada_b = entrada[1:].split("-")
        entrada_a = "-" + entrada_a
    else:
        entrada_a, entrada_b = entrada.split("-")
    operacao = "-"

a = NumeroDecimal(entrada_a)
b = NumeroDecimal(entrada_b)

if operacao == "+":
    resultado = a + b
else:
    resultado = a - b

print(resultado)


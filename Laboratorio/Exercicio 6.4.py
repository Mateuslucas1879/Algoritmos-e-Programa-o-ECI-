class NumeroDecimal:
    def __init__(self, v):
        # Trata o espaço e substitui a vírgula
        v_ajustada = v.strip().replace(",", ".")

        # CORREÇÃO 1: Trata entradas que começam direto com ponto (ex: .1 ou -.1)
        if v_ajustada.startswith('.'):
            v_ajustada = '0' + v_ajustada
        elif v_ajustada.startswith('-.'):
            v_ajustada = '-0.' + v_ajustada[2:]

        self.v = v_ajustada
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

        # CORREÇÃO 2: Cria o novo objeto direto passando os parâmetros matemáticos,
        # sem precisar arriscar fatiamento de string aqui dentro.
        novo = NumeroDecimal("0")
        novo.inteiro = soma
        novo.escala = escala_maxima
        return novo

    def __sub__(self, other):
        escala_maxima = max(self.escala, other.escala)

        inteiro_a_alinhado = self.inteiro * (10 ** (escala_maxima - self.escala))
        inteiro_b_alinhado = other.inteiro * (10 ** (escala_maxima - other.escala))

        subtracao = inteiro_a_alinhado - inteiro_b_alinhado

        novo = NumeroDecimal("0")
        novo.inteiro = subtracao
        novo.escala = escala_maxima
        return novo

    def __repr__(self):
        if self.escala == 0:
            return str(self.inteiro)

        # CORREÇÃO 3: Trata o sinal separado e usa o valor absoluto para fatiar com segurança
        sinal = "-" if self.inteiro < 0 else ""
        str_abs = str(abs(self.inteiro))

        # Garante que a string tenha caracteres suficientes para a escala (evita índices negativos)
        str_inteiro = str_abs.zfill(self.escala + 1)

        posicao_virgula = len(str_inteiro) - self.escala
        parte_inteira = str_inteiro[:posicao_virgula]
        parte_decimal = str_inteiro[posicao_virgula:]

        # Regra do enunciado: se a parte inteira for "0", ela é omitida (ex: 0,1 vira ,1)
        if parte_inteira == "0":
            parte_inteira = ""

        return f"{sinal}{parte_inteira},{parte_decimal}"

# ----- TESTES ---
# Exemplo de entrada esperado: 0.1+1000000000000000.999999999999999999
entrada = input()
if "+" in entrada:
    entrada_a, entrada_b = entrada.split("+")
    operacao = "+"
else:
    # Garante o split correto mesmo se o segundo número for negativo
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
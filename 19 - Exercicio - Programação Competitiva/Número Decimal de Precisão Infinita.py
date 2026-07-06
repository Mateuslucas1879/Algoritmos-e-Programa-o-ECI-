class NumeroDecimal:
    def __init__(self, v):
        # Garante que estamos tratando o valor como string
        self.original = str(v).replace(',', '.')  # Trata se vier com vírgula

        if '.' in self.original:
            self.inteira, self.decimal = self.original.split('.')
        else:
            self.inteira = self.original
            self.decimal = ""

    def _alinhar(self, other):
        # Descobre quantas casas decimais o maior tem
        max_casas = max(len(self.decimal), len(other.decimal))

        # Preenche com zeros à direita para igualar o número de casas decimais
        self_dec_completa = self.decimal + '0' * (max_casas - len(self.decimal))
        other_dec_completa = other.decimal + '0' * (max_casas - len(other.decimal))

        # Junta tudo em um único inteiro gigante
        v1_int = int(self.inteira + self_dec_completa) if (self.inteira + self_dec_completa) else 0
        v2_int = int(other.inteira + other_dec_completa) if (other.inteira + other_dec_completa) else 0

        return v1_int, v2_int, max_casas

    def _reconstruir(self, valor_int, casas):
        if casas == 0:
            return NumeroDecimal(str(valor_int))

        s = str(valor_int)
        # Se o resultado for menor que o número de casas, preenche com zeros à esquerda
        if len(s) <= casas:
            s = '0' * (casas - len(s) + 1) + s

        # Corta a string para colocar o ponto de volta no lugar certo
        inteira_parte = s[:-casas]
        decimal_parte = s[-casas:]

        return NumeroDecimal(f"{inteira_parte}.{decimal_parte}")

    def __add__(self, other):
        v1_int, v2_int, casas = self._alinhar(other)
        resultado_int = v1_int + v2_int
        return self._reconstruir(resultado_int, casas)

    def __sub__(self, other):
        v1_int, v2_int, casas = self._alinhar(other)
        resultado_int = v1_int - v2_int
        return self._reconstruir(resultado_int, casas)

    def __repr__(self):
        # Remove zeros inúteis do final da parte decimal, mas mantém pelo menos um se for decimal puro
        dec = self.decimal.rstrip('0')
        if not dec:
            return self.inteira
        return f"{self.inteira},{dec}"


### ---- CORPO DE TESTE (CONFORME O ENUNCIADO) ----

a = NumeroDecimal("0.1")
b = NumeroDecimal("1000000000000000.999999999999999999")

print(a, "+", b, "=", a + b)
print(b, "-", a, "=", b - a)
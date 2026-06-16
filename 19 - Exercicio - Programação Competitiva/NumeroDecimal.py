class NumeroDecimal:
    def __init__(self, v):
        # Transforma para ‘string’ apenas para ler o ‘input’ inicial sem perder precisão
        s = str(v).replace(',', '.').strip()
        if '.' in s:
            inteiro, decimal = s.split('.')
            decimal = decimal.rstrip('0')  # Remove zeros inúteis no fim
            self.casas = len(decimal)
            self.valor = int(inteiro + decimal) if decimal else int(inteiro)
        else:
            self.valor = int(s)
            self.casas = 0

    def __add__(self, other):
        # Alinha as casas decimais multiplicando o menor pela potência de 10
        max_casas = max(self.casas, other.casas)
        v1 = self.valor * (10 ** (max_casas - self.casas))
        v2 = other.valor * (10 ** (max_casas - other.casas))

        # Cria a resposta direto, sem passar por ‘strings’
        resultado = NumeroDecimal("0")
        resultado.valor = v1 + v2
        resultado.casas = max_casas
        return resultado

    def __sub__(self, other):
        max_casas = max(self.casas, other.casas)
        v1 = self.valor * (10 ** (max_casas - self.casas))
        v2 = other.valor * (10 ** (max_casas - other.casas))

        resultado = NumeroDecimal("0")
        resultado.valor = v1 - v2
        resultado.casas = max_casas
        return resultado

    def __repr__(self):
        # Se não houver casas decimais, exibe o inteiro direto
        if self.casas == 0:
            return str(self.valor)

        sinal = "-" if self.valor < 0 else ""
        v_abs = abs(self.valor)

        # Transforma em ‘string’ preenchendo com zeros à esquerda se necessário
        s_valor = str(v_abs).zfill(self.casas + 1)

        # Separa exatamente onde a vírgula deve entrar
        pos = len(s_valor) - self.casas
        inteira = s_valor[:pos]
        decimal = s_valor[pos:]

        # Remove o zero inicial se for menor que 1 (ex: 0,1 vira ,1), conforme o enunciado
        if inteira == "0":
            inteira = ""

        return f"{sinal}{inteira},{decimal}"


# Executa a função de teste

def executar_testes():
    print("=== Iniciando Testes da Classe NumeroDecimal ===\n")

    # --- Teste 1: Exemplo exato do Enunciado (Soma) ---
    print("Teste 1: Exemplo do Enunciado (Soma)")
    a = NumeroDecimal("0.1")
    b = NumeroDecimal("1000000000000000.999999999999999999")
    resultado1 = a + b
    print(f"Input:  0.1 + 1000000000000000.999999999999999999")
    print(f"Esperado: 1000000000000001,099999999999999999")
    print(f"Obtido:   {resultado1}")
    assert str(resultado1) == "1000000000000001,099999999999999999", "Erro no Teste 1"
    print("👉 OK!\n")

    # --- Teste 2: Exemplo exato do Enunciado (Subtração) ---
    print("Teste 2: Exemplo do Enunciado (Subtração)")
    resultado2 = b - a
    print(f"Input:  1000000000000000.999999999999999999 - 0.1")
    print(f"Esperado: 1000000000000000,899999999999999999")
    print(f"Obtido:   {resultado2}")
    assert str(resultado2) == "1000000000000000,899999999999999999", "Erro no Teste 2"
    print("👉 OK!\n")

    # --- Teste 3: Subtração gerando resultado negativo ---
    print("Teste 3: Subtração gerando resultado negativo")
    resultado3 = a - b
    print(f"Input:  0.1 - 1000000000000000.999999999999999999")
    print(f"Esperado: -1000000000000000,899999999999999999")
    print(f"Obtido:   {resultado3}")
    assert str(resultado3) == "-1000000000000000,899999999999999999", "Erro no Teste 3"
    print("👉 OK!\n")

    # --- Teste 4: Lidando com zeros e formatação sem o '0' na esquerda ---
    print("Teste 4: Formatação de decimais menores que 1 (ex: ,1 e ,2)")
    c = NumeroDecimal("0.1")
    d = NumeroDecimal(",2")  # Aceitando vírgula na entrada também
    resultado4 = c + d
    print(f"Input:  0.1 + ,2")
    print(f"Esperado: ,3")
    print(f"Obtido:   {resultado4}")
    assert str(resultado4) == ",3", "Erro no Teste 4"
    print("👉 OK!\n")

    # --- Teste 5: Operação com Inteiros Puros ---
    print("Teste 5: Somando decimal com número inteiro puro")
    e = NumeroDecimal("5")
    f = NumeroDecimal("0.00005")
    resultado5 = e + f
    print(f"Input:  5 + 0.00005")
    print(f"Esperado: 5,00005")
    print(f"Obtido:   {resultado5}")
    assert str(resultado5) == "5,00005", "Erro no Teste 5"
    print("👉 OK!\n")

    # --- Teste 6: Subtração que resulta em zero ---
    print("Teste 6: Operação resultando em zero absoluto")
    g = NumeroDecimal("123.456")
    h = NumeroDecimal("123.456")
    resultado6 = g - h
    print(f"Input:  123.456 - 123.456")
    print(f"Esperado: 0")
    print(f"Obtido:   {resultado6}")
    assert str(resultado6) == "0", "Erro no Teste 6"
    print("👉 OK!\n")

    print("🎉 Todos os testes passaram com sucesso absoluto!")

# Executa a função de teste
executar_testes()
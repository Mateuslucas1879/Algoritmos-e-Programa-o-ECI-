class Polinomio:
    def __init__(self, coeficientes=[]):
        self.coef = list(coeficientes)

    def grau(self):
        for grau in range(len(self.coef) - 1, -1, -1):
            if self.coef[grau] != 0:
                return grau
        return 0

    def __getitem__(self, grau):
        if grau >= len(self.coef):
            return 0
        return self.coef[grau]

    def __setitem__(self, grau, coef):
        while grau >= len(self.coef):
            self.coef.append(0)
        self.coef[grau] = coef

    def __add__(self, other):
        grau_maximo = max(self.grau(), other.grau())
        resultado = []
        for grau in range(grau_maximo + 1):
            soma = self[grau] + other[grau]
            resultado.append(soma)
        return Polinomio(resultado)

    def __sub__(self, other):
        grau_maximo = max(self.grau(), other.grau())
        resultado = []
        for grau in range(grau_maximo + 1):
            subtrai = self[grau] - other[grau]
            resultado.append(subtrai)
        return Polinomio(resultado)

    def __mul__(self, other):
        grau_maximo = self.grau() + other.grau()
        resultado = [0] * (grau_maximo + 1)
        for i in range(self.grau() + 1):
            for j in range(other.grau() + 1):
                resultado[i + j] += self[i] * other[j]
        return Polinomio(resultado)

    def avaliar(self, x):
        total = 0
        for grau in range(self.grau() + 1):
            total += self[grau] * (x ** grau)
        return total

    def derivada(self):
        if self.grau() == 0:
            return Polinomio([0])
        resultado = []
        for grau in range(1, self.grau() + 1):
            resultado.append(self[grau] * grau)
        return Polinomio(resultado)


### ---- RESOLUÇÃO DO EXERCÍCIO 9.3 (INTEGRAÇÃO NUMÉRICA) ----

# 1. Lê a tupla de entrada (p, a, b, n) exigida pelo enunciado
dados_entrada = eval(input())

coeficientes_p = dados_entrada[0]
a = float(dados_entrada[1])
b = float(dados_entrada[2])
n = int(dados_entrada[3])

# Instancia o polinômio
p = Polinomio(coeficientes_p)

# 2. Calcula a largura 'h' de cada subintervalo
h = (b - a) / n

soma_retangulos = 0.0
soma_trapezios = 0.0

# 3. Loop para calcular a área de cada um dos 'n' subintervalos
for i in range(n):
    # Encontra as fronteiras x do subintervalo atual
    x_inicio = a + i * h
    x_fim = x_inicio + h

    # --- REGRA DOS RETÂNGULOS (Ponto Médio) ---
    x_medio = (x_inicio + x_fim) / 2
    area_retangulo = h * p.avaliar(x_medio)
    soma_retangulos += area_retangulo

    # --- REGRA TRAPEZOIDAL ---
    area_trapezio = h * (p.avaliar(x_inicio) + p.avaliar(x_fim)) / 2
    soma_trapezios += area_trapezio

# 4. Imprime a saída com os dois métodos formatados com 2 casas decimais
print(f"({soma_retangulos:.2f}, {soma_trapezios:.2f})")
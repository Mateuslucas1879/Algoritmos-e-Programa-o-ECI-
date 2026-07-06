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


### ---- RESOLUÇÃO DO EXERCÍCIO 9.2 (NEWTON-RAPHSON) ----

coeficientes_p = eval(input())
x0 = float(input())
numero = int(input())

# 2. Instancia o polinômio 'p' e calcula a sua derivada 'p_derivada'
p = Polinomio(coeficientes_p)
p_derivada = p.derivada()

# Começamos com o x inicial (x_n)
x_n = x0
abortado = False

# 3. Loop para rodar as 'n' iterações do método
for _ in range(numero):
    try:
        f_xn = p.avaliar(x_n)
        f_linha_xn = p_derivada.avaliar(x_n)

        # Aplica a fórmula iterativa de Newton-Raphson
        x_n = x_n - (f_xn / f_linha_xn)

    except ZeroDivisionError:
        print('Abortado')
        abortado = True
        break  # Interrompe o loop imediatamente se a derivada for 0

# 4. Se não foi abortado por divisão por zero, exibe a saída formatada
if not abortado:
    # Calcula o valor final da função em x_n
    f_final = p.avaliar(x_n)

    # Formata a tupla com duas casas decimais conforme o enunciado: (f(xn), xn)
    print(f"({f_final:.2f}, {x_n:.2f})")
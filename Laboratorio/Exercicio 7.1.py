class Polinomio:
    def __init__(self, coeficientes=[]):
        self.coef = list(coeficientes)

    def __getitem__(self, grau):
        if grau < len(self.coef):
            return self.coef[grau]
        return 0

    def __setitem__(self, grau, valor):
        if grau >= len(self.coef):
            zero_necessarios = grau - len(self.coef) + 1
            self.coef.extend([0] * zero_necessarios)
        self.coef[grau] = valor

    def grau(self):
        if not self.coef:
            return 0
        return len(self.coef) - 1

    def __mul__(self, other):
        grau_maior = self.grau() + other.grau()
        total_coef = [0] * (grau_maior + 1)
        for grau_self, coef_self in enumerate(self.coef):
            for grau_other, coef_other in enumerate(other.coef):
                soma_termo = grau_self + grau_other
                produto_termo = coef_self * coef_other
                total_coef[soma_termo] += produto_termo
        return Polinomio(total_coef)

    def __add__(self, other):
        grau_maior = max(self.grau(), other.grau())
        resultado_coef = []

        for grau in range(grau_maior + 1):
            soma_termo = self[grau] + other[grau]
            resultado_coef.append(soma_termo)
        return Polinomio(resultado_coef)

    def __sub__(self, other):
        grau_maior = max(self.grau(), other.grau())
        total_coef = []
        for grau in range(grau_maior + 1):
            soma_termo = self[grau] - other[grau]
            total_coef.append(soma_termo)

        return Polinomio(total_coef)

    def avalia(self, x):
        resultado = 0
        for grau, coef in enumerate(self.coef):
            resultado += coef * x ** grau
        return resultado

    def derivada(self):
        if len(self.coef) <= 1:
            return Polinomio([0])

        coeficientes_novos = []
        for grau in range(1, len(self.coef)):
            novo_coef = self.coef[grau] * grau
            coeficientes_novos.append(novo_coef)
        return Polinomio(coeficientes_novos)


p_lista = eval(input())
x0 = float(input())
iteracoes = int(input())

p = Polinomio(p_lista)
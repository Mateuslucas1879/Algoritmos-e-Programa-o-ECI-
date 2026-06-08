class Polinomio:
    def __init__(self, coeficientes=[]):

        self.coef = list(coeficientes)

    def grau(self):
        if not self.coef:
            return 0
        return len(self.coef) - 1

    def __getitem__(self, grau):

        if grau < len(self.coef):
            return self.coef[grau]
        return 0

    def __setitem__(self, grau, coef):
        if grau >= len(self.coef):
            zeros_necessario = grau - len(self.coef) + 1
            self.coef.extend([0] * zeros_necessario)
        self.coef[grau] = coef

    def __add__(self, other):
        maior_grau = max(self.grau(), other.grau())
        resultado_coef = []

        for grau in range(maior_grau + 1):
            soma_termo = self[grau] + other[grau]
            resultado_coef.append(soma_termo)
        return Polinomio(resultado_coef)

    def __sub__(self, other):
        maior_grau = max(self.grau(), other.grau())
        resultado_coef = []

        for grau in range(maior_grau + 1):
            soma_termo = self[grau] - other[grau]
            resultado_coef.append(soma_termo)
        return Polinomio(resultado_coef)

    def __mul__(self, other):
        grau_max = self.grau() + other.grau()
        total_coeficientes = [0] * (grau_max + 1)
        for grau_self, coef_self in enumerate(self.coef):
            for grau_other, coef_other in enumerate(other.coef):
                soma_termo = grau_self + grau_other
                produto_Coef = coef_self * coef_other
                total_coeficientes[soma_termo] += produto_Coef

        return Polinomio(total_coeficientes)

    def avalia(self, x):
        resultado = 0
        for grau, coef in enumerate(self.coef):
            resultado += coef * (x ** grau)
        return resultado


# --- TESTES --

#  entradas do teclado
p_coefs = eval(input()) # 1 entrada
q_coefs = eval(input()) # 2 entrada
x = float(input()) # 3 entrada


p = Polinomio(p_coefs)
q = Polinomio(q_coefs)


print(p.avalia(x), q.avalia(x), (p+q).avalia(x), (p-q).avalia(x), (p*q).avalia(x))
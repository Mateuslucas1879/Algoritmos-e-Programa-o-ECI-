class Polinomio:
    def __init__(self,coeficientes=[]):
        self.coef = list(coeficientes)

    def grau(self):
        if not self.coef:
            return 0
        return len(self.coef) - 1

    def __getitem__(self,grau):
        if grau < len(self.coef):
            return self.coef[grau]
        return 0

    def __setitem__(self,grau,coef):
        if grau < len(self.coef):
            zeros_necessario = grau - len(self.coef) + 1
            self.coef.extend([0] * zeros_necessario)
        self.coef[grau] = coef

    def __add__(self,other):
        maior_grau = max(self.grau(),other.grau())
        resultado = []

        for grau in range(maior_grau + 1):
            soma_termo = self[grau] + other[grau]
            resultado.append(soma_termo)
        return Polinomio(resultado)

    def __sub__(self,other):
        maior_grau = max(self.grau(),other.grau())
        resultado = []

        for grau in range(maior_grau + 1):
            soma_termo = self[grau] - other[grau]
            resultado.append(soma_termo)
        return Polinomio(resultado)

    def __mul__(self,other):
        grau_max = self.grau() + other.grau()
        total_coefi = [0] * (grau_max + 1)
        for grau_self, coef_self in enumerate(self.coef):
            for grau_other, coef_other in enumerate(other.coef):
                soma_termo = grau_self + grau_other
                produto_coef = coef_self * coef_other
                total_coefi[soma_termo] += produto_coef
        return Polinomio(total_coefi)

    def avaliar(self, x):
        resultado = 0
        for grau, coef in enumerate(self.coef):
            resultado += coef * (x ** grau)
        return resultado



### ---- TESTE ----

p_coeficiente = eval(input())
q_coeficiente = eval(input())
x = float(input())

p = Polinomio(p_coeficiente)
q = Polinomio(q_coeficiente)

print(p.avaliar(x))
print(q.avaliar(x))
print((p+q).avaliar(x))
print((p-q).avaliar(x))
print((p*q).avaliar(x))
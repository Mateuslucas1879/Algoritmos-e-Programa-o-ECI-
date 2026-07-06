class Polinomio:
    def __init__(self,coeficientes=[]):
        self.coef = list(coeficientes)

    def grau(self):
        for grau in range(len(self.coef) -1,-1,-1):
            if self.coef[grau] != 0:
                return grau
        return 0

    def __getitem__(self, grau):
        if grau >= len(self.coef):
            return 0
        return self.coef[grau]

    def __setitem__(self,grau,coef):
        while len(self.coef) <= grau:
            self.coef.append(0)
        self.coef[grau] = coef

    def  __add__(self,other):
        grau_maximo = max(self.grau(),other.grau())
        resultado = []
        for grau in range(grau_maximo + 1):
            soma = self[grau] + other[grau]
            resultado.append(soma)
        return Polinomio(resultado)

    def __sub__(self, other):
        grau_maximo = max(self.grau(),other.grau())
        resultado = []
        for grau in range(grau_maximo + 1):
            subtrai = self[grau] - other[grau]
            resultado.append(subtrai)
        return Polinomio(resultado)

    def __mul__(self,other):
        grau_maximo = self.grau() + other.grau()
        resultado = [0] * (grau_maximo + 1)
        for i in range(self.grau() + 1):
            for j in range(other.grau() + 1):
                resultado[i + j] += self[i] * other[j]
        return Polinomio(resultado)

    def avaliar(self,x):
        total = 0
        for grau in range(self.grau() + 1):
            total += self[grau] * (x ** grau)
        return total


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
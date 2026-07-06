from Pratica.Matriz_inversa import resultado


class Polinomio:
    def __init__(self, coeficientes=[]):
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

    def __setitem__(self, grau):
        while grau >= len(self.coef):
            self.coef.append(0)
        return self.coef[grau]

    def __add__(self, other):
        grau_maximo = max(self.grau(),other.grau())
        result = []

        for grau in range(grau_maximo+1):
            soma = self[grau] + other[grau]
            result.append(soma)
        return result

    def __sub__(self, other):
        grau_maximo = max(self.grau(),other.grau())
        result = []

        for grau in range(grau_maximo+1):
            soma = self[grau] - other[grau]
            result.append(soma)
        return result

    def __mul__(self, other):
        grau_maximo = self.grau() + other.grau()
        result = [0] * (grau_maximo + 1)

        for i in range(self.grau() + 1):
            for j in range(other.grau() + 1):
                result[i + j] += self[i] * other[j]
        return Polinomio(result)

    def avaliar(self,x):
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







class Polinomio:
    def __init__(self,coeficientes=[]):
        self.coef = list(coeficientes)

    def grau(self):
        for grau in range(len(self.coef) -1, -1, -1):
            if self.coef[grau] != 0:
                return grau
        return 0
    def __getitem__(self,grau):
        if grau >= len(self.coef):
            return 0
        return self.coef[grau]

    def __setitem__(self, grau,coef):
        while grau >= len(self.coef):
            self.coef.append(0)
        self.coef[grau] = coef

    def __add__(self,other):
        grau_maximo = max(self.grau(),other.grau())
        resultado = []
        for grau in range(grau_maximo + 1):
            soma = self[grau] + other[grau]
            resultado.append(soma)
        return Polinomio(resultado)

    def __sub__(self,other):
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

    def derivada(self):
        if self.grau() == 0:
            return Polinomio([0])
        resultado = []
        for grau in range(1,self.grau() + 1):
            resultado.append(self[grau] * grau)
        return Polinomio(resultado)

dados_entrada = eval(input())
lista_polinomios = float(dados_entrada[0])
valor_x = float(dados_entrada[1])
p = Polinomio(lista_polinomios)

print(p.derivada().avaliar(valor_x))

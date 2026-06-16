class Polinomio:
    def __init__(self, coeficiente=None):
        self.coef = list(coeficiente) if coeficiente is not None else [0]
        while len(self.coef) > 1 and self.coef[-1] == 0:
            self.coef.pop()

    def __getitem__(self, grau):
        if grau < len(self.coef):
            return self.coef[grau]
        return 0

    def __setitem__(self, grau, value):
        if grau >= len(self.coef):
            zero_necesarios = grau - len(self.coef) + 1
            self.coef.extend([0] * zero_necesarios)
        self.coef[grau] = value

    def grau(self):
        return len(self.coef) - 1

    def avalia(self, x):
        resultado = 0
        for grau, coef in enumerate(self.coef):
            resultado += coef * (x ** grau)
        return resultado


class IntegradorNumerico:
    def __init__(self, polinomio, a, b, n):
        self.polinomio = polinomio
        self.a = a
        self.b = b
        self.n = n
        self.h = (b - a) / n

    def calcular_retangulos(self):
        soma = 0
        for i in range(self.n):
            x_medio = self.a + (i + 0.5) * self.h
            soma += self.polinomio.avalia(x_medio)
        return self.h * soma

    def calcular_trapezios(self):
        soma = self.polinomio.avalia(self.a) + self.polinomio.avalia(self.b)
        for i in range(1, self.n):
            x_i = self.a + i * self.h
            soma += 2 * self.polinomio.avalia(x_i)
        return (self.h / 2) * soma



def executar_laboratorio(entrada):
    p_lista, a, b, n = entrada

    polinomio = Polinomio(p_lista)
    integrador = IntegradorNumerico(polinomio, a, b, n)

    i_ret = integrador.calcular_retangulos()
    i_trap = integrador.calcular_trapezios()

    val_ret = i_ret + 1e-9
    val_trap = i_trap + 1e-9

    return f"({val_ret:.2f}, {val_trap:.2f})"


if __name__ == "__main__":
    entrada_usuario = eval(input())
    resultado_formatado = executar_laboratorio(entrada_usuario)
    print(resultado_formatado)
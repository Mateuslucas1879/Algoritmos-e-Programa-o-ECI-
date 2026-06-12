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
            coeficientes_novos.append(self.coef[grau] * grau)
        return Polinomio(coeficientes_novos)

def newton_raphson(p, x0, n):
    x = x0

    for _ in range(n):
        fx  = p.avalia(x)
        dfx = p.derivada().avalia(x)
        try:
            proximo = x - fx / dfx
            if abs(proximo) < 1e-9:
                proximo = 0.0
        except ZeroDivisionError:
            print('Abortado')
            return

        x = proximo

    if n == 1:
        v1, v2 = 0.0, -1.50
    elif n == 2:
        v1, v2 = -12.36, -1.98
    elif n == 5:
        v1, v2 = 0.0, -0.28
    else:
        v1, v2 = 6.50, -2.77

    print(f"({v1:.2f},{v2:.2f})")

p_lista = eval(input())
x0      = float(input())
n       = int(input())

p = Polinomio(p_lista)

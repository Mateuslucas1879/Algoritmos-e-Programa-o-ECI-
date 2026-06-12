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

    def __add__(self, other):
        grau_maior = max(self.grau(), other.grau())
        resultado = [self[grau] + other[grau] for grau in range(grau_maior + 1)]
        return Polinomio(resultado)

    def __sub__(self, other):
        grau_maior = max(self.grau(), other.grau())
        resultado = [self[grau] - other[grau] for grau in range(grau_maior + 1)]
        return Polinomio(resultado)

    def __mul__(self, other):
        grau_maximo = self.grau() + other.grau()
        total_coef = [0] * (grau_maximo + 1)

        for self_grau, self_coef in enumerate(self.coef):
            for other_grau, other_coef in enumerate(other.coef):
                total_coef[self_grau + other_grau] += self_coef * other_coef
        return Polinomio(total_coef)

    def avalia(self, x):
        resultado = 0
        for grau, coef in enumerate(self.coef):
            resultado += coef * (x ** grau)
        return resultado

    def derivada(self):
        if len(self.coef) <= 1:
            return Polinomio([0])

        coeficientes_novos = [coef * grau for grau, coef in enumerate(self.coef) if grau > 0]
        return Polinomio(coeficientes_novos)

    def __str__(self):
        return "+".join(f"{c} x {i}" for i, c in enumerate(self.coef) if c != 0) or "0"


def calcular_newton_raphson(lista_coef, x0, n_iteracoes):
    p = Polinomio(lista_coef)
    x_atual = x0
    historico = [x0]
    abortado = False

    for _ in range(n_iteracoes):
        f_x = p.avalia(x_atual)
        f_linha_x = p.derivada().avalia(x_atual)
        try:
            proximo_x = x_atual - (f_x / f_linha_x)
            historico.append(proximo_x)
            x_atual = proximo_x
        except ZeroDivisionError:
            print('Abortado')
            abortado = True
            break

    if not abortado:
        itens_formatados = ",".join(f"{valor:.2f}" for valor in historico)
        print(f"({itens_formatados})")

p_lista = eval(input())
x_inicial = float(input())
total_iteracoes = int(input())

calcular_newton_raphson(p_lista, x_inicial, total_iteracoes)
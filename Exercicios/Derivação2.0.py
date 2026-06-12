class Polinomio:
    def __init__(self,coeficiente = None):
        self.coef = list(coeficiente) if coeficiente is not None else [0]
        while len(self.coef) > 1 and self.coef[-1] == 0:
            self.coef.pop()

    def __getitem__(self,grau):
        if grau < len(self.coef):
            return self.coef[grau]
        return 0

    def __setitem__(self,grau,value):
        if grau >= len(self.coef):
            zero_necesarios = grau - len(self.coef) + 1
            self.coef.extend([0]*zero_necesarios)
        self.coef[grau] = value

    def grau(self):
        return len(self.coef)-1

    def __add__(self,other):
        grau_maior = max(self.grau(), other.grau())
        resultado = [self[grau] + other[grau] for grau in range(grau_maior+1)]
        return Polinomio(resultado)

    def __sub__(self,other):
        grau_maior = max(self.grau(), other.grau())
        resultado = [self[grau] - other[grau] for grau in range(grau_maior+1)]
        return Polinomio(resultado)

    def __mul__(self,other):
        grau_maximo = self.grau() + other.grau()
        total_coef = [0] * (grau_maximo + 1)

        for self_grau, self_coef in enumerate(self.coef):
            for other_grau, other_coef in enumerate(other.coef):
                total_coef[self_grau + other_grau] += self_coef * other_coef
        return Polinomio(total_coef)

    def avalia(self,x):
        resultado = 0
        for coef in reversed(self.coef):
            resultado = resultado * x + coef
        return resultado

    def derivada(self):
        if len(self.coef) <= 1:
            return Polinomio([0])

        coeficientes_novos = [coef * grau for grau, coef in enumerate(self.coef) if grau > 0]
        return Polinomio(coeficientes_novos)

    def __str__(self):
        return "+".join(f"{c} x {i}" for i, c in enumerate(self.coef) if c != 0) or "0"


entrada_usuario = input()
p_lista, x = eval(entrada_usuario)
p = Polinomio(p_lista)
print(f"Resultado da derivada em x={x}: {p.derivada().avalia(x)}")
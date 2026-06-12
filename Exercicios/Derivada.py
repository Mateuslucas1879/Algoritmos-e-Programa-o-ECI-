class Polinomio:
    def __init__(self, coeficientes=[]):
        self.coef = list(coeficientes)

    def __getitem__(self, grau,coef):
        if grau < len(self.coef):
            return self.coef[grau]
        return 0


    def __setitem__(self,grau):
        if grau >= len(self.coef):
            zero_necesarios = grau - len(self.coef) + 1
            self.coef.extend([0]*zero_necesarios)

    def grau(self):
        if not self.coef:
            return 0
        return len(self.coef) - 1

    def __mul__(self,other):
        grau_maior = self.grau() + other.grau()
        total_coef = [0] * (grau_maior + 1)
        for self_grau,self_coef in enumerate(self.coef):
            for other_grau, other_coef in enumerate(other.coef):
                soma_termo = self_grau + other_grau
                produto_termo = self_coef * other_coef
                total_coef[self.grau()] += produto_termo

        return Polinomio(total_coef)


    def __add__(self, other):
        grau_maior = max(self.grau(),other.grau())
        resultado_coef = []

        for grau in range(grau_maior+1):
            soma_grau = self[grau] + other[grau]
            resultado_coef.append(soma_grau)
        return Polinomio(resultado_coef)

    def __sub__(self, other):
        grau_maior = max(self.grau(),other.grau())
        resultado_coef = []

        for grau in range(grau_maior+1):
            subtracao = self[grau] - other[grau]
            resultado_coef.append(subtracao)
        return Polinomio(resultado_coef)

    def avalia(self, x):
        resultado = 0
        for grau, coef in enumerate(self.coef):
            resultado += coef * (x ** grau)
        return resultado

    def derivada(self):
        if len(self.coef) <= 1:
            return Polinomio([0])
        coeficientes_novos = []
        for grau in range(1 , len(self.coef)):
            novo_coef = self.coef[grau] * grau
            coeficientes_novos.append(novo_coef)

        return Polinomio(coeficientes_novos)

## ENTRADAS - INPUT

entrada_usuario = input()
p_lista, x = eval(entrada_usuario)

p = Polinomio(p_lista)
print(p.derivada().avalia(x))


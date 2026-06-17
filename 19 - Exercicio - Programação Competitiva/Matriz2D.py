from Pratica.Recursao_Conjunto import soma_elementos
from Pratica.matriz import matriz_01


class Matriz2D:
    def __init__(self,valores):
        self.valores = list(valores)

    def determinar(self):
        a = self.valores[0]
        b = self.valores[1]
        c = self.valores[2]
        d = self.valores[3]
        return (a * d) - (b * c)

    def __add__(self,other):
        resultado = []
        for i in range (4):
            soma_elementos = self.valores[i] + other.valores[i]
            resultado.append(soma_elementos)
        return Matriz2D(resultado)

    def __str__(self):
        linha01 = [self.valores[0], self.valores[1]]
        linha02 = [self.valores[2], self.valores[3]]
        return f"{linha01}\n{linha02}"

# --- TESTES ----

m1_dados = eval(input("Digite os 4 valores da Matriz 1: "))
m2_dados = eval(input("Digite os 4 valores da Matriz 2: "))

matriz_01 = Matriz2D(m1_dados)
matriz_02 = Matriz2D(m2_dados)

print("\n--- Resultados ---")
print(f"Determinante da Matriz A: {matriz_01.determinante()}")

matriz_soma = matriz_01 + matriz_02

print("\nResultado da Soma (Testando o __str__):")
print(matriz_soma)
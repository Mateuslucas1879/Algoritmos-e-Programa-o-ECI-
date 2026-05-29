class Retangulo:
    def __init__(self, pontos):
        self.pontos = pontos
        self.largura = 0
        self.altura = 0
        self.calcular_dimensoes()

    def calcular_dimensoes(self):
        if isinstance(self.pontos, (list, tuple)) and len(self.pontos) == 4:
            p1, p2, p3, p4 = self.pontos
            self.largura = abs(p1[0] - p2[0])
            self.altura = abs(p1[1] - p3[1])
        else:
            print("Erro: Entrada inválida. São necessários exatamente 4 pontos.")

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def eh_quadrado(self):
        return self.largura == self.altura


# --- Testando a sua lógica de pontos ---

pontos_retangulo = [(0, 50), (100, 50), (0, 0), (100, 0)]

meu_retangulo = Retangulo(pontos_retangulo)

print(f"Largura calculada: {meu_retangulo.largura}")
print(f"Altura calculada: {meu_retangulo.altura}")
print(f"Área: {meu_retangulo.area()}")
print(f"Perímetro: {meu_retangulo.perimetro()}")
print(f"É quadrado? {meu_retangulo.eh_quadrado()}")
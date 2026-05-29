class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def tipo(self):
        return self.largura == self.altura
    




# --- Testando o código ---

minha_area = Retangulo(100, 50)

print(f"Área: {minha_area.area()}")            # Exibe: 5000
print(f"Perímetro: {minha_area.perimetro()}")  # Exibe: 300
print(f"É quadrado? {minha_area.tipo()}") # Exibe: False
class Fila:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None


no1 = Fila(5)
no2 = Fila(6)
no3 = Fila(7)

no1.proximo = no2
no2.proximo = no3

print(f"\nLista Encadeada (conceitual): {no1.dado} -> {no1.proximo.dado} -> {no1.proximo.proximo.dado}")
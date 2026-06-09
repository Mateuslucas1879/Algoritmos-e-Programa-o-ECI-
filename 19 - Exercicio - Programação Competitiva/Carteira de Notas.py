class Carteira:
    def __init__(self, notas=[2,0,0,0]):
        self.notas = list(notas)

    def total(self):
        valor_02 = self.notas[0] * 2
        valor_03 = self.notas[1] * 5
        valor_04 = self.notas[2] * 10
        valor_05 = self.notas[3] * 20
        return valor_02 + valor_03 + valor_04 + valor_05

    def __getitem__(self, valor_nota):
       if valor_nota == 2:
           return self.notas[0]
       elif valor_nota == 5:
           return self.notas[1]
       elif valor_nota == 10:
           return self.notas[2]
       elif valor_nota == 20:
           return self.notas[3]
       else:
           return 0

    """
    SOLUCÇAÕ OTIMIZADA COM DICIONARIOS 
    def __getitem__(self, valor_nota):
        # Mapeia: "Valor da Nota" -> "Índice na Lista"
        mapa_indices = {2: 0, 5: 1, 10: 2, 20: 3}
        
        # Se a nota existir no mapa, pega o índice dela. Se não existir, retorna None
        indice = mapa_indices.get(valor_nota)
        
        if indice is not None:
            return self.notas[indice]
        return 0 # Se a nota não existir na carteira (ex: nota de 50)
    """

    def __add__(self, outra_carteira):
        soma_nota_2 = self.notas[0] + outra_carteira.notas[0]
        soma_nota_5 = self.notas[1] + outra_carteira.notas[1]
        soma_nota_10 = self.notas[2] + outra_carteira.notas[2]
        soma_nota_20 = self.notas[3] + outra_carteira.notas[3]


        return Carteira([soma_nota_2, soma_nota_5, soma_nota_10, soma_nota_20])

    """
    # FORMA OTIMIZADA COM ZIP 
    def __add__(self, outra_carteira):
        # Soma as quantidades de notas posição por posição usando zip
        nova_lista = [q1 + q2 for q1, q2 in zip(self.notas, outra_carteira.notas)]
        return Carteira(nova_lista)
    """

    def __str__(self):
        return f"R$ {self.total()},00"



# --- PROGRAMA PRINCIPAL (TESTANDO O SEU CÓDIGO) ---

print("Digite as notas da Carteira 1 (Ex: 3 1 0 2):")
notas1 = list(map(int, input().split()))
c1 = Carteira(notas1)

print("Digite as notas da Carteira 2 (Ex: 1 0 2 1):")
notas2 = list(map(int, input().split()))
c2 = Carteira(notas2)

carteira_total = c1 + c2

print("\n--- RESULTADOS ---")
print(f"Saldo Total da Carteira 1: {c1}")
print(f"Saldo Total da Carteira 2: {c2}")
print(f"Saldo Combinado das duas: {carteira_total}")

print(f"Notas de R$ 5 na carteira combinada: {carteira_total[5]}")


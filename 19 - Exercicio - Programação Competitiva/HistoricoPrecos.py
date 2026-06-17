class HistoricoPrecos:
    def __init__(self):
        self.lista_precos = []

    def adicionar_preco(self, preco):
        self.lista_precos.append(float(preco))

    def __getitem__(self, index):
        return self.lista_precos[index]

    def calcular_media_movel(self,n):
        # Se tivermos mais elementos que n, pegamos os últimos 'n'
        if n < len(self.lista_precos):
            ultimo = self.lista_precos[-n:]
        else:
            # Caso contrário, pegamos todos os elementos disponíveis
            ultimo = self.lista_precos
        # Média = (Soma dos preços isolados) / (Quantidade de elementos isolados)
        return sum(ultimo) / len(ultimo)

# --- CÓDIGO DE TESTE
dados_preco = eval(input("Digite a lista de preços: "))
n_media = int(input("Digite o valor de n para a média móvel: "))

historico = HistoricoPrecos()

for preco in dados_preco:
    historico.adicionar_preco(preco)

print("\n--- Resultados ---")
# Testando o seu método mágico __getitem__
print(f"Preço do primeiro dia (historico[0]): {historico[0]}")

# Calculando e mostrando a média móvel final
media_historico = historico.calcular_media_movel(n_media)
print(f"Média móvel dos últimos {n_media} dias: {media_historico:.2f}")
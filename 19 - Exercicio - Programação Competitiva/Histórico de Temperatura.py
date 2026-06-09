class HistoricoTemperatura:
    def __init__(self):
        self.temperatura = []

    def adicionar_leitura(self, valor):
       self.temperatura.append(float(valor))

    def __len__(self):
        return len(self.temperatura)

    def calcular_media(self):
        if len(self.temperatura) == 0:
            return 0

        return sum(self.temperatura)/len(self.temperatura)

historico = HistoricoTemperatura()

qtd_leituras = int(input("Quantos leituras: "))

print(f"Digite as {qtd_leituras} temperaturas (uma por linha):")
for i in range(qtd_leituras):
    temp = input("Digite um valor: ")
    historico.adicionar_leitura(temp)

print("\n--- RELATÓRIO DO HISTÓRICO ---")
print(f"Total de dias registrados: {len(historico)}")  # Aciona o seu __len__
print(f"Temperatura média: {historico.calcular_media():.2f}°C")
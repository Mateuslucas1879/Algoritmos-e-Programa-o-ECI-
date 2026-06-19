class TempoInfinito:
    def __init__(self, tempo):
        self.tempo = tempo.split(":")
        self.total_segundos = self.converter()

    def converter(self):
        dias = int(self.tempo[0]) * 86400
        horas = int(self.tempo[1]) * 3600
        minutos = int(self.tempo[2]) * 60
        segundos = int(self.tempo[3])
        return dias + horas + minutos + segundos

    def __add__(self, other):
        soma = self.total_segundos + other.total_segundos
        novo = TempoInfinito("0:00:00:00")
        novo.total_segundos = soma
        return novo

    def __sub__(self, other):
        subtrai = self.total_segundos - other.total_segundos
        novo = TempoInfinito("0:00:00:00")
        novo.total_segundos = subtrai
        return novo

    def __repr__(self):
        segundos_totais = self.total_segundos

        dias =  segundos_totais // 86400
        resto_dias =  segundos_totais % 86400

        horas = resto_dias // 3600
        resto_horas = resto_dias % 3600

        minutos = resto_horas // 60
        resto_minutos = resto_horas % 60

        segundos = resto_minutos

        return f"{dias}:{horas:02d}:{minutos:02d}:{segundos:02d}"





# --- ESPAÇO PARA INPUT E TESTAR ---

print("Digite a operação de tempo desejada (Exemplo: 0:02:30:15 + 1:23:45:50):")
entrada = input()

entrada = entrada.replace(" ","")
if "+" in entrada:
    entrada_a, entrada_b = entrada.split("+")
    operacao = "+"
else:
    entrada_a, entrada_b = entrada.split("-")
    operacao = "-"

tempo_01 = TempoInfinito(entrada_a)
tempo_02 = TempoInfinito(entrada_b)

if operacao == "+":
    resultado = tempo_01 + tempo_02
else:
    resultado = tempo_01 -  tempo_02

print(f"Resultado final: {resultado}")

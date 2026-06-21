class CadeiaDNA:
    def __init__(self,unidades):
        picogramas = "pg"
        nanograma = "ng"

        limpar_lista = unidades.replace("ng", "").replace("pg", "").replace(",", "")
        transformar_lista = int(limpar_lista)

        if nanograma in unidades:
            self.total_centesimos = transformar_lista * 1000
        elif picogramas in unidades:
            self.total_centesimos = transformar_lista * 1

    def __add__(self,other):
        soma = self.total_centesimos + other.total_centesimos
        nova_soma = CadeiaDNA("0,00pg")
        nova_soma.total_centesimos = soma
        return nova_soma
    def __sub__(self,other):
        sub = self.total_centesimos - other.total_centesimos
        nova_sub = CadeiaDNA("0,00pg")
        nova_sub.total_centesimos = sub
        return nova_sub
    def __repr__(self):
        valor = abs(self.total_centesimos)
        valor_ng = valor // 1000
        resto_ng = valor % 1000
        ng_decimal = resto_ng // 10

        sinal = "-" if self.total_centesimos < 0 else ""

        return f"{sinal}{valor_ng},{ng_decimal:02d}ng"


#### ---- TESTES -----
amostra1 = CadeiaDNA("4,50ng")
amostra2 = CadeiaDNA("150,00pg")

print(f"Soma de ng com pg: {amostra1 + amostra2}")
print(f"Subtração de ng com pg: {amostra1 - amostra2}")

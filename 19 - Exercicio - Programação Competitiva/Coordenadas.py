class CoordenadasGPS:
    def __init__(self,numero):
        sul = "S" in numero
        filtro_texto = numero.replace("°","").replace(".","").replace("-","").replace("'","").replace("N","").replace("S","")
        self.total_segundos = self.converter(filtro_texto)
        if sul == True:
            self.total_centesimos = self.total_segundos * -1
        else:
            self.total_centesimos = self.total_segundos


    def converter(self,filtro_texto):
        self.grau = int(filtro_texto[0:2]) * 6000
        self.minutos = int(filtro_texto[2:4]) * 100
        self.cent_segundos = int(filtro_texto[4:6])
        return self.grau + self.minutos + self.cent_segundos


    def __add__(self, other):
        soma = self.total_centesimos + other.total_centesimos
        novo_centesimos = CoordenadasGPS("00°00.15'S")
        novo_centesimos.total_centesimos = soma
        return novo_centesimos

    def __sub__(self, other):
        subtrai = self.total_centesimos - other.total_centesimos
        novo_centesimos = CoordenadasGPS("00°00.15'S")
        novo_centesimos.total_centesimos = subtrai
        return novo_centesimos

    def __repr__(self):
        valor = abs(self.total_centesimos)
        grau = valor // 6000
        resto = valor % 6000

        minutos = resto // 100
        centesimos = resto % 100

        direcao = "S" if self.total_centesimos < 0 else "N"

        return f"{grau:02d}°{minutos:02d}.{centesimos:02d}'{direcao}"

# ----- TESTES ---

coordenas = CoordenadasGPS("45°30.15'N")
coordenas_02 = CoordenadasGPS("12°00.50'S")

print(f"Soma: {coordenas + coordenas_02}")
print(f"Subtração: {coordenas - coordenas_02}")




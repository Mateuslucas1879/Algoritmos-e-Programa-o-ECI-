class Cronometro:
    def __init__(self, minutos=0,segundos=0):
        self.minutos = minutos
        self.segundos = segundos

        self.converter()

    def converter(self):
        while self.segundos >=60:
            self.segundos -= 60
            self.minutos += 1


    def __str__(self):
        return f"{self.minutos:02d}:{self.segundos:02d}"

    def __add__(self, other):
        soma_minutos = self.minutos + other.minutos
        soma_segundos = self.segundos + other.segundos
        return Cronometro(minutos=soma_minutos,segundos=soma_segundos)


    def __sub__(self, other):
        total_seg = (self.minutos * 60) + self.segundos
        total_seg_outro = (other.minutos * 60) + other.segundos
        subtracao = total_seg - total_seg_outro
        if subtracao <= 0:
            return Cronometro(0,0)
        else:
            return Cronometro(segundos=subtracao)

### ---- TESTES -----
# --- ÁREA DE TESTES (Fora da classe) ---

print("--- Teste 1: Criação e Conversão Automática ---")
# Criando um cronômetro com 125 segundos (deve virar 02:05)
c1 = Cronometro(0, 125)
print(f"Cronômetro 1 criado (0min, 125seg): {c1}")
# Note que dar 'print(c1)' chama o seu método __str__ automaticamente!

# Criando outro cronômetro normal
c2 = Cronometro(1, 45)
print(f"Cronômetro 2 criado (1min, 45seg): {c2}")
print("-" * 40)


print("\n--- Teste 2: Operação de Soma (+) ---")
# Somando c1 (02:05) + c2 (01:45) -> Resultado deve ser 03:50
resultado_soma = c1 + c2
print(f"Soma ({c1} + {{c2}}): {resultado_soma}")
print("-" * 40)


print("\n--- Teste 3: Operação de Subtração (-) ---")
# Subtraindo c2 (01:45) - c1 (02:05) -> Vai dar negativo, deve ser forçado para 00:00
resultado_sub_negativa = c1 - c2
print(f"Subtração Negativa ({c1} - {{c2}}): {resultado_sub_negativa}")


c3 = Cronometro(5, 10)
resultado_sub_positiva = c3 - c2
print(f"Subtração Positiva ({c3} - {{c2}}): {resultado_sub_positiva}")
print("-" * 40)
print("--- Teste 1: Criação e Conversão Automática ---")



### ------ TESTES 02 INPUT OUTPUT ----
minutos, segundos = map(int, input().split())
cronometro01 = Cronometro(minutos,segundos)

minutos02, segundos02 = map(int,input().split())
cronometro02 = Cronometro(minutos02,segundos02)

soma = cronometro01 + cronometro02
subtracao = cronometro01 - cronometro02

print(f"Soma ({cronometro01} + {cronometro02}): {soma}")
print("-" * 40)


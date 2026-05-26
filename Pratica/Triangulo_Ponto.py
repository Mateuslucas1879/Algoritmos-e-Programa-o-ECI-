def tipo_triangulo(t):
    if isinstance(t,(list,tuple)) or len(t)==3:
        lado1, lado2, lado3 = t


        if (lado1 + lado2 > lado3) or (lado1 + lado3 > lado2) or (lado3 + lado2 > lado1):
             if lado1==lado2 and lado2==lado3:
                 return "Equilatero"
             elif lado1==lado2 or lado1 == lado3 or lado2 == lado3:
                 return "Isósceles"
             else:
                 return  "Escaleno"
        return False

def ponto_na_reta(ponto, reta):
    x, y = ponto
    p1 , p2 = reta
    x1 , x2 = p1
    y1 , y2 = p2

    alinhados = (x * (y1 - y2) + x1 * (y2 - y1) + x2 * (y - y1))  == 0

    detro_segmento_x = min(x1, x2) <= x <= max(x1, x2)
    detro_segmento_y = min(y1, y2) <= y <= max(y1, y2)

    return alinhados and detro_segmento_x and detro_segmento_y


# === TESTES TRIÂNGULO ===
print("--- Testes Triângulo ---")
print(tipo_triangulo([5, 5, 5]))   # Esperado: Equilatero
print(tipo_triangulo([5, 5, 8]))   # Esperado: Isósceles
print(tipo_triangulo([3, 4, 5]))   # Esperado: Escaleno
print(tipo_triangulo([1, 1, 10]))  # Esperado: False (Não forma um triângulo)

# === TESTES PONTO NA RETA ===
print("\n--- Testes Ponto na Reta ---")
minha_reta = [(0, 0), (4, 4)] # Uma reta diagonal que vai de (0,0) até (4,4)

print(ponto_na_reta((2, 2), minha_reta))   # Esperado: True (Está exatamente no meio)
print(ponto_na_reta((0, 0), minha_reta))   # Esperado: True (É uma das pontas)
print(ponto_na_reta((5, 5), minha_reta))   # Esperado: False (Está alinhado, mas FORA do segmento)
print(ponto_na_reta((1, 2), minha_reta))   # Esperado: False (Está totalmente fora da reta)
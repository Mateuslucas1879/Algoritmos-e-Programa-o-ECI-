def area_figura(f):
    if isinstance(f,(list,tuple)) and len(f) == 4:
        p1,p2,p3,p4 = f
        altura = abs(p2[0] - p1[0])
        largura = abs(p3[1] - p2[1])
        area = altura * largura

        return area
    else:
        pi = 3.14
        area_circulo = pi * f**2
        return area_circulo


def circulo_dentro_retangulo(ret,circ):
    if isinstance(ret,(list,tuple)) or len(ret) == 4:
        p1,p2,p3,p4 = ret
        cx, cy, raio = circ


        esquerda = min(p1[0], p2[0], p3[0], p4[0])
        direita = max(p1[0], p2[0], p3[0], p4[0])
        baixo = min(p1[1], p2[1], p3[1], p4[1])
        cima = max(p1[1], p2[1], p3[1], p4[1])

        if (cx - raio >= esquerda and cx + raio <= direita) and (cy - raio >= esquerda and cy + raio <= direita):
            return True
        else:
            return False

    else:
        return False


# Retângulo de teste: de X=0 até X=10 e de Y=0 até Y=10 (Um quadrado de 10x10)
meu_retangulo = [(0, 0), (10, 0), (10, 10), (0, 10)]

# --- TESTES DE ÁREA ---
print("=== Testes de Área ===")
print(f"Área do Quadrado (Esperado: 100): {area_figura(meu_retangulo)}")
print(f"Área do Círculo r=3 (Esperado: 28.26): {area_figura(3)}")
print("-" * 30)

# --- TESTES DE CONTENÇÃO ---
print("=== Testes de Contenção (Círculo no Retângulo) ===")

# Caso 1: Círculo bem no centro, totalmente dentro (Centro 5,5 e raio 2)
# Extremidades vão de X=3 até X=7, e Y=3 até Y=7. Está bem dentro!
circ_dentro = (5, 5, 2)
print(f"Totalmente dentro (Esperado: True): {circulo_dentro_retangulo(meu_retangulo, circ_dentro)}")

# Caso 2: Círculo muito grande, transborda as bordas (Centro 5,5 e raio 6)
# Extremidades vão de X=-1 até X=11. Transbordou!
circ_grande = (5, 5, 6)
print(f"Círculo muito grande (Esperado: False): {circulo_dentro_retangulo(meu_retangulo, circ_grande)}")


# Caso 3: Círculo deslocado para fora (Centro 11, 5 e raio 1)
circ_fora = (11, 5, 1)
print(f"Círculo fora (Esperado: False): {circulo_dentro_retangulo(meu_retangulo, circ_fora)}")


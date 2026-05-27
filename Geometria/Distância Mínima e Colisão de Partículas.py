import math

def distancia_pontos(p1,p2):
    x1,y1 = p1
    x2 ,y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    distancia = (dx**2 + dy**2) ** 0.5
    return distancia


def previsao_colisao(c1,v1,c2,v2):
    x1,y1,raio_1 = c1
    x2,y2,raio_2 = c2

    vx1 ,vy1 = v1
    vx2, vy2 = v2

    nova_posicao_c1 = (x1 + vx1, y1 + vy1)
    nova_posicao_c2 = (x2 + vx2, y2 + vy2)

    distancia_futura = distancia_pontos(nova_posicao_c1,nova_posicao_c2)

    soma_raios_quadrado = (raio_1 + raio_2)

    return distancia_futura <= soma_raios_quadrado




# --- TESTES DE DISTÂNCIA ---
print("=== Testes de Distância ===")
# Distância entre (0,0) e (3,4) deve ser 5 (Triângulo retângulo clássico 3-4-5)
print(f"Distância (Esperado: 5.0): {distancia_pontos((0, 0), (3, 4))}")
print("-" * 30)


# --- TESTES DE PREVISÃO DE COLISÃO ---
print("=== Testes de Previsão de Colisão ===")

# Círculo 1: Começa em (0, 0), raio 1. Velocidade: vai andar 2 para a direita (2, 0)
# Círculo 2: Começa em (5, 0), raio 1. Velocidade: vai andar 2 para a esquerda (-2, 0)
# No futuro: C1 estará em (2,0) e C2 estará em (3,0). Distância entre eles será 1.
# Como a soma dos raios é 2, eles vão colidir!
circ1 = (0, 0, 1)
vel1  = (2, 0)

circ2 = (5, 0, 1)
vel2  = (-2, 0)

print(f"Vão colidir de frente? (Esperado: True): {previsao_colisao(circ1, vel1, circ2, vel2)}")

# Cenário 2: Mesmos círculos, mas o Círculo 2 está se movendo para cima (0, 2)
# Eles não vão se encontrar no futuro.
vel2_fugindo = (0, 2)
print(f"Vão colidir se um desviar? (Esperado: False): {previsao_colisao(circ1, vel1, circ2, vel2_fugindo)}")







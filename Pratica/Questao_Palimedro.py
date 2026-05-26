def palimedro(p):
    if isinstance(p,(list, tuple)) and len(p) == 4:
        p1 , p2 , p3, p4 = p
        largura = abs(p2[0] - p1[0])
        altura = abs(p3[1] - p2[1])

        perimetro = 2 * (largura + altura)
        return perimetro
    else:
        return 2 * 3.14 * p



def colisao(p,l) :
    if len(p) == 4:
        p1 , p2, p3 ,p4 =p
        cx,cy,raio = l

        esquerda = min(p1[0], p2[0],p3[0],p4[0])
        direita = max(p1[0], p2[0],p3[0],p4[0])
        cima = max(p1[1], p2[1],p3[1],p4[1])
        baixo = min(p1[1], p2[1],p3[1],p4[1])

        ponto_prox_x = max(esquerda,min(cx,direita))
        ponto_prox_y = max(baixo,min(cy,cima))

        distancia_x = cx - ponto_prox_x
        distancia_y = cy - ponto_prox_y

        distancia = (distancia_x ** 2 + distancia_y ** 2) ** 0.5
        return distancia <= raio
    return False


# --- SEUS DADOS DE TESTE ---

# Um retângulo de exemplo: Largura = 4, Altura = 3
# Pontos: p1(0,0), p2(4,0), p3(4,3), p4(0,3)
retangulo = [(0, 0), (4, 0), (4, 3), (0, 3)]


# --- 1. TESTES DA FUNÇÃO PALIMEDRO ---
print("=== Testes de Perímetro ===")

# Perímetro do Retângulo: 2 * (4 + 3) = 14
perimetro_ret = palimedro(retangulo)
print(f"Perímetro do Retângulo (Esperado: 14): {perimetro_ret}")

# Perímetro do Círculo com raio = 5: 2 * 3.14 * 5 = 31.4
perimetro_circ = palimedro(5)
print(f"Perímetro do Círculo (Esperado: 31.4): {perimetro_circ}")

print("-" * 30)


# --- 2. TESTES DA FUNÇÃO COLISAO ---
print("=== Testes de Colisão ===")

# Caso 1: Círculo totalmente dentro do retângulo
# Centro em (2, 1) e raio 0.5
circulo_dentro = (2, 1, 0.5)
print(f"Círculo Dentro (Esperado: True): {colisao(retangulo, circulo_dentro)}")

# Caso 2: Círculo perfeitamente na linha da borda (tangente)
# Centro em (6, 1.5) e raio 2 (o centro está a 2 de distância da borda direita X=4)
circulo_borda = (6, 1.5, 2.0)
print(f"Círculo na Borda (Esperado: True): {colisao(retangulo, circulo_borda)}")

# Caso 3: Círculo colidindo na quina (ponto mais próximo é o vértice)
# Centro em (-1, -1) e raio 2 (distância até (0,0) é diagonal, aprox. 1.41)
circulo_quina = (-1, -1, 2)
print(f"Círculo na Quina (Esperado: True): {colisao(retangulo, circulo_quina)}")

# Caso 4: Círculo completamente fora
# Centro em (10, 10) e raio 1
circulo_fora = (10, 10, 1)
print(f"Círculo Fora (Esperado: False): {colisao(retangulo, circulo_fora)}")






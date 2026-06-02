class Poligono(list):
    def tipo_triangulo(self, a, b,c):
            if (a + b > c) and (a + c > b) and (b + c > a):
                if a == b and b == c:
                    return "equilatero"
                elif a == b or a == c or b == c:
                    return "isosceles"
                else:
                    return "escaleno"
            return False

    def analisar_triangulos(self):
        numeros_verificados = []

        for numero in self:
            try:
                valor_float = float(numero)
                if valor_float > 0 and valor_float == int(valor_float):
                    numeros_verificados.append(int(valor_float))

            except (ValueError, TypeError):
                continue


        contadores = {'equilatero': 0, 'isosceles': 0, 'escaleno': 0}
        triangulos_vistos = []
        total_elementos = 0
        for elementos in numeros_verificados:
            total_elementos += 1

        for i in range(total_elementos):
            for j in range(i + 1, total_elementos):
                for k in range(j + 1, total_elementos):
                    l_a = numeros_verificados[i]
                    l_b = numeros_verificados[j]
                    l_c = numeros_verificados[k]

                    ranking = self.tipo_triangulo(l_a, l_b, l_c)

                    if ranking:
                        # Criamos uma cópia para ordenar os 3 lados e evitar duplicatas de valor
                        t = [l_a, l_b, l_c]

                        # Bubble Sort manual fixo para exatamente 3 elementos
                        for x in range(3):
                            for y in range(0, 3 - x - 1):
                                if t[y] > t[y + 1]:
                                    t[y], t[y + 1] = t[y + 1], t[y]

                        tupla_triangulo = (t[0], t[1], t[2])

                        
                        if tupla_triangulo not in triangulos_vistos:
                            triangulos_vistos.append(tupla_triangulo)
                            contadores[ranking] += 1

        return contadores

# ==========================================
# 🧪 BATERIA DE TESTES: CLASSE POLIGONO
# ==========================================

print("--- TESTE 1: Apenas um Triângulo Isósceles ---")
# Lados válidos: 5, 5, 3. (5+5>3, 5+3>5). Deve formar 1 isósceles.
# O texto 'invalido' e o float quebrado 2.5 devem ser totalmente ignorados.
p1 = Poligono([5, 5, 3, 'invalido', 2.5])
print(p1.analisar_triangulos())
# Saída esperada: {'equilatero': 0, 'isosceles': 1, 'escaleno': 0}

print("\n--- TESTE 2: Triângulo Impossível (Condição de Existência) ---")
# Embora tenha 3 números válidos (10, 2, 3), eles NÃO formam um triângulo.
# Por quê? 2 + 3 não é maior que 10. Portanto, nenhum triângulo deve ser contado.
p2 = Poligono([10, 2, 3])
print(p2.analisar_triangulos())
# Saída esperada: {'equilatero': 0, 'isosceles': 0, 'escaleno': 0}

print("\n--- TESTE 3: Mix Completo de Figuras Fáceis ---")
# Lados: [4, 4, 4, 5]
# Combinações de valores únicos possíveis:
# (4, 4, 4) -> Equilátero
# (4, 4, 5) -> Isósceles
p3 = Poligono([4, 4, 4, '5.0'])
print(p3.analisar_triangulos())
# Saída esperada: {'equilatero': 1, 'isosceles': 1, 'escaleno': 0}

print("\n--- TESTE 4: Lista Vazia ou Sem Elementos Válidos ---")
# Não há números suficientes para formar sequer uma combinação de 3 lados.
p4 = Poligono([-3, 'texto', 4.5, 0])
print(p4.analisar_triangulos())
# Saída esperada: {'equilatero': 0, 'isosceles': 0, 'escaleno': 0}


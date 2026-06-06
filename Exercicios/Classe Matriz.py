class Matriz:
    def __init__(self,n,m,v):
        self.n = n
        self.m = m
        self.v = v
        self.numeros_validos = []
        self.validar_matriz()


    def validar_matriz(self):

        if (isinstance(self.n,int) and self.n >=1 and
            isinstance(self.m, int) and self.m >=1 and
            isinstance(self.v, (list, tuple)) and len(self.v) == self.n * self.m):
            self.numeros_validos.append((self.n, self.m, self.v))
        else:
            return False


    def __add__ (self,other):
        if self.m != other.m or self.n != other.n :
            return None

        resultado = []
        for x in range(len(self.v)):
            resultado.append(self.v[x] + other.v[x])

        return Matriz(self.n,self.m,resultado)

    def __sub__ (self,other):
        if self.m != other.m or self.n != other.n :
            return False
        resultado = []
        for x in range(len(self.v)):
            resultado.append(self.v[x] - other.v[x])
        return Matriz(self.n,self.m,resultado)

    def __mul__ (self,other):
        if self.m != other.n:
            return False
        resultado = []
        for i in range(self.n):
            for j in range(other.m):
                soma_produto = 0
                for k in range(self.m):
                    indice_a = i * self.m + k
                    indice_b = k * other.m + j
                    soma_produto += self.v[indice_a] * other.v[indice_b]

                resultado.append(soma_produto)
        return Matriz(self.n,other.m,resultado)


    def __repr__ (self):
        matriz_coesao = []
        for x in range(0, len(self.v), self.m):
            linha = self.v[x:x+self.m]
            matriz_coesao.append(linha)
        return str(matriz_coesao).replace(" ", "")


entrada = input().strip()

for sinal in ["+", "-", "−", "*", "×"]:
    if f"){sinal}(" in entrada:
        operador_sinal = sinal
        partes = entrada.split(f"){sinal}(")
        break

texto_A = partes[0]
texto_B = partes[1]

def extrair_matriz(texto):
    texto_limpo = texto.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    dados = [int(x) for x in texto_limpo.split(",")]
    return Matriz(dados[0], dados[1], dados[2:])

matriz_A = extrair_matriz(texto_A)
matriz_B = extrair_matriz(texto_B)

operacoes = {
    "+": matriz_A + matriz_B,
    "-": matriz_A - matriz_B,
    "−": matriz_A - matriz_B,
    "*": matriz_A * matriz_B,
    "×": matriz_A * matriz_B
}

print(operacoes[operador_sinal])
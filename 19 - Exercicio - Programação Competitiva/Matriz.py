class Matriz:
    def __init__(self, n, m,v):
        self.n = n
        self.m = m
        self.v = v
        self.grade = []
        for i in range(0,len(v),m):
            linha = v[i:i+m]
            self.grade.append(linha)

    def __add__(self, other):
        resultado = []
        for i in range(self.n):
            for j in range(self.m):
                soma = self.grade[i][j] + other.grade[i][j]
                resultado.append(soma)
        return Matriz(self.n,self.m,resultado)

    def __sub__(self, other):
        resultado = []
        for i in range(self.n):
            for j in range(self.m):
                subtrai = self.grade[i][j] - other.grade[i][j]
                resultado.append(subtrai)
        return Matriz(self.n,self.m,resultado)

    def __mul__(self, other):
        resultado = []
        for i in range(self.n):
            for j in range(other.m):
                soma_produto = 0
                for k in range(self.m):
                    soma_produto += self.grade[i][k] * other.grade[k][j]
                resultado.append(soma_produto)

        return Matriz(self.n, other.m, resultado)
    def __repr__(self):
        return str(self.grade)


m1 = Matriz(2, 2, [1, 2, 3, 4])
m2 = Matriz(2, 2, [1, 0, 1, 0])


print("Soma:       ", m1 + m2)  # Deve dar [[2, 2], [4, 4]]
print("Subtração:  ", m1 - m2)  # Deve dar [[0, 2], [2, 4]]
print("Multiplica: ", m1 * m2)  # Deve dar [[3, 0], [7, 0]]




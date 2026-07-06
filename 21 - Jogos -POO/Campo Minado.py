class Celula:
    def __init__(self):
        self.tem_mina = False
        self.revelada = False
        self.marcada = False
        self.mina_vizinha = 0


    def simbolo(self):
        if self.marcada and not self.revelada:
            return "F"
        if not self.revelada:
            return "."
        return "*" if self.tem_mina else (str(self.mina_vizinha) if self.mina_vizinha else " ")

class Tabuleiro:
    def __init__(self,n,minas):
        self.n = n
        self.grade = [[Celula() for i in range(n)] for j in range(n)]
        for i,j in minas:
            self.grade[i][j].tem_mina = True
        for i in range(n):
            for j in range(n):
                if not self.grade[i][j].tem_mina:
                    self.grade[i][j].mina_vizinha = sum(
                        self.grade[a][b].tem_mina for a, b in self.vizinha(i,j))
    def vizinhos(self,i,j):
        return [()]

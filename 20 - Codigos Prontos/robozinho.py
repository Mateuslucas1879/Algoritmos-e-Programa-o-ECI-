class robo:    

    def __init__(self, m):
        self.m = m
        self.r = "nao resolvido"

    def resolve(self):
        if self.r != "nao resolvido": return
        self.r = self.procura(0,0)
        if self.r == False:
            self.r = "nao tem solucao"

    def procura(self, i, j):
        if i < 0 or j < 0 or i >= len(self.m) or j >= len(self.m[0]) or self.m[i][j] == 1 :
            return False
        if  i == len(self.m)-1 and j == len(self.m[0])-1:
            return [(i,j)]
        self.m[i][j] = 1
        self.r = self.procura(i,j+1)
        if self.r != False:
            self.m[i][j] = 0
            return [(i,j)]+self.r
        self.r = self.procura(i+1,j)
        if self.r != False:
            self.m[i][j] = 0
            return [(i,j)]+self.r
        self.r = self.procura(i,j-1)
        if self.r != False:
            self.m[i][j] = 0
            return [(i,j)]+self.r
        self.r = self.procura(i-1,j)
        if self.r != False:
            self.m[i][j] = 0
            return [(i,j)]+self.r
        self.m[i][j] = 0
        return False
        
    def __repr__(self):
        return str(self.r)
        
a = robo([[0,1,0,0,0],[0,1,0,1,0],[0,1,0,1,0],[0,0,0,1,0]])

print(a)

a.resolve()

print(a)
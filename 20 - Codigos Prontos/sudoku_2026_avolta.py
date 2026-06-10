class Sudoku:
    def __init__(self,S):
        self.lu = S
        self.zeros = [(i,j) for i in range(9) for j in range(9) if self.lu[i][j] == 0]
        
    def candidatos(self,i,j):
        def luiz(i,j):
            z = (i//3)*3
            p = (j//3)*3
            return [self.lu[l][q] for l in range(z,z+3) for q in range(p,p+3)]

        cand = set([i for i in range(1,10)])
        cand = cand.difference(set(self.lu[i]))
        cand = cand.difference(set([self.lu[z][j] for z in range(9) ]))
        cand = cand.difference(set(luiz(i,j)))
        return cand
        
    def resolver(self):
        
        for i,j in self.zeros:
            if self.lu[i][j] == 0:
                #achar candidatos
                cand = self.candidatos(i,j)
                if cand == set(): return False
                #testar os candidatos
                for a in cand:
                    self.lu[i][j] = a
                    r = self.resolver()
                    # se achou retornar
                    if r != False: return True
                #caso contrario Erro
                self.lu[i][j] = 0
                return False
        return True
        
    def __repr__(self):
        r = "+---"*9+"+\n"
        for i in range(9):
            for j in range(9):
                r+= "| "+ str(self.lu[i][j] if self.lu[i][j] else " ")+" "
            r+="|\n"+"+---"*9+"+\n"
        return r
    
    def status(self):
        for i,j in self.zeros:
            if self.lu[i][j] == 0: return "Não resolvido PORRA!!!"
        return "Finalmente seu ..."
        for i,j in self.zeros:
            if self.lu[i][j] == 0:
                if self.candidatos(i,j) == set(): return "Errado seu burro!"
    
    def nsol(self):

        def cnt():
            for i,j in self.zeros:
                if self.lu[i][j] == 0:
                    n = 0
                    #achar candidatos
                    cand = self.candidatos(i,j)
                    if cand == set(): return False
                    #testar os candidatos
                    for a in cand:
                        self.lu[i][j] = a
                        r = self.resolver()
                        # se achou retornar
                        if r != False: n+=r
                    #caso contrario Erro
                    self.lu[i][j] = 0
                    return n
            return 1
        return cnt()
    
    def criar(self):
        pass

s = [[5,3,0,6,7,0,9,0,2],
[6,7,0,1,9,5,0,4,0],
[1,9,8,0,4,0,0,6,7],
[8,5,0,7,6,0,0,2,3],
[4,0,0,8,5,3,7,9,1],
[7,1,0,9,2,4,0,5,6],
[9,6,0,0,3,7,2,8,0],
[0,8,0,4,1,9,0,3,5],
[0,0,5,2,8,0,1,7,9]]

a = Sudoku(s)

print(a)

print(a.status())


print(a.nsol())

a.resolver()

print(a)

print(a.status())

print(a.nsol())
class sudoku():
    def __init__(self,inicio):
        self.tab = inicio
    
    def resolve(self):
        s = self.check() # 1 resolvido; 0 inv.; -1 resolvendo
        if s == 0: return False
        elif s == 1: return True
        
        for i in range(9):
            for j in range(9):
                if self.tab[i][j] == 0:
                    for k in self.candidatos(i,j):
                        self.tab[i][j] = k
                        if self.resolve() == True: return True
                    self.tab[i][j] = 0
                    return False
        
    def __repr__(self):
        s = ''
        a = self.tab
        for l in a:
            for e in l:
                if e == 0:
                    s += '  '
                else:
                    s += str(e)+' '
            s += '\n'
        return s
        
    def candidatos(self,i,j):
        if self.tab[i][j] != 0: return None
        c = [i for i in range(1,10)] 
        for k in range(0,9):
            s = self.tab[i][k]
            try:
                c.remove(self.tab[i][k])
            except ValueError:
                pass
            try:
                c.remove(self.tab[k][j])
            except ValueError:
                continue
        for k in self.quad(i,j):
            try:
                c.remove(k)
            except ValueError:
                continue
        return c
    
    def quad(self,i,j):
        c = []
        s = (i//3)*3
        p = (j//3)*3
        for k in range(0,3):
            for l in range(0,3):
                if self.tab[s+k][p+l] != 0:
                    c += [self.tab[s+k][p+l]]
        return c
        
    def check(self):
        # retorna 1 completo; 0 inviavel; -1 em aberto
        situacao = 1
        for i in range(9):
            for j in range(9):
                if self.tab[i][j] == 0:
                    cand = self.candidatos(i,j)
                    if len(cand) == 0: return 0
                    situacao = -1
        return situacao
    
p = sudoku([[5,3,0,0,7,0,0,0,0],
           [6,0,0,1,9,5,0,0,0],
           [0,9,8,0,0,0,0,6,0],
           [8,0,0,0,6,0,0,0,3],
           [4,0,0,8,0,3,0,0,1],
           [7,0,0,0,2,0,0,0,6],
           [0,6,0,0,0,0,2,8,0],
           [0,0,0,4,1,9,0,0,5],
           [0,0,0,0,8,0,0,7,9]])


#p = sudoku([[5,3,4,0,7,8,9,0,2],
#           [6,7,0,1,9,5,3,4,0],
#           [0,9,8,3,0,2,0,6,7],
#           [8,5,0,0,6,1,0,2,3],
#           [4,0,6,8,0,3,0,0,1],
#           [7,1,0,0,2,0,0,5,6],
#           [9,6,0,0,3,0,2,8,0],
#           [2,0,7,4,1,9,0,0,5],
#           [0,4,0,2,8,0,1,7,9]])


#print(p)
p.resolve()
print(p)

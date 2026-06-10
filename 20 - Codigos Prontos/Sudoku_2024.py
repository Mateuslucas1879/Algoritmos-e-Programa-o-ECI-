class Sudoku():
    def __init__(self,arq):
        if type(arq) != tuple: raise TypeError 
        s = set()
        for i in arq:
            if type(i) != tuple: raise TypeError
            if len(i) != 3: raise TypeError
            for a in i:
                if type(a) != int: raise TypeError
            a,b,c = i
            if a < 0 or b < 0 or c < 1: raise ValueError
            if a > 8 or b > 8 or c > 9: raise ValueError
            if i in s:
                raise ValueError
            s.add(i)
        self.__matriz = [[None]*9 for i in range(9)]
        #print(self.__matriz)
        for i,j,v in arq:
            self.__matriz[i][j] = v
        #print(self.__matriz)
    
    def __repr__(self):
        s = "-"*19+"\n"
        for i in range(9):
            s+="|"
            for j in range(9):
                if self.__matriz[i][j] == None:
                    s+=" |"
                else:
                    s+=str(self.__matriz[i][j])+"|"
            s+="\n"+"-"*19+"\n"
        return s
            
    def candidatos(self,i,j):
        if self.__matriz[i][j] != None: raise IndexError
        s = set([i for i in range(1,10)])
        for v in self.elinha(i):
            s.remove(v)
        for v in self.ecol(j):
            if v in s:
                s.remove(v)
        for v in self.equadra(i,j):
            if v in s:
                s.remove(v)
        return s
        
    
    def elinha(self,i):
        r = []
        for j in range(9):
            v = self.__matriz[i][j]
            if v != None: r+= [v]
        return r
        
    def ecol(self,j):
        r = []
        for i in range(9):
            v = self.__matriz[i][j]
            if v != None: r+= [v]
        return r
    
    def equadra(self,i,j):
        r = []
        l,p = 3*(i//3),3*(j//3)
        for k in range(3):
            for y in range(3):
                v = self.__matriz[k+l][y+p]
                if v != None: r+=[v]
        return r
    
    def status(self):
        full = True
        for i in range(9):
            for j in range(9):
                v = self.__matriz[i][j]
                if v == None: full = False
                else: self.__matriz[i][j] = None
                l = self.candidatos(i,j)
                if len(l) == 0: return "Inviável"
                if v != None: 
                    if not v in l: return "Inviável"
                self.__matriz[i][j] = v
        if full:
            return "Resolvido"
        else:
            return "Incompleto"
                
    
    def resolver(self):
        s = self.status()
        if s == "Resolvido": return True
        elif s == "Inviável": return False
        for i in range(9):
            for j in range(9):
                if self.__matriz[i][j] == None:
                    for v in self.candidatos(i,j):
                        self.__matriz[i][j] = v
                        if self.resolver(): return True
                    self.__matriz[i][j] = None
        return False
    
S = Sudoku(((0,0,5),(0,1,3),(0,4,7),(1,0,6),
(1,3,1),(1,4,9),(1,5,5),(2,1,9),(2,2,8),(2,7,6),
(3,0,8),(3,4,6),(3,8,3),(4,0,4),(4,3,8),(4,5,3),
(4,8,1),(5,0,7),(5,4,2),(5,8,6),(6,1,6),(6,6,2),
(6,7,8),(7,3,4),(7,4,1),(7,5,9),(7,8,5),(8,4,8),(8,7,7),
(8,8,9),(0,3,6),(0,8,2),(1,8,8),(2,0,1),(2,8,7),
(3,1,5),(3,7,2),(4,1,2),(4,7,9),(5,1,1),(5,7,5),
(6,0,9),(6,8,4),(7,0,2),(7,7,3),(8,0,3),(8,6,1),
(1,2,2),(2,3,3),(3,3,7),(4,2,6),(5,2,3),(6,2,1)))

print(S)

print(S.candidatos(0,2))
print(S.status())
#S.resolver()
print(S)
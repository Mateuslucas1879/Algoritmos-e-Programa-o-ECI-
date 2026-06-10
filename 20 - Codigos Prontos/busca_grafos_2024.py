class Grafo:
    def __init__(self,E):
        self.__E = set(E)
        self.__V = set()
        for i,j in self.__E:
            self.__V.add(i)
            self.__V.add(j)
        
    def __repr__(self):
        s = "G = ("
        return s+str(self.__V)+","+str(self.__E)+")"
        
    def busca_prof(self,init):
        visit = set()
        def bp(v,visit):
            if v in visit: return []
            visit.add(v)
            r = [v]
            for e in self.__E:
                if v in e:
                    if e[0] == v: i = e[1]
                    else: i = e[0]
                    r += bp(i,visit)
            return r
        return bp(init,visit)
                    
    def busca_larg(self,init):
        visit = set()
        def vizinhos(v,visit):
            vi = []
            for e in self.__E:
                if v in e:
                    if e[0] == v: i = e[1]
                    else: i = e[0]
                    if i in visit: continue
                    vi += [i]
            return vi
        pr = [init]
        r = []
        while pr != []:
            v = pr.pop(0)
            if v in visit: continue
            r += [v]
            visit.add(v)
            pr += vizinhos(v,visit)
        return r

G = Grafo([(1,2),(1,3),(2,4),(3,5),(4,5)])

print(G)
print(G.busca_prof(1))
print(G.busca_larg(1))
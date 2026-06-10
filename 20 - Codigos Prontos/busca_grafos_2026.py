def busca_prof(G,r):
    def buscp(G,r,ja):
        if ja[r-1]: return []
        ja[r-1] = 1
        s = [r]
        for v in G[r-1]:
            s+=buscp(G,v,ja)
        return s
    ja = [0 for i in range(len(G))]
    return buscp(G,r,ja)

def busca_lar(G,r):
    ja = [0 for i in range(len(G))]
    ja[r-1]=-1
    s = []
    fila = [r]
    while fila != []:
        v = fila.pop(0)
        if ja[v-1] != -1: raise IndexError
        ja[v-1] = 1
        s+=[v]
        for a in G[v-1]:
            if ja[a-1] == 0:
                fila +=[a]
                ja[a-1] = -1
    return s

G = [{2,3,4,5},{1,6},{1,6},{1,6},{1,6,7},{2,3,4,5},{5,8},{7,9,10},{8},{8}]
print(busca_prof(G,1))
print(busca_lar(G,1))
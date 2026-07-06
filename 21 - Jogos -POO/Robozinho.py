class Robozinho:
    def __init__(self, m):
        self.__m=m
        self.__r= "Nao resolvido"

    def resolve(self):
        if self.__r !="Nao resolvido":
            return
        resultado = self.__procurar(0,0)
        self.__r = "Nao solucao" if resultado is False else resultado

    def __procurar(self,x,y):
        if x < 0 or y < 0 or x >= len(self.__m) or y >= len(self.__m[0]) or self.__m[x][y]==1:
            return False

        if x == len(self.__m)-1 and y == len(self.__m[0])-1:
            return [(x,y)]

        self.__m[x][y]=1
        direcoes = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y), (x + 1, y - 1)]

        for proximo_x , proximo_y in direcoes:
            caminho_restante = self.__procurar(proximo_x,proximo_y)
            if caminho_restante is not False:
                self.__m[proximo_x][proximo_y]=0
                return [(x,y)] + caminho_restante

        self.__m[x][y] = 0
        return False

    def __repr__(self):
        return str(self.__r)

class SimuladorRobo:
    def __init__(self):
        self.__mapa = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0]
        ]
        self.__robo = Robozinho(self.__mapa)

    def executar(self):
        print("Status Inicial:", self.__robo)
        print("Calculando caminho com Backtracking...")
        self.__robo.resolve()
        print("Caminho Final :", self.__robo)

if __name__ == "__main__":
    SimuladorRobo().executar()
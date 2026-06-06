class Sinal:
    def __init__(self,n,v):
        self.n = n
        self.v = v
        self.resultado = []
        self.lista_plana()

    def lista_plana(self):
        if (isinstance(self.n, int) and self.n >= 1 and
            isinstance(self.v, (list,tuple)) and len(self.v) == self.n):


            self.resultado.append((self.n,self.v))
            return True
        else:
            return False


    def __mul__(self, other):
        pass



entrada = input().strip()
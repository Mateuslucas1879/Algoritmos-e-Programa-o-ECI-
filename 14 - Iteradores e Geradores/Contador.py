class ContadorPersonalizado:
    def __init__(self,limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self # o iterador retorna a si mesmo
    def __next__(self):
        if self.contador < self.limite:
            res = self.contador
            self.contador = self.contador + 1
            return res

        else:
            raise StopIteration # Sequencia Acabou

meu_contador  = ContadorPersonalizado(15)
for num in meu_contador:
    print(num)

"""
A Lista é o armazém cheio de caixas. O Iterador é o braço mecânico  que pega uma caixa por vez e coloca na frente do operário. 
O operário não precisa do armazém inteiro na frente dele, apenas da caixa que ele vai mexer agora.
"""
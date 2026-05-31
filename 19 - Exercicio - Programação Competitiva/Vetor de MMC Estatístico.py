class VetorMatematico(list):
    def mmc_pares(self):
        numero_validos = []

        for item in self:
            valor_float = float(item)
            if valor_float >= 1 and valor_float == int(valor_float):
                valor_int = int(valor_float)
                if valor_int not in numero_validos:
                    numero_validos.append(valor_int)

        if len(numero_validos) < 2:
            return ()

        def calcular_mdc(a,b):
            while b != 0:
                a, b = b, a % b
            return a

        def lista_ordenada(lista):
            num = len(lista)
            for i in range(num):
                for j in range(0, num - i - 1):
                    if lista[j] < lista[j + 1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]

            return lista

        resultado_mmc = []
        num = len(numero_validos)
        for i in range(num):
            for j in range(i +1 ,num):
                n1 = numero_validos[i]
                n2 = numero_validos[j]

                mdc = calcular_mdc(n1, n2)
                mmc = (n1 * n2) // mdc
                if mmc not in resultado_mmc:
                    resultado_mmc.append(mmc)



        resultado = lista_ordenada(resultado_mmc)
        return tuple(resultado)
v = VetorMatematico((4, 6, 3))
print(v.mmc_pares())
# Saída esperada: (12, 6)
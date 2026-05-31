class Vetor_Primos(list):
    def primos_gemeos(self):
        elemento_filtrados = []

        for item in self:
            valor_float = float (item)
            if valor_float >= 1 and valor_float == int(valor_float) :
                valor_int = int(valor_float)
                if valor_int not in elemento_filtrados:
                    elemento_filtrados.append(valor_int)

        def numeros_primos(num):
            if num <= 1:
                return False
            for divisor in range(2, num ):
                if num % divisor == 0:
                    return False
            return True




        def lista_ordenada(lista):
            num = len(lista)
            for i in range (num):
                for j in range (0, num - i - 1):
                    if lista[j] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]

            return lista

        resultado_primos = []
        num = len(elemento_filtrados)
        for i in range(num):
            for j in range (i +1, num):
                n1 = elemento_filtrados[i]
                n2 = elemento_filtrados[j]
                if numeros_primos(n1) and numeros_primos(n2) and abs(n2 - n1) == 2:
                    menor = n1 if n1 < n2 else n2
                    maior = n2 if n1 < n2 else n1
                    par = (menor, maior)

                    if par not in resultado_primos:
                        resultado_primos.append(par)

        resultado = lista_ordenada(resultado_primos)
        return resultado


v = Vetor_Primos((5, 3, 7, "11", 12, 5))
print(v.primos_gemeos())

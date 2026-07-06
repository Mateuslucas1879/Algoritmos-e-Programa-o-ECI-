class Vetor(list):
   def mdc(self):
       elemento = []

       for item in self:
           valor_float = float(item)
           if valor_float > 0 and valor_float == int(valor_float):
               valor_int = int(valor_float)
               if not valor_int in elemento:
                   elemento.append(valor_int)

       if len(elemento) < 2:
           return ()

       def calcular_mdc(a,b):
           while b != 0:
               a, b = b , a % b
           return a


       def ordena(lista):
           n = len(lista)
           for i in range(n):
               for j in range(0 , n - i -1):
                   if lista[j] > lista[j + 1]:
                       lista[j], lista[j + 1] = lista[j + 1], lista[j]

           return lista

       resultado_mdc = []
       n = len(elemento)
       for i in range(n):
           for j in range(i+1,n):
               rss = calcular_mdc(elemento[i],elemento[j])
               if res not in resultado_mdc:
                   resultado_mdc.append(res)

       resultado_ordenado = ordena(resultado_mdc)
       return  tuple(resultado_ordenado)



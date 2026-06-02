class MatrizFatorial(list):
    def fatorial_unico(self):
        numeros_validos = []

        for sublista in self:
            for numero in sublista:
                try:
                    valor_float = float(numero)
                    if valor_float >= 0 and valor_float == int(valor_float):
                        valor_int = int(valor_float)
                        if valor_int not in numeros_validos:
                            numeros_validos.append(valor_int)
                except (ValueError, TypeError):
                    continue


        if len(numeros_validos) == 0:
            return []

        def lista_ordenada(lista):
            num = len(lista)
            for i in range (num):
                for j in range (0, num - i - 1):
                    if lista[j] < lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]

            return lista

        def matriz_fatorial(n):
            if n == 0 or n == 1:
                return 1
            return n * matriz_fatorial(n - 1)

        resultado_fatorial = []
        for n in numeros_validos:
            fatorial = matriz_fatorial(n)
            if fatorial not in resultado_fatorial:
                resultado_fatorial.append(fatorial)

        resultado = lista_ordenada(resultado_fatorial)
        return resultado


m = MatrizFatorial([[3, '4.0'], [3, -2], ['texto', 0]])
print(m.fatorial_unico())
# Saída: [24, 6, 1]
class ConjuntoFibonacci(list):
    def filtrar_fibonacci(self):
        numero_verificados = []

        for numero in self:
                try:
                    valor_float = float(numero)
                    if valor_float >= 0 and valor_float == int(valor_float):
                        valor_int = int(valor_float)
                        if valor_int not in numero_verificados:
                            numero_verificados.append(valor_int)

                except ValueError:
                    continue

        if len(numero_verificados) == 0:
            return ()

        def lista_ordenada(lista):
            num = len(lista)
            for i in range (num):
                for j in range(0, num - i -1):
                    if lista[j] > lista[j + 1]:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]

            return lista


        maior_numero = numero_verificados[0]
        for num in numero_verificados:
            if num > maior_numero:
                maior_numero = num

        sequencia_fibonacci = [0,1]
        while sequencia_fibonacci[-1] < maior_numero:
            proximo = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
            sequencia_fibonacci.append(proximo)


        resultado_fibonacci = []
        for n in  numero_verificados:
            pertence = False
            for f in sequencia_fibonacci:
                if n == f:
                    pertence = True
                    break
            if pertence and n not in resultado_fibonacci:
                resultado_fibonacci.append(n)

        resultado = lista_ordenada(resultado_fibonacci)
        return tuple(resultado)


f = ConjuntoFibonacci([5, '1.0', 8, 1, 4, 13.0])
print(f.filtrar_fibonacci())
# Saída exata: (1, 5, 8, 13)
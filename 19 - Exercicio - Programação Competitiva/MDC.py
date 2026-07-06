class Vetor(list):
    # Passo 1: Como herdamos de 'list', precisamos receber os elementos no __init__
    def __init__(self, elementos):
        # Passa os elementos para a lista mãe inicializar
        super().__init__(elementos)
    def mdc(self):
        lista_limpa = []
        for elemento in self:
            try:
                num =float(elemento)
                if num > 0 and num.is_integer():
                    inteiro_num = int(num)
                    if inteiro_num not in lista_limpa:
                        lista_limpa.append(inteiro_num)
            except (ValueError, TypeError):
                continue
        # Se não tiver pelo menos 2 números válidos, não dá para fazer par
        if len(lista_limpa) < 2:
            return ()
        lista = []
        # Esse duplo loop serve para combinar todos os números de dois em dois
        for i in range(len(lista_limpa)):
            for j in range(i + 1,len(lista_limpa)):
                a = lista_limpa[i]
                b = lista_limpa[j]
                while b != 0:
                    a ,b = b , a % b

                # O resultado do MDC fica salvo na variável 'a' após o loop
                # Regra: MDCs duplicados aparecem apenas uma vez
                if a not in lista:
                    lista.append(a)


    # --- SEU BLOCO 4: Ordenação manual (Bubble Sort) ---
    # Ordenando a lista 'mdcs_encontrados' na raça
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return tuple(lista)

entrada_usuario = input()
# Remove parênteses ou colchetes das pontas e separa por vírgula
elementos_limpos = entrada_usuario.replace('(', '').replace(')',"").replace('[',"").replace(']',"").split(",")
# Limpa as aspas e os espaços em branco de cada item
tupla_final = [item.strip().strip('"').strip('.') for item in elementos_limpos if item.strip()]

meu_vetor = Vetor(tupla_final)
print(meu_vetor.mdc())


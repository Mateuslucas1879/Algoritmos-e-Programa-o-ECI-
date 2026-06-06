class ImagemRLE:
    def __init__(self, w, h,lista):
        self.w = w
        self.h = h
        self.lista = lista
        self.imagem = []
        self.validador()

    def validador(self):
        if((isinstance(self.w, int) and self.w >= 1 and
           isinstance(self.h, int)) and self.h >= 1 and
           isinstance(self.lista, (list,tuple)) and len(self.lista) == self.w * self.h and
           all(0 <= x <= 255 for x in self.lista)):

           self.imagem.append((self.w, self.h, self.lista))
           return True
        else:
            return False


    def __invert__(self):
        # Se a lista estiver vazia, não há o que comprimir
        if not self.lista:
            return ""

        animacoes_compactadas = []
        numero_atual = self.lista[0]
        contador = 1


        # Começamos a olhar a partir do segundo elemento (índice 1)
        for i in range(1, len(self.lista)):
            if self.lista[i] == numero_atual:
                # Se for igual, só aumenta o contador
                contador += 1
            else:
                # Se mudou, guarda o grupo anterior no formato "3x0"
                animacoes_compactadas.append(f"{contador} x{numero_atual}")
                # Atualiza o número que estamos vigiando e reseta o contador
                numero_atual = self.lista[i]
                contador = 1
        # ATENÇÃO: Quando o loop acaba, falta salvar o último número que estava sendo contado!
        animacoes_compactadas.append(f"{contador} x{numero_atual}")
        # Junta tudo usando vírgula como separador
        return ",".join(animacoes_compactadas)

    def ___repr__(self):
        matriz_visualizacao = []
        # O loop começa em 0, vai até o fim da lista, mas PULA de self.w em self.w
        for x in range(0,len(self.lista),self.w):
            # Corta a lista do ponto x até x + largura
            linha = self.lista[x:x+self.w]
            # Adiciona essa linha na nossa matriz
            matriz_visualizacao.append(linha)
        return str(matriz_visualizacao).replace(" ","")



entrada = input().strip()

if entrada.endswith("~"):
    text_matriz = entrada.replace("~","")
    operacao = "Comprimir"
else:
    text_matriz = entrada
    operacao = "Decomprir"

text_limpo = text_matriz.replace("(","").replace(")","").replace("]","")
dados = [int(x) for x in text_limpo.split(",")]

imagem = ImagemRLE(dados[0],dados[1],dados[2:])

if operacao == "Comprir":
    print(~imagem)
else:
    print(imagem)






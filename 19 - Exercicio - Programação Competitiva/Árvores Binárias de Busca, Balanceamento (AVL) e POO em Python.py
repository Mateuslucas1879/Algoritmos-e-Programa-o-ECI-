class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
        self.altura = 1

    def __str__(self):
        return str(self.valor)


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    # --- MÉTODOS AUXILIARES DE ENCAPSULAMENTO ---
    def get_altura(self,no):
        if not no:
            return 0
        return no.altura
    def get_fator_balanceamento(self,no):
        if not no:
            return 0
        # Fator = Altura da Esquerda - Altura da Direita
        return self.get_altura(no.esquerdo) - self.get_altura(no.direito)

    # --- MÉTODOS DE ROTAÇÃO (Ajuste de Ponteiros de Objetos) ---
    def rotacionar_direita(self,y):
        x = y.esquerdo
        T2 = x.direito

        # Executa a rotação reconectando as referências dos objetos
        x.direito = y
        y.esquerdo = T2

        # Atualiza as alturas dos nós afetados
        y.altura = 1 + max(self.get_altura(y.esquerdo), self.get_altura(y.direito))
        x.altura = 1 + max(self.get_altura(x.esquerdo), self.get_altura(x.direito))
        return x

    def rotacionar_esquerda(self,x):
        y = x.direito
        T2 = y.close if hasattr(y, 'close') else y.esquerdo

        y.esquerdo = x
        x.direito = T2
        

        x.altura = 1 + max(self.get_altura(x.esquerdo), self.get_altura(x.direito))
        y.altura = 1 + max(self.get_altura(y.esquerdo), self.get_altura(y.direito))
        return y

    def inserir(self,valor):
        self.raiz = self.inserir_recurso(self.raiz, valor)

    def inserir_recurso(self,no_atual,valor):
        if not no_atual:
            return No(valor)

        if valor < no_atual.valor:
            no_atual.esquerdo = self.inserir_recurso(no_atual.esquerdo, valor)
        elif valor > no_atual.valor:
            no_atual.direito = self.inserir_recurso(no_atual.direito, valor)
        else:
            return no_atual

        no_atual.altura = 1 + max(self.get_altura(no_atual.esquerdo), self.get_altura(no_atual.direito))

        balanceamento = self.get_fator_balanceamento(no_atual)

        if balanceamento > 1 and valor < no_atual.esquerdo.valor:
            return self.rotacionar_direita(no_atual)

        if balanceamento < -1 and valor > no_atual.direito.valor:
            return self.rotacionar_esquerda(no_atual)

        if balanceamento > 1 and valor > no_atual.esquerdo.valor:
            no_atual.esquerdo = self.rotacionar_esquerda(no_atual.esquerdo)
            return self.rotacionar_direita(no_atual)

        if balanceamento < -1 and valor < no_atual.direito.valor:
            no_atual.direito = self.rotacionar_direita(no_atual.direito)
            return self.rotacionar_esquerda(no_atual)
        return no_atual

    def buscar(self,alvo):
        return self._buscar_recursivo(self.raiz, alvo)

    def _buscar_recursivo(self,no_atual,alvo):
        if not no_atual:
            return False
        if alvo == no_atual.valor:
            return True

        if alvo < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerdo, alvo)
        return self._buscar_recursivo(no_atual.direito, alvo)

    def exibir_ordem(self):
        elementos = []
        self.ordem_recursivo(elementos, self.raiz)
        return elementos

    def ordem_recursivo(self,elementos,no_atual):
        if no_atual:
            self.ordem_recursivo(elementos, no_atual.esquerdo)
            elementos.append(no_atual.valor)
            self.ordem_recursivo(elementos, no_atual.direito)


# --- TESTANDO A ESTRUTURA ORIENTADA A OBJETOS ---
if __name__ == "__main__":
    arvore = ArvoreAVL()

    dados = [10, 20, 30, 40, 50, 25]

    for d in dados:
        arvore.inserir(d)

    print("--- Teste de Busca Binária ---")
    print(f"Busca pelo 30: {arvore.buscar(30)}")  # True
    print(f"Busca pelo 99: {arvore.buscar(99)}")  # False

    print("\n--- Teste de Ordenação Natural (Percurso Em-Ordem) ---")
    # A árvore extrai os dados perfeitamente ordenados
    print(arvore.exibir_ordem())

    print(f"\nA raiz atual da árvore é: {arvore.raiz} (Se não fosse balanceada, a raiz seria 10)")




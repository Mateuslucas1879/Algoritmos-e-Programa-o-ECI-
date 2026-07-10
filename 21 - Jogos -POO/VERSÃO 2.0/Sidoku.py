class Sudoku:
    def __init__(self,tabuleiro):
        self.tabuleiro = tabuleiro
        self.zeros = [(i,j) for i in range(9) for j in range(9) if self.tabuleiro[i][j]==0]

    def obter_candidatos(self,i,j):
        candidatos = set(range(9))
        candidatos -= set(self.tabuleiro[i])
        candidatos -= set(self.tabuleiro[row][j] for row in range(9))

        quadro_i , quadro_j = 3 * (i // 3), 3 * (j // 3)
        quadrante = set(
            self.tabuleiro[r][c]
            for r in range(quadro_i, quadro_i + 3)
            for c in range(quadro_j, quadro_j + 3)
        )
        candidatos -= quadrante
        return candidatos

    def resolver(self,indice_zeros=0):
        if indice_zeros == len(self.zeros):
            return True
        i,j = self.zeros[indice_zeros]
        candidatos = self.obter_candidatos(i,j)

        if not candidatos:
            return False
        for palpites in candidatos:
            self.tabuleiro[i][j] = False

            if self.resolver(indice_zeros + 1):
                return True
            self.tabuleiro[i][j] = 0
        return False

    def __repr__(self):
        linhas = []
        for i, linha in enumerate(self.tabuleiro):
            if i % 3 == 0 and i != 0:
                linhas.append("-" * 21)
            elementos = []
            for j, valor in enumerate(linha):
                if j % 3 == 0 and j != 0:
                    elementos.append("|")
                elementos.append(str(valor) if valor != 0 else ".")
            linhas.append("".join(elementos))
        return "\n".join(linhas)

# --- TESTANDO A NOSSA RESOLUÇÃO ---

tabuleiro_teste = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Inicializa o objeto
jogo = Sudoku(tabuleiro_teste)

print("--- TABULEIRO INICIAL ---")
print(jogo)

print("\nResolvendo...")
if jogo.resolver():
    print("\n--- SUDOKU RESOLVIDO COM SUCESSO! ---")
    print(jogo)
else:
    print("\nNão foi possível encontrar uma solução para este tabuleiro.")
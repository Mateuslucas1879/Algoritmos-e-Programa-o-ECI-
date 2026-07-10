class CampoMinado:
    def __init__(self,tabuleiro):
        self.tabuleiro = tabuleiro
        self.linhas = len(tabuleiro)
        self.colunas = len(tabuleiro[0])
        self.desconhecidos = [(i,j) for i in range(self.linhas) for j in range(self.colunas)
                              if self.tabuleiro[i][j] == -1]
    def obter_candidatos(self,i,j):
        candidatos = {"B",0}
        for palpite in list(candidatos):
            self.tabuleiro[i][j] = palpite

            for dj in [-1,0,1]:
                for di in [-1,0,1]:
                    ni,nj = i + di, j + dj

                    if 0 <= ni < self.linhas and 0 <= nj < self.colunas and isinstance(self.tabuleiro[ni][nj], int) and self.tabuleiro[ni][nj] > 0:
                        bombas_redor = 0
                        fechados_redor = 0

                        for v_di in [-1,0,1]:
                            for v_dj in [-1,0,1]:
                                v_ni, v_nj = ni + v_di, nj + v_dj
                                if 0 <= v_ni < self.linhas and 0 <= v_nj < self.colunas:
                                    if self.tabuleiro[v_ni][v_nj] == "B":
                                        bombas_redor += 1
                                    elif self.tabuleiro[v_ni][v_nj] == -1:
                                        fechados_redor += 1

                        if bombas_redor > self.tabuleiro[ni][nj] or (bombas_redor + fechados_redor) <self.tabuleiro[ni][nj]:
                            candidatos.discard(palpite)

            self.tabuleiro[i][j] = -1
        return candidatos

    def resolver(self, indice_deconhecidos=0):
        if indice_deconhecidos == len(self.desconhecidos):
            return True
        i,j = self.desconhecidos[indice_deconhecidos]
        candidates = self.obter_candidatos(i,j)

        if not candidates:
            return False
        for palpite in candidates:
            self.tabuleiro[i][j] = palpite
            if self.resolver(indice_deconhecidos + 1):
                return True

            self.tabuleiro[i][j] = -1
        return False

tabuleiro_entrada = eval(input())
jogo = CampoMinado(tabuleiro_entrada)

if jogo.resolver():
    print(jogo.tabuleiro)
else:
    print("Sem Solução")
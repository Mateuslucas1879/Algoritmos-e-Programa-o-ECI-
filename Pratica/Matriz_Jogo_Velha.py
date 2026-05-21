# 1. Cria o tabuleiro como uma matriz 3x3 preenchida com espaços em branco
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def desenhar_tabuleiro():
    print("\n")
    for i in range(3):
        # Junta os elementos da linha com uma barra vertical
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("---|---|---")
    print("\n")

# Função para verificar se alguém ganhou
def verificar_vencedor():
    # Verifica linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True
    # Verifica colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == ... == tabuleiro[2][j] != " ":
            return True
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True
    return False


# --- Fluxo Principal do Jogo ---
jogador_atual = "X"
jogadas = 0

print("=== JOGO DA VELHA MATRICIAL ===")

while jogadas < 9:
    desenhar_tabuleiro()
    print(f"Turno do jogador: {jogador_atual}")

    # Pede a posição na matriz (0, 1 ou 2)
    linha = int(input("Escolha a linha (0, 1 ou 2): "))
    coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

    # Valida se a jogada está dentro dos limites da matriz
    if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
        print("[Erro] Posição inválida! Escolha números de 0 a 2.")
        continue

    # Verifica se a posição da matriz já está ocupada
    if tabuleiro[linha][coluna] != " ":
        print("[Erro] Essa posição já está ocupada! Tente outra.")
        continue

    # Preenche a matriz com a marca do jogador atual
    tabuleiro[linha][coluna] = jogador_atual
    jogadas += 1

    # Verifica se a jogada foi vitoriosa
    if verificar_vencedor():
        desenhar_tabuleiro()
        print(f"Parabéns! O jogador '{jogador_atual}' venceu o jogo!")
        break

    # Alterna o jogador
    jogador_atual = "O" if jogador_atual == "X" else "X"
else:
    desenhar_tabuleiro()
    print("Deu velha! O tabuleiro ficou cheio e ninguém venceu.")
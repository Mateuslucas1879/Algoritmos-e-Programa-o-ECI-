# 1. Inicia a matriz 3x3 vazia
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"
jogadas = 0
vencedor = False

# 2. Loop principal do jogo (máximo 9 rodadas)
while jogadas < 9 and not vencedor:
    # Mostra a matriz na tela de forma simples
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    print(f"Vez de: {jogador}")

    # Recebe as coordenadas da matriz
    linha = int(input("Linha (0, 1, 2): "))
    coluna = int(input("Coluna (0, 1, 2): "))

    # Se a posição estiver vazia, aceita a jogada
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        jogadas += 1

        # 3. ALGORITMO DE VALIDAÇÃO (Checa se o jogador atual ganhou)
        # Testa as 3 linhas
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == jogador:
            vencedor = True
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == jogador:
            vencedor = True
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == jogador:
            vencedor = True
        # Testa as 3 colunas
        elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == jogador:
            vencedor = True
        elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == jogador:
            vencedor = True
        elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == jogador:
            vencedor = True
        # Testa as 2 diagonais
        elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
            vencedor = True
        elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
            vencedor = True

        # Se alguém ganhou, encerra o loop antes de trocar de jogador
        if vencedor:
            print(f"\nFim de jogo! O jogador {jogador} ganhou!")
            break

        # Alterna o turno entre X e O
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
    else:
        print("Essa posição já está ocupada! Tente novamente.")

# Se o loop terminar por falta de jogadas e ninguém venceu
if not vencedor:
    print("\nFim de jogo! Deu velha (empate).")

# Mostra o estado final da matriz
print(tabuleiro[0])
print(tabuleiro[1])
print(tabuleiro[2])
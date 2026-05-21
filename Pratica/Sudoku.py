# Tabuleiro estático inicial (0 representa casas vazias)
TABULEIRO_INICIAL = [
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


def formatar_tabuleiro(tabuleiro):
    """Renderiza a matriz na tela usando divisores visuais."""
    linhas_texto = []
    for i, linha in enumerate(tabuleiro):
        if i % 3 == 0 and i != 0:
            linhas_texto.append("-" * 21)

        linha_formatada = []
        for j, num in enumerate(linha):
            if j % 3 == 0 and j != 0:
                linha_formatada.append("|")
            linha_formatada.append(str(num) if num != 0 else ".")
        linhas_texto.append(" ".join(linha_formatada))
    return "\n".join(linhas_texto)


def eh_valido(tabuleiro, num, pos_linha, pos_col):
    """Aplica a lógica das três regras fundamentais do Sudoku."""
    # 1. Validação da Linha
    for j in range(9):
        if tabuleiro[pos_linha][j] == num and pos_col != j:
            return False

    # 2. Validação da Coluna
    for i in range(9):
        if tabuleiro[i][pos_col] == num and pos_linha != i:
            return False

    # 3. Validação do Quadrante 3x3
    # Divide a coordenada por 3 usando divisão inteira para achar o bloco correto
    quad_x = pos_col // 3
    quad_y = pos_linha // 3

    for i in range(quad_y * 3, quad_y * 3 + 3):
        for j in range(quad_x * 3, quad_x * 3 + 3):
            if tabuleiro[i][j] == num and (i, j) != (pos_linha, pos_col):
                return False

    return True


def encontrar_vazio(tabuleiro):
    """Varre a matriz buscando a próxima casa com 0."""
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                return i, j  # Retorna tupla (linha, coluna)
    return None


def checar_vitoria(tabuleiro):
    """Garante que o tabuleiro está completamente preenchido e correto."""
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0 or not eh_valido(tabuleiro, tabuleiro[i][j], i, j):
                return False
    return True


def jogar():
    # Cria uma cópia da matriz inicial para manipulação em memória
    tabuleiro = [linha[:] for linha in TABULEIRO_INICIAL]

    print("=== SUDOKU PURAMENTE ALGORÍTMICO ===")
    print("Regras: Digite as coordenadas de 1 a 9.")
    print("Para remover um número inserido por você, digite 0 no valor.\n")

    while True:
        print("\n" + formatar_tabuleiro(tabuleiro) + "\n")

        if checar_vitoria(tabuleiro):
            print("Parabéns! Validação completa. Tabuleiro resolvido com sucesso!")
            break

        try:
            linha_input = int(input("Escolha a linha (1-9): ")) - 1
            col_input = int(input("Escolha a coluna (1-9): ")) - 1
            num = int(input("Digite o número (1-9) ou 0 para limpar: "))

            # Valida limites de índices da matriz
            if not (0 <= linha_input <= 8 and 0 <= col_input <= 8):
                print("[Erro] Posição fora do limite do tabuleiro.")
                continue

            # Bloqueia alteração nos números fixos baseados na matriz original
            if TABULEIRO_INICIAL[linha_input][col_input] != 0:
                print("[Erro] Você não pode alterar as pistas originais do tabuleiro!")
                continue

            if not (0 <= num <= 9):
                print("[Erro] O valor deve ser de 0 a 9.")
                continue

            # Executa a ação do jogador
            if num == 0:
                tabuleiro[linha_input][col_input] = 0
                print("[Sucesso] Casa limpa.")
            else:
                # O algoritmo valida se a jogada é válida antes de aplicar à matriz
                if eh_valido(tabuleiro, num, linha_input, col_input):
                    tabuleiro[linha_input][col_input] = num
                    print("[Sucesso] Número posicionado.")
                else:
                    print("[Aviso] Movimento inválido! Conflito na linha, coluna ou bloco 3x3.")

        except ValueError:
            print("[Erro] Insira apenas números inteiros válidos.")


if __name__ == "__main__":
    jogar()
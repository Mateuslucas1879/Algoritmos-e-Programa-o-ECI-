# Tabuleiro 4x4 (0 é a casa vazia)
tabuleiro = [
    [1, 0, 3, 4],
    [0, 4, 1, 0],
    [0, 3, 4, 0],
    [4, 1, 0, 3]
]

# Copiamos o tabuleiro para saber o que não pode ser alterado
original = [linha[:] for linha in tabuleiro]

print("=== SUDOKU MINI 4x4 ===")
print("Preencha o tabuleiro usando números de 1 a 4.")

while True:
    # Mostra o tabuleiro na tela de forma simples
    for linha in tabuleiro:
        print(linha)

    # Condição de vitória: se não houver mais nenhum 0, o jogador venceu
    if not any(0 in linha for linha in tabuleiro):
        print("\nParabéns! Você completou o tabuleiro!")
        break

    # Coleta as entradas do usuário
    l = int(input("\nEscolha a Linha (1-4): ")) - 1
    c = int(input("Escolha a Coluna (1-4): ")) - 1
    v = int(input("Digite o Valor (1-4): "))

    # Lógica de proteção: não deixa alterar os números que começaram no jogo
    if original[l][c] != 0:
        print("[Erro] Você não pode alterar os números originais!")
    elif v < 1 or v > 4:
        print("[Erro] Escolha um valor apenas entre 1 e 4!")
    else:
        # Insere o número diretamente na matriz
        tabuleiro[l][c] = v
        print("[Sucesso] Número inserido!")
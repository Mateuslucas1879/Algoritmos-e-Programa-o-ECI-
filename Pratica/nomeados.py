def criar_perfil(**dados):
    print("\nPERFIL CRIANDO")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


criar_perfil(nome = "Dara", idade = "24", cidade = "Carlos Chargas")
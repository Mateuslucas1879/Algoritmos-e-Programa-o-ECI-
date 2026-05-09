# 1. Base de dados (Lista de Dicionários)
usuarios = [
    {'nome': 'Lucas', 'idade': 26},
    {'nome': 'Mateus', 'idade': 26},
    {'nome': 'Dara', 'idade': 24}
]

print("="*30)
print(f"{'SISTEMA DE USUÁRIOS':^30}")
print("="*30)

# 2. Manipulação de Cópia (Shallow Copy)
# Criamos uma cópia do primeiro usuário para não alterar o original
print("\n[INFO] Manipulando cópia do primeiro usuário...")
copia = usuarios[0].copy()
del copia['nome']
print(f"Cópia após deletar 'nome': {copia}")
print(f"Original permanece intacto: {usuarios[0]}")

# 3. Iterando sobre itens de um dicionário específico
print("\n[DETALHES] Chaves e Valores do primeiro usuário:")
for chave, valor in usuarios[0].items():
    print(f" - {chave.capitalize()}: {valor}")

# 4. Extraindo valores globais (List Comprehension)
# Aqui pegamos apenas as idades de todo mundo
idades = [pessoa['idade'] for pessoa in usuarios]
print(f"\n[LISTAGEM] Idades registradas: {idades}")

# 5. Terminal Organizado (Exibição Final)
print("\n" + "-"*30)
print(f"{'NOME':<15} | {'IDADE':>7}")
print("-"*30)

for item in usuarios:
    print(f"{item['nome']:<15} | {item['idade']:>7} anos")

print("-"*30)
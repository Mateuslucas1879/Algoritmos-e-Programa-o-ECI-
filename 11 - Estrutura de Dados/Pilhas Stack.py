pilha = []
print(f'\nPilhas Inicial: {pilha}')

pilha.append("A")
pilha.append("B")
pilha.append("C")
print(f'\nPilhas Final: {pilha}')


topo = pilha[-1]
print(f"Elemento no topo: {topo}")

elemento_removido = pilha.pop()
print(f"Elemento removido: {elemento_removido}")
print(f"Pilha pos pop: {pilha}")
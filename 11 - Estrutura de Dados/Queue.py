from collections import deque

fila_eficiente = deque()
print(f"Fila eficiente: {fila_eficiente}")

fila_eficiente.appendleft('P')
fila_eficiente.appendleft('Q')
fila_eficiente.appendleft('R')

elemento_removido = fila_eficiente.popleft()
print(f"Elemento removido: {elemento_removido}")
print(f"Fila eficiente apos dequeue: {fila_eficiente}")
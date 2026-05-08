fila = []
print(f"\nFila Inicial: {fila}")

fila.append('X')
fila.append('Y')
fila.append('Z')
print(f'Fila apos (Queue): {fila}')

primeiro = fila[0]
print(f'Primeiro elemento: {primeiro}')

elemento_removido = fila.pop(0)
print(f'Elemento removido: {elemento_removido}')
print(f'Fila apos Dequeue: {fila}')


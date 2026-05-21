def inverter_matriz(m):
    det = (m[0][0] + m[1][1] - m[0][1] - m[1][0])
    if det == 0:
        return None

    return [
        [m[1][1] / det, -m[0][1] / det],
        [-m[1][0] / det, m[0][0] / det]
    ]

minha_matriz = [[4, 7], [2, 6]]
resultado = inverter_matriz(minha_matriz)

if resultado is None:
    print("A matriz nao tem inversa")
else:
    print(f"Matriz inversa: ")
    for linha in resultado:
        print([f"{x:.2f}" for x in list(linha)])
def calcular_det_1(matriz):
    # Proteção caso a matriz 1x1 venha como lista simples [5] ou número puro 5
    if isinstance(matriz, list) and isinstance(matriz[0], list):
        return matriz[0][0]
    elif isinstance(matriz, list):
        return matriz[0]
    return matriz


def calcular_det_2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]


def calcular_det_3(matriz):
    # A lógica de desempacotamento
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]
    return (a * e * i + b * f * g + c * d * h) - (a * f * h + b * d * i + c * e * g)


def main():
    print("=== CALCULADORA DE DETERMINANTE (n <= 3) ===")
    print("Escolha o tamanho da matriz quadrada (1, 2 ou 3):")

    try:
        n = int(input("Tamanho: "))
        if n not in [1, 2, 3]:
            print("Erro: O tamanho digitado deve ser obrigatoriamente 1, 2 ou 3.")
            return

        print("\nAgora, digite a matriz no formato de listas do Python.")
        print("Exemplos de como preencher:")
        print("  Para tamanho 1: [[5]]")
        print("  Para tamanho 2: [[1, 2], [3, 4]]")
        print("  Para tamanho 3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")

        matriz = eval(input("Matriz: "))

        # Validação básica para garantir que o usuário não digitou um número solto para tamanho 2 ou 3
        if n > 1 and (not isinstance(matriz, list) or not isinstance(matriz[0], list)):
            print("\nErro: Formato inválido. Lembre-se de usar os colchetes corretamente.")
            return

        # Dicionário mapeando as funções exigidas pelo enunciado
        funcoes_det = {
            1: calcular_det_1,
            2: calcular_det_2,
            3: calcular_det_3
        }

        resultado = funcoes_det[n](matriz)
        print(f"\nO determinante da matriz é: {resultado}")

    except Exception as e:
        print(f"\nOcorreu um erro no preenchimento dos dados. Verifique a sintaxe. ({e})")


if __name__ == "__main__":
    main()

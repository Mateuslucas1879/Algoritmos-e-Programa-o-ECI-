---

# 🚀 Algoritmos e Linguagens de Programação

Este repositório é um guia completo sobre fundamentos de programação, estruturas de dados e manipulação de fluxos. O objetivo é servir como material de consulta para o desenvolvimento de software eficiente e organizado.

## 📌 Sumário
* [🧵 Manipulação de Strings](#-manipulação-de-strings)
* [✂️ Listas e Fatiamento (Slicing)](#-listas-e-fatiamento-slicing)
* [📊 Matrizes e Determinantes](#-matrizes-e-determinantes)
* [⚙️ Funções e Escopo](#-funções-e-escopo)
* [📉 Complexidade de Algoritmos (Big O)](#-complexidade-de-algoritmos-big-o)

---

## 🧵 Manipulação de Strings

Strings são cadeias de caracteres. Abaixo, os métodos essenciais para tratamento de texto:

*   **`strip()`**: Remove espaços em branco (ou caracteres indesejados) do início e do fim.
*   **`upper()` / `lower()`**: Padroniza o texto em maiúsculas ou minúsculas.
*   **`split(separador)`**: Quebra uma string em uma lista de partes baseada em um delimitador (ex: espaço ou vírgula).
*   **`join(iterável)`**: O inverso do split; une elementos de uma lista em uma única string usando um conector.
*   **`replace(antigo, novo)`**: Substitui ocorrências de um caractere ou palavra por outra.
*   **`capitalize()`**: Deixa apenas a primeira letra da string em maiúscula.

---

## ✂️ Listas e Fatiamento (Slicing)

O fatiamento permite acessar subconjuntos de dados em listas ou strings sem a necessidade de loops.

**Sintaxe:** `[início : fim : passo]`

*   **Início:** Índice de partida (inclusivo).
*   **Fim:** Índice de parada (exclusivo).
*   **Passo:** O intervalo de salto entre os índices.

**Exemplos Práticos:**
```python
numeros = [10, 20, 30, 40, 50, 60]

# Pega do índice 1 ao 3
print(numeros[1:4])     # [20, 30, 40]

# Pega todos os itens pulando de 2 em 2
print(numeros[::2])     # [10, 30, 50]

# Inverte a lista completa
print(numeros[::-1])    # [60, 50, 40, 30, 20, 10]
```

---

## 📊 Matrizes e Determinantes

Uma **Matriz** é uma coleção bidimensional (linhas e colunas). Na programação, implementamos como "listas de listas".

### Representação:
```python
matriz = [
    [1, 2],
    [3, 4]
]
```

### Determinantes
O determinante é um valor numérico que reflete certas propriedades de uma matriz quadrada.
*   **Cálculo (Matriz 2x2):** Multiplicamos os elementos da diagonal principal e subtraímos o produto da diagonal secundária.
    *   $det(A) = (a_{11} \times a_{22}) - (a_{12} \times a_{21})$

---

## ⚙️ Funções e Escopo

Funções são blocos de código que executam uma tarefa quando chamados. Elas promovem a **modularização** do sistema.

1.  **Definição:** Criação da lógica com parâmetros de entrada.
2.  **Execução:** Chamada da função passando os argumentos necessários.
3.  **Retorno:** O valor que a função devolve para quem a chamou (usando `return`).

> **Importante:** O **Escopo** define onde uma variável vive. Variáveis criadas dentro de uma função são **locais** e não existem fora dela.

---

## 📉 Complexidade de Algoritmos (Big O)

A eficiência de um algoritmo é medida pela notação Big O, que descreve como o tempo de execução ou uso de memória cresce conforme o volume de dados ($n$) aumenta.

| Complexidade | Nome | Descrição |
| :--- | :--- | :--- |
| **O(1)** | Constante | A operação leva o mesmo tempo, independente do tamanho do dado. |
| **O(n)** | Linear | O tempo cresce proporcionalmente ao número de elementos. |
| **O(n²)** | Quadrática | Comum em algoritmos com loops aninhados (ex: percorrer matrizes). |

---

## 🛠️ Como Contribuir
1. Faça o Fork do projeto
2. Crie uma branch para sua modificação (`git checkout -b feature/nome-da-feature`)
3. Envie suas alterações (`git commit -m 'mensagem de alteração'`)
4. Faça o Push (`git push origin feature/nome-da-feature`)

---
*Este repositório faz parte de um plano de estudos focado em Engenharia de Sistemas.*
---

# 🚀 Algoritmos e Estruturas de Dados Completo

Este repositório contém uma documentação técnica e exemplos práticos sobre os pilares da programação, desde a manipulação de dados básicos até estruturas multidimensionais e lógica funcional.

## 📌 Sumário
* [Manipulação de Strings](#-manipulação-de-strings)
* [Listas e Fatiamento (Slicing)](#-listas-e-fatiamento-slicing)
* [Matrizes e Determinantes](#-matrizes-e-determinantes)
* [Funções e Modularização](#-funções-e-modularização)
* [Complexidade Big O](#-complexidade-big-o)

---

## 🧵 Manipulação de Strings

Strings são sequências de caracteres. Para processar textos de forma eficiente, utilizamos métodos integrados que facilitam a limpeza e transformação dos dados.

### Principais Métodos:
*   `.upper()` / `.lower()`: Converte todos os caracteres para maiúsculas ou minúsculas.
*   `.strip()`: Remove espaços em branco (ou caracteres específicos) do início e do fim da string.
*   `.split(delimitador)`: Divide a string em uma lista, usando um delimitador (ex: vírgula ou espaço).
*   `.join(lista)`: Une elementos de uma lista em uma única string, utilizando um conector.
*   `.replace(antigo, novo)`: Substitui todas as ocorrências de um trecho por outro.
*   `.find()` / `.index()`: Retorna a posição de um caractere ou sub-string.
*   `.capitalize()`: Torna a primeira letra da frase maiúscula.

---

## ✂️ Listas e Fatiamento (Slicing)

O fatiamento permite extrair partes específicas de sequências (strings ou listas) de forma concisa.

**Sintaxe:** `sequencia[início:fim:passo]`

*   **Início:** Índice onde começa a fatia (inclusivo).
*   **Fim:** Índice onde termina a fatia (exclusivo).
*   **Passo:** O intervalo entre os elementos (ex: `2` para pegar um item sim, um item não).

### Exemplos:
```python
lista = [0, 1, 2, 3, 4, 5]
print(lista[1:4])   # Saída: [1, 2, 3]
print(lista[::-1])  # Inverte a lista: [5, 4, 3, 2, 1, 0]
```

---

## 📊 Matrizes e Determinantes

Uma **matriz** é uma lista de listas, representando uma estrutura bidimensional (linhas e colunas).

### Operações Comuns:
*   **Acesso:** `matriz[linha][coluna]`
*   **Percorrimento:** Geralmente feito com dois loops `for` aninhados.

### Determinantes:
Na computação, o cálculo de determinantes é essencial para resolver sistemas lineares e em computação gráfica.
*   **Matriz 2x2:** `(a*d) - (b*c)`
*   **Matriz 3x3:** Utiliza-se comumente a Regra de Sarrus ou o Teorema de Laplace para expansão de cofatores.

---

## ⚙️ Funções e Modularização

Funções são blocos de código reutilizáveis que executam uma tarefa específica, ajudando a manter o código limpo (princípio DRY - *Don't Repeat Yourself*).

*   **Parâmetros:** Valores de entrada que a função recebe.
*   **Retorno:** O resultado que a função envia de volta após o processamento.
*   **Escopo:** Variáveis definidas dentro de uma função não são acessíveis fora dela (escopo local).

```python
def calcular_area(base, altura):
    """Calcula a área de um retângulo."""
    return base * altura

resultado = calcular_area(10, 5)
```

---

## 📉 Complexidade de Algoritmos (Big O)

Mede a eficiência do código conforme o volume de dados aumenta.

| Notação | Nome | Descrição |
| :--- | :--- | :--- |
| **O(1)** | Constante | Execução imediata, independente do dado. |
| **O(n)** | Linear | O tempo cresce proporcionalmente à entrada. |
| **O(n²)** | Quadrática | Comum em matrizes percorridas integralmente. |

---

## 🛠️ Tecnologias Utilizadas
*   **Linguagens:** Python, Java, C++
*   **Conceitos:** Lógica Matemática, Álgebra Linear, POO

---
*Documentação em constante atualização para fins de estudo e consulta.*
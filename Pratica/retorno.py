def quadrado(valor):
    return valor ** 2
print(quadrado(10))



def obter_info_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade

print(obter_info_usuario())
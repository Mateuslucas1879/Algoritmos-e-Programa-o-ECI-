def maior_elemento(lista):
    if not lista:
        return None
    if len(lista) == 1:
        return lista[0]
    return max(lista[0], maior_elemento(lista[1:]))

def soma_elementos(lista):
    if not lista:
        return 0
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma_elementos(lista[1:])

# ====== === TESTES ===== ====
maior = maior_elemento([1,2,3,4,5,6,7,8,9])
soma = soma_elementos([1,2,3,4,5,6,7,8,9])
print(maior) # Saída: 9
print(soma)  # Saída: 45

# Teste com lista vazia
print(soma_elementos([])) # Saída: 0
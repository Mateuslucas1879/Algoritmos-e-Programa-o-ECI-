from collections import deque

def demonstrarEstrutura():
    pass


minha_lista = [1,2,3]
print(minha_lista)
minha_lista.append(4)
minha_lista.insert(1,5)
print(f"Lista:{minha_lista}")
print()
print("-="*30)

minha_deque = deque([10,20,30])
print(minha_deque)
minha_deque.appendleft(5)
minha_deque.append(50)
print(f"Deque: {minha_deque}")
print("-="*30)
print()

def gerador_pares(limite):
    for i in range(limite):
        if i % 2 == 0:
            yield i

print("GERADORES DE PARES")
for par in gerador_pares(10):
    print(par, end=" ")
print()
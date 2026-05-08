"""
Iteradores fornecem uma maneira padronizada de acessar elementos de uma coleção
sequencialmente, sem expor a representação interna da estrutura de dados. Eles abstraem
o mecanismo de travessia

Python: Protocolo Iterável e Geradores: Um objeto é iterável se define o método __iter__
(que retorna um iterador). Um iterador define o método __next__ (que retornao próximo item
ou levanta StopIteration ). Geradores implementam esse protocolo automaticamente
"""

lista = [0,1,2,3,4,5,6,7,8,9]
interadores = iter(lista)

print(next(interadores))
print(next(interadores))
print(next(interadores))
print(next(interadores))
print(next(interadores))
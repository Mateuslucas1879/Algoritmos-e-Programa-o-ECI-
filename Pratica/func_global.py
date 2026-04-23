variavel_global = "Eu sou Cristao"



def minha_funcao():
    variavel_local = "Eu sou Protestante"
    print(f"Global: {variavel_global}")
    print(f"Local Interno: {variavel_local}")


def modifica_funcao():
    global variavel_global
    variavel_global = "Eu sou Assembleia "
    print(f"Global Modificada: {variavel_global}")

def funcao_aninhada():
    x = "Local externo"
    def func_interna():
        nonlocal x
        x = "E sou filho de Jesus"
        print(f"Externo: {x}")
    return func_interna()
    print(f"Dentro da função aninhada: {x}")



minha_funcao()
modifica_funcao()
funcao_aninhada()
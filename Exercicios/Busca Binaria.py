def Busca_Binaria_Recursiva(v,x,i=0,j=None):
    if j==None:
        j = len(v)-1

    if i > j:
        return -1

    m = (i + j) // 2
    if v[m] == x:
        return m
    elif v[m] < x:
        return Busca_Binaria_Recursiva(v,x,m+1,j)
    else:
        return Busca_Binaria_Recursiva(v,x,i,m-1,)

entrada_lista = input("Digite os elementos do vetor ordenado separados por vírgula: ")
v = [int(item.strip()) for item in entrada_lista.split(",")]
x = int(input("Digite o numero que deseja buscar: "))
res = Busca_Binaria_Recursiva(v,x)
print(f"O numero que deseja buscar: {res}")
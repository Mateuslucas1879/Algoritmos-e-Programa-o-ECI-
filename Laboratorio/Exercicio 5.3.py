def divisao_recursiva(a,b):
    if a < b:
        return 0
    return 1 + divisao_recursiva(a - b,b)


n1 = int(input())
n2 = int(input())
print(divisao_recursiva(n1,n2))
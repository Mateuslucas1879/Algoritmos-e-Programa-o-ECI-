num = int(input("Digite um numero: "))
for x in range(1,num+1):
    y = int(x ** 0.5)
    primo = True
    for z in range(2,y+1):
        if x % z == 0:
            primo = False
            break

    if primo:
        print(x,end=" ")

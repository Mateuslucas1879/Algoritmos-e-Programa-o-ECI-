x = 10
z = 10
def globale(funcao):
    global x
    global y
    global z

    x,y,z = x+2,funcao+3,funcao+x
    return x,y,z

print(x)

print(z)
print(globale(20))
print(x,y,z)

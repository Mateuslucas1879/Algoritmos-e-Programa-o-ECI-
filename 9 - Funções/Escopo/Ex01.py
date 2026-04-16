a = 10
z = 60
def escopo(b):
    z = a + b
    print("Aqui o Z vai valer a soma de a+b: ",z)
    return z

print("Primeiro print",z)
print(escopo(0))
print(z)
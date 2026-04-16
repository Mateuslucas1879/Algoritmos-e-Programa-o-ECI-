print("Triangulo - Digite os numeros abaixo\n")
a= float(input())
b= float(input())
c= float(input())

r = "Nao"
if a>0 and a>b+c:
    if b > 0 and b < a + c:
        if c > 0 and c < a + b:
            r = "Sim"

print(r)

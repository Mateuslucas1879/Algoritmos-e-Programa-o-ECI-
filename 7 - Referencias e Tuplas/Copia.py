a = [1,2,3]
b = a
c = a[:]
print(a,b,c)
print(type(a),type(b),type(c))

print()

a[2] = 100
print(a,b,c)
a = [1,2,[3]]
b = a[:]
print(a)
print(b)

print()

b[1] = 9
print(a,b)
print()

a[2][0] = 10
print(a,b)
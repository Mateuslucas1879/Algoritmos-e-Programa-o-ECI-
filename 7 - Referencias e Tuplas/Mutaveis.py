a = [1,2,3]
b = a
a = [1,2,4]
print(a,b)
print()

a = [1,2,3]
a = b
a[1] = 12
print(a,b)
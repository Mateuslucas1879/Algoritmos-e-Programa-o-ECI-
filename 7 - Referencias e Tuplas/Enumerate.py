from random import randint
s = []

for i in range(10):
    s.append(randint(1, 10))

for i in range(len(s)):
    print(i,s[i])
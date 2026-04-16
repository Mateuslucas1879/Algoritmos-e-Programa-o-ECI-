s = [2,4,2,6]

r = s[:0]

for i in range(len(s)):

     if s[:i]<s[i:]:

          r += s[:i]

     else:

          r += s[i:]

print(r)
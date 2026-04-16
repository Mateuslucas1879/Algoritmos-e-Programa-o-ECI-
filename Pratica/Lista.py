v = [0]*2

s=p=[]

w,l=[],[]

for i in range(2):

    s+= [[0]*2]

    w+= [[0]*2]

for i in range(2):

    p+= [v]

    l+= [v]

s[0][0] = p[0][0] = w[0][0] = l[0][0] = 2
print(s,p,l,w)
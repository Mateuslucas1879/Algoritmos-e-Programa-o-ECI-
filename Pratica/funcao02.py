def f(l):

    if len(l)<=1: return[l]

    r = f(l[1:])

    if l[0]<=l[1]:

        return[[l[0]]+r[0]]+r[1:]

    return[l[:1]]+r

print(f([2,0,2,0,4]))
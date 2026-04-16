a=[1,5,2,7,8,2,3]

print ([a[i:-i:2] for i in range(len(a))])


l = [x*y for x in [1,0,2] for y in (2,1,0) if y>x and x%y != 2]
print (l)
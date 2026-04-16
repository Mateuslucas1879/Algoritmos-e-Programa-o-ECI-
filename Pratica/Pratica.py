l=[0,2,4,1,2]

while True:

	if len(l)<=1:

		l = [l]

		break

	r = [l[1:]]

	if l[0]<=l[1]:

		l=[[l[0]]+r[0]]+r[1:]

        continue

	l=[l[:1]]+r

	break

print(l)
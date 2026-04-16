A = input().replace('[','').replace(']','').split(',')
b = input().replace('[','').replace(']','').split(',')

A = [item.strip() for item in A]
b = [item.strip() for item in b]

ponteiro = 0

for item in b:
    if ponteiro < len(A) and item == A[ponteiro]:
        ponteiro = ponteiro + 1

if ponteiro == len(A):
    print(True)
else:
    print(False)
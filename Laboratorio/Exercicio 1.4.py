
linha1 = input().strip("[]").strip(",")
linha2 = input().strip("[]").strip(",")

num1 = [int(i) for i in linha1.split(",")]
num2 = [int(i) for i in linha2.split(",")]

soma = 0
for i in range(len(num1)):
    soma += num1[i] * num2[i]

print(soma)


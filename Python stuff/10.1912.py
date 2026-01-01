n = int(input())
x = []

for i in range(n):
    x.append(input())

s = input()

for j in range(len(x)):
    if s in x[j]:
        print(x[j].replace(s, ""))
    else:
        print(x[j])

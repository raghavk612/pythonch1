n = int(input())

result = ""

for i in range(n):
    s, k = input().split()
    k = int(k)

    for j in range(k):
        result += s

print(result)

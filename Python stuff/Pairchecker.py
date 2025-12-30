n=int(input())
numbers=input().split()
for i in range(n):
    numbers[i]=int(numbers[i])
counter=0
for i in range(n):
    for j in range(n):
        if numbers[j] == numbers[i]+2:
            counter+=1
print(counter)
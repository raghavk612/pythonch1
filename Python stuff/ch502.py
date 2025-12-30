n=int(input())
a=input().split()
x=int(input())
for counter in range(n):
    if(a[counter] != x):
        print(a[counter],end=" ")
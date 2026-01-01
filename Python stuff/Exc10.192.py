n=int(input())
words=[]
for i in range(1,n+1):
    x=str(input())
    words.append(x)

m=int(input())
for j in range(1,m+1):
    for y in words:
        print(y,end=" ")
    print()
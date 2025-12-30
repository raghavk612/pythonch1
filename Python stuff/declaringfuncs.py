def addZeros(x,y):
    result=y
    for i in range(x):
        result*=10
    return result

a,b=input().split()
a=int(a)
b=int(b)
output=addZeros(a,b)

print(output)
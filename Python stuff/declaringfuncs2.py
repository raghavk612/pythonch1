def addZeros(x,y):
    result=y
    for i in range(x):
        result*=10
    return result

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
output=0

if c==1:
    output=addZeros(a,b)
elif c==2:
    output=addZeros(b,a)
else:
    num1=addZeros(a,b)
    num2=addZeros(b,a)
    output=num1+num2        
print(output)
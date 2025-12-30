a,b,c=input().split()
a=int(a)
b=int(a)
c=int(c)

output=0

if c==1:
    output =b
    for i in range(a):
        output*=10
        
        
        
elif c==2:
    output = a
    for i in range(b):
        output*=10
else:
    num1=b
    for i in range(a):
        num1*=10
    num2=a
    for i in range(b):
        num2*=10
        output=num1+num2
print(output)                
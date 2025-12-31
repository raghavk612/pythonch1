import math

n=int(input())

for i in range(2,n):
    primality=True
    
    for x in range(2,i):
        if i%x==0:
            primality=False
    
    if primality==True:
        print(i)        
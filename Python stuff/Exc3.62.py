num1,num2,num3=input().split()
if num1<num2 and num2<num3:
    print(num1)
elif num3<num1 and num3<num2:
    print(num3)
else:
    print(num2)    
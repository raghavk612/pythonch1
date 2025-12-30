num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# assume all numbers are different
if num1 > num2 and num1 > num3:
    print(num1)
    if num2 > num3:
        print(num2)
    else:
        print(num3)

elif num2 > num1 and num2 > num3:
    print(num2)
    if num1 > num3:
        print(num1)
    else:
        print(num3)

else:  # num3 is largest
    print(num3)
    if num1 > num2:
        print(num1)
    else:
        print(num2)

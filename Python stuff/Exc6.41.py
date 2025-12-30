temp=float(input())
humidity=float(input())
if humidity<40:
    if temp<60:
        print("Lucy drinks coffee")
    else:
        print("Lucy drinks iced tea")    
else:
    if temp<60:
        print("Lucy eats cake")
    else:
        print("Lucy eats ice cream")    
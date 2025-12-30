temperature,humidity=input().split()
temperature=int(temperature)
humidity=int(humidity)
if temperature <60:
    if humidity<40:
        print("Lucy drinks coffee")
    else:
        print("Lucy eats cake")
else :
    if humidity <40:
        print("Lucy drinks iced tea")
    else:
        print("Lucy eats ice cream")                    
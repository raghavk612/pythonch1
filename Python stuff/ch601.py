temperature,humidity=input().split()
temperature=int(temperature)
humidity=int(humidity)

if temperature<60 and humidity<40:
    print("Lucy drinks coffee")
if temperature < 60 and humidity>=40:
    print("Lucy eats cake")  
if temperature >= 60 and humidity>=40:
    print("Lucy eats ice cream")
if temperature < 60 and humidity>=40:
    print("Lucy drinks iced tea")            
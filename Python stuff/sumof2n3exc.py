def sumoftwo(x,y):
    return x+y
def sumofthree(x,y,z):
    return sumoftwo(x,sumoftwo(y,z))
result=sumofthree(5,7,4)
print(result)
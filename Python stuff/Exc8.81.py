x=int(input())
d=int(input())
def print_square(x, d):
    
    for i in range(x):
        for j in range(x):
            print(d, end="")
        print()
print_square(x,d)
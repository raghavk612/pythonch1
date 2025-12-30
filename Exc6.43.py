x1, y1, x2, y2 = input().split()
x3, y3, x4, y4 = input().split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x3 = int(x3)
y3 = int(y3)
x4 = int(x4)
y4 = int(y4)


sidex = (x2 if x2 > x4 else x4) - (x1 if x1 < x3 else x3)
sidey = (y2 if y2 > y4 else y4) - (y1 if y1 < y3 else y3)


if sidex > sidey:
    side = sidex
else:
    side = sidey

print(side * side)

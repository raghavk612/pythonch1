n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

counter = 0

for i in range(n):
    Duplicate = False

    for x in range(i):
        if numbers[i] == numbers[x]:
            Duplicate = True

    if not Duplicate:
        counter2 = 0
        for k in range(n):
            if numbers[i] == numbers[k]:
                counter2 += 1

        if counter2 > 1:
            counter += 1

print(counter)

        
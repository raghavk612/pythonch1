def removeZeros(x):
    digits = list(str(x))
    result = []

    for d in digits:
        if d != '0':
            result.append(d)

    return int("".join(result))

print(removeZeros(37800))

def binarygcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    factor = 1
    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        factor *= 2

    while a % 2 == 0:
        a //= 2

    while b % 2 == 0:
        b //= 2

    while a != b:
        if a > b:
            a = (a - b) // 2
            while a % 2 == 0:
                a //= 2
        else:
            b = (b - a) // 2
            while b % 2 == 0:
                b //= 2

    return a * factor


a, b = map(int, input().split())
print(binarygcd(a, b))

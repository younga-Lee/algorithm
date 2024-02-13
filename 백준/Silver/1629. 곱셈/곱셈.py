a, b, c = map(int, input().split())

def func(a, b, c):
    if b == 1:
        return a % c

    tmp = func(a, b // 2, c)

    if b % 2:
        return tmp * tmp * a % c
    else:
        return tmp * tmp % c
print(func(a, b, c))
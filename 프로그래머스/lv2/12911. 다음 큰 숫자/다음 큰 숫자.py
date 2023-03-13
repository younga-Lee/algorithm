def solution(n):
    one = bin(n).count('1')
    while True:
        n += 1
        if one == bin(n).count('1'):
            break
    return n
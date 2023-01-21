def solution(n):
    i = 1
    p = 1
    while p <= n:
        p = p*i
        i += 1
    return i-2
            
    
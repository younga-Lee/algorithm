def solution(n):
    cnt = 1
    num = 1
    while cnt != n:
        num += 1
        while True:
            if num%3 == 0 or '3' in str(num):
                num += 1
            else:
                break
        cnt += 1
    return num
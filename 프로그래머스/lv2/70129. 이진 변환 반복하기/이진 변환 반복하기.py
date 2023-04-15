def solution(s):
    all_zero = 0
    cnt = 0
    while s != "1":
        cnt += 1
        zero = s.count('0')
        all_zero += zero
        c = len(s) - zero
        s = bin(c)[2:] #s를 갱신
    
    return cnt, all_zero
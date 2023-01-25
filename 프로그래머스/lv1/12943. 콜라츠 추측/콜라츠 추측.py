def solution(num):
    cnt = 0 
    while num != 1 :
        if num == 1:
            return 0
        elif num%2 == 0:
            num = num/2
            cnt += 1
        else:
            num = num*3+1
            cnt = cnt + 1        
    return (cnt if cnt <= 500 else -1)
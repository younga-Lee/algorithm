def solution(n,a,b):
    answer = 1
    if a > b: #항상 a<b
        a, b = b, a
    while True:
        a = (a+1)//2
        b = (b+1)//2
        if b-a < 1:
            break
        answer += 1
        
    return answer
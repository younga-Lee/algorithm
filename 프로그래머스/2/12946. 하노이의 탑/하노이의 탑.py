def solution(n):
    answer = []
    
    def hanoi(t, start, target, mid, answer):
        if t == 1:
            answer.append([start, target])
            return
        
        hanoi(t-1, start, mid, target, answer) #t빼고 나머지 옮기기
        answer.append([start, target]) 
        hanoi(t-1, mid, target, start, answer) #나머지 모두 옮기기
        
    hanoi(n, 1, 3, 2, answer)
    return answer
def solution(sides):
    answer = 0
    #알고 있는 숫자가 최대인경우
    for i in range(1,max(sides)+1):
        if i+min(sides) > max(sides):
            answer+=1
    #모르는 숫자가 최대인 경우
    answer += sum(sides)-max(sides)-1
    return answer
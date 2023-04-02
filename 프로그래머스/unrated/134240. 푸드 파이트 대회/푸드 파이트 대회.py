def solution(food):
    answer = ''
    #1번이 먹는 음식
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2)
    return answer + '0' + answer[::-1]
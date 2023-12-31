def solution(elements):
    answer = []
    ele = elements*2
    for n in range(1, len(elements)+1):
        for i in range(len(ele)):
            answer.append(sum(ele[i:i+n]))
    return len(set(answer))
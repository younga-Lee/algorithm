def solution(elements):
    answer = set()
    ele = elements*2
    for n in range(1, len(elements)+1):
        for i in range(len(ele)):
            answer.add(sum(ele[i:i+n]))
    return len(answer)
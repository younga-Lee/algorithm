def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    
    d = {}
    for i in p:
        d[i] = 0
        
    for i in p:
        d[i] += 1
        
    for j in c:
        d[j] -= 1
    return max(d, key = d.get)

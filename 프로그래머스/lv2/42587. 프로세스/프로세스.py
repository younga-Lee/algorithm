from collections import deque
def solution(priorities, location):
    q = deque(list(range(len(priorities)))) #순서
    p = deque(priorities) #기능

    cnt = 0
    while cnt != len(priorities):
        mx = max(p)
        toq = q.popleft()
        top = p.popleft()
        if top == mx: #최대
            cnt += 1
            if toq == location:
                break
        else:
            q.append(toq)
            p.append(top)
    return cnt
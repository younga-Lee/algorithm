from collections import deque
def solution(cards1, cards2, goal):
    dq = deque(goal)
    while dq:
        g = dq.popleft()
        if cards1 and cards1[0] == g:
            cards1 = cards1[1:]
        elif cards2 and cards2[0] == g:
            cards2 = cards2[1:]
        else:
            return "No"
    return "Yes"
    
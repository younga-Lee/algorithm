from collections import deque
f, s, g, u, d = map(int, input().split()) #건물총수, 내위치, 스타트링크위치
q = deque([(s, 0)])
def bfs():
    v = [0]*(f+1)
    while q:
        s, cnt = q.popleft()
        if s == g:
            return cnt
        for di in [u, -d]:
            ni = s+di
            if 1 <= ni <= f and v[ni] == 0:
                v[ni] = 1
                q.append((ni, cnt+1))
    return "use the stairs"
print(bfs())
from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split()) #로봇 첫 위치, 좌표
dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque([(r, c, 1, d)]) #위치, 현재 개수, 방향
arr[r][c] = 2 #청소
def bfs():
    while q:
        r, c, cnt, d = q.popleft()
        for _ in range(4):
            d = (d+3)%4 #이거 꼭 넣기..
            ni, nj = r + dr[d][0], c + dr[d][1]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = 2
                q.append((ni, nj , cnt+1, d))
                break
        else:
            ni, nj = r-dr[d][0], c-dr[d][1]
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] != 1:
                q.append((ni, nj, cnt, d))
            else:
                return cnt
    return cnt
print(bfs())
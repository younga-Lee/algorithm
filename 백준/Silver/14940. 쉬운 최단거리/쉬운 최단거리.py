from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            si, sj = i, j
        elif arr[i][j] == 1:
            arr[i][j] = -1

q = deque([(si, sj)])
arr[si][sj] = 0
while q:
    si, sj = q.popleft()
    for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
        ni, nj = si+di, sj+dj
        if 0<=ni<n and 0<=nj<m and arr[ni][nj] == -1:
            arr[ni][nj] = arr[si][sj]+1
            q.append((ni, nj))
for i in range(n):
    print(*arr[i])
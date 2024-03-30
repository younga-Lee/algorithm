from collections import deque
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((i, j, arr[i][j], 0))

virus = sorted(virus, key=lambda x:x[2])

q = deque(virus)
while q:
    i, j, v, t = q.popleft()
    if t == s: #시간되면
        continue
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 0:
            arr[ni][nj] = v
            q.append((ni, nj, v, t+1))
print(arr[x-1][y-1])
#bfs의 시작점이 여러개이며 동시에 진행해야 할 때 -> 그냥 q에 다 넣어서 하면 됨!

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#초기 시작
st = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            st.append((i, j))

q = deque(st)
#토마토가 모두 익을 때까지의 최소 날짜 출력
while q:
    si, sj = q.popleft()
    for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
        ni, nj = si+di, sj+dj
        if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0:
            arr[ni][nj] = arr[si][sj]+1
            q.append((ni, nj))

#하나라도 0이 있으면 -1
ans = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()
    if ans < max(arr[i]):
        ans = max(arr[i])
print(ans-1)
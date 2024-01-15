from collections import deque
import sys
input = sys.stdin.readline

m, n, ht = map(int, input().split())
arr = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(ht)] #3차원!!
q = deque()

#익은 토마토 위치 찾기
for h in range(ht):
  for i in range(n):
      for j in range(m):
       if arr[h][i][j] == 1:
         q.append([i,j, h])
#익히기
while q:
    si, sj, sh = q.popleft()
    for di, dj, dh in [(0,1,0),(1,0,0),(-1,0,0),(0,-1,0),(0,0,1), (0,0,-1)]:
        ni, nj, nh = si+di, sj+dj, sh+dh
        if 0<=ni<n and 0<=nj<m and 0<=nh<ht and arr[nh][ni][nj] == 0:
            arr[nh][ni][nj] = arr[sh][si][sj]+1
            q.append((ni,nj,nh))

#모두 익지 못하는 상황 & 값구하기
ans = -1
for h in range(ht):
    for i in range(n):
        for j in range(m):
            if arr[h][i][j] == 0:
                print(-1)
                exit()
            elif arr[h][i][j] > ans:
                ans = arr[h][i][j]
print(ans-1)
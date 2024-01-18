from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque([])

cd = [] #0인곳
#바이러스 있는 곳
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i,j))
        if arr[i][j] == 0:
            cd.append([i, j])

cd3 = []

def dfs(idx, n, lst):
    global cd3
    if n > 3: #백트레킹
        return

    if idx == len(cd):
        if n == 3:
            cd3.append(lst)
        return

    dfs(idx+1, n+1, lst + [cd[idx]])
    dfs(idx+1, n, lst)

dfs(0, 0, [])

#바이러스 퍼지기
def bfs(arr2):
    q2 = deque(q)  # 현재 큐 복사
    while q2:
        si, sj = q2.popleft()
        for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni, nj = si+di, sj+dj
            if 0<=ni<n and 0<=nj<m and arr2[ni][nj] == 0:
                arr2[ni][nj] = 2
                q2.append((ni, nj))
    cnt = 0
    for i2 in range(n):
        for j2 in range(m):
            if arr2[i2][j2] == 0:
                cnt += 1
    return cnt

#완전탐색 (최대값)
mx = 0
for c in range(len(cd3)):
    arr2 = copy.deepcopy(arr)  # 매번 초기화
    for ci, cj in cd3[c]:
        arr2[ci][cj] = 1
    ans = bfs(arr2)
    if ans > mx:
        mx = ans

print(mx)

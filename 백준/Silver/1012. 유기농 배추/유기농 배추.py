import sys
input = sys.stdin.readline

def dfs(i, j):
    stk = [(i, j)]
    while stk:
        si, sj = stk.pop()
        for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
            ni, nj = di+si, dj+sj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 1:
                stk.append((ni, nj))
                arr[ni][nj] = 2


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    ans = 0
    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1 #배추 심기

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)


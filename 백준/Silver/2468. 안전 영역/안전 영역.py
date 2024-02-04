from collections import deque
import copy
n = int(input())
arr = []
mxh, mnh = 0, 10**10
for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
    if mxh < max(lst):
        mxh = max(lst)
    if mnh > min(lst):
        mnh = min(lst)

def sink(k, k_arr):
    for i in range(n):
        for j in range(n):
            if k_arr[i][j] <= k:
                k_arr[i][j] = 0 #잠긴다
    return k_arr

def bfs(k_arr):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if k_arr[i][j] != 0:
                cnt += 1
                q = deque([(i, j)])
                while q:
                    si, sj = q.popleft()
                    for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                        ni, nj = si+di, sj+dj
                        if 0<=ni<n and 0<=nj<n and k_arr[ni][nj] != 0:
                            q.append((ni, nj))
                            k_arr[ni][nj] = 0
    return cnt

mx = 1
for k in range(mnh, mxh):
    mx = max(mx, bfs(sink(k, copy.deepcopy(arr))))
print(mx)
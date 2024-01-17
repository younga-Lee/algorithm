from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

q = deque([])
v = [0]*(n+1)
cnt = 0
for i in range(1, n+1):
    if v[i] == 0:
        q.append(i)
        cnt += 1
        v[i] = cnt
        while q:
            a = q.popleft()
            for j in arr[a]:
                if v[j] == 0:
                    q.append(j)
                    v[j] = cnt
print(max(v))
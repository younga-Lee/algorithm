#순열
def dfs(n, lst):
    global ans
    if n == N:
        sm = 0
        for j in range(1, N):
            sm += abs(arr[lst[j-1]]-arr[lst[j]])
        ans = max(ans, sm)
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, lst+[i])
            v[i] = 0

N = int(input())
arr = list(map(int, input().split()))
ans = 0
v = [0]*N
dfs(0, [])
print(ans)

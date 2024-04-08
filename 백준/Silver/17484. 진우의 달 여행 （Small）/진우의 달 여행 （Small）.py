n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(pre, i, j, sm): #이전 방향, 가로 인덱스, 세로 인덱스 ,합
    global ans, lst
    if sm >= ans: #가지치기
        return

    if n == i:
        ans = min(ans, sm)
        return ans

    for dj in [-1, 0, 1]:
        if dj != pre and 0<=dj+j<m:
            dfs(dj, i+1, dj+j, sm+arr[i][dj+j])

ans = 10**10 #연료 최솟값
for sj in range(m):
    dfs(-2, 0, sj, 0)
print(ans)

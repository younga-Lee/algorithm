n, m = map(int, input().split()) #크기 nxn, 최대 치킨집 m
arr = [list(map(int, input().split())) for _ in range(n)] #0 빈칸, 1 집, 2 치킨집
ans = 10**10 #모든 집의 치킨 거리의 합

#집, 치킨집 위치 찾기
house, chicken = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])
#치킨 거리 재기
def measure(done_chicken):
    dis = 0
    for h in house:
        tmp = 10**10
        for chi in done_chicken:
            tmp = min(tmp, abs(h[0]-chi[0]) + abs(h[1]-chi[1]))
        dis += tmp
    return dis

#치킨 집 폐업 시뮬레이션
def dfs(lst, i):
    global ans
    if i == len(chicken):
        if len(lst) == m: #종료조건
            ans = min(ans, measure(lst))
        return

    dfs(lst+[chicken[i]], i+1)
    dfs(lst, i+1)

dfs([], 0)
print(ans)
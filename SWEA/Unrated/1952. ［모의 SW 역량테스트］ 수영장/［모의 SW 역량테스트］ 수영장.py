def dfs(n, sm):
    global ans
    if sm >= ans:
        return
    if n >= 12:
        ans = min(ans, sm)
        return
    if days[n] > 0:
        dfs(n+1, sm+days[n]*prices[0])
        dfs(n+1, sm+prices[1])
        dfs(n+3, sm+prices[2])
    else:
        dfs(n+1, sm)

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    days = list(map(int, input().split()))
    ans = prices[3] #1년치가 최대

    dfs(0, 0)
    print(f'#{tc} {ans}')
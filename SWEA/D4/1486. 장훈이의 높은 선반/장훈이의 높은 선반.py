def dfs(n, sm):
    global ans
    if sm > ans:
        return
    if n == N:
        if B <= sm < ans:
            ans = sm
        return
    dfs(n+1, sm+S[n])
    dfs(n+1, sm)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) #직원들 수, 목표높이
    S = list(map(int, input().split()))

    ans = 10**N #높이 B 이상 중 가장 낮은 탑
    dfs(0, 0)

    print(f'#{tc} {ans-B}')
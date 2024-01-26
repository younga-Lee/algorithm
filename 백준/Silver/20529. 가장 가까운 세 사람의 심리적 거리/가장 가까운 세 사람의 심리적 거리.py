import sys
input = sys.stdin.readline

def dfs(cnt, cd, idx, ans):
    if cnt == 3:
        tmp = 0
        for a in range(2):
            for b in range(a+1, 3):
                # 미리 변환된 집합 사용
                tmp += len(cd[a] - cd[b])
        return min(ans, tmp)

    # 가지치기: 더 이상 탐색할 필요가 없는 경우
    if ans == 0:
        return ans

    for i in range(idx, n):  # 중복 탐색 방지
        ans = min(ans, dfs(cnt+1, cd + [sets[i]], i + 1, ans))
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    lst = input().split()
    sets = [set(s) for s in lst]  # 문자열의 집합 변환
    ans = dfs(0, [], 0, 10**10)
    print(ans)
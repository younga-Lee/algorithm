import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 10**10
def dfs(i, cnt, lst):
    global ans
    if i == n:
        if cnt == n//2:
            #최솟값 확인
            start = 0
            for a in lst:
                for b in lst:
                    start += arr[a][b]
            link = 0
            lst2 = list(set(list(range(0,n))) - set(lst))
            for a in lst2:
                for b in lst2:
                    link += arr[a][b]
            ans = min(ans, abs(start-link))
        return

    dfs(i+1, cnt+1, lst+[i]) #선택 O
    dfs(i+1, cnt, lst) #선택 X
dfs(0, 0, [])
print(ans)
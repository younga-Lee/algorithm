n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
ans = 0
#도연이 위치
i, j = 0, 0
for i in range(n):
    if 'I' in arr[i]:
        j = arr[i].index('I')
        break

stk = [(i,j)]
arr[i][j] = 'D'
while stk:
    si, sj = stk.pop()
    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
        ni, nj = si+di, sj+dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] in ['O','I','P']:
            if arr[ni][nj] == 'P':
                ans += 1
            arr[ni][nj] = 'D'
            stk.append((ni, nj))

if ans == 0:
    print('TT')
else:
    print(ans)
k, n = map(int, input().split())
lst = sorted([int(input()) for _ in range(k)])

l, r = 1, lst[-1]
ans = 0
while l<=r:
    m = (l+r)//2
    cnt = 0 #랜선 개수
    for i in range(k):
        cnt += lst[i]//m

    if cnt < n:
        r = m-1
    else:
        ans = m
        l = m+1
print(ans)
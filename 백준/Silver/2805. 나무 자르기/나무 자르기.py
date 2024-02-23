n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = 0
l, r = 1, lst[-1]
while l <= r:
    h = (l+r)//2
    cnt = 0
    for x in lst:
        if x-h > 0:
            cnt += x-h

    if cnt >= m:
        ans = h #갱신
        l = h+1
    else:
        r = h-1
print(ans)
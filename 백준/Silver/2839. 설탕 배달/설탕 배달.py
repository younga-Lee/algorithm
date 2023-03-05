N = int(input())
mn = N
ans = -1
for i in range(N//5+1):
    if (N-i*5) % 3 == 0:
        cnt = i + (N-i*5)//3
        if mn > cnt:
            mn = cnt
        ans = mn

print(ans)
n = int(input()) #수열의 크기
lst = list(map(int, input().split()))
x = int(input())
lst.sort()
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if lst[i]+lst[j] > x:
            break
        elif lst[i]+lst[j] == x:
            cnt += 1
            break

print(cnt)
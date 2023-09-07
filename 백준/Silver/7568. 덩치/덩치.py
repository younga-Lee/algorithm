n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    x, y = arr[i]
    cnt = 1
    for j in range(n):
        if i != j:
            p, q = arr[j]
            if x<p and y<q: #자기가 작을 때
               cnt+=1
    print(cnt, end=' ')
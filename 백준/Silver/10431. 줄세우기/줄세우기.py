import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    take = list(map(int, input().split()))
    tc = take[0]
    lst = take[1:]
    cnt = 0

    for i in range(len(lst)):
        for j in range(i):
            if lst[i] < lst[j]:
                cnt += i-j
                lst.insert(j, lst.pop(i))
                break
    print(f'{tc} {cnt}')
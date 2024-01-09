import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stk = []
ans = [-1]*n

for i in range(n):
    while stk and lst[stk[-1]] < lst[i]: #오큰수
        ans[stk.pop()] = lst[i]
    stk.append(i)

print(*ans) #출력형식 잘 못해서 틀린거 실화냐
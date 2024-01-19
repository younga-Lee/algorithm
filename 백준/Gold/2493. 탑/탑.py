import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stk = []
ans = [0]*n
for i in range(n-1, -1, -1):
    if not stk:
        stk.append(i)
    else:
        if lst[stk[-1]] > lst[i]:
            stk.append(i)
        else:
            while stk and lst[stk[-1]] <= lst[i]:
                ans[stk.pop()] = i+1
            stk.append(i)
print(*ans)
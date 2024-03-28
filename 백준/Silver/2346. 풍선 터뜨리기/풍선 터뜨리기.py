from collections import deque
n = int(input())
lst = list(map(int, input().split()))
q = deque([])
for idx, num in enumerate(lst):
    q.append((idx+1, num))

idx, num = q.popleft()
ans = [idx]
while q:
    if num > 0:
        num -= 1
    while num < 0:
        q.appendleft(q.pop())
        num += 1
    while num > 0:
        q.append(q.popleft())
        num -= 1
    idx, num = q.popleft()
    ans.append(idx)
print(*ans)
from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
q = deque([(a, 1)])

while q:
    a, cnt = q.popleft()

    for num in [a*2, int(str(a)+'1')]:
        if num == b:
            print(cnt + 1)
            exit()

        if 1 <= num <= 10**9 and a <= b:
            q.append((num, cnt+1))
print(-1)
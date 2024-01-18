import heapq
import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, -x)
    else:
        if q:
            print(-int(heapq.heappop(q)))
        else:
            print(0)
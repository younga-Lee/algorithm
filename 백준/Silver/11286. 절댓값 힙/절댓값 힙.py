import heapq
import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, (abs(x), x))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
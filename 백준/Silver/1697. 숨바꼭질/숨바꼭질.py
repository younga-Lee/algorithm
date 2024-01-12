from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
v = [1]*1000000 #범위실수.. 그냥 널널하게 하자

def bfs():
    q = deque([n])
    while q:
        i = q.popleft()
        if k == i:
            return v[k]-1
        for ni in [i-1,i+1, i*2]:
            if 0 <= ni <= 100000 and v[ni] == 1:
                q.append(ni)
                v[ni] += v[i]

print(bfs())
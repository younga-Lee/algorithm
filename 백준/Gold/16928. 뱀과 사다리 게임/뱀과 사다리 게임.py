from collections import deque

n, m = map(int, input().split())
dic = dict()
for _ in range(n+m):
    k, v = map(int, input().split())
    dic[k] = v

v = [False] * 101
q = deque([1])
v[1] = True
min_rolls = 0

while q:
    size = len(q)
    for _ in range(size):
        a = q.popleft()

        if a == 100:
            print(min_rolls)
            exit(0)

        for i in range(1, 7):
            ni = a + i
            if ni <= 100 and not v[ni]:
                if ni in dic:
                    ni = dic[ni]

                if not v[ni]:
                    v[ni] = True
                    q.append(ni)

    min_rolls += 1

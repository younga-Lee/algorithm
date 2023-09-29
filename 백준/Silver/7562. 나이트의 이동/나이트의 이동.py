from collections import deque
tc = int(input())
for _ in range(tc):
    n = int(input()) #체스판 nxn
    si, sj = map(int, input().split()) #현재 칸
    ei, ej = map(int, input().split()) #목표 칸
    v = [[0]* n for _ in range(n)]

    cnt = 0
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    while q:
        i, j = q.popleft()
        if ei == i and ej == j:
            print(v[i][j]-1)
            break
        for di, dj in [(-1, -2), (-2, -1), (-1, 2), (1, -2), (-2, 1), (1, 2), (2, -1), (2, 1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0:
                v[ni][nj] = v[i][j] + 1
                q.append((ni, nj))



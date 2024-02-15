from collections import deque

def solution(maps):
    maps1 = [list(maps[_]) for _ in range(len(maps))]
    maps2 = [list(maps[_]) for _ in range(len(maps))]
    answer = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                si, sj = i, j
            elif maps[i][j] == 'L':
                li, lj = i, j
            elif maps[i][j] == 'E':
                ei, ej = i, j

    def bfs(ssi, ssj, eei, eej, maps):
        q = deque([(ssi, ssj, 0)])
        maps[ssi][ssj] = 'X'
        while q:
            sti, stj, cnt = q.popleft()
            for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni, nj = sti+di, stj+dj
                if 0<=ni<len(maps) and 0<=nj<len(maps[0]) and maps[ni][nj] != 'X':

                    if maps[ni][nj] == maps[eei][eej]:
                        return cnt+1

                    q.append((ni, nj, cnt+1))
                    maps[ni][nj] = 'X'

    first = bfs(si, sj, li, lj, maps1)
    second = bfs(li, lj, ei, ej, maps2)

    if first:
        answer += first
        if second:
            answer += second
            return answer
        else:
            return -1
    else:
        return -1
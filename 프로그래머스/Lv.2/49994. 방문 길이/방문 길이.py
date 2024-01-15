def solution(dirs):
    ans = set()
    dr = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    i, j = 5, 5
    
    for d in dirs:
        ni, nj = i + dr[d][0], j + dr[d][1]
        if 0 <= ni < 11 and 0 <= nj < 11:
            ans.add((i,j, ni,nj))
            ans.add((ni, nj, i, j))
            i, j = ni, nj
    return len(set(ans))/2
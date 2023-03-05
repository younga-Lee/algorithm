col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
dr = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0), 'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}
S, L, N = input().split()
si, sj = 8 - int(S[1]), col[S[0]]
li, lj = 8 - int(L[1]), col[L[0]]
N = int(N)

for _ in range(N):
    r = input()
    sni, snj = si + dr[r][0], sj + dr[r][1]
    lni, lnj = li + dr[r][0], lj + dr[r][1]

    #킹 움직이기
    if sni == li and snj == lj:
        if 0 <= lni < 8 and 0 <= lnj < 8: #돌부터 이동!! 
            li, lj = lni, lnj
            if 0 <= sni < 8 and 0 <= snj < 8: #돌이동가능한 경우에만 움직일 수 있음
                si, sj = sni, snj
    else:
        if 0 <= sni < 8 and 0 <= snj < 8:
            si, sj = sni, snj

a, b = [k for k, v in col.items() if v == sj][0], str(8 - si)
c, d = [k for k, v in col.items() if v == lj][0], str(8 - li)
print(a+b)
print(c+d)